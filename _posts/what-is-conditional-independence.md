---
title: What is Conditional Independence?
date: 2023-02-19 13:18:32
categories: [statistics]
tags: [statistics,independence, conditional-independence,random-variables,joint-probability,conditional-probability,subset,finite-set]
math: true
---

> **Definition** (Pearl 2009)
>
> Let $S = \{V_1, \ldots, V_n\}$ be a finite set of random variables. And let F_{V_1, \ldots, V_n}(v_1, \ldots, v_n) be a joint probability function over the random variables in $S$. Taking $X$, $Y$, and $Z$ to be any three subsets of $S$, then we say that $X$ and $Y$ are conditionally independent given $Z$ if 
> $$Pr \left[ x | y, z \right] = Pr \left[ x | z \right]$$
> if-and-only-if $P(y,z) > 0$.

Marginal or unconditional independence can be thought of as conditional independence between two variables given an empty set, denoted $(X \perp Y | \emptyset)$. 
