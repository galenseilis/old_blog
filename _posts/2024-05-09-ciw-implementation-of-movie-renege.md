---
title: A Ciw Implementation of SimPy's Movie Renege Example
date: 2024-02-20 04:51:15
categories: [simulation,discrete-event-simulation,python,ciw]
tags: [simulation,discrete-event-simulation,python,ciw,simpy,processes,environment,python,queueing-network,queueing-theory,event-based-simulation,random-variables,exponential-distribution]
math: true
mermaid: true
---

This post provides an implementation of SimPy's [Movie Renege](https://simpy.readthedocs.io/en/latest/examples/movie_renege.html) example. In this implementation I subclassed three times. One class is `TicketArrivalNode` which replaces the ordinary `ciw.ArrivalNode` in order for individuals to be given tickets when they arrive in the simulation. The `TheatreNode` class keeps track of which movies there are and whether they are sold out. Lastly `RenegeAtServiceDist` is responsible for keeping track of the change in number of tickets and assigning whether a customer reneged.

```python
import random
from typing import NoReturn

import ciw
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

movies = ['Python Unchained', 'Kill Process', 'Pulp Implementation']


class TicketArrivalNode(ciw.ArrivalNode):
    """Node generating customers requiring tickets.

    Attributes:
        None

    Methods:
        send_individual: Assigns individuals a random number of tickets and a movie choice.

    """
    
    def send_individual(self, next_node: ciw.Node, next_individual: ciw.Individual) -> NoReturn:
        """Assigns individuals to have a required number of tickets for a movie.

        Args:
            next_node: The next node in the simulation.
            next_individual: The individual to assign tickets to.

        Returns:
            None

        """
        next_individual.num_tickets = random.randint(1,6)
        next_individual.movie = random.choice(movies)
        next_node.accept(next_individual)


class TheatreNode(ciw.Node):
    """Node representing the theatre in the simulation.

    Attributes:
        num_renegers (dict): Dictionary to track the number of reneging customers.
        available_movies (dict): Dictionary to track available tickets for each movie.
        sold_out (dict): Dictionary to track whether each movie is sold out.
        sold_out_time (dict): Dictionary to track the time each movie sold out.

    Methods:
        __init__: Initializes the TheatreNode object.
        write_individual_record: Writes a data record for an individual when leaving the node.

    """
    def __init__(self, *args, **kwargs) -> NoReturn:
        """Initializes the TheatreNode object."""
        super().__init__(*args, **kwargs)

        self.num_renegers = {}
        self.available_movies = {movie:50 for movie in movies}
        self.sold_out = {movie:False for movie in movies}
        self.sold_out_time = {movie:float('inf') for movie in movies}
        

    def write_individual_record(self, individual: ciw.Individual):
        """Write a data record for an individual when leaving a node.

        Args:
            individual: The individual leaving the node.

        Returns:
            None

        """
        if ciw.node.isinf(self.c) or self.slotted:
            server_id = False
        else:
            server_id = individual.server.id_number

        record = ciw.DataRecord(
            id_number=individual.id_number,
            customer_class=individual.previous_class,
            original_customer_class=individual.original_class,
            node=self.id_number,
            arrival_date=individual.arrival_date,
            waiting_time=individual.service_start_date - individual.arrival_date,
            service_start_date=individual.service_start_date,
            service_time=individual.service_end_date - individual.service_start_date,
            service_end_date=individual.service_end_date,
            time_blocked=individual.exit_date - individual.service_end_date,
            exit_date=individual.exit_date,
            destination=individual.destination,
            queue_size_at_arrival=individual.queue_size_at_arrival,
            queue_size_at_departure=individual.queue_size_at_departure,
            server_id=server_id,
            record_type="renege" if individual.reneged_at_service else "service",
        )
        individual.data_records.append(record)

    

class RenegeAtServiceDist(ciw.dists.Distribution):
    """Distribution to handle reneging at service time.

    Attributes:
        dist_accept: Distribution for accepting customers.
        dist_renege: Distribution for reneging customers.

    Methods:
        __init__: Initializes the RenegeAtServiceDist object.
        sample: Samples the distribution to determine if a customer will renege.

    """

    def __init__(self, dist_accept: ciw.dists.Distribution, dist_renege: ciw.dists.Distribution) -> float:
        """Initializes the RenegeAtServiceDist object."""
        self.dist_accept = dist_accept
        self.dist_renege = dist_renege

    def sample(self, t=None, ind=None):
        """Samples the distribution to determine if a customer will renege.

        Args:
            t: Time parameter for the distribution (default is None).
            ind: Individual to sample for (default is None).

        Returns:
            float: The sampled value from the distribution.

        """
        selected_individual = ind
        selected_movie = selected_individual.movie
        current_node = selected_individual.simulation.nodes[selected_individual.node]
        available_tickets = current_node.available_movies[selected_movie]

        movie_sold_out = current_node.sold_out[selected_movie]
        insufficient_tickets = available_tickets < selected_individual.num_tickets
        
        if movie_sold_out or insufficient_tickets:
            selected_individual.reneged_at_service = True
        else:
            selected_individual.reneged_at_service = False
            current_node.available_movies[selected_movie] -= selected_individual.num_tickets
            if current_node.available_movies[selected_movie] < 2:
                current_node.sold_out[selected_movie] = True
                available_tickets = 0
                current_node.sold_out_time[selected_movie] = selected_individual.simulation.current_time
                
        
        if ind.reneged_at_service:
            return self.dist_renege.sample()
        return self.dist_accept.sample()


network = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(2)],
    service_distributions=[
        RenegeAtServiceDist(
            ciw.dists.Deterministic(1.0),
            ciw.dists.Deterministic(0.5)
            )
        ],
    number_of_servers=[1]
    )

results = []

for i in range(10):
    simulation = ciw.Simulation(network, arrival_node_class=TicketArrivalNode, node_class=TheatreNode)
    simulation.simulate_until_max_time(120)
    results.append(simulation.nodes[1].sold_out_time)

results = pd.DataFrame(results, columns=results[0].keys())
sns.boxplot(data=results)
plt.savefig('ciw_simpy_movie_renege.png', dpi=300)
plt.close()
```


