---
title: Implementing a M/G/k Queue in Ciw
date: 2023-12-20 13:51:15
categories: [simulation,discrete-event-simulation,queueing-networks,ciw]
tags: [mgk-queue, simulation,discrete-event-simulation,queueing-networks,ciw,python,queue,queueing-theory,exponential-distribution,statistics,operations-research,random-variable,inter-arrival-time,service-time,random-number-generator,seed,servers]
math: true
mermaid: true
---

[Ciw](https://ciw.readthedocs.io/en/latest/) is a [Python](https://www.python.org/) package for [simulating](https://en.wikipedia.org/wiki/Discrete-event_simulation) [queueing networks](https://en.wikipedia.org/wiki/Queueing_theory). 

Since G in M/G/k can be any distribution with non-negative support, we will use a [gamma distribution](https://en.wikipedia.org/wiki/Gamma_distribution) for the sake of example. A gamma distribution is the result of a sum of [independent](https://en.wikipedia.org/wiki/Independence_(probability_theory)) [exponentially-distributed](https://en.wikipedia.org/wiki/Exponential_distribution) [random variable](https://en.wikipedia.org/wiki/Random_variable), and thus for this example we have an interpretation that the servicing is implicitly a multi-step process where each step has an exponentially-distributed completion time. 

A [M/G/k queue](https://en.wikipedia.org/wiki/M/G/k_queue) as described can be implemented and simulated using Ciw in the following way.

```python
import ciw

ciw.seed(2018)

ARRIVAL_TIME = 1
SERVICE_SHAPE = 6 / 10
SERVICE_SCALE = 12 / 10
NUM_SERVERS = 2
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [ciw.dists.Exponential(ARRIVAL_TIME)],
    service_distributions = [ciw.dists.Gamma(shape=SERVICE_SHAPE, scale=SERVICE_SCALE)],
    number_of_servers = [NUM_SERVERS]
    )
    
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
```
