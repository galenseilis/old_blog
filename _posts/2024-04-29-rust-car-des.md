---
title: A Rust Implementation of a Simple Car DES
date: 2024-04-29 14:51:15
categories: [simulation,discrete-event-simulation,rust]
tags: [discrete-event-simulation,simulation,processes,environment,event-based-simulation,constant-random-variable,timing,rust,computer-programming,simpy]
math: true
mermaid: true
---

This post gives an implementation of [this example](https://simpy.readthedocs.io/en/latest/simpy_intro/basic_concepts.html) from the SimPy documentation:

```python
import simpy

def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

if __name__ == '__main__':
	env = simpy.Environment()
	env.process(car(env))
	env.run(until=15)
```

Based on my post [*A Rust Implementation of a Simple Clock DES*](https://galenseilis.github.io/posts/rust-clock-des/) I implemented the above car example. The major difference is the introduction of enums for driving events and parking events rather than just having a single type of event.


```rust
// car.rs

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

#[derive(Debug, PartialEq, PartialOrd)]
enum EventType {
    Parking,
    Driving,
}

#[derive(Debug, PartialEq, PartialOrd)]
struct Event {
    time: f64,
    event_type: EventType
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
    fn new(time: f64, event_type: EventType) -> Self {
        Self { time, event_type }
    }

    fn execute(&self, env: &mut Environment) {
        match self.event_type {
            EventType::Parking => {
                println!("Start parking at {}", self.time);
                let parking_duration = 5.0;
                env.schedule_event(Event::new(self.time + parking_duration, EventType::Driving));
            }
            EventType::Driving => {
                println!("Start driving at {}", self.time);
                let trip_duration = 2.0;
                env.schedule_event(Event::new(self.time + trip_duration, EventType::Parking));
            }
        }
    }
}

fn main() {
    let mut env = Environment::new();

    // Schedule the initial clock event
    env.schedule_event(Event::new(0.0, EventType::Parking));

    // Run the simulation until max time
    env.run_until(15.0);

}
```

I was curious to get a sense of the run time performance of my Rust implementation vs the SimPy implementation. I ran the following script to collect the run times of these two implementations (with and without PyPy3 for the SimPy implementation).

```python
import subprocess
import time

import matplotlib.pyplot as plt
import pandas as pd

REPLICATES = 1000

rust_cmd = ["./car"]
simpy_cmd = ["python3", "simpy_car.py"]
pypy_simpy_cmd = ["pypy3", "simpy_car.py"]

COMMANDS = [rust_cmd, simpy_cmd, pypy_simpy_cmd]


def capture_execution_time(command):
    try:
        # Run the command and capture both stdout and stderr
        result = subprocess.run(
            ["/usr/bin/time", "-v"] + command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )

        # Check for errors
        result.check_returncode()

        # Extract time information from stderr
        time_info = result.stderr

        return time_info

    except subprocess.CalledProcessError as e:
        # Handle errors, if any
        print(f"Error: {e}")
        return None


results = []
for command in COMMANDS:
    for _ in range(REPLICATES):
        result = capture_execution_time(command)
        if result is not None:
            result = [
                line.replace("\t", "").replace("\n", "").split(": ")
                for line in result.split("\n\t")
            ]
            result = {i[0]: i[1] for i in result}
            print(_, result["Command being timed"], result["User time (seconds)"])
            results.append(result)


df = pd.DataFrame(results)

for col in df.columns:
    try:
        df[col] = df[col].astype(float)
    except Exception as e:
        print(e)

df.to_csv("results.csv", index=False)
```

With the results in a simple file format, I used common libraries to plot histograms of the run times.

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("results.csv")


# Histogram
for group, groupdf in df.groupby("Command being timed"):
    plt.hist(groupdf["User time (seconds)"], label=group, bins=30)

plt.ylabel("Frequency")
plt.xlabel("Run Time (seconds)")
plt.xscale("log")
plt.legend()
plt.savefig("run_time_hist.png", dpi=300, transparent=True)
plt.close()


# Markdown table
result = ""

for group, group_df in df.groupby("Command being timed"):
    result += group.replace('"', "`") + "\n\n"
    result += group_df.describe().to_markdown() + "\n\n"

with open("results.md", "w") as f:
    f.write(result)
```

Here are the results:

![](./assets/images/run_time_hist_car_rust_vs_simpy.png)

Clearly the Rust implementation is faster. I would naïvely attribute that to Rust being a compiled (and statically typed) language that also doesn't have a garbage collector. Interestly the PyPy3 interpreter was actually slower than the CPython interpreter in this case.
