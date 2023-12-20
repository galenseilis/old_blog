---
title: Implementing a Kelly Network in Ciw
date: 2023-12-20 13:51:15
categories: [simulation,discrete-event-simulation,queueing-networks,ciw]
tags: [kelly-network, simulation,discrete-event-simulation,queueing-networks,ciw,python,queue,queueing-theory,exponential-distribution,statistics,operations-research,random-variable,inter-arrival-time,service-time,random-number-generator,seed,servers]
math: true
mermaid: true
---

[Ciw](https://ciw.readthedocs.io/en/latest/) is a [Python](https://www.python.org/) package for [simulating](https://en.wikipedia.org/wiki/Discrete-event_simulation) [queueing networks](https://en.wikipedia.org/wiki/Queueing_theory). 

Suppose there are two classes of patient, "Baby" and "Child", and three service nodes. Both are registered at a receptionist's desk where a single receptionist works. Babies arrived every hour on average and children arrive every half of an hour on average at the receptionist's desk. It takes 15 minutes on average for babies to get registered, and an average of 10 minutes for children to get registered. Once registered, babies and children go into separate waiting clinics where they wait to be seen by separate specialists. It takes an average of an hour for either babies or children to complete their appointments with their respective specialists. There are two specialists in the babies' room, and three specialists in the childrens' room. Each specialist has their own working room where they serve their patient.

An example of a [Kelly network](https://en.wikipedia.org/wiki/Kelly_network) can be implemented and simulated for 9 hours using Ciw in the following way.

```python
import ciw

ciw.seed(2018)

N = ciw.create_network(
    arrival_distributions={
        'Baby': [ciw.dists.Exponential(rate=1.0),
                 None,
                 None],
        'Child': [ciw.dists.Exponential(rate=2.0),
                  None,
                  None]
    },
    service_distributions={
        'Baby': [ciw.dists.Exponential(rate=4.0),
                 ciw.dists.Exponential(rate=1.0),
                 ciw.dists.Deterministic(value=0.0)],
        'Child': [ciw.dists.Exponential(rate=6.0),
                  ciw.dists.Deterministic(value=0.0),
                  ciw.dists.Exponential(rate=1.0)]
    },
    routing={'Baby': [[0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0]],
             'Child': [[0.0, 0.0, 1.0],
                       [0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0]]
    },
    number_of_servers=[1, 2, 3],
)

Q = ciw.Simulation(N)

Q.simulate_until_max_time(9)

recs = Q.get_all_records()
```
