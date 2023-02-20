---
title: Uncertainty as Hidden Variables
date: 2021-01-01
categories: [math]
tags: [math,lorenz-system,differential-equations,probability,dynamical-systems]
math: true
mermaid: true
---

# Introduction

For years now I have been thinking about the nature of uncertainty and determinism. I won't attempt a detailed treatment of the philosophy in this post, but rather explore an approach to bridging these ideas.

One approach to thinking about uncertainty is probability theory. The following threads provide an appetizer to some of the fundamental notions.
- [Are randomness and probability really logically dependent notions?](https://stats.stackexchange.com/questions/549914/are-randomness-and-probability-really-logically-dependent-notions)
- [Do all observations arise from probability distributions?](https://stats.stackexchange.com/questions/558327/do-all-observations-arise-from-probability-distributions/558334)
- [Is Anything Inherently Random?](https://stats.stackexchange.com/questions/558348/is-anything-inherently-random?)

I will take a modelling approach, meaning I will suppose some things for the sake of constructing a model but I don't know/claim that these must be taken as philosohical axioms. The key idea I will investigate here is the notion that there is an underlying ([almost-surely](https://en.wikipedia.org/wiki/Almost_surely)) deterministic model for a system which appears random to us when we measure it. The measurement process is itself modelled as a change of variables.

Let us suppose that the state of a system at time $t$ is described as a vector $\vec x (t)$.

# Example: The Lorenz System

The Lorenz system can be represented as the following system of differential equations:

$$\frac{dx}{dt}(t) = \sigma (y(t) - x(t))$$

$$\frac{dy}{dt}(t) = x(t) (\rho - z(t)) - y(t)$$

$$\frac{dz}{dt}(t) = x(t)y(t) - \beta z(t)$$

The following are the histograms of the sampled states for each variable.

![](/assets/images/lorenz_histgrams.png)

Personally, if someone showed me these histograms without telling me they were from the Lorenz system I would have no idea what to guess about them. Each of these plots supposes we kept one variable and discarded (or didn't know) the others. That is to say, when only some of the variables are observable, we get distributions. This isn't special to dropping down to only one observed variable. Suppose we could see two out of the three variables in such a Lorenz system, we could see one of these pairwise plots instead. I have plotted these the joint kernel density estimates on the lower triangle below, the marginal kernel density estimates on the diagonal, and the scatterplots on the upper diagonal.


The following is a pair grid of plots of the simulated states of the Lorenz system. The diagonal entries are the univariate kernel density estimates of the variables. The lower triangle are the bivariate kernel density estimates. The upper triangle are the bivariate scatter plots.

![](/assets/images/lorenz_pairgrid.png)

The bivariate plots say a lot more about the sampled manifold than the univariate plots, although the Lorenz system in particular is nice because Taken's embedding theorem allows you to reconstruct some aspects of the manifold from just a single variable along with time.

Clearly, we can obtain empirical distributions from a given set of differential equations. But I am wondering if it is possible to do this analytically. I liken dropping some of the variables to a change in variables, but it isn't clear that the usual approach of using the Jacobian would work since "dropping variables" doesn't seem like a smooth operation. Suppose we have a system of variables $x_1(t), ..., x_n(t)$ and we choose to partition them into observed variables and unobserved variables. Is there a way to obtain (1) a density over the observed variables for all time as illustrated above or (2) a time-dependent density (maybe with a given distribution defined over the initial conditions of the unobserved variables) at a given time?

Sufficed to say, my thinking on this topic is in its infancy.

# Code
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import seaborn as sns

# Setup and simulate Lorenz system
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 100.0, 0.01)

states = odeint(f, state0, t)

# Histograms of simulated coordinates
fig, axes = plt.subplots(1, 3)

axes[0].hist(states[:,0], bins=200, label='X')
axes[0].set_xlabel('X')
axes[1].hist(states[:,1], bins=200, label='Y')
axes[1].set_xlabel('Y')
axes[2].hist(states[:,2], bins=200, label='Z')
axes[2].set_xlabel('Z')
plt.tight_layout()
plt.savefig('lorenz_histgrams.png', dpi=300, transparent=True)
plt.close()

# Pairgrid of simulated coordinates
d = {'X':states[:,0], 'Y':states[:,1], 'Z':states[:,2]}
df = pd.DataFrame(d)

g = sns.PairGrid(df, diag_sharey=False)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot)

plt.savefig('lorenz_pairgrid.png', dpi=300, transparent=True)
plt.close()
```

# References
# Citation
