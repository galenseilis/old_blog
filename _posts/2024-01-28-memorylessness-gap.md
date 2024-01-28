---
title: The Curvature of the Graph of the Expectation of a Random Scalar
date: 2024-01-28 06:30:15
categories: [mathematics,mathematical-statistics]
tags: [mathematics,statistics,mathematical-statistcs,calculus,functions,random-variable,random-element,random-scalar,exponential-distribution,memorylessness,memoryless-gap]
math: true
mermaid: true
---

This post is just some spitballing around the idea of quantifying the memory of a distribution.

The exponential distribution is the only distribution with the memorylessnss property. What this means is that 

What this means is that 

$$Pr[T > t + s \mid T > s] = Pr[T > t]$$

for all $s,t \geq 0$. 

What I would suggest calling the "memoryless gap" is simply the difference:

$$\mathcal{R}_T(s,t) = Pr[T > t + s \mid T > s] - Pr[T > t]$$
Note that in general $\mathcal{R}_{T}(s,t)$ is a function both of the variable $t$ and the added translation parameter $s$, so the memoryless gap is a surface. For the case of the exponential it is a plane over $\mathbb{R}^2$ with elevation of zero.

As it is defined in terms of the excedence probabilites, one primarily needs to know a cumulative distribution function for the variable of interest.
$$
\begin{align}
	\mathcal{R}_{X}(s,x) \triangleq &  \frac{1 - F_{X}(x + s)}{1 - F_{X}(x)} - (1 - F_X(x)) \\
	= & \frac{1 - F_{X}(x + s)}{1 - F_{X}(x)} + F_{X}(x) - 1 
\end{align}
$$

Without further analysis it is *prima facie* possible to have either positive or negative values for $\mathcal{R}(s,x)$ which indirectly indicates a stochastic ordering at a given point. When $\mathcal{R}(s,x) > 0$ it suggests that more time was required than what would have been expected had the memorylessness property held, and a similar point holds for $\mathcal{R}(s,x) < 0$ *mutatis mutandis*.

Even though a distribution may not be memoryless everywhere does not mean that it has memory for all points $x$ and translations $s$. Perhaps there are choices of $s$ and $x$ that can be found for a given distribution such that memorylessness holds.

Even though a distribution may not be memoryless everywhere (or almost everywhere) doesn't mean that the amount of memory is the same. The optima of $\mathcal{R}(s,x)$ are a set of points where the memory is the strongest or the weakest in its signed value, and further finding the minima of functions like $|\mathcal{R}(s,x) |$ or $\mathcal{R}(s,x)^2$ could help us find where the distribution has the least memory regardless of sign.

A property like this makes me wonder about optimization objectives. Could there be any modelling benefit to finding a least-memory parametrization of a distribution? Or using the memoryless gap as a regularization term analogous to lasso/ridge?
