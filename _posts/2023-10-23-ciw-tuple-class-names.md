---
title: Can Ciw Use Tuples For Class IDs?
date: 2023-10-23 00:50:15
categories: [discrete-event-simulation,queueing-networks,ciw]
tags: [discrete-event-simulation,queueing-networks,ciw,python,computer-programming,]
math: true
mermaid: true
---

It would be convienent to keep track of classes of customers in Ciw networks based on a collection of attributes. A first approximation is to try using tuples since they are immutable.

The following code works, and demonstrates that we can use tuples as the class names for Ciw.

```python
N = ciw.create_network(
    arrival_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=1.0),
                 None,
                 None],
        ('Child',1): [ciw.dists.Exponential(rate=2.0),
                  None,
                  None]
    },
    service_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=4.0),
                 ciw.dists.Exponential(rate=1.0),
                 ciw.dists.Deterministic(value=0.0)],
        ('Child',1): [ciw.dists.Exponential(rate=6.0),
                  ciw.dists.Deterministic(value=0.0),
                  ciw.dists.Exponential(rate=1.0)]
    },
    routing={('Baby',0): [[0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0]],
             ('Child',1): [[0.0, 0.0, 1.0],
                       [0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0]]
    },
    number_of_servers=[1, 2, 3],
)

Q = ciw.Simulation(N)
Q.simulate_until_max_time(9)
```

Also note that the tuples do not need to be of the same length provided since the lexicographical ordering used to evaluate tuples in Python will stop at the end of the shortest tuple.


But they do need to have order-compatible data. For example, the following code raises `TypeError: '<' not supported between instances of 'int' and 'str'`. 

```python
N = ciw.create_network(
    arrival_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=1.0),
                 None,
                 None],
        (1,): [ciw.dists.Exponential(rate=2.0),
                  None,
                  None]
    },
    service_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=4.0),
                 ciw.dists.Exponential(rate=1.0),
                 ciw.dists.Deterministic(value=0.0)],
        (1,): [ciw.dists.Exponential(rate=6.0),
                  ciw.dists.Deterministic(value=0.0),
                  ciw.dists.Exponential(rate=1.0)]
    },
    routing={('Baby',0): [[0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0]],
             (1, ): [[0.0, 0.0, 1.0],
                       [0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0]]
    },
    number_of_servers=[1, 2, 3],
)

Q = ciw.Simulation(N)
Q.simulate_until_max_time(9)
```

One approach is to ensure equal tuple lengths *and* corresponding types by having empty types (e.g. empty string `''`) or zeros (i.e. `0`). Here is the code using the empty string instead of `'child'`.

```python
N = ciw.create_network(
    arrival_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=1.0),
                 None,
                 None],
        ('',1): [ciw.dists.Exponential(rate=2.0),
                  None,
                  None]
    },
    service_distributions={
        ('Baby',0): [ciw.dists.Exponential(rate=4.0),
                 ciw.dists.Exponential(rate=1.0),
                 ciw.dists.Deterministic(value=0.0)],
        ('',1): [ciw.dists.Exponential(rate=6.0),
                  ciw.dists.Deterministic(value=0.0),
                  ciw.dists.Exponential(rate=1.0)]
    },
    routing={('Baby',0): [[0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0]],
             ('',1): [[0.0, 0.0, 1.0],
                       [0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0]]
    },
    number_of_servers=[1, 2, 3],
)

Q = ciw.Simulation(N)
Q.simulate_until_max_time(9)
```

Tuples are a good first start. It should be possible to make a data-containing class which is immutable and ordered.
