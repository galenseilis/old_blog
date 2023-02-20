---
title: Notes On Order Theory
date: 2023-02-19 23:09:34
categories: [math,order-theory]
tags: [math,order-theory,partial-orders,reflexivity,transitivity,antisymmtry,cartesian-product,binary-relation,relation,python,latex,directed-acyclic-graph,strict-order]
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

Let us consider an example of a partial order and some of the ways we can represent them.

> **Example**
> Let $X = \{a, b, c, d, e \}$, then we might have a partial order $\{aa, ac, ae, bb, bc, bd, be, cc, dd, de, ee\}$. This partial order can be represented as a matrix.
>
> $$\begin{array}{c c} &
\begin{array}{c c c c c} a & b & c & d & e \\
\end{array}
\\
\begin{array}{c c c c c}
a \\
b \\
c \\
d \\
e \\
\end{array}
&
\left[
\begin{array}{c c c c c}
1 & 0 & 1 & 0 & 1 \\
 & 1 & 1 & 1 & 1 \\
 &  & 1 & 0 & 0 \\
 & \huge 0 &  & 1 & 1 \\
 &  &  &  & 1 \\
\end{array}
\right]
\end{array}
$$
> 
Another representation is a directed graph (AKA a digraph):
> ![](/assets/images/example_digraph_representation_of_a_partial_order.png)

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

> The digraph diagram in the previous example can be made with the following snippet of code:
```python
from graphviz import Digraph
XxX = 'aa', 'ac', 'ae', 'bb', 'bc', 'bd', 'be', 'cc', 'dd', 'de', 'ee'
D = Digraph('example_partial_order')
for xx in XxX:
    D.edge(xx[0], xx[1])
D.view()
```
> This will produce a `PDF` named `example_partial_order.gv.pdf`.
{: .prompt-tip}


> **Definition**
> A strict order is a pair $(X, <)$ composed of a set $X$ called the ground set and $<$ is a binary relation with the following relation:
- transitivity: $x < y \land y < z \implies x < z\  \forall x,y,z \in X$
- asymmetry: $\lnot (x < y \land y < x) \  \forall x,y \in X$
