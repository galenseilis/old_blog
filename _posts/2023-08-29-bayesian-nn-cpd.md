---
title: Bayesian Rank-1 Non-Negative Canonical Polyadic Decomposition In PyMC
date: 2023-08-29 02:00:15
categories: [statistics,bayesian-statistics,bayesian-canonical-polyadic-decomposition,bayesian-non-negative-canonical-polyadic-decomposition]
tags: [statistics,bayesian-statistics,bayesian-canonical-polyadic-decomposition,bayesian-non-negative-canonical-polyadic-decomposition]
math: true
mermaid: true
---

This post is just a quick example of how to perform Bayesian non-negative [canonical polyadic decomposition](https://en.wikipedia.org/wiki/Tensor_rank_decomposition) in PyMC. Here we will only perform a rank 1 decomposition with unit coefficients.

Let us suppose that we have a sequence of random vectors

$$\vec u_1, \ldots, \vec u_k$$

$$\vec u_i \sim \text{Exponential}(\vec \lambda_i)$$

then their outer product makes

$$\mathcal{L} = \bigotimes_{i=1}^k \vec u_i$$

and we'll suppose that 

$$\mathcal{X} \sim \text{Exponential}(\mathcal{L})$$

is our observed random variable.


```python
'''Toy example of tensor decomposition in PyMC.

This example only performs a rank-1 decomposition.
'''

import pickle

import arviz as az
import numpy as np
import pymc as pm
from pytensor import tensor as at

# Prior Predictive Simulation
SIZE = 3

u1 = np.random.exponential(0.001, size=SIZE)
u2 = np.random.exponential(0.001, size=SIZE)
u3 = np.random.exponential(0.001, size=SIZE)
x = np.outer(u1, u2)
x = np.outer(x, u3).reshape((SIZE,) * 3).flatten()

# Model Specification
model = pm.Model()

with model:
    u1 = pm.Exponential("u1", lam=1, size=SIZE)
    u2 = pm.Exponential("u2", lam=1, size=SIZE)
    u3 = pm.Exponential("u3", lam=1, size=SIZE)
    mu = at.outer(at.outer(u1, u2), u3).flatten()

    X = pm.Exponential("X", mu, shape=SIZE * 3, observed=x)


if __name__ == "__main__":
    # Sample from the posterior distribution
    with model:
        idata = pm.sample(cores=12)

    # Save results for further analysis.
    with open("test.pickle", "wb") as handle:
        pickle.dump(idata, handle)
```

The more general cases of finite rank-$r$ decomposition should be built with a function or class that constructs it. One option is [`pymc_experimental.model_builder.ModelBuilder`](https://www.pymc.io/projects/experimental/en/latest/generated/pymc_experimental.model_builder.ModelBuilder.html). I imagine such a class should have a parameter for the rank, a parameter for distribution(S) for the random vectors, and also a parameter for the distribution of the observations. A complicated case would be to specify the distribution of every random variable, but then the config alone for the model would be complicated. A possible partial solution for that is to default to assume that the input specifies a distribution family for all the random vectors, or if a dict is passed specifying modes then those distributions are used over the mode. I think specifying the distribution of every coefficient parameter and every element of every vector is sufficiently "custom" that one might as well use the default PyMC model construction class in a context wrapper.
