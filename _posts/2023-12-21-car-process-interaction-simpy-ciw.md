---
title: A Ciw Implementation of SimPy's Car Example
date: 2023-12-20 14:51:15
categories: [mathematics,symmetry]
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

What the driver Python generator does is raise a Python exception after 3 units of simulation time have elapsed.
