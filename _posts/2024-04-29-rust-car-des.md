---
title: A Rust Implementation of a Simple Car DES
date: 2024-04-29 14:51:15
categories: [simulation,discrete-event-simulation,rust]
tags: [discrete-event-simulation,simulation,processes,environment,event-based-simulation,constant-random-variable,timing,rust,computer-programming,simpy]
math: true
mermaid: true
image:
    path: /assets/images/03b8d264-0ddc-4839-9471-469f0fc7be05.jpg
    alt: Simulated Cars
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

![Run Time of Rust vs SimPy Implementation](/assets/images/run_time_hist_car_rust_vs_simpy.png)

`./car`

|       |   User time (seconds) |   System time (seconds) |   Average shared text size (kbytes) |   Average unshared data size (kbytes) |   Average stack size (kbytes) |   Average total size (kbytes) |   Maximum resident set size (kbytes) |   Average resident set size (kbytes) |   Major (requiring I/O) page faults |   Minor (reclaiming a frame) page faults |   Voluntary context switches |   Involuntary context switches |   Swaps |   File system inputs |   File system outputs |   Socket messages sent |   Socket messages received |   Signals delivered |   Page size (bytes) |   Exit status |
|:------|----------------------:|------------------------:|------------------------------------:|--------------------------------------:|------------------------------:|------------------------------:|-------------------------------------:|-------------------------------------:|------------------------------------:|-----------------------------------------:|-----------------------------:|-------------------------------:|--------:|---------------------:|----------------------:|-----------------------:|---------------------------:|--------------------:|--------------------:|--------------:|
| count |                  1000 |                    1000 |                                1000 |                                  1000 |                          1000 |                          1000 |                            1000      |                                 1000 |                                1000 |                               1000       |                         1000 |                    1000        |    1000 |                 1000 |                  1000 |                   1000 |                       1000 |                1000 |                1000 |          1000 |
| mean  |                     0 |                       0 |                                   0 |                                     0 |                             0 |                             0 |                            2071.52   |                                    0 |                                   0 |                                 86.906   |                            1 |                       0.024    |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| std   |                     0 |                       0 |                                   0 |                                     0 |                             0 |                             0 |                              53.0929 |                                    0 |                                   0 |                                  2.20364 |                            0 |                       0.153126 |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                   0 |             0 |
| min   |                     0 |                       0 |                                   0 |                                     0 |                             0 |                             0 |                            1932      |                                    0 |                                   0 |                                 81       |                            1 |                       0        |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 25%   |                     0 |                       0 |                                   0 |                                     0 |                             0 |                             0 |                            2028      |                                    0 |                                   0 |                                 86       |                            1 |                       0        |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 50%   |                     0 |                       0 |                                   0 |                                     0 |                             0 |                             0 |                            2084      |                                    0 |                                   0 |                                 87       |                            1 |                       0        |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 75%   |                     0 |                       0 |                                   0 |                                     0 |                             0 |                             0 |                            2104      |                                    0 |                                   0 |                                 89       |                            1 |                       0        |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| max   |                     0 |                       0 |                                   0 |                                     0 |                             0 |                             0 |                            2176      |                                    0 |                                   0 |                                 92       |                            1 |                       1        |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |

`pypy3 simpy_car.py`

|       |   User time (seconds) |   System time (seconds) |   Average shared text size (kbytes) |   Average unshared data size (kbytes) |   Average stack size (kbytes) |   Average total size (kbytes) |   Maximum resident set size (kbytes) |   Average resident set size (kbytes) |   Major (requiring I/O) page faults |   Minor (reclaiming a frame) page faults |   Voluntary context switches |   Involuntary context switches |   Swaps |   File system inputs |   File system outputs |   Socket messages sent |   Socket messages received |   Signals delivered |   Page size (bytes) |   Exit status |
|:------|----------------------:|------------------------:|------------------------------------:|--------------------------------------:|------------------------------:|------------------------------:|-------------------------------------:|-------------------------------------:|------------------------------------:|-----------------------------------------:|-----------------------------:|-------------------------------:|--------:|---------------------:|----------------------:|-----------------------:|---------------------------:|--------------------:|--------------------:|--------------:|
| count |          1000         |           1000          |                                1000 |                                  1000 |                          1000 |                          1000 |                             1000     |                                 1000 |                           1000      |                                1000      |                    1000      |                      1000      |    1000 |              1000    |                  1000 |                   1000 |                       1000 |                1000 |                1000 |          1000 |
| mean  |             0.18273   |              0.02527    |                                   0 |                                     0 |                             0 |                             0 |                            79497     |                                    0 |                              0.671  |                                9192.85   |                       2.183  |                         4.631  |       0 |               136.16 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| std   |             0.0200761 |              0.00883205 |                                   0 |                                     0 |                             0 |                             0 |                               81.561 |                                    0 |                             21.2189 |                                  26.4655 |                      19.4996 |                        12.8299 |       0 |              4305.76 |                     0 |                      0 |                          0 |                   0 |                   0 |             0 |
| min   |             0.14      |              0          |                                   0 |                                     0 |                             0 |                             0 |                            78644     |                                    0 |                              0      |                                8679      |                       1      |                         0      |       0 |                 0    |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 25%   |             0.17      |              0.02       |                                   0 |                                     0 |                             0 |                             0 |                            79452     |                                    0 |                              0      |                                9186      |                       1      |                         1      |       0 |                 0    |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 50%   |             0.18      |              0.02       |                                   0 |                                     0 |                             0 |                             0 |                            79508     |                                    0 |                              0      |                                9188      |                       2      |                         2      |       0 |                 0    |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 75%   |             0.2       |              0.03       |                                   0 |                                     0 |                             0 |                             0 |                            79520     |                                    0 |                              0      |                                9190      |                       2      |                         3      |       0 |                 0    |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| max   |             0.3       |              0.05       |                                   0 |                                     0 |                             0 |                             0 |                            80020     |                                    0 |                            671      |                                9343      |                     618      |                       258      |       0 |            136160    |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |

`python3 simpy_car.py`

|       |   User time (seconds) |   System time (seconds) |   Average shared text size (kbytes) |   Average unshared data size (kbytes) |   Average stack size (kbytes) |   Average total size (kbytes) |   Maximum resident set size (kbytes) |   Average resident set size (kbytes) |   Major (requiring I/O) page faults |   Minor (reclaiming a frame) page faults |   Voluntary context switches |   Involuntary context switches |   Swaps |   File system inputs |   File system outputs |   Socket messages sent |   Socket messages received |   Signals delivered |   Page size (bytes) |   Exit status |
|:------|----------------------:|------------------------:|------------------------------------:|--------------------------------------:|------------------------------:|------------------------------:|-------------------------------------:|-------------------------------------:|------------------------------------:|-----------------------------------------:|-----------------------------:|-------------------------------:|--------:|---------------------:|----------------------:|-----------------------:|---------------------------:|--------------------:|--------------------:|--------------:|
| count |          1000         |           1000          |                                1000 |                                  1000 |                          1000 |                          1000 |                             1000     |                                 1000 |                                1000 |                               1000       |                         1000 |                      1000      |    1000 |                 1000 |                  1000 |                   1000 |                       1000 |                1000 |                1000 |          1000 |
| mean  |             0.13354   |              0.02021    |                                   0 |                                     0 |                             0 |                             0 |                            19422     |                                    0 |                                   0 |                               3406.91    |                            1 |                        10.01   |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| std   |             0.0171803 |              0.00986678 |                                   0 |                                     0 |                             0 |                             0 |                              121.677 |                                    0 |                                   0 |                                  2.43512 |                            0 |                        10.0043 |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                   0 |             0 |
| min   |             0.08      |              0          |                                   0 |                                     0 |                             0 |                             0 |                            19068     |                                    0 |                                   0 |                               3400       |                            1 |                         2      |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 25%   |             0.12      |              0.01       |                                   0 |                                     0 |                             0 |                             0 |                            19344     |                                    0 |                                   0 |                               3405       |                            1 |                         6      |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 50%   |             0.13      |              0.02       |                                   0 |                                     0 |                             0 |                             0 |                            19444     |                                    0 |                                   0 |                               3407       |                            1 |                         7      |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| 75%   |             0.14      |              0.03       |                                   0 |                                     0 |                             0 |                             0 |                            19509     |                                    0 |                                   0 |                               3409       |                            1 |                         9      |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |
| max   |             0.2       |              0.05       |                                   0 |                                     0 |                             0 |                             0 |                            19704     |                                    0 |                                   0 |                               3414       |                            1 |                       111      |       0 |                    0 |                     0 |                      0 |                          0 |                   0 |                4096 |             0 |



Clearly the Rust implementation is faster. I would naïvely attribute that to Rust being a compiled (and statically typed) language that also doesn't have a garbage collector. Interestly the PyPy3 interpreter was actually slower than the CPython interpreter in this case.
