---
title: Notes On Order Theory
date: 2023-02-15 23:09:34
categories: [math,order-theory]
tags: [math,order-theory,partial-orders,reflexivity,transitivity,antisymmtry]
math: true
mermaid: true
---


# Fundamentals

## Essential Definitions and Examples

> **Definition**
> A partial order is a pair $(X, \leq)$ composed of a set $X$ called the ground set and $\leq$ is a binary relation with the following relation:
- reflexivity: $x \leq x\ \forall x \in X$
- transitivity: $x \leq y \land y \leq z \implies x \leq z\  \forall x,y,z \in X$
- antisymmtry: $x \leq y \land y \leq x \implies x = y\  \forall x,y \in X$

> **Example**
> Let $X = \{a, b, c, d, e \}$, then $X \times X = \{aa, ab, ac, ad, ae, ba, bb, bc, bd, be, ca, cb, cc, cd, ce, da, db, dc, dd, de, ea, eb, ec, ed, ee\}$.

> The previous example only required a relatively small subset of the Cartesian $X \times X$. When you a have too many elements in $X$ to deal with by hand, one quick Python script to make the pairs in a format suitable for $\LaTeX$ is the following:
```python
from itertools import product
X = 'a', 'b', 'c', 'd', 'e'
XxX = [''.join(i) for i in product(X,X)]
XxX = sorted(XxX)
XxX = str(XxX).replace("'", "")
XxX = XxX.replace("[", "\\{")
XxX = XxX.replace("]", "\\}")
print(XxX)
```
This will print `\{aa, ab, ac, ad, ae, ba, bb, bc, bd, be, ca, cb, cc, cd, ce, da, db, dc, dd, de, ea, eb, ec, ed, ee\}`.
{: .prompt-tip}

