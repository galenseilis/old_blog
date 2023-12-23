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
| Original author(s) | [Geraint Palmer](https://github.com/geraintpalmer/), [Vincent Knight](https://github.com/drvinceknight/), [Paul Harper](https://sites.google.com/site/profpaulharper/home), and Asyl Hawa |
| Developer(s) | [Ciw Development Team and Contributors](https://ciw.readthedocs.io/en/latest/Reference/authors.html) |
| Initial release | 14th of December, 2015 |
| Repository | [github.com/CiwPython/Ciw](https://github.com/CiwPython/Ciw){:target="_blank"} |
| Written in | Python |
| Operating system | Cross-platform |
| Type | [Discrete event simulation](https://en.wikipedia.org/wiki/Discrete-event_simulation), [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory){:target="_blank"} |
| License | [MIT](https://en.wikipedia.org/wiki/MIT_License){:target="_blank"} |
| Website | [ciw.readthedocs.io](https://ciw.readthedocs.io/en/latest/){:target="_blank"} |

## Ciw

Ciw is a three-phase approach discrete-event simulation framework specialized in simulating queueing networks.<sup>[1][1]{:target="_blank"}</sup> It enables configuration and customization of arrival distributions, service disciplines, service time distributions, and routing. While the documentation emphasizes that Ciw can be used for open queueing networks,<sup>[2][2]{:target="_blank"}</sup>  it can also be used to simulate closed queueing networks by designing the system's routing behaviour such that individuals never leave.

"Ciw" is Welsh for "queue".<sup>[2][2]{:target="_blank"}</sup> 

Here is Geraint Palmer back in 2016 introducing the package at Pycon UK 2016:

<iframe width="560" height="315" src="https://www.youtube.com/embed/0_sIus0mPSM?si=ifG6m0hSm9cezrZD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Overview

Ciw uses an event scheduling approach composed of three types of events: A, B, and C. A-type events move the system's clock forward in time. B-type events have been per-scheduled. C-type events are events triggered by B-type events.<sup>[3][3]{:target="_blank"}</sup> 

Ciw simulations are "time-to-event", meaning that time between events are skipped over in the simulation.<sup>[4][4]{:target="_blank"}</sup>  This approach becomes more efficient relative to simulating the state for every time step as the linear density of events over time decreases. Ciw uses an arbitrary scale of time so it is the responsibility of the user to decide whether the base unit of the simulation is in second, minutes, hours, days, years or some other unit.

The core Python classes in Ciw include Simulation, ArrivalNode, ExitNode, Server, and Individual.<sup>[5][5]{:target="_blank"}</sup> The simulation object is responsible for running the simulation, running a state tracker, and recording a log. The arrival node is responsible for generating individuals as the unit that flows through the network. Individuals either remain in the network, or they go to a terminating state called the "exit node". Servers are the units of capacity that limit how many individuals can be served at a node in parallel.

There are also some abstractions in Ciw oriented around the topic of input and a queue representation. These include Network, ServiceCentre, CustomerClasses, and Distributions.<sup>[5][5]{:target="_blank"}</sup>

Two optional components of Ciw are the abstractions of StateTracker and DeadlockDetector.<sup>[5][5]{:target="_blank"}</sup> The state trackers are responsible for collecting aggregrate information of the state of the simulation.<sup>[6][6]{:target="_blank"}</sup> An example is system population tracker, which records the overall number of individuals in the queueing network for each time when an event occurs. The dead lock detector is for Type I blocking,<sup>[3][3]{:target="_blank"}</sup> which is one of three types of blocking.<sup>[7][7]{:target="_blank"},[8][8]{:target="_blank"}</sup>

Although it does not have an explicitly recreational scope, Ciw has been used for recreation in the form of simulating an asynchronous variant of snakes and ladders.<sup>[9][9]{:target="_blank"}</sup>

Ciw v3.1.0 requires Python 3.7 or greater.<sup>[10][10]{:target="_blank"}</sup> The project has had 15-17 contributors as of December 18th, 2023.<sup>[11][11]{:target="_blank"},[12][12]{:target="_blank"}</sup>

## Features

This section lists many of the features available in Ciw. While Ciw be used to implement any queueing network which can be specified in standard Kendall's notation, it can be configured to model queueing networks which deviate from that family of models.<sup>[13][13]{:target="_blank"}</sup>

### Distributions

Distributions are an essential component in Ciw simulations. By default they influence inter-arrival times and service times, but can also be used to define the service discipline, routing, and server behaviour at a given node. Distributions can be time-dependent, state-dependent, or both.<sup>[14][14]{:target="_blank"}</sup>

Ciw supports a variety of common distributions,<sup>[15][15]{:target="_blank"}</sup> including phase-type distributions for complicated latent state or mixing behaviour.<sup>[16][16]{:target="_blank"}</sup>

### Arrivals

When a network is initialized in Ciw, every node is assigned an inter-arrival time distribution.<sup>[17][17]{:target="_blank"}</sup> This distribution is sampled from in order to determine when the next arrival will be. The main requirement for arrival times is that they have non-negative support, which includes any of the supported distributions over non-negative number.<sup>[15][15]{:target="_blank"}</sup>

Sometimes it is desirable for batches of individuals to arrive at a node simultaneously. Ciw supports a batch arrivals feature in which the number of arriving individuals can be sampled according to a distribution.<sup>[18][18]{:target="_blank"}</sup> Batch arrivals can use many, but not all, of the available distribution because the batch sizes must be non-negative integers.

### Restricted Networks

A restricted network is a queueing network in which at least some of its queues have a constraint on the number of individuals that can be on it at once. When an individual attempts to enter a queue that is full it results in Type I blocking of that individual.<sup>[3][3]{:target="_blank"},[19][19]{:target="_blank"},[20][20]{:target="_blank"}</sup> It is possible for circular blocking (i.e. blocking along a cycle of the network) to occur, which incurs a situation called "deadlock".<sup>[21]{:target="_blank"}</sup>

### Multiple Classes of Individual

Ciw supports queueing networks with multiple classes of individual, including Kelly networks. This is a network in which there are multiple types of individuals who are distinguished in simulation by Value objects.

Once multiple classes of individual are being used in Ciw, many of the other features become individual-class-dependent. This includes arrivals, service discipline, server behaviour, and routing.

Dynamic classes of individual (i.e. the class of individual can changing) are supported in two ways in Ciw:<sup>[22][22]{:target="_blank"}</sup>

- Customer class can change after service.<sup>[22][22]{:target="_blank"}</sup>
- Customer class can change while queueing (i.e. waiting).<sup>[22][22]{:target="_blank"}</sup>

### Waiting Behaviour

In addition to customer classes being dynamic as mentioned in the previous subsection, Ciw also supports the following waiting behaviours of individuals:

- Baulking, which is when the individual does not join the queue when it attempts to (for reasons other than Type I blocking).<sup>[25][25]{:target="_blank"}</sup>
- Reneging, where the individual leaves the queue after a certain amount of time waiting. They might go to another node, or they may leave the network altogether.<sup>[26][26]{:target="_blank"}</sup>

### Routing

Routing of individuals occurs when an individual goes from one node to another having completed their service at the previous node. When there are multiple nodes there are consequently multiples places that an individual could go. Routing is the process of deciding where such individuals go.

Ciw has three approaches to routing:

- Routing matrices
- Process-based routing
- Custom routing (i.e. time and state-dependent)

#### Routing Matrices

A routing matrix is an $n \times n$ matrix (where $n$ is the number of nodes in the network) such that the $(i,j)$th element $P_{ij}$ corresponds to the probability of transitioning to node $j$ after service at node $i$.<sup>[27][27]{:target="_blank"}</sup> This is similar to a Stochastic matrix in the sense that the elements are probabilities of state transitions, however the sum of a given row can be less than one. This is due to the fact that the complement of each sum is the probability of an individual leaving the network altogether from that node. This can be donated by the following equation: 

 $$Pr[\text{Leave Network From Node}_i]= 1-\sum _{j}^{n} P_{ij}$$

When this form of routing is specified Ciw will sample which node is the next node according to the provided routing matrix, or otherwise leave the network.

#### Process-Based Routing

In process-based routing the simulation simply dictates where an individual goes as it flows through the network. Ciw has a feature in which a function returns a path to be followed.<sup>[28][28]{:target="_blank"}</sup> When an individual completes service at the final node in the path, it leaves the network.

#### Custom Routing

Through Subclassing the core Node class and overwriting its the next_node method, any time-dependent or state-dependent routing can be achieved.

An example custom is when individuals join the shortest available queue in a processor sharing system. There are a couple of implementations of this type of behaviour in the Ciw documentation.<sup>[29][29]{:target="_blank"},[30][30]{:target="_blank"}</sup>

### Service

There are multiple components to how a service works in a queueing network, including service times, service disciplines, and server behaviour.

#### Service Times

The service times follow a distribution with non-negative support.<sup>[17][17]{:target="_blank"}</sup> Any of the supported distributions can be used for service times.<sup>[15][15]{:target="_blank"}</sup>

#### Service Disciplines

A service discipline in Ciw is whatever rule determines which individual gets served next.

By default Ciw uses a first come, first serve (FCFS), which is termed first-in-first-out (FIFO) in Ciw in adherence to computer science terminology.<sup>[31][31]{:target="_blank"}</sup> Two other built-in service disciplines include "last in, first out" (LIFO) and "service in random order" SIRO.<sup>[31][31]{:target="_blank"}</sup>

When multiple classes are used, it is optionally possible to provide priority classes which achieves a priority queue service discipline.<sup>[32][32]{:target="_blank"}</sup>

As part of Ciw's create_network interface, the service discipline can be changed to any provided function which takes the individuals at a queue and returns the next individual chosen to be served. Because every individual has a reference to the simulation instance as an attribute, which has access to the complete time and state of the system, it is possible to have time and state-dependent service disciplines. This customization feature subsumes the other service disciplines mentioned above.

Process sharing is service discipline where a number of individuals are served simultaneously and the service load is shared equally among the individuals receiving the service.<sup>[33][33]{:target="_blank"}</sup> This creates a monotonic relationship between the number of individuals being served and their service time.

#### Server Behaviour

Servers represent a unit of capacity for a service center at a node.

- The number of available servers can dependent on the state.<sup>[34][34]{:target="_blank"}</sup>
- The service rate can dependent on the server.<sup>[35][35]{:target="_blank"}</sup>
- Servers themselves can have priorities which can dependent on the individual being served.<sup>[36][36]{:target="_blank"}</sup>
- The number of servers can follow a pre-calculated schedule,<sup>[37][37]{:target="_blank"}</sup> including slotted schedules.<sup>[38][38]{:target="_blank"}</sup>

### Stopping & Resuming

There are three ways to stop a Ciw simulation:

- simulate up to a maximum amount of time.<sup>[39][39]{:target="_blank"}</sup>
- simulate for a specific number of individuals to have done one of the following:<sup>[40][40]{:target="_blank"}</sup>
  - reach the Exit Node.
  - spawn at the Arrival node.
  - spawn and be accepted at the Arrival node (in case of blocking).
- simulate until a state of deadlock (restricted networks only)<sup>[21][21]{:target="_blank"}</sup>

When a simulation was run to a maximum amount of time it is possible to resume the simulation by calling the same method with an even greater maximum time.<sup>[41][41]{:target="_blank"}</sup>

### Collecting Results

When a simulation is run there is often some question to be answered based on that simulation's history or output. This can require collecting data about the state. Ciw supports this by collecting records of the completed visits (i.e. from arrival to exiting the node) by default<sup>[42][42]{:target="_blank"}</sup>, and the simulation class supports state trackers which can record selected aggregate information about the system's state.<sup>[43][43]{:target="_blank"},[6][6]{:target="_blank"}</sup>

Ciw supports the following attributes in its visit records:

|        Attribute        |                                                                                  Description                                                                                 |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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
|       `destination`       | The number of the customer’s destination, that is the next node  the customer will join after leaving the current node. If the customer  leaves the system, this will be `-1`. |
|  `queue_size_at_arrival`  | The size of the queue at the customer’s arrival date. Does not include the individual themselves.                                                                            |
| `queue_size_at_departure` | The size of the queue at the customer’s exit date. Does not include the individual themselves.                                                                               |
|        `server_id`        | The unique identification number of the server that served that customer.                                                                                                    |
|       `record_type`       | Indicates what type of data record this is. See below.                                                                                                                       |

The attribute `record_type` can be one of:

- `"service"`: a completed service
- `"interrupted service"`: an interupted service
- `"renege"`: the waiting time while a customer waited before reneging
- `"baulk"`: the record of a customer baulking
- `"rejection"`: the record of a customer being rejected due to the queue being full

## Miscellaneous

Some of the miscellaneous features of Ciw include being able to set a progress bar to display the progress of a simulation<sup>[44][44]{:target="_blank"}</sup> and set numerical calculations to be exact.<sup>[45][45]{:target="_blank"}</sup>
Extended Behaviour

There is some additional behaviour that can be obtained from Ciw that are not officially supported features.

- Ciw can be hybridized with other forms of time-dependent processes including Differential equations even it is not a built-in feature.<sup>[46][46],[47][47],[48][48]{:target="_blank"}</sup>
- Ciw does not have a built-in feature for initializing the state of the system, however the HCiw package provides this functionality.<sup>[49][49]{:target="_blank"}</sup>
- There are no utilities in Ciw to schedule non-queueing functions, but this is possible with external code.<sup>[50][50]{:target="_blank"}</sup>
- Parallel computing computing is not a built-in feature but can be utilized for repeated runs of the simulation under differing input or pseudorandom seed.<sup>[51][51]{:target="_blank"}</sup>
- While Ciw collects complete records, it does not automatically report incomplete records (i.e. those that are still in a node at the end of the simulation). It is possible to further extract that information.<sup>[52][52]{:target="_blank"}</sup>
    
## Examples

[*Anscombe's quartet, variability and studying queues with Python](https://vknight.org/unpeudemath/mathematics/2016/10/29/anscombes-quartet-variability-and-ciw.html){:target="_blank"} is a post on Vincent Knight's blog which uses Ciw.

A [list of example implementations of some classic queue models in Ciw](https://galenseilis.github.io/posts/list-of-queues-ciw/){target="_blank"} is available.

The blog post [Queueing Simulations](https://www.programmingopiethehokie.com/2023/01/queueing-simulations.html){target="_blank"} on the *programming opiethehokie* illustrates using Ciw to simulation a restricted M/M/c queueing model.

[Monks & Harper 2023](https://pubmed.ncbi.nlm.nih.gov/37881450/){target="_blank"} use Ciw to simulate an urgent care calling centre.


[1]: https://arxiv.org/abs/1710.03561 "Ciw: An open source discrete event simulation library"
[2]: https://ciw.readthedocs.io/en/latest/ "Welcome to Ciw's documentation! — Ciw 3.1.0 documentation"
[3]: https://ciw.readthedocs.io/en/latest/Background/mechanisms.html "Notes on Ciw's Mechanisms — Ciw 3.1.0 documentation"
[4]: https://www.youtube.com/watch?v=0KvA92ykPKI "Discrete-Event Simulation with Lewis Bobbermen"
[5]: https://ciw.readthedocs.io/en/latest/Background/codestructure.html "Code Structure — Ciw 3.1.0 documentation"
[6]: https://ciw.readthedocs.io/en/latest/Reference/state_trackers.html "List of Implemented State Trackers — Ciw 3.1.0 documentation"
[7]: https://www.sciencedirect.com/science/article/abs/pii/0167637786900672 "On equivalencies of blocking mechanisms in queueing networks with blocking"
[8]: https://stats.stackexchange.com/a/632255/69508 "Are there other types of blocking in queueing networks beyond Type I?"
[9]: https://galenseilis.github.io/posts/ciw-snakes-ladders/ "A Discrete Event Simulation Generalization of Snakes and Ladders Using Ciw"
[10]: https://github.com/CiwPython/Ciw "Ciw, CiwPython"
[11]: https://github.com/CiwPython/Ciw/graphs/contributors "Contributors to CiwPython/Ciw"
[12]: https://ciw.readthedocs.io/en/latest/Reference/authors.html "Authors — Ciw 3.1.0 documentation"
[13]: https://ciw.readthedocs.io/en/latest/Background/kendall.html "Kendall's Notation — Ciw 3.1.0 documentation"
[14]: https://ciw.readthedocs.io/en/latest/Guides/time_dependent.html "How to Define Time and State Dependent Distributions — Ciw 3.1.0 documentation"
[15]: https://ciw.readthedocs.io/en/latest/Reference/distributions.html "List of Supported Distributions — Ciw 3.1.0 documentation"
[16]: https://ciw.readthedocs.io/en/latest/Guides/phasetype.html "How to Set Phase-Type Distributions — Ciw 3.1.0 documentation"
[17]: https://ciw.readthedocs.io/en/latest/Guides/set_distributions.html "How to Set Arrival & Service Distributions — Ciw 3.1.0 documentation"
[18]: https://ciw.readthedocs.io/en/latest/Guides/batching.html "How to Set Batch Arrivals — Ciw 3.1.0 documentation"
[19]: https://ciw.readthedocs.io/en/latest/Tutorial-II/tutorial_vi.html "Tutorial VI: Restricted Networks — Ciw 3.1.0 documentation"
[20]: https://stats.stackexchange.com/a/632255/69508 "Are there other types of blocking in queueing networks beyond Type I?"
[21]: https://ciw.readthedocs.io/en/latest/Guides/deadlock.html "How to Detect Deadlock — Ciw 3.1.0 documentation"
[22]: https://ciw.readthedocs.io/en/latest/Guides/dynamic_customerclasses.html "How to Set Dynamic Customer Classes — Ciw 3.1.0 documentation"
[23]: https://ciw.readthedocs.io/en/latest/Guides/change-class-after-service.html#changeclass-afterservice "How to Change Customer Class After Service — Ciw 3.1.0 documentation"
[24]: https://ciw.readthedocs.io/en/latest/Guides/change-class-while-queueing.html#changeclass-whilequeueing "How to Change Customer Class While Queueing — Ciw 3.1.0 documentation"
[25]: https://ciw.readthedocs.io/en/latest/Guides/baulking.html "How to Simulate Baulking Customers — Ciw 3.1.0 documentation"
[26]: https://ciw.readthedocs.io/en/latest/Guides/reneging.html "How to Simulate Reneging Customers — Ciw 3.1.0 documentation"
[27]: https://ciw.readthedocs.io/en/latest/Tutorial-II/tutorial_v.html "Tutorial V: A Network of Queues — Ciw 3.1.0 documentation"
[28]: https://ciw.readthedocs.io/en/latest/Guides/process_based.html "How to Define Process-Based Routing — Ciw 3.1.0 documentation"
[29]: https://ciw.readthedocs.io/en/latest/Guides/behaviour/ps_routing.html "Join Shortest Queue in Processor Sharing Systems — Ciw 3.1.0 documentation"
[30]: https://ciw.readthedocs.io/en/latest/Guides/behaviour/custom_routing.html "State-dependent Routing — Ciw 3.1.0 documentation"
[31]: https://ciw.readthedocs.io/en/latest/Guides/service_disciplines.html "How to Change Service Discipline — Ciw 3.1.0 documentation"
[32]: https://ciw.readthedocs.io/en/latest/Guides/priority.html "How to Set Priority Classes — Ciw 3.1.0 documentation"
[33]: https://ciw.readthedocs.io/en/latest/Guides/processor-sharing.html "How to Simulate Processor Sharing — Ciw 3.1.0 documentation"
[34]: https://ciw.readthedocs.io/en/latest/Guides/behaviour/custom_number_servers.html "Variable Number of Servers — Ciw 3.1.0 documentation"
[35]: https://ciw.readthedocs.io/en/latest/Guides/behaviour/server_dependent_dist.html "Server-dependent Services — Ciw 3.1.0 documentation"
[36]: https://ciw.readthedocs.io/en/latest/Guides/server_priority.html "How to Set Server Priorities — Ciw 3.1.0 documentation"
[37]: https://ciw.readthedocs.io/en/latest/Guides/server_schedule.html "How to Set Server Schedules — Ciw 3.1.0 documentation"
[38]: https://ciw.readthedocs.io/en/latest/Guides/slotted.html "How to Set Slotted Services — Ciw 3.1.0 documentation"
[39]: https://ciw.readthedocs.io/en/latest/Tutorial-I/tutorial_i.html "Tutorial I: Defining & Running a Simulation — Ciw 3.1.0 documentation"
[40]: https://ciw.readthedocs.io/en/latest/Guides/sim_numcusts.html "How to Simulate For a Certain Number of Customers — Ciw 3.1.0 documentation"
[41]: https://ciw.readthedocs.io/en/latest/Guides/pause_restart.html "How to Pause and Restart the Simulation — Ciw 3.1.0 documentation"
[42]: https://ciw.readthedocs.io/en/latest/Tutorial-I/tutorial_iii.html "Tutorial III: Collecting Results — Ciw 3.1.0 documentation"
[43]: https://ciw.readthedocs.io/en/latest/Guides/state_trackers.html "How to Track the System's State — Ciw 3.1.0 documentation"
[44]: https://ciw.readthedocs.io/en/latest/Guides/progressbar.html "How to Implement a Progress Bar — Ciw 3.1.0 documentation"
[45]: https://ciw.readthedocs.io/en/latest/Guides/exact.html "How to Implement Exact Arithmetic — Ciw 3.1.0 documentation"
[46]: https://ciw.readthedocs.io/en/latest/Guides/behaviour/hybrid.html "DES+SD Hybrid Simulation with Ciw — Ciw 3.1.0 documentation"
[47]: http://www.geraintianpalmer.org.uk/2023/08/03/hybrid-simulation-ciw/ "A Guide to Building Hybrid DES+SD Simulations in Ciw"
[48]: https://orca.cardiff.ac.uk/id/eprint/145799/1/main.pdf "Implementing hybrid simulations that integrate DES+SD in Python"
[49]: https://github.com/galenseilis/HCiw/blob/main/src/hciw/waitlist.py "HCiw/src/hciw/waitlist.py at main · galenseilis/HCiw"
[50]: https://galenseilis.github.io/posts/ciw-external-schedule/ "External Schedule of Ciw Simulations"
[51]: https://ciw.readthedocs.io/en/latest/Guides/parallel_process.html "How to Parallelise Trials — Ciw 3.1.0 documentation"
[52]: https://github.com/galenseilis/HCiw/blob/main/src/hciw/results.py "HCiw/src/hciw/results.py at main · galenseilis/HCiw"
