---
title: Bandit Versus Bandit
date: 2023-03-09 21:12:00
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

And then I ran Bandit recursively on its own source.

```bash
$ bandit -r /home/galen/.local/lib/python3.10/site-packages/bandit
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.10.6
Working... ━━━━━━━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  22% 0:00:02[manager]       WARNING Test in comment: _lines is not a test name or id, ignoring
[manager]       WARNING Test in comment: is is not a test name or id, ignoring
[manager]       WARNING Test in comment: a is not a test name or id, ignoring
[manager]       WARNING Test in comment: dict is not a test name or id, ignoring
[manager]       WARNING Test in comment: of is not a test name or id, ignoring
[manager]       WARNING Test in comment: line is not a test name or id, ignoring
[manager]       WARNING Test in comment: number is not a test name or id, ignoring
[manager]       WARNING Test in comment: set is not a test name or id, ignoring
[manager]       WARNING Test in comment: of is not a test name or id, ignoring
[manager]       WARNING Test in comment: tests is not a test name or id, ignoring
[manager]       WARNING Test in comment: to is not a test name or id, ignoring
[manager]       WARNING Test in comment: ignore is not a test name or id, ignoring
Working... ━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━  33% 0:00:02[manager]       WARNING Test in comment: tkelsey is not a test name or id, ignoring
[manager]       WARNING Test in comment: catching is not a test name or id, ignoring
[manager]       WARNING Test in comment: expected is not a test name or id, ignoring
[manager]       WARNING Test in comment: exception is not a test name or id, ignoring
Working... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Run started:2023-03-10 05:19:38.870733

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/cli/baseline.py:18:0
17      import shutil
18      import subprocess
19      import sys

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/cli/baseline.py:105:25
104                 try:
105                     output = subprocess.check_output(bandit_command)
106                 except subprocess.CalledProcessError as e:

--------------------------------------------------
>> Issue: [B110:try_except_pass] Try, Except, Pass detected.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b110_try_except_pass.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/core/utils.py:73:8
72                      prefix = deepgetattr(node, "value.id")
73              except Exception:
74                  # NOTE(tkelsey): degrade gracefully when we can't get the fully
75                  # qualified name for an attr, just return its base name.
76                  pass
77

--------------------------------------------------
>> Issue: [B405:blacklist] Using cElementTree to parse untrusted XML data is known to be vulnerable to XML attacks. Replace cElementTree with the equivalent defusedxml package, or make sure defusedxml.defuse_stdlib() is called.
   Severity: Low   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b405-import-xml-etree
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/formatters/xml.py:38:0
37      import sys
38      from xml.etree import cElementTree as ET
39

--------------------------------------------------
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   CWE: CWE-605 (https://cwe.mitre.org/data/definitions/605.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b104_hardcoded_bind_all_interfaces.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/plugins/general_bind_all_interfaces.py:46:29
45      def hardcoded_bind_all_interfaces(context):
46          if context.string_val == "0.0.0.0":
47              return bandit.Issue(

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/plugins/general_hardcoded_tmp.py:62:29
61          if name == "hardcoded_tmp_directory":
62              return {"tmp_dirs": ["/tmp", "/var/tmp", "/dev/shm"]}
63

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/plugins/general_hardcoded_tmp.py:62:37
61          if name == "hardcoded_tmp_directory":
62              return {"tmp_dirs": ["/tmp", "/var/tmp", "/dev/shm"]}
63

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/plugins/general_hardcoded_tmp.py:62:49
61          if name == "hardcoded_tmp_directory":
62              return {"tmp_dirs": ["/tmp", "/var/tmp", "/dev/shm"]}
63

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/plugins/general_hardcoded_tmp.py:72:20
71          else:
72              tmp_dirs = ["/tmp", "/var/tmp", "/dev/shm"]
73

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/plugins/general_hardcoded_tmp.py:72:28
71          else:
72              tmp_dirs = ["/tmp", "/var/tmp", "/dev/shm"]
73

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
   Location: /home/galen/.local/lib/python3.10/site-packages/bandit/plugins/general_hardcoded_tmp.py:72:40
71          else:
72              tmp_dirs = ["/tmp", "/var/tmp", "/dev/shm"]
73

--------------------------------------------------

Code scanned:
        Total lines of code: 7961
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 4
                Medium: 7
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 7
                High: 4
Files skipped (0):
```

It is interesting to see that a software package intended to detect security issues finds some potential security issues within itself. None of the issues were rated as being high severity, and they're potentially all justified depending on if/how they were considered by the developers of Bandit. You can see that each issue has a documented description in the results.
