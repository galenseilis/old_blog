---
title: Notes On Beautiful Python Refactoring Video
date: 2023-10-22 00:50:15
categories: [computer-programming,refactoring]
tags: [computer-programming,refactoring,python]
math: true
mermaid: true
---

This post is just some notes I took while watching the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/KTIl1MugsSY?si=k7RR05hWGEICmF7b" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

ITM Antipattern
The initialize then modify (ITM) antipattern is where something it initialized outside a loop and then it is modified in the loop. For change 1 we used `enumerate`, and for change 2 we used a list comprehension.

Redundant Comments
    - Remove **redundant** comments.
    - Redundant comments just restate the literal command.
    
Index ITM
    - Initializing index outside of a loop and then incrementing it inside the loop.
    - Solution: Use `enumerate`.

Deprecated Print Statements 
    - Delete any print statements that are no longer needed.

List Comprehensions
    - Replace for loops with list comprehensions when the list copmrehension itself will be readible.

Deprecated Conrol Flow
    - Delete control flow (`if/elif/else`) that won't be relevant to future use cases.

Iterable Slicing
    - Use slicing instead of looping over an iterable when the location of the target information is reliable.

Changes 6 and 7 we have seen above.

Try/Except/Pass
    - Remove `try <type_cast> except pass` patterns.
    - Replace with a conditional expression `<type_cast> if <condition> else <other>`.
    
Specialized Libraries
    - Use existing tools designed for the task instead of maintaining your legacy code.
    
Some principles:
1. Know your algorithms
2. Know your collections
3. Know your libraries

Some useful features mentioned in the Python Bytes podcast:
- list comprehensions
- generator expressions
- slice assignment
- iterable unpacking
