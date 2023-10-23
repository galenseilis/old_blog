---
title: Ciw Hack to Get Resampling Routing Matrices
date: 2023-10-22 00:50:15
categories: [discrete-event-simulation,queueing-networks,ciw]
tags: [discrete-event-simulation,queueing-networks,ciw,python,computer-programming,]
math: true
mermaid: true
---

The Ciw library allows for a stochastic matrix representing probabilities of transitioning from one service to another. Here is an example [from the documentation](https://ciw.readthedocs.io/en/latest/Tutorial-II/tutorial_v.html).

```python
import ciw

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.3),
                           ciw.dists.Exponential(rate=0.2),
                           None],
    service_distributions=[ciw.dists.Exponential(rate=1.0),
                           ciw.dists.Exponential(rate=0.4),
                           ciw.dists.Exponential(rate=0.5)],
    routing=[[0.0, 0.3, 0.7],
             [0.0, 0.0, 1.0],
             [0.0, 0.0, 0.0]],
    number_of_servers=[1, 2, 2]
)
```

This example will only use a fixed stochastic matrix, however. If the probabilities were estimated from data or there is *a priori* uncertainty in the entries of the stochastic matrix then we might want to account for that.

Strictly-speaking, the Ciw library provides process-based routing customization that is extremely flexible. See this [guide](https://ciw.readthedocs.io/en/latest/Guides/process_based.html) for how to use their process-based routing. But as a weird flex I would like to share a little hack to incorporate uncertainty into the stochastic matrices themselves.

We can make a subclass from `list` and provide methods such that it samples new values whenever it is accessed!

```python
import numpy as np

class RandomDirichletList(list):
    """
    List that contains and resamples from a Dirichlet distribution.

    This class represents a list-like structure that contains and
    resamples from a Dirichlet distribution. It is designed for
    working with probabilistic values that sum to 1, such as probability
    distributions. The Dirichlet distribution is used to generate
    such values.

    Attributes:
        alphas (list or array-like): The alpha parameters of the
            Dirichlet distribution. These parameters control the
            shape of the distribution.

    Methods:
        __init__(self, alphas):
            Initializes the RandomDirichletList with the provided alpha
            parameters. It ensures that the alpha parameters are positive
            and populates the list with Dirichlet-distributed values. The
            probabilities are adjusted to ensure they sum to 1.

        _renormalize_probs(self):
            Private method to renormalize the probabilities. It ensures
            that the probabilities sum to 1 according to the built-in
            sum function. This is important for working with certain
            libraries that require normalized probabilities.

        sample(self):
            Sample new values from the Dirichlet distribution and ensure
            they sum to 1. This method is used to initialize or reinitialize
            the probabilities in the list.

        __getitem__(self, index):
            Resamples from the Dirichlet distribution and returns the
            value at the specified index. This method updates the list
            with newly sampled values and then returns the requested
            item.

        __min__(self):
            Returns the minimum value in the list of probabilities.
            This method provides functionality similar to the built-in
            min() function for RandomDirichletList.

        __max__(self):
            Returns the maximum value in the list of probabilities.
            This method provides functionality similar to the built-in
            max() function for RandomDirichletList.

        __len__(self):
            Returns the length of the list, which corresponds to the
            number of elements in the probability distribution.

        __repr__(self):
            Returns a string representation of the RandomDirichletList
            object, displaying its current list of probabilities.
    """

    def __init__(self, alphas):

        if np.any(alphas) <= 0:
            raise ValueError("Alpha parameters must be positive")
        else:
            self.alphas = alphas

        self.sample()
        super().__init__(self.probs)

    def _renormalize_probs(self):
        """Sum renormalize probabilities.

        NumPy provides probabilities that are close to
        summing to one, but to work with Ciw they need
        to sum 1 according to the built-in sum function.
        """
        self.probs /= sum(self.probs)

    def sample(self):

        # Sample new values to get started
        self.probs = np.random.dirichlet(self.alphas)
        self._renormalize_probs()

        # If needed, resample until normalization passes
        while sum(self.probs) != 1.0:
            self.probs = np.random.dirichlet(self.alphas)
            self._renormalize_probs()

    def __getitem__(self, index):
        """Resample and then get item."""
        self.sample()
        return self.probs[index]

    def __min__(self):
        return min(self.probs)

    def __max__(self):
        return max(self.probs)

    def __len__(self):
        return len(self.probs)

    def __repr__(self):
        return f"RDL{self.probs}"
```

Here is an example of indexing the same element of the instance and yet sampling different values! This is achieved by resampling from a Dirichlet distribution every time `__getitem__` is called.

```python
>>> np.random.seed(seed=2018)
>>> rdl = RandomDirichletList([1.1, 2, 3])
>>> print([rdl[0] for i in range(10)])
[0.29042591447408683, 0.023680603962985814, 0.11617557745526234, 0.1422083243333615, 0.1914130984353422, 0.17498591805601912, 0.22902976104654874, 0.28693524142371135, 0.40673998074008844, 0.0788396847445936]
```

The `RandomDirichletList` has implementations of `__min__`, `__max__`, and `__len__` to help reassure Ciw that it has the right properties to be a stochastic matrix. 

However, sometimes `np.random.dirichlet` produces numbers that are merely 'close' to summing to unity. This can sometimes result in Ciw raising a `ValueError`. To tackle this I implemented `sample` and such that `_renormalize_probs` combined with [rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling) should eventually produce a valid stochastic matrix for Ciw.

Here is an example of creating a list of instances of `RandomDirichletList` which Ciw accepts and uses in the simulation.

```python
import ciw
import numpy
import pandas as pd

np.random.seed(seed=2018)

# Assume RandomDirichletList is in namespace

sm = [
    RandomDirichletList([1, 2, 3]),
    RandomDirichletList([3, 4, 5]),
    RandomDirichletList([6, 7, 8]),
]

N = ciw.create_network(
    arrival_distributions=[
        ciw.dists.Exponential(rate=0.3),
        ciw.dists.Exponential(rate=0.2),
        None,
    ],
    service_distributions=[
        ciw.dists.Exponential(rate=1.0),
        ciw.dists.Exponential(rate=0.4),
        ciw.dists.Exponential(rate=0.5),
    ],
    routing=sm,
    number_of_servers=[1, 2, 2],
)

sim = ciw.Simulation(N)
sim.simulate_until_max_time(10)

pd.DataFrame(
    sim.get_all_records()
    ).to_markdown('out.md')
```

Here is the output!

|    |   id_number | customer_class   | original_customer_class   |   node |   arrival_date |   waiting_time |   service_start_date |   service_time |   service_end_date |   time_blocked |   exit_date |   destination |   queue_size_at_arrival |   queue_size_at_departure |   server_id | record_type   |
|---:|------------:|:-----------------|:--------------------------|-------:|---------------:|---------------:|---------------------:|---------------:|-------------------:|---------------:|------------:|--------------:|------------------------:|--------------------------:|------------:|:--------------|
|  0 |           5 | Customer         | Customer                  |      1 |      6.58458   |        0       |            6.58458   |      0.166573  |            6.75116 |              0 |     6.75116 |             1 |                       0 |                         0 |           1 | service       |
|  1 |           5 | Customer         | Customer                  |      1 |      6.75116   |        0       |            6.75116   |      0.776417  |            7.52757 |              0 |     7.52757 |             1 |                       0 |                         0 |           1 | service       |
|  2 |           5 | Customer         | Customer                  |      1 |      7.52757   |        0       |            7.52757   |      0.291603  |            7.81918 |              0 |     7.81918 |             2 |                       0 |                         0 |           1 | service       |
|  3 |           6 | Customer         | Customer                  |      1 |      7.86023   |        0       |            7.86023   |      0.119357  |            7.97959 |              0 |     7.97959 |             2 |                       0 |                         0 |           1 | service       |
|  4 |           3 | Customer         | Customer                  |      1 |      3.85674   |        0       |            3.85674   |      0.634459  |            4.4912  |              0 |     4.4912  |             2 |                       0 |                         0 |           1 | service       |
|  5 |           3 | Customer         | Customer                  |      2 |      4.4912    |        3.57364 |            8.06484   |      0.0020501 |            8.06689 |              0 |     8.06689 |             2 |                       2 |                         4 |           1 | service       |
|  6 |           7 | Customer         | Customer                  |      1 |      8.12925   |        0       |            8.12925   |      0.502056  |            8.63131 |              0 |     8.63131 |             1 |                       0 |                         0 |           1 | service       |
|  7 |           7 | Customer         | Customer                  |      1 |      8.63131   |        0       |            8.63131   |      0.409412  |            9.04072 |              0 |     9.04072 |             2 |                       0 |                         0 |           1 | service       |
|  8 |           4 | Customer         | Customer                  |      2 |      5.8277    |        2.23919 |            8.06689   |      0.1871    |            8.25399 |              0 |     8.25399 |             3 |                       3 |                         4 |           1 | service       |
|  9 |           4 | Customer         | Customer                  |      3 |      8.25399   |        0       |            8.25399   |      1.19738   |            9.45138 |              0 |     9.45138 |             2 |                       1 |                         1 |           2 | service       |
| 10 |           1 | Customer         | Customer                  |      2 |      0.0166038 |        0       |            0.0166038 |      2.44758   |            2.46419 |              0 |     2.46419 |             2 |                       0 |                         0 |           1 | service       |
| 11 |           1 | Customer         | Customer                  |      2 |      2.46419   |        0       |            2.46419   |      5.60065   |            8.06484 |              0 |     8.06484 |             3 |                       0 |                         5 |           1 | service       |

Have fun!
