---
title: A Ciw Implementation of SimPy's Car Example With a Process Interaction
date: 2023-12-20 14:51:15
categories: [simulation,discrete-event-simulation,python,ciw]
tags: [simpy,discrete-event-simulation,simulation,processes,environment,python,python-generator,ciw,queueing-network,queueing-theory,routing,process-based-simulation,random-variables,constant-random-variable,arrival-distributions,service-distributions,timing,initialization]
math: true
mermaid: true
---

This post is a continuation of [*A Ciw Implementation of SimPy's Car Example*](https://galenseilis.github.io/posts/car-simpy-ciw/), and may be considered a prerequisite for reading this post.

The SimPy documentation extends the car example to have the cycling between driving and parking be interrupted. They introduce this `driver` Python generator:

```python
def driver(env: simpy.Environment, car: Car) -> Generator[simpy.events.Timeout, None, None]:
    """
    Simulates a driver interrupting the action of a car after a timeout.

    Parameters:
    - env (simpy.Environment): The simulation environment in which the driver operates.
    - car (Car): The car object representing the vehicle whose action will be interrupted.

    Yields:
    - simpy.events.Timeout: A simulation event representing the passage of time.

    Notes:
    This function yields a timeout event after 3 simulation time units, at which point
    it interrupts the action of the specified car using the `interrupt` method.

    Example:
    ```python
    import simpy

    class Car:
        def __init__(self):
            self.action = env.process(self.drive())

        def drive(self):
            while True:
                print("Car is moving.")
                yield env.timeout(1)

    env = simpy.Environment()
    car = Car()
    env.process(driver(env, car))
    env.run(until=10)
    ```
    """
    yield env.timeout(3)
    car.action.interrupt()
```

And they upgrade their car process to a class definition:

```python
from typing import Generator, NoReturn
from simpy import Environment, Process, Timeout, Interrupt

class Car(object):
    """A simulation of an electric car that alternates between parking and charging,
    and driving states within a simulation environment.

    Attributes:
        env (Environment): The simulation environment in which the car operates.
        action (Process): The simulation process representing the car's activity.

    Methods:
        __init__(self, env: Environment):
            Initializes a new instance of the Car class.

            Parameters:
                env (Environment): The simulation environment.

        run(self) -> Generator[None, None, None]:
            The main behavior loop of the car, alternating between parking and charging,
            and driving states.

        charge(self, duration: int) -> Generator[None, None, None]:
            Simulates the charging process of the car for a specified duration.

            Parameters:
                duration (int): The duration for which the car charges its battery.
    """

    def __init__(self, env: Environment) -> NoReturn:
        """
        Initializes a new instance of the Car class.

        Parameters:
            env (Environment): The simulation environment.
        """
        self.env: Environment = env
        self.action: Process = env.process(self.run())

    def run(self) -> Generator[Timeout, None, None]:
        """
        The main behavior loop of the car, alternating between parking and charging,
        and driving states.
        """
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration: float = 5

            try:
                yield self.env.process(self.charge(charge_duration))
            except Interrupt:
                print('Was interrupted. Hope, the battery is full enough ...')

            print('Start driving at %d' % self.env.now)
            trip_duration: float = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration: float) -> Generator[Timeout, None, None]:
        """
        Simulates the charging process of the car for a specified duration.

        Parameters:
            duration (float): The duration for which the car charges its battery.
        """
        yield self.env.timeout(duration)
```

The overall behavior of `Car` is not fundamentally different from before in terms of parking (with the added fluff of "charging"). The main thing that changes any of the consequent log of events is `self.action: Process = env.process(self.run())`. That is, at $t=3$ we need to print: `Was interrupted. Hope, the battery is full enough ...`.

This isn't the most interesting example, and there are more interesting examples to get to in the SimPy docs, so let's make this quick. All we need to do is update the logic in `PrintDistWrapper.sample` from last time so that it prints the message. Here is the source with a sufficient edit:


```python
from typing import Callable, NoReturn

import ciw
import hciw
from hciw.waitlist import create_existing_customers_from_list
import pandas as pd


from typing import NoReturn
import ciw

class StepDist(ciw.dists.Distribution):
    """A custom distribution representing a step function with two values.

    This distribution returns the first value until a specified time, after which
    it switches to the second value.

    Attributes:
        first_value (float): The initial value of the step function.
        second_value (float): The value of the step function after the step time.
        step_t (float): The time at which the step occurs.

    Methods:
        __init__(self, first_value: float, second_value: float, step_t: float) -> NoReturn:
            Initializes a new instance of the StepDist class.

            Parameters:
                first_value (float): The initial value of the step function.
                second_value (float): The value of the step function after the step time.
                step_t (float): The time at which the step occurs.

        sample(self, t: float = None, ind: ciw.Individual = None) -> float:
            Samples the step function at a given time.

            Parameters:
                t (float, optional): The time at which to sample the step function.
                    Defaults to None.
                ind (ciw.Individual, optional): Not used in this distribution.
                    Defaults to None.

            Returns:
                float: The sampled value of the step function at the specified time.
    """

    def __init__(self, first_value: float, second_value: float, step_t: float) -> NoReturn:
        """
        Initializes a new instance of the StepDist class.

        Parameters:
            first_value (float): The initial value of the step function.
            second_value (float): The value of the step function after the step time.
            step_t (float): The time at which the step occurs.
        """
        super().__init__()
        self.first_value: float = first_value
        self.second_value: float = second_value
        self.step_t: float = step_t

    def sample(self, t: float = None, ind: ciw.Individual = None) -> float:
        """
        Samples the step function at a given time.

        Parameters:
            t (float, optional): The time at which to sample the step function.
                Defaults to None.
            ind (ciw.Individual, optional): Not used in this distribution.
                Defaults to None.

        Returns:
            float: The sampled value of the step function at the specified time.
        """
        if t is not None and t <= self.step_t:
            return self.first_value
        else:
            return self.second_value



class PrintDistWrapper(ciw.dists.Distribution):
    """
    A wrapper class for a probability distribution that adds a print statement
    before sampling from the underlying distribution.

    Parameters:
    - dist (ciw.dists.Distribution): The underlying probability distribution to be wrapped.
    - message (str): A custom message to be printed before sampling.

    Note: This class inherits from ciw.dists.Distribution.

    Example:
    ```
    underlying_dist = SomeDistributionClass(parameters)
    wrapper_dist = PrintDistWrapper(underlying_dist, "Sampling from the distribution:")
    sample_result = wrapper_dist.sample()
    ```
    """

    def __init__(self, dist: ciw.dists.Distribution, message) -> NoReturn:
        """
        Initialize the PrintDistWrapper instance.

        Parameters:
        - dist (ciw.dists.Distribution): The underlying probability distribution to be wrapped.
        - message (str): A custom message to be printed before sampling.
        """
        super().__init__()
        self.dist = dist
        self.message = message
            
    def sample(self, t=None, ind=None):
        """
        Generate a sample from the underlying distribution, printing a custom message.

        Parameters:
        - t: Optional parameter (if applicable to the underlying distribution).
        - ind: Optional parameter (if applicable to the underlying distribution).

        Returns:
        - The sampled value from the underlying distribution.

        Note: This method overrides the sample method of ciw.dists.Distribution.
        """
        if ind.node == 2 and t == 3:
            if t == 3:
                print('Was interrupted. Hope, the battery is full enough ...')
        else:
                print(self.message, t)
            
        return self.dist.sample(t, ind)
        




arrival_dists = [ciw.dists.Sequential([0, float('inf')]), None]
service_dists = [PrintDistWrapper(StepDist(3,5,3), 'Start parking at'), PrintDistWrapper(ciw.dists.Deterministic(2), 'Start driving at')]
num_servers = [1, 1]
R = [[0, 1], [1, 0]]

network = ciw.create_network(
    arrival_distributions = arrival_dists,
    service_distributions = service_dists,
    number_of_servers = num_servers,
    routing=R
    )

simulation = ciw.Simulation(network)

simulation.simulate_until_max_time(15)
```

And the output will be the desired

```python
Start parking at 0
Was interrupted. Hope, the battery is full enough ...
Start parking at 5
Start driving at 10
Start parking at 12
```

Onward! 🚀
