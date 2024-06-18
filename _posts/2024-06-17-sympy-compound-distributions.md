---
title: SymPy Supports Compound Distributions
date: 2024-06-17 04:51:15
categories: [python,sympy,statistics]
tags: [statistics,probability,normal-distribution,exponential-distribution,compound-distribution,mathematical-statistics,math,maths,moments,expectation,expected-value]
math: true
mermaid: true
---

[Compound distributions](https://en.wikipedia.org/wiki/Compound_probability_distribution) allow us to compose probability distributions together. In other words, it allows us to have parameters in our model that are themselves random variables. This facilities including a hierarchical structure (e.g. like in a [BHM](https://en.wikipedia.org/wiki/Bayesian_hierarchical_modeling)) in our models.

A few weeks ago I learned that [SymPy supports compound distributions](https://docs.sympy.org/latest/modules/stats.html#compound-distribution). 

Here is an example. Suppose 

$$X \sim \text{Normal}(2, 4)$$

$$L \sim \text{Exponential}(100)$$

$$N \sim \text{Normal}(X, L)$$

In SymPy we can represent this model as follows:

```python
from sympy.stats.compound_rv import CompoundDistribution
from sympy.stats.crv_types import NormalDistribution
from sympy.stats import Exponential, Normal
from sympy.abc import x
X = Normal('X', 2, 4)
L = Exponential('L', 100)
N = NormalDistribution(X, L)
C = CompoundDistribution(N)
```

I'm looking forward to seeing more advancements in SymPy for statistics. Mathematical statistics can get particularly difficult when performed by hand. Having specialized classes with handy methods for distributions or [random variables](https://en.wikipedia.org/wiki/Random_variable) could be a huge benefit to bringing in reproducible mathematical derivations of [moments](https://en.wikipedia.org/wiki/Moment_(mathematics)) (e.g. [expectations](https://en.wikipedia.org/wiki/Expected_value)) and [distributions](https://en.wikipedia.org/wiki/Probability_distribution).
