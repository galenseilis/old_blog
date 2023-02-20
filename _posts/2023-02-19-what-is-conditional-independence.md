---
title: What is Conditional Independence?
date: 2023-02-19 13:18:32
categories: [statistics]
tags: [statistics,independence, conditional-independence,random-variables,joint-probability,conditional-probability,subset,finite-set]
math: true
---

> **Definition** (Pearl 2009)
>
> Let $V = \{V_1, V_2, \ldots \}$ be a finite set of variables. Let $P(\cdot)$ be a joint probability function over the variables in $V$, and let $X$, $Y$, $Z$ stand for any three subsets of the variables in $V$. The sets $X$ and $Y$ are said to be conditionally independent given $Z$ if  $P(x \vert y, z) = P(x \vert z)$ whenever $P(y,z) > 0$. 

Marginal or unconditional independence can be thought of as conditional independence between two variables given an empty set, denoted $(X \perp Y \vert \emptyset)$. 

There are some general properties of conditional independence:
- Symmetry: $(X \mathrel{\unicode{x2AEB}} Y \vert Z)_P \implies (Y \mathrel{\unicode{x2AEB}} X \vert Z)_P$
- Decomposition: $(X \mathrel{\unicode{x2AEB}} YW \vert Z)_P \implies (X \mathrel{\unicode{x2AEB}} Y \vert ZW)_P$

