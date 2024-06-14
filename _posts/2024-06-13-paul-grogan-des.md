---
title: Paul Grogan's DES Example
date: 2024-06-13 04:51:15
categories: [simulation,discrete-event-simulation,python,ciw]
tags: [simulation,discrete-event-simulation,pythonp,processes,environment,python,queueing-network,queueing-theory,event-based-simulation,random-variables,exponential-distribution,youtube]
math: true
mermaid: true
---

I watched a YouTube video over a year ago that showed an implementation of a specific discrete event simulation. Here is the video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/oJyf8Q0KLRY?si=-xRxMyPWZn8guR6x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I typed out the implementation in that video, and added some docstrings and type annotations.

```python
import numpy as np

class Simulation:
    def __init__(self):
        """
        Initialize the simulation with default parameters.

        Attributes:
            num_in_system (int): The number of entities currently in the system.
            clock (float): The current simulation time.
            t_arrival (float): The time of the next arrival event.
            t_depart (float): The time of the next departure event.
            num_arrivals (int): The total number of arrivals that have occurred.
            num_departs (int): The total number of departures that have occurred.
            total_wait (float): The cumulative waiting time of all entities.
        """
        self.num_in_system: int = 0
        self.clock: float = 0.0
        self.t_arrival: float = self.generate_interarrival()
        self.t_depart: float = float("inf")
        self.num_arrivals: int = 0
        self.num_departs: int = 0
        self.total_wait: float = 0.0

    def advance_time(self) -> None:
        """
        Advance the simulation time to the next event (either arrival or departure).

        This method updates the clock, total waiting time, and handles the next event.
        """
        t_event: float = min(self.t_arrival, self.t_depart)
        self.total_wait += self.num_in_system * (t_event - self.clock)
        self.clock = t_event

        if self.t_arrival <= self.t_depart:
            self.handle_arrival_event()
        else:
            self.handle_departure_event()

    def handle_arrival_event(self) -> None:
        """
        Handle an arrival event in the simulation.

        This method updates the number of entities in the system, schedules the next
        departure event if the system was previously empty, and schedules the next arrival event.
        """
        self.num_in_system += 1
        self.num_arrivals += 1
        if self.num_in_system <= 1:
            self.t_depart = self.clock + self.generate_service()
        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_departure_event(self) -> None:
        """
        Handle a departure event in the simulation.

        This method updates the number of entities in the system, schedules the next
        departure event if there are remaining entities, or sets the departure time to infinity if empty.
        """
        self.num_in_system -= 1
        self.num_departs += 1
        if self.num_in_system > 0:
            self.t_depart = self.clock + self.generate_service()
        else:
            self.t_depart = float("inf")

    def generate_interarrival(self) -> float:
        """
        Generate the time until the next arrival event using an exponential distribution.

        Returns:
            float: The interarrival time.
        """
        return np.random.exponential(1 / 3)

    def generate_service(self) -> float:
        """
        Generate the service time for an entity using an exponential distribution.

        Returns:
            float: The service time.
        """
        return np.random.exponential(1 / 4)
```

We can then initialize the simulation and run it for discrete units of times like this:

```python
S = Simulation()

for _ in range(2018):
    S.advance_time()
```

Grogan's implementation is a pedagogical example that can be quickly coded and explained. What can we use for prototyping and using something more flushed out?

The [Ciw package](https://ciw.readthedocs.io/en/latest/) is a ready-to-use discrete event simulation package for queueing networks. It covers a variety of cases, including a similar simulation:

```python
import ciw

# Define the parameters for the arrival and service processes
arrival_rate = 3  # Interarrival rate (lambda)
service_rate = 4  # Service rate (mu)

# Define the parameters for the Ciw network
network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(arrival_rate)],
    service_distributions=[ciw.dists.Exponential(service_rate)],
    number_of_servers=[1]
)

# Create and run the simulation
ciw.seed(2018)
sim = ciw.Simulation(network)
sim.simulate_until_max_time(2018)
```
