---
title: External Schedule of Ciw Simulations
date: 2023-10-25 00:50:15
categories: [discrete-event-simulation,queueing-networks,ciw]
tags: [discrete-event-simulation,queueing-networks,ciw,python,computer-programming,]
math: true
mermaid: true
---

It would be desirable to make arbitrary changes to the state of a simulation according to a schedule. This is useful to simulating emergencies and disasters where the system has a change point where its behaviour changes substantially.

```python
import ciw

from <local_script> import ops

schedule = ( # Ordered schedule of time-to-event and the functions to be applied to update the state of a simulation.
(10, (ops.func1, ops.func2)), 
(30, (ops.func1,)), 
(23, (ops.func1,))
)

def scheduled_changes(sim, sched):
	'''
	parameters:
		sim: Ciw Simulation
		sched (tuple): tuple of times and functions 
	'''
	for event in events:
		time_to, funcs = event
		sim.simulate_until_max_time(sim.current_time + time_to)
		for func in funcs:
			sim = func(sim) # Transform the state of the simulation
	return sim
```

The above is a rough prototype. It assumes that the time-to-events are constants fixed ahead of time, but I could see extension to this where the time-to-events change depending on what has happened in the simulation so far. Likewise, control flow to change the events that occur depending on the state might also be beneficial.
