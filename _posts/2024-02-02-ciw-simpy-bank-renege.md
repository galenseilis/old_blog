---
title: A Ciw Implementatin of SimPy's Bank Renege Example
date: 2024-02-02 06:30:15
categories: [simulation,discrete-event-simulation,python,ciw]
tags: [simpy,dicrete-event-simulation,simulation,processes,environment,python,python-generator,ciw,queueing-network,queueing-theory,reneging,process-based-simulation,event-based-simulation,random-variables]
math: true
mermaid: true
---

In this post we look at implementing SimPy's [Bank Renege](https://simpy.readthedocs.io/en/latest/examples/bank_renege.html) example using Ciw. At a first glance this example is essentially a [M/M/1 queue](https://en.wikipedia.org/wiki/M/M/1_queue), but it has a couple of custom features. The first customized aspect is reneging customers with a uniformly-distributed reneging patience. See [Bocquet 2005](https://apps.dtic.mil/sti/pdfs/ADA444342.pdf) for some discussion of basic queueing theory with reneging. The second aspect is that there is a fixed total number of customers.

Initially we could consider the arrivals to follow an exponential distribution

$$T_{\text{Arrivals}} \sim \text{Exponential} \left( \frac{1}{10}  \right)$$

but since this will only be true for the first 5 customer we need a more customized distribution. Specifically

$$T_{\text{Arrivals}} \sim \begin{cases}  \delta(\infty) & \text{\\#Customers} \geq 5 \\ \text{Exponential} \left( \frac{1}{10}  \right) & \text{\\#Customers} < 5  \end{cases}$$

where $\delta(\infty)$ denotes a [Dirac delta distribution](https://en.wikipedia.org/wiki/Dirac_delta_function) centered at infinity. You can consider this an abuse of notation that simply indicates that arrivals stop after 5 customers, or you could take a couple of distinct approaches: one defining this concept in terms of limits or the other in terms of the [extended real numbers](https://en.wikipedia.org/wiki/Extended_real_number_line). We'll just stick to it being an informal abuse of notation here. In Python we'll define this as `MaxArrivalDist`:

```python
class MaxArrivalDist(ciw.dists.Distribution):
    """
    A custom distribution that limits the number of arrivals based on a maximum count.

    Attributes:
    - dist (ciw.dists.Distribution): The underlying distribution used for sampling.
    - max_arrivals (int): The maximum number of arrivals allowed.
    - arrival_count (int): The current count of arrivals.

    Methods:
    - sample(t: Optional[float] = None, ind: Optional[ciw.sampler.Individual] = None) -> float:
      Samples from the underlying distribution until the maximum number of arrivals is reached.
    """

    def __init__(self, dist: ciw.dists.Distribution, max_arrivals: int = 5):
        """
        Initializes the MaxArrivalDist.

        Parameters:
        - dist (ciw.dists.Distribution): The underlying distribution to be used for sampling.
        - max_arrivals (int): The maximum number of arrivals allowed. Default is 5.
        """
        self.dist = dist
        self.max_arrivals = max_arrivals
        self.arrival_count = 0

    def sample(self, t: Optional[float] = None, ind: Optional[ciw.Individual] = None) -> float:
        """
        Samples from the underlying distribution until the maximum number of arrivals is reached.

        Parameters:
        - t (Optional[float]): Time parameter.
        - ind (Optional[ciw.sampler.Individual]): Individual parameter representing the arrival.

        Returns:
        - float: The sampled value from the distribution or positive infinity if the maximum arrivals limit is reached.
        """
        if self.arrival_count < self.max_arrivals:
            self.arrival_count += 1
            return self.dist.sample()
        else:
            return float('inf')
```

Just so we don't simulate for too much or too little time, we can also set the termination condition of our simulation to be the number of customers that have left the system (i.e. have received service and left). Following the Ciw guide [*How to Simulate For a Certain Number of Customers*](https://ciw.readthedocs.io/en/latest/Guides/sim_numcusts.html) we can call the `simulate_until_max_customers(5, method='Finish')` method on an instance of `Simulation` to achieve this result. This way the `current_time` at the end of the simulation will be the amount of time for all five customers to sojourn.

The service distribution is just an exponential distribution:

$$T_{\text{Service}} \sim \text{Exponential} \left( \frac{1}{12} \right)$$

The reneging times for the customers will simply be according to a continuous unifom distribution:

$$T_{\text{Renege}} \sim \mathcal{U}_{[1,3]}.$$

Following Ciw guide [*How to Simulate Reneging Customers*](https://ciw.readthedocs.io/en/latest/Guides/reneging.html), we can simply pass in `reneging_time_distributions=[ciw.dists.Uniform(1,3)]`.


```python
from typing import Optional


import ciw
import numpy as np
from scipy.stats import gamma

ciw.seed(2018)
          
class MaxArrivalDist(ciw.dists.Distribution):
    """
    A custom distribution that limits the number of arrivals based on a maximum count.

    Attributes:
    - dist (ciw.dists.Distribution): The underlying distribution used for sampling.
    - max_arrivals (int): The maximum number of arrivals allowed.
    - arrival_count (int): The current count of arrivals.

    Methods:
    - sample(t: Optional[float] = None, ind: Optional[ciw.sampler.Individual] = None) -> float:
      Samples from the underlying distribution until the maximum number of arrivals is reached.
    """

    def __init__(self, dist: ciw.dists.Distribution, max_arrivals: int = 5):
        """
        Initializes the MaxArrivalDist.

        Parameters:
        - dist (ciw.dists.Distribution): The underlying distribution to be used for sampling.
        - max_arrivals (int): The maximum number of arrivals allowed. Default is 5.
        """
        self.dist = dist
        self.max_arrivals = max_arrivals
        self.arrival_count = 0

    def sample(self, t: Optional[float] = None, ind: Optional[ciw.Individual] = None) -> float:
        """
        Samples from the underlying distribution until the maximum number of arrivals is reached.

        Parameters:
        - t (Optional[float]): Time parameter.
        - ind (Optional[ciw.sampler.Individual]): Individual parameter representing the arrival.

        Returns:
        - float: The sampled value from the distribution or positive infinity if the maximum arrivals limit is reached.
        """
        if self.arrival_count < self.max_arrivals:
            self.arrival_count += 1
            return self.dist.sample()
        else:
            return float('inf')


network = ciw.create_network(
    arrival_distributions=[MaxArrivalDist(ciw.dists.Exponential(1/10), 5)],
    service_distributions=[ciw.dists.Exponential(1/12)],
    number_of_servers=[1],
    reneging_time_distributions=[ciw.dists.Uniform(1,3)]
)

simulation = ciw.Simulation(network)
simulation.simulate_until_max_customers(5, method='Finish')
```

How long should we expect this simulation to take? According to queueing theory, such a system is stable if $\rho \triangleq \frac{\lambda}{\mu} < 1$. In this case $\lambda = \frac{1}{10}$ and $\mu = \frac{1}{12}$ so $\rho = \frac{6}{5} > 1$. But there actually is something importantly different from this classic theoretical setting: we know ahead of time we're simulating for only 5 customers. So the theoretically concern of the length of the waitlist having unbounded asymptotic behaviour is not a concern here. That doesn't mean that the distribution is easy to estimate. One cannot, for example, simply add the random variables to get the correct distribution as that would ignore that there is waiting time on the queue and that some of the customers will renege. Instead, we'll simulate and record the simulation times that result.


```python
from typing import Optional


import ciw
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Config stuff
plt.style.use('dark_background')
ciw.seed(2018)

class MaxArrivalDist(ciw.dists.Distribution):
    """
    A custom distribution that limits the number of arrivals based on a maximum count.

    Attributes:
    - dist (ciw.dists.Distribution): The underlying distribution used for sampling.
    - max_arrivals (int): The maximum number of arrivals allowed.
    - arrival_count (int): The current count of arrivals.

    Methods:
    - sample(t: Optional[float] = None, ind: Optional[ciw.sampler.Individual] = None) -> float:
      Samples from the underlying distribution until the maximum number of arrivals is reached.
    """

    def __init__(self, dist: ciw.dists.Distribution, max_arrivals: int = 5):
        """
        Initializes the MaxArrivalDist.

        Parameters:
        - dist (ciw.dists.Distribution): The underlying distribution to be used for sampling.
        - max_arrivals (int): The maximum number of arrivals allowed. Default is 5.
        """
        self.dist = dist
        self.max_arrivals = max_arrivals
        self.arrival_count = 0

    def sample(self, t: Optional[float] = None, ind: Optional[ciw.Individual] = None) -> float:
        """
        Samples from the underlying distribution until the maximum number of arrivals is reached.

        Parameters:
        - t (Optional[float]): Time parameter.
        - ind (Optional[ciw.sampler.Individual]): Individual parameter representing the arrival.

        Returns:
        - float: The sampled value from the distribution or positive infinity if the maximum arrivals limit is reached.
        """
        if self.arrival_count < self.max_arrivals:
            self.arrival_count += 1
            return self.dist.sample()
        else:
            return float('inf')


network = ciw.create_network(
    arrival_distributions=[MaxArrivalDist(ciw.dists.Exponential(1/10), 5)],
    service_distributions=[ciw.dists.Exponential(1/12)],
    number_of_servers=[1],
    reneging_time_distributions=[ciw.dists.Uniform(1,3)]
)

def runtime():
	simulation = ciw.Simulation(network)
	simulation.simulate_until_max_customers(5, method='Finish')
	return max([ind.exit_date for ind in simulation.get_all_records()])


x = np.array([runtime() for i in range(1_000_000)])
params = gamma.fit(x)
q = np.linspace(x.min(), x.max(), num=100)
p = gamma.pdf(q, *params)

plt.hist(x, density=True, bins=200)
plt.plot(q, p, label=f'Gamma(shape={np.round(params[0],2)},scale={np.round(params[2],2)})')
plt.xlabel('Simulation Time')
plt.ylabel('Density')
plt.legend()
plt.savefig('bank-renege-run-times.png', dpi=300, transparent=True)
plt.close()
```

The above code results in the plot:

![](/assets/images/bank-renege-run-times.png)

You may be wondering how I knew that it would be a Gamma distribution that would fit so well to the simulation results. Honestly, I guessed. Gamma distributions 'often' given good approximations to time-to-event distributions, and happen to generalize some common waiting time distributions such as exponential distributions and Erlang distributions. Nonetheless, it is satisfying to see such a nearly-perfect fit to a relatively simple distribution.
