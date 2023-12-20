---
title: Implementing a G/G/1 Queue in Ciw
date: 2023-12-20 13:51:15
categories: [simulation,discrete-event-simulation,queueing-networks,ciw]
tags: [gg1-queue, simulation,discrete-event-simulation,queueing-networks,ciw,python,queue,queueing-theory,exponential-distribution,statistics,operations-research,random-variable,inter-arrival-time,service-time,random-number-generator,seed,servers]
math: true
mermaid: true
---

[Ciw](https://ciw.readthedocs.io/en/latest/) is a [Python](https://www.python.org/) package for [simulating](https://en.wikipedia.org/wiki/Discrete-event_simulation) [queueing networks](https://en.wikipedia.org/wiki/Queueing_theory). 

The two G's in G/G/1 do not have to be the same distribution, and respectively can be any distribution with non-negative support.

We will use a [Hyperexponential distribution](https://en.wikipedia.org/wiki/Hyperexponential_distribution) for the arrival distribution. A hyperexponential distribution is exactly a [mixture distribution](https://en.wikipedia.org/wiki/Mixture_distribution) of [exponential distributions](https://en.wikipedia.org/wiki/Exponential_distribution). This has an interpretation of there being an implicit set of arrival processes that each have their own distinct but independent exponential arrival times. In this case we will choose a mixture of four such arrival processes with distinct arrival rates:

$$\begin{align} U_1 \sim & \text{Exponential}\left( \frac{1}{9} \right) \\ U_2 \sim & \text{Exponential}\left( \frac{1}{5} \right) \\ U_3 \sim & \text{Exponential}\left( \frac{1}{6} \right) \\ U_4 \sim & \text{Exponential}\left( 1 \right) \end{align}$$

The following mixture distribution for the arrival times will be used:

$$T_{\text{arrivals}} \sim \frac{1}{5} f_{U_1} + \frac{1}{10} f_{U_2} + \frac{3}{5} f_{U_3} + \frac{1}{10} f_{U_4}$$

We will use a [gamma distribution](https://en.wikipedia.org/wiki/Gamma_distribution) for the sake of example. A gamma distribution is the result of a sum of [independent](https://en.wikipedia.org/wiki/Independence_(probability_theory)) [exponentially-distributed](https://en.wikipedia.org/wiki/Exponential_distribution) [random variable](https://en.wikipedia.org/wiki/Random_variable), and thus for this example we have an interpretation that the servicing is implicitly a multi-step process where each step has an exponentially-distributed completion time. 

A [G/G/1 queue](https://en.wikipedia.org/wiki/G/G/1_queue) as described can be implemented and simulated using Ciw in the following way.

```python
import ciw

ciw.seed(2018)

arrival_dist = ciw.dists.HyperExponential(rates=[9, 5, 6, 1], probs=[0.2, 0.1, 0.6, 0.1])
service_dist = ciw.dists.Gamma(shape=0.6, scale=1.2)
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [arrival_dist],
    service_distributions = [service_dist],
    number_of_servers = [1]
    )
    
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
```
