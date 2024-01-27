---
title: Rust Implementation of a Simple Clock DES
date: 2024-01-26 14:51:15
categories: [simulation,discrete-event-simulation,rust]
tags: [discrete-event-simulation,simulation,processes,environment,event-based-simulation,constant-random-variable,timing]
math: true
mermaid: true
---

Here is a Rust implementation of a simple event-based discrete event simulation.

First we need to import some needed libraries so that events can be implemented to have an order relation, a heap which provides the core implementation of the event schedule, and a reverse function for allowing a "min heap" behaviour so that events are scheduled chronologically.


```rust
use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::cmp::Reverse;
```

Here are the core components for implementing events as structs. Each event has a time, and some notion of ordering. I provide an implementation for the `Event` struct. Every event also has an implementation of `execute` which changes the state of the system.

```rust
#[derive(Debug, PartialEq, PartialOrd)]
struct Event {
    time: f64,
}

impl Eq for Event {}

impl Ord for Event {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Equal)
    }
}

impl Event {
    fn new(time: f64) -> Self {
        Self { time }
    }

    fn execute(&self, env: &mut Environment) {
        println!("Clock event executed at time: {}", self.time);
        env.schedule_event(Event::new(self.time + 0.5)); // Reschedule the clock event
    }
}
```

The environment struct contains the binary heap which itself will contain the events as a representation of the event schedule. The environment also has `clock` which represents the clock time in the simulation. The `schedule_event` takes a mutable reference of self and an event to be scheduled and puts in on the schedule. The `run_until` function will iteratively pop events from the event schedule, update the time, and execute the event. When the event schedule is empty or the time runs out the loop will be broken.

```rust
struct Environment {
    event_queue: BinaryHeap<Reverse<Event>>,
    clock: f64,
}

impl Environment {
    fn new() -> Self {
        Self {
            event_queue: BinaryHeap::new(),
            clock: 0.0,
        }
    }

    fn schedule_event(&mut self, event: Event) {
        self.event_queue.push(Reverse(event));
    }

    fn run_until(&mut self, end_time: f64) {
        while let Some(Reverse(current_event)) = self.event_queue.pop() {
            if current_event.time < end_time {
                self.clock = current_event.time;
                current_event.execute(self);
            } else {
                self.clock = end_time;
                break;
            }
        }
    }

    fn now(&self) -> f64 {
        self.clock
    }
}
```

The previous two components are quite generic. In a specific simulation of a hypothetical clock I define events such that they execute a 'tick' which prompts the next 'tick' of the clock. Below I run the simulation for a total of 5 units of simulated time.

```rust
fn main() {
    let mut env = Environment::new();

    // Schedule the initial clock event
    env.schedule_event(Event::new(0.0));

impl Event {
    fn new(time: f64) -> Self {
        Self { time }
    }

    fn execute(&self, env: &mut Environment) {
        println!("Clock event executed at time: {}", self.time);
        env.schedule_event(Event::new(self.time + 0.5)); // Reschedule the clock event
    }
}
    // Run the simulation until max time
    env.run_until(5.0);

    // Print the current time after simulation
    println!("Simulation ended at time: {}", env.now());
}
```

Here is the whole code together that can be copy-pasted:

```rust
// clock.rs

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

#[derive(Debug, PartialEq, PartialOrd)]
struct Event {
    time: f64,
}

impl Eq for Event {}

impl Ord for Event {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Equal)
    }
}

struct Environment {
    event_queue: BinaryHeap<Reverse<Event>>,
    clock: f64,
}

impl Environment {
    fn new() -> Self {
        Self {
            event_queue: BinaryHeap::new(),
            clock: 0.0,
        }
    }

    fn schedule_event(&mut self, event: Event) {
        self.event_queue.push(Reverse(event));
    }

    fn run_until(&mut self, end_time: f64) {
        while let Some(Reverse(current_event)) = self.event_queue.pop() {
            if current_event.time < end_time {
                self.clock = current_event.time;
                current_event.execute(self);
            } else {
                self.clock = end_time;
                break;
            }
        }
    }

    fn now(&self) -> f64 {
        self.clock
    }
}

impl Event {
    fn new(time: f64) -> Self {
        Self { time }
    }

    fn execute(&self, env: &mut Environment) {
        println!("Clock event executed at time: {}", self.time);
        env.schedule_event(Event::new(self.time + 0.5)); // Reschedule the clock event
    }
}

fn main() {
    let mut env = Environment::new();

    // Schedule the initial clock event
    env.schedule_event(Event::new(0.0));

    // Run the simulation until max time
    env.run_until(5.0);

    // Print the current time after simulation
    println!("Simulation ended at time: {}", env.now());
}

```

Next you can compile it easily:

```bash
rustc clock.rs
```

And run the simulation:

```bash
./clock
```

The simulation will print the following output:

```bash
Clock event executed at time: 0
Clock event executed at time: 0.5
Clock event executed at time: 1
Clock event executed at time: 1.5
Clock event executed at time: 2
Clock event executed at time: 2.5
Clock event executed at time: 3
Clock event executed at time: 3.5
Clock event executed at time: 4
Clock event executed at time: 4.5
Simulation ended at time: 5
```
