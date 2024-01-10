---
title: A Ciw Implementation of SimPy's Clock Example
date: 2023-12-19 08:49:15
authors: [galen]
categories: [discrete-event-simulation]
tags: [python,discrete-event-simulation,ciw,simpy,queueing-theory,queueing-network,process-based-simulation,dirac-delta-distribution,constant-random-variable,random-variables,arrival-distributions,service-distributions,timing,warm-up,intitialization]
math: true
mermaid: true
---


## Introduction

This post looks at implementing a simple simulation described in the SImPy documentation using the Ciw Python package.

## SimPy Simulation
On the home page of the [SimPy](https://simpy.readthedocs.io/en/latest/) documentation there is an example of a clock:

```python
import simpy
def clock(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)

env = simpy.Environment()

env.process(clock(env, 'fast', 0.5))
env.process(clock(env, 'slow', 1))

env.run(until=2)
```

It involves two clocks that tick deterministically at two distinct rates. One clock ticks at a rate of 0.5 units of time. The other clock ticks at 1 unit of time. This simulation runs for two units of time total. Here is the printout of the SimPy simulation:

```python
fast 0
slow 0
fast 0.5
slow 1
fast 1.0
fast 1.5
```

## Ciw Simulation
Let's do this in Ciw. First, we need to import Ciw, and I would also like Pandas for a later processing step.

```python
import ciw
import pandas
```

We 'could' just use the `ciw.dists.Deterministic` and a simple loop achieve the same output, but that would seem to ignore how Ciw is motivated.  Ciw is for queueing models, so let's keep to that aim. Instead of taking the easy way, let's map our understanding of the clock problem into being a queueing network problem so that we can follow the typical Ciw workflow.

Let us take each clock to be a node in a queueing network. We will consider the case of two clocks as per the original example.

Our clocks are not self-contained like ordinary clocks. They require an input signal to tell them when to tick. We will call these discrete units of signal "packets". The clocks and the inputs/outputs act as completely separate systems, so for our two clocks we can assume the following routing matrix:

$$R = \begin{bmatrix}0 & 0 \\ 0 & 0 \end{bmatrix}$$

which means that packets that are used at a clock are never seen again. They leave, or are consumed, or... something. 👻 

Such a routing matrix can be tersely written in Python as a nested list:

```python
routing = [[0] * 2] * 2
```

The servers at each clock are some component of the clock that make it tick, called a "ticker". 😉 Each clock has only one ticker. For Ciw, this means that each node has only one server, which we can represent in a list:

```python
number_of_tickers = [1, 1]
```

We can treat each completed tick of these clocks as the completion of a service. Each clock completes a tick at an exact deterministic rate, so the inter-arrival times of ticks are [constant random variables](https://en.wikipedia.org/wiki/Degenerate_distribution#Constant_random_variable).We can think of these service times mathematically as

$$T_{\text{service}} \sim \delta \left( s \right)$$

where $\delta$ is the [Dirac delta distribution](https://en.wikipedia.org/wiki/Dirac_delta_function) and $s$ the "speed parameter" for the clock's ticks. We can store our clock speeds in a list:

```python
clock_speeds = [0.5, 1]
```

In order to ensure that each ticker has a correctly-timed packet we must consider the arrival times of packets onto the queue. If we provide too few packets then the clock won't keep time; ticks will be delayed. If we provide more packets than necessary then we will start to have a queue filling up with packets which is a waste of memory. Instead we should have packets arrive at the same rate that they are needed. Thus the arrival rate will also equal:

$$T_{\text{arrivals}} \sim \delta \left( s \right)$$

Because the order of the packets doesn't matter, the [service discipline](https://en.wikipedia.org/wiki/Network_scheduler)doesn't either. We'll allow Ciw to use its default of first-come, first-serve, but it wouldn't matter if we used something else.

Just because we have the rates of change correct doesn't mean that we are starting in the correct state. The last, and trickiest, business of this exercise is to start the system with the correct number of packets. If it takes $s$ units of time for a packet to arrive and it takes another $s$ units of time for a packet to be processed into a tick, then each packet has a sojourn time of $2s$. Which means that at the start of the simulation there will be a delay before the clocks start ticking. We could chalk this up to simulation [warm-up](https://ciw.readthedocs.io/en/latest/Tutorial-I/tutorial_iv.html), but let's get this right. What we can do is have a distribution that 

$$f(t; s, c, \ell) = \begin{cases} \delta \left( 0 \right) & t \leq 0 \land c < \ell \\ \delta \left( s \right) & \text{Otherwise} \end{cases}$$

where $t$ is the simulation time, $c \in \mathbb{N}_0$ is a count of how many times the distribution has been used at or before $t = 0$, and $\ell \in \mathbb{N}_0$  is the maximum number of times that we will allow this distribution to be used for $t \leq 0$. Kinda weird, right? What it specifies is that we can pass packets into the system that take zero units of time to arrive and zero units of time to process. That will allow us to have a couple of packets run straight away! One implementation of Python for this looks like this:

```python
class IASDeterministic(ciw.dists.Distribution):
    """
    Represents an "instant at start" (IAS) deterministic distribution.

    This distribution generates values based on an initial value, and it can be limited
    to a specified number of samples to be initially generated.

    Parameters:
        value (float): The fixed value to be returned by the distribution.
        limit (int, optional): The maximum number of samples to be initially generated. Defaults to 1.

    Attributes:
        value (float): The fixed value to be returned by the distribution.
        count (int): The current count of samples generated.
        limit (int): The maximum number of samples to be initially generated.

    Methods:
        sample(t=None, ind=None):
            Generates a sample from the distribution.

    Example:
        >>> dist = IASDeterministic(value=3.14, limit=2)
        >>> dist.sample(0)
        0
        >>> dist.sample(0)
        0
        >>> dist.sample(0)
        3.14
    """

    def __init__(self, value: float, limit: float = 1) -> NoReturn:
        """
        Initializes the IASDeterministic distribution with the given parameters.

        Parameters:
            value (float): The fixed value to be returned by the distribution.
            limit (int, optional): The maximum number of samples to be initially generated. Defaults to 1.
        """
        self.value = value
        self.count = 0
        self.limit = limit
    
    def sample(self, t:float = None, ind: ciw.Individual = None) -> float:
        """
        Generates a sample from the distribution.

        Parameters:
            t (float, optional): Time parameter.
            ind (int, optional): Index parameter.

        Returns:
            float: The fixed value if conditions are met; otherwise, returns None.
        """
        if t  <= 0 and self.count < self.limit:
            self.count += 1
            return 0
        else:
            return self.value

    def __repr__(self):
        return f"IASDistribution(value={self.value}, limit={self.limit})"
```

Okay, that's a decent chunk of code but it is mostly just docstrings. All it does is initialize the system as we discussed. We can make one of these for each node's arrival and service distributions:

```python
arrival_dists = [IASDeterministic(speed, 2) for speed in clock_speeds]
service_dists = [IASDeterministic(speed) for speed in clock_speeds]
```

You may have noticed that for arrival distributions that we put the limit at two packets rather than 1. This is because we need one packet to be processed at $t=0$ but also have another ready at $t=0$ to begin service using the post-initialization rate.

If you have not used Ciw before, you may be wondering how we put these pieces together. In Ciw everything about the design of the queueing network goes into the `ciw.create_network` function.

```python
network = ciw.create_network(
    arrival_distributions = arrival_dists,
    service_distributions = service_dists,
    number_of_servers = number_of_tickers,
    routing = routing
    )
```

Now we can instantiate our simulation and run it for two units of time:

```python
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(2)
```

The simulation instance has collected records about the completed packets. Let's stick that in a Pandas dataframe, and then we'll print out the results to a markdown table.

```python
records = pd.DataFrame(simulation.get_all_records())
print(records[['node', 'exit_date']].to_markdown(index=False))
```

|   node |   exit_date |
|-------:|------------:|
|      1 |         0   |
|      2 |         0   |
|      1 |         0.5 |
|      2 |         1   |
|      1 |         1   |
|      1 |         1.5 |

Note that node 1 corresponds to the fast clock, and node 2 corresponds to the slow clock. That's it. We did it. 


## Conclusions

Ciw can definitely handle this toy simulation of a pair of clocks, but it is not the most naturally suited tool for this example. It is a bit like coordinating the [BFG-10000](https://doom.fandom.com/wiki/BFG-10000) to take aim at a squirrel; more work than needed but gets the job done.
