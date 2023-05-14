> **Question**
>
> Write a simple queue model in SimPy.


> **Answer**
>
> Sure! Here's an example of a simple queue model in SimPy:

```python
import simpy

class Queue:
    def __init__(self, env, capacity):
        self.env = env
        self.capacity = capacity
        self.items = []

    def enqueue(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            print("Queue is full, can't enqueue", item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            print("Queue is empty, can't dequeue")

def customer(env, queue):
    print(f"Customer arrives at {env.now}")
    queue.enqueue(env.now)
    yield env.timeout(1)
    print(f"Customer leaves at {env.now}")
    queue.dequeue()

env = simpy.Environment()
queue = Queue(env, capacity=5)
env.process(customer(env, queue))
env.run(until=5)
```

> In this example, we define a Queue class that has a capacity and a list of items. The enqueue method adds an item to the list if there is capacity, and the dequeue method removes the first item from the list if it exists.
>
> We then define a customer process that arrives at the queue, enqueues itself, waits for 1 time unit (in this case, we use seconds), dequeues itself, and then leaves. Finally, we create an environment, a queue, and a customer process and run the simulation for 5 time units.
>
> Note that this is a very simple example and does not take into account many real-world factors, such as different customer arrival rates, service times, and priorities. However, it should give you an idea of how to create a basic queue model in SimPy.
