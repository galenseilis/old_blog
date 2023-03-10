---
title: Bandit Passes Bandit
date: 2023-03-09 20:00:00
categories: [security,information-security]
tags: [python,security,information-security,bandit]
---

Bandit is a Python package for checking for security issues in Python code. I have been thinking about using Bandit to check for security risks in my own sofware as well as 3rd party packages that I use. I couldn't help but venture to the potentially ironic situation of Bandit evaluating that Bandit itself is insecure.

First I checked for the version and where to find it on my system (after installing it using pip).

```python
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import bandit
>>> bandit.__version__
'1.7.5'
>>> bandit.__file__
'/home/galen/.local/lib/python3.10/site-packages/bandit/__init__.py'
```

And then I ran Bandit on its own source:

```bash
$ bandit /home/galen/.local/lib/python3.10/site-packages/bandit/
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.10.6
[manager]       WARNING Skipping directory (/home/galen/.local/lib/python3.10/site-packages/bandit/), use -r flag to scan contents
Run started:2023-03-10 05:03:56.249656

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 0
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 0
Files skipped (0):
```

While I sometimes enjoy a little irony, I'm glad to see that the Bandit package evaluates that it is secure (from known issues).
