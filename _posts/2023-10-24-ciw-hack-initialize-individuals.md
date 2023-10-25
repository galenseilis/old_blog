---
title: Can Ciw Queues be Initialized With Individuals?
date: 2023-10-23 00:50:15
categories: [discrete-event-simulation,queueing-networks,ciw]
tags: [discrete-event-simulation,queueing-networks,ciw,python,computer-programming,]
math: true
mermaid: true
---

Although this [issue](https://github.com/CiwPython/Ciw/issues/98) has been considered in the past, Ciw does not have an officially supported way to begin a waitlist (i.e. queue) with a collection of individuals. For simulated real-world systems it can be valuable for the waitlist to be initialized in a realistic state, but Ciw will begin the simulation with the waitlists being empty.

Here is a small example of putting individuals on the waitlist.

```python
import ciw

import pandas as pd

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    number_of_servers=[3]
)


Q = ciw.Simulation(N)

# Directly setting individuals to Node 1 (a queue)
Q.nodes[1].individuals = [[ciw.Individual(-i) for i in range(100)]]

Q.simulate_until_max_time(1000)

recs = pd.DataFrame(Q.get_all_records())
```

Note that not everything about the individuals will be handled as an ordinary instance of `Individual` as they would be created in the arrival node with certain attributes assigned to them. We can take a look at how it affects the results by running `print(recs[recs.id_number <= 0].sort_values(by='id_number').to_markdown())` after running the previous code block in an interactive session. This produced the following table:

|    |   id_number | customer_class   | original_customer_class   |   node | arrival_date   |   waiting_time |   service_start_date |   service_time |   service_end_date |   time_blocked |   exit_date |   destination | queue_size_at_arrival   |   queue_size_at_departure |   server_id | record_type   |
|---:|------------:|:-----------------|:--------------------------|-------:|:---------------|---------------:|---------------------:|---------------:|-------------------:|---------------:|------------:|--------------:|:------------------------|--------------------------:|------------:|:--------------|
| 10 |          -9 | Customer         | Customer                  |      1 | False          |        73.8624 |              73.8624 |        4.746   |            78.6084 |              0 |     78.6084 |            -1 | False                   |                         1 |           2 | service       |
|  9 |          -8 | Customer         | Customer                  |      1 | False          |        70.8479 |              70.8479 |        3.01446 |            73.8624 |              0 |     73.8624 |            -1 | False                   |                         2 |           2 | service       |
| 12 |          -7 | Customer         | Customer                  |      1 | False          |        65.0723 |              65.0723 |       30.1633  |            95.2356 |              0 |     95.2356 |            -1 | False                   |                         3 |           3 | service       |
|  7 |          -6 | Customer         | Customer                  |      1 | False          |        59.6327 |              59.6327 |        5.43967 |            65.0723 |              0 |     65.0723 |            -1 | False                   |                         4 |           3 | service       |
|  8 |          -5 | Customer         | Customer                  |      1 | False          |        54.8621 |              54.8621 |       15.9859  |            70.8479 |              0 |     70.8479 |            -1 | False                   |                         3 |           2 | service       |
| 11 |          -4 | Customer         | Customer                  |      1 | False          |        51.339  |              51.339  |       32.7551  |            84.0941 |              0 |     84.0941 |            -1 | False                   |                         2 |           1 | service       |
|  6 |          -3 | Customer         | Customer                  |      1 | False          |        49.7486 |              49.7486 |        9.88403 |            59.6327 |              0 |     59.6327 |            -1 | False                   |                         5 |           3 | service       |
|  3 |          -2 | Customer         | Customer                  |      1 | False          |        42.856  |              42.856  |        6.89266 |            49.7486 |              0 |     49.7486 |            -1 | False                   |                         5 |           3 | service       |
|  2 |          -1 | Customer         | Customer                  |      1 | False          |        34.2057 |              34.2057 |        8.65025 |            42.856  |              0 |     42.856  |            -1 | False                   |                         6 |           3 | service       |
|  5 |           0 | Customer         | Customer                  |      1 | False          |        20.3638 |              20.3638 |       34.4982  |            54.8621 |              0 |     54.8621 |            -1 | False                   |                         4 |           2 | service       |

Notably, the `arrival_date` and `queue_size_at_arrival` at arrival are `False`. The `id_number` columns are non-positive to avoid conflicts with instances of `Individual` that are added later. Otherwise you can end up with collisions like having two individuals with the ID of 1. The IDs being set to non-positive values is an easy way to circumvent these collisions.

Something a bit more insideous for this hack is that `self.simulation` internal to these custom instances of `Individual` will also be `False`. If you ever use service disiplines that require accessing something else about the system's state via the instance of `Simulation`, you will get errors or unexpected behaviour. Here is another version of the code that uses a service discipline to print out the default value of `self.simulation`.

```python
import ciw

import pandas as pd


def print_has_simulation_LIFO(individuals):

    if individuals[-1].id_number <= 0:
        print(individuals[-1].id_number, individuals[-1].simulation)

    return individuals[-1]

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    service_disciplines=[print_has_simulation_LIFO],
    number_of_servers=[3]
)


Q = ciw.Simulation(N)
Q.nodes[1].individuals = [[ciw.Individual(-i) for i in range(10)]]

Q.simulate_until_max_time(1000)
```

The above will print out something like this:
```python
-9 False
-8 False
-7 False
-6 False
-5 False
-4 False
-3 False
-2 False
-1 False
0 False
```

What we can do is assign the simulation instance to `self.simulation` when we initialize each instance of `Individual`. Here is an example:

```python
import ciw

import pandas as pd


def print_has_simulation_LIFO(individuals):

    if individuals[-1].id_number <= 0:
        print(individuals[-1].id_number, individuals[-1].simulation)

    return individuals[-1]

N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    service_disciplines=[print_has_simulation_LIFO],
    number_of_servers=[3]
)


Q = ciw.Simulation(N)

# Ensure the instances have the simulation instance
init_individuals = []
for i in range(10):
    initial_ind = ciw.Individual(-i, simulation=Q)
    init_individuals.append(initial_ind)
    
Q.nodes[1].individuals = [init_individuals]

Q.simulate_until_max_time(1000)
```

The above will print out something like this:

```python
-9 Simulation
-8 Simulation
-7 Simulation
-6 Simulation
-5 Simulation
-4 Simulation
-3 Simulation
-2 Simulation
-1 Simulation
0 Simulation
```

And perhaps you want to set `arrival_date` and `queue_size_at_arrival`, and change some of the other default values. You can likewise set those values either through the `__init__` method, or by assigning attributes after you have instantiated the object.

It doesn't seem elegant, but it appears that in this post we have shown how to prepare queues to be initialized with individuals already waiting on them.
