---
title: A Python CLI to Log the Trace
date: 2024-01-31 05:30:15
categories: [computer-programming,python]
tags: [computer-programming,python,trace,logging,script,command-line-interface]
math: true
mermaid: true
---


This is just a short script implementing a logger of the trace of a Python program's execution.

```python
import datetime
from typing import Optional, Callable, Any, Tuple
import sys

import click

def trace_function(frame: Any, event: str, arg: Any) -> Optional[Callable]:
    """
    Trace function for monitoring function calls.

    Args:
        frame (frame): The current frame being executed.
        event (str): The event type triggering the trace function.
        arg (Any): The argument associated with the event.

    Returns:
        Optional[Callable]: The trace function or None to stop tracing.
    """
    if not hasattr(trace_function, 'log_initialized'):
        # Initialize log file with column titles if not already done
        with open('trace_log.txt', 'w') as log_file:
            log_file.write("Timestamp | Event | Function | File | Line | Argument\n")
        trace_function.log_initialized = True

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = frame.f_globals.get('__file__', 'unknown')
    log_entry = f"{current_time} | {event} | {frame.f_code.co_name} | {file_name} | {frame.f_lineno} | {arg}\n"
    with open('trace_log.txt', 'a') as log_file:
        log_file.write(log_entry)
    return trace_function

@click.command()
@click.argument('target_script', type=click.Path(exists=True))
def trace(target_script: str) -> None:
    """
    Trace function to monitor the execution of a target script.

    Args:
        target_script (str): Path to the target script to be traced.

    Returns:
        None
    """
    # Set the trace function
    sys.settrace(trace_function)

    # Run the target script
    with open(target_script, 'r') as script_file:
        exec(script_file.read(), {})

    # Disable the trace function
    sys.settrace(None)

if __name__ == '__main__':
    trace()
```

Using it is straightforward:

```bash
$ Python trace_util.py you_python_script.py
```
