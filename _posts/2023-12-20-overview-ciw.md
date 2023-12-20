---
title: An Overview of Ciw
date: 2023-12-20 14:51:15
categories: [simulation,discrete-event-simulation,queueing-networks,ciw]
tags: [simulation,discrete-event-simulation,queueing-networks,ciw,python,queue,queueing-theory,exponential-distribution,statistics,operations-research,random-variable,inter-arrival-time,service-time,random-number-generator,seed,servers]
math: true
mermaid: true
---

| Attribute | Description |
| --- | --- |
| Original author(s) | Geraint Palmer, Vincent Knight, Paul Harper, and Asyl Hawa |
| Developer(s) | Ciw Development Team and Contributors |
| Initial release | 14 December 2015 |
| Repository | github.com/CiwPython/Ciw |
| Written in | Python |
| Operating system | Cross-platform |
| Type | Discrete event simulation,Queueing theory |
| License | MIT |
| Website | ciw.readthedocs.io |

## Ciw

Ciw is a three-phase approach discrete-event simulation framework specialized in simulating queueing networks.[1] It enables configuration and customization of arrival distributions, service disciplines, service time distributions, and routing. While the documentation emphasizes that Ciw can be used for open queueing networks,[2] it can also be used to simulate closed queueing networks by designing the system's routing behaviour such that individuals never leave.

"Ciw" is Welsh for "queue".[2]

## Overview

Ciw uses an event scheduling approach composed of three types of events: A, B, and C. A-type events move the system's clock forward in time. B-type events have been per-scheduled. C-type events are events triggered by B-type events.[3]

Ciw simulations are "time-to-event", meaning that time between events are skipped over in the simulation.[4] This approach becomes more efficient relative to simulating the state for every time step as the linear density of events over time decreases. Ciw uses an arbitrary scale of time so it is the responsibility of the user to decide whether the base unit of the simulation is in second, minutes, hours, days, years or some other unit.

The core Python classes in Ciw include Simulation, ArrivalNode, ExitNode, Server, and Individual.[5] The simulation object is responsible for running the simulation, running a state tracker, and recording a log. The arrival node is responsible for generating individuals as the unit that flows through the network. Individuals either remain in the network, or they go to a terminating state called the "exit node". Servers are the units of capacity that limit how many individuals can be served at a node in parallel.

There are also some abstractions in Ciw oriented around the topic of input and a queue representation. These include Network, ServiceCentre, CustomerClasses, and Distributions.[5]

Two optional components of Ciw are the abstractions of StateTracker and DeadlockDetector.[5] The state trackers are responsible for collecting aggregrate information of the state of the simulation.[6] An example is system population tracker, which records the overall number of individuals in the queueing network for each time when an event occurs. The dead lock detector is for Type I blocking[3], which is one of three types of blocking .[7][8]

Although it does not have an explicitly recreational scope, Ciw has been used for recreation in the form of simulating an asynchronous variant of snakes and ladders.[9]

Ciw v3.1.0 requires Python 3.7 or greater.[10] The project has had 15-17 contributors as of December 18th, 2023.[11][12]
Features

This section lists many of the features available in Ciw. While Ciw be used to implement any queueing network which can be specified in standard Kendall's notation, it can be configured to model queueing networks which deviate from that family of models.[13]
Distributions

Distributions are an essential component in Ciw simulations. By default they influence inter-arrival times and service times, but can also be used to define the service discipline, routing, and server behaviour at a given node. Distributions can be time-dependent, state-dependent, or both.[14]

Ciw supports a variety of common distributions,[15] including phase-type distributions for complicated latent state or mixing behaviour.[16]

### Arrivals

When a network is initialized in Ciw, every node is assigned an inter-arrival time distribution.[17] This distribution is sampled from in order to determine when the next arrival will be. The main requirement for arrival times is that they have non-negative support, which includes any of the supported distributions over non-negative number.[15]

Sometimes it is desirable for batches of individuals to arrive at a node simultaneously. Ciw supports a batch arrivals feature in which the number of arriving individuals can be sampled according to a distribution.[18] Batch arrivals can use many, but not all, of the available distribution because the batch sizes must be non-negative integers.

### Restricted Networks

A restricted network is a queueing network in which at least some of its queues have a constraint on the number of individuals that can be on it at once. When an individual attempts to enter a queue that is full it results in Type I blocking of that individual.[3][19][20] It is possible for circular blocking (i.e. blocking along a cycle of the network) to occur, which incurs a situation called "deadlock".[21]

### Multiple Classes of Individual

Ciw supports queueing networks with multiple classes of individual, including Kelly networks. This is a network in which there are multiple types of individuals who are distinguished in simulation by Value objects.

Once multiple classes of individual are being used in Ciw, many of the other features become individual-class-dependent. This includes arrivals, service discipline, server behaviour, and routing.

Dynamic classes of individual (i.e. the class of individual can changing) are supported in two ways in Ciw:[22]

- Customer class can change after service.[23]
- Customer class can change while queueing (i.e. waiting).[24]

### Waiting Behaviour

In addition to customer classes being dynamic as mentioned in the previous subsection, Ciw also supports the following waiting behaviours of individuals:

- Baulking, which is when the individual does not join the queue when it attempts to (for reasons other than Type I blocking).[25]
- Reneging, where the individual leaves the queue after a certain amount of time waiting. They might go to another node, or they may leave the network altogether.[26]

### Routing

Routing of individuals occurs when an individual goes from one node to another having completed their service at the previous node. When there are multiple nodes there are consequently multiples places that an individual could go. Routing is the process of deciding where such individuals go.

Ciw has three approaches to routing:

- Routing matrices
- Process-based routing
- Custom routing (i.e. time and state-dependent)

#### Routing Matrices

A routing matrix is an n × n n\times n matrix (where n n is the number of nodes in the network) such that the ( i , j ) (i,j)th element P i j P_{ij} corresponds to the probability of transitioning to node j j after service at node i i.[27] This is similar to a Stochastic matrix in the sense that the elements are probabilities of state transitions, however the sum of a given row can be less than one. This is due to the fact that the complement of each sum is the probability of an individual leaving the network altogether from that node. This can be donated by the following equation: 

 $$P r [ Leave Network From Node  i ] = 1 − ∑ j n P i j {\displaystyle Pr[{\text{Leave Network From Node }}i]=1-\sum _{j}^{n}P_{ij}}$$

When this form of routing is specified Ciw will sample which node is the next node according to the provided routing matrix, or otherwise leave the network.

#### Process-Based Routing

In process-based routing the simulation simply dictates where an individual goes as it flows through the network. Ciw has a feature in which a function returns a path to be followed.[28] When an individual completes service at the final node in the path, it leaves the network.

#### Custom Routing

Through Subclassing the core Node class and overwriting its the next_node method, any time-dependent or state-dependent routing can be achieved.

An example custom is when individuals join the shortest available queue in a processor sharing system. There are a couple of implementations of this type of behaviour in the Ciw documentation.[29][30]

### Service

There are multiple components to how a service works in a queueing network, including service times, service disciplines, and server behaviour.

#### Service Times

The service times follow a distribution with non-negative support.[17] Any of the supported distributions can be used for service times.[15]

#### Service Disciplines

A service discipline in Ciw is whatever rule determines which individual gets served next.

By default Ciw uses a first come, first serve (FCFS), which is termed first-in-first-out (FIFO) in Ciw in adherence to computer science terminology.[31] Two other built-in service disciplines include "last in, first out" (LIFO) and "service in random order" SIRO.[31]

When multiple classes are used, it is optionally possible to provide priority classes which achieves a priority queue service discipline.[32]

As part of Ciw's create_network interface, the service discipline can be changed to any provided function which takes the individuals at a queue and returns the next individual chosen to be served. Because every individual has a reference to the simulation instance as an attribute, which has access to the complete time and state of the system, it is possible to have time and state-dependent service disciplines. This customization feature subsumes the other service disciplines mentioned above.

Process sharing is service discipline where a number of individuals are served simultaneously and the service load is shared equally among the individuals receiving the service.[33] This creates a monotonic relationship between the number of individuals being served and their service time.

#### Server Behaviour

Servers represent a unit of capacity for a service center at a node.

- The number of available servers can dependent on the state.[34]
- The service rate can dependent on the server.[35]
- Servers themselves can have priorities which can dependent on the individual being served.[36]
- The number of servers can follow a pre-calculated schedule,[37] including slotted schedules.[38]

### Stopping & Resuming

There are three ways to stop a Ciw simulation:

    simulate up to a maximum amount of time.[39]
    simulate for a specific number of individuals to have done one of the following:[40]
        reach the Exit Node.
        spawn at the Arrival node.
        spawn and be accepted at the Arrival node (in case of blocking).
    simulate until a state of deadlock (restricted networks only)[21]

When a simulation was run to a maximum amount of time it is possible to resume the simulation by calling the same method with an even greater maximum time.[41]

### Collecting Results

When a simulation is run there is often some question to be answered based on that simulation's history or output. This can require collecting data about the state. Ciw supports this by collecting records of the completed visits (i.e. from arrival to exiting the node) by default[42], and the simulation class supports state trackers which can record selected aggregate information about the system's state.[43][6]

Ciw supports the following attributes in its visit records:

|        Attribute        |                                                                                  Description                                                                                 |
|:-----------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|        `id_number`        | The unique identification number for that customer.                                                                                                                          |
|      `customer_class`     | The number of that customer’s customer class. If dynamic customer  classes are used, this is the customer’s class that they were when they  recieved service at that node.   |
| `original_customer_class` | The number of the customer’s class when they arrived at the node.                                                                                                            |
|           `node`          | The number of the node at which the service took place.                                                                                                                      |
|       `arrival_date`      | The date of arrival to that node, the date which the customer joined the queue.                                                                                              |
|       `waiting_time`      | The amount of time the customer spent waiting for service at that node.                                                                                                      |
|    `service_start_date`   | The date at which service began at that node.                                                                                                                                |
|       `service_time`      | The amount of time spent in service at that node.                                                                                                                            |
|     `service_end_date`    | The date which the customer finished their service at that node.                                                                                                             |
|       `time_blocked`      | The amount of time spent blocked at that node. That is the time between finishing service at exiting the node.                                                               |
|        `exit_date`        | The date which the customer exited the node. This may be  immediatly after service if no blocking occured, or after some period of  being blocked.                           |
|       `destination`       | The number of the customer’s destination, that is the next node  the customer will join after leaving the current node. If the customer  leaves the system, this will be -1. |
|  `queue_size_at_arrival`  | The size of the queue at the customer’s arrival date. Does not include the individual themselves.                                                                            |
| `queue_size_at_departure` | The size of the queue at the customer’s exit date. Does not include the individual themselves.                                                                               |
|        `server_id`        | The unique identification number of the server that served that customer.                                                                                                    |
|       `record_type`       | Indicates what type of data record this is. See below.                                                                                                                       |

The attribute `record_type` can be one of:

- "service": a completed service
- "interrupted service": an interupted service
- "renege": the waiting time while a customer waited before reneging
- "baulk": the record of a customer baulking
- "rejection": the record of a customer being rejected due to the queue being full

## Miscellaneous

Some of the miscellaneous features of Ciw include being able to set a progress bar to display the progress of a simulation[44] and set numerical calculations to be exact.[45]
Extended Behaviour

There is some additional behaviour that can be obtained from Ciw that are not officially supported features.

- Ciw can be hybridized with other forms of time-dependent processes including Differential equations even it is not a built-in feature.[46][47][48]
- Ciw does not have a built-in feature for initializing the state of the system, however the HCiw package provides this functionality.[49]
- There are no utilities in Ciw to schedule non-queueing functions, but this is possible with external code.[50]
- Parallel computing computing is not a built-in feature but can be utilized for repeated runs of the simulation under differing input or pseudorandom seed.[51]
- While Ciw collects complete records, it does not automatically report incomplete records (i.e. those that are still in a node at the end of the simulation). It is possible to further extract that information.[52]
    
## Examples

A [list of example implementations of some classic queue models in Ciw](https://galenseilis.github.io/posts/list-of-queues-ciw/) is available.

## References

- [1] Palmer, Geraint I.; Knight, Vincent A.; Harper, Paul R.; Hawa, Asyl L. (2017-09-27), Ciw: An open source discrete event simulation library, doi:10.48550/arXiv.1710.03561, retrieved 2023-12-18
- [2] "Welcome to Ciw's documentation! — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [3] "Notes on Ciw's Mechanisms — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [4] Discrete-Event Simulation with Lewis Bobbermen, retrieved 2023-12-19
- [5] "Code Structure — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [6] "List of Implemented State Trackers — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [7] Onvural, Raif O.; Perros, H. G. (1986-12-01). "On equivalencies of blocking mechanisms in queueing networks with blocking". Operations Research Letters. 5 (6): 293–297. doi:10.1016/0167-6377(86)90067-2. ISSN 0167-6377.
- [8] "Are there other types of blocking in queueing networks beyond Type I?". Cross Validated. Retrieved 2023-12-19.
- [9] "A Discrete Event Simulation Generalization of Snakes and Ladders Using Ciw". Galen’s Blog. 2023-11-25. Retrieved 2023-12-19.
- [10] Ciw, CiwPython, 2023-11-29, retrieved 2023-12-19
- [11] "Contributors to CiwPython/Ciw". GitHub. Retrieved 2023-12-19.
- [12] "Authors — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [13] "Kendall's Notation — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [14] "How to Define Time and State Dependent Distributions — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [15] "List of Supported Distributions — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [16] "How to Set Phase-Type Distributions — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [17] "How to Set Arrival & Service Distributions — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [18] "How to Set Batch Arrivals — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [19] "Tutorial VI: Restricted Networks — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [20] "Are there other types of blocking in queueing networks beyond Type I?". Cross Validated. Retrieved 2023-12-19.
- [21] "How to Detect Deadlock — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [22] "How to Set Dynamic Customer Classes — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [23] "How to Change Customer Class After Service — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [24] "How to Change Customer Class While Queueing — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [25] "How to Simulate Baulking Customers — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [26] "How to Simulate Reneging Customers — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [27] "Tutorial V: A Network of Queues — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [28] "How to Define Process-Based Routing — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [29] "Join Shortest Queue in Processor Sharing Systems — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [30] "State-dependent Routing — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [31] "How to Change Service Discipline — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [32] "How to Set Priority Classes — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [33] "How to Simulate Processor Sharing — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [34] "Variable Number of Servers — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [35] "Server-dependent Services — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [36] "How to Set Server Priorities — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [37] "How to Set Server Schedules — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [38] "How to Set Slotted Services — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [39] "Tutorial I: Defining & Running a Simulation — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [40] "How to Simulate For a Certain Number of Customers — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [41] "How to Pause and Restart the Simulation — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [42] "Tutorial III: Collecting Results — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [43] "How to Track the System's State — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [44] "How to Implement a Progress Bar — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [45] "How to Implement Exact Arithmetic — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [46] "DES+SD Hybrid Simulation with Ciw — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [47] "A Guide to Building Hybrid DES+SD Simulations in Ciw". www.geraintianpalmer.org.uk. Retrieved 2023-12-19.
- [48] Palmer, Geraint I.; Tian, Yawen (2023-05-04). "Implementing hybrid simulations that integrate DES+SD in Python". Journal of Simulation. 17 (3): 240–256. doi:10.1080/17477778.2021.1992312. ISSN 1747-7778.
- [49] "HCiw/src/hciw/waitlist.py at main · galenseilis/HCiw". GitHub. Retrieved 2023-12-19.
- [50] "External Schedule of Ciw Simulations". Galen’s Blog. 2023-10-24. Retrieved 2023-12-19.
- [51] "How to Parallelise Trials — Ciw 3.1.0 documentation". ciw.readthedocs.io. Retrieved 2023-12-19.
- [52] "HCiw/src/hciw/results.py at main · galenseilis/HCiw". GitHub. Retrieved 2023-12-19.
