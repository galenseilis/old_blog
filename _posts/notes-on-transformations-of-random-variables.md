---
title: Notes On Transformations of Random Variables
date: 2023-02-25 21:23:30
categories: [statistics,transformations]
tags: [statistics,transformations,probability]
math: true
mermaid: true
---


# Introduction 
A common setup in probability theory and statistics is to suppose that random variables represent your measurements. Random variables are mathematical concepts that suppose a probability space, which includes a probability measure. There is a variation of the *garbage in, garbage out* (GIGO) principles which I call the *uncertainty in, uncertainty out* (UIUO; which I pronounce "you-ee-oh") principle. That is, whenever we are computing functions on quantities that are uncertain, we should expect there to be uncertainty about the quantities in the output (i.e. image) of the function. Likewise, (measurable) functions of random variables give us random variables.

This UIUO principle is not entirely correct because we can compute a function of a random variable which results in a degenerate or constant random variable. In practice this is often not the case, and the point of the principle is to remind ourselves to *consider* the propogation of uncertainty when we do calculations.

Since measurements pretty much always have uncertainty, the UIUO principle usually applies. This is not to say that the uncertainty might be so small in some cases that modelling the uncertainty isn't required. The rest of this post supposes that the UIUO principle applies.

Starting with a random variable $X$ we would like to apply some function $f : S \mapsto S^{\prime}$ to that variable. This transformation results in some new random  $Y = f(X)$.

# Foundations

There are some key definitions that should be understood before proceed. First, we begin with a set $\Omega$. This set $\Omega$ is usually assumed to be one of some familiar sets such as $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, or $\mathbb{R}$. These sets are perhaps the most useful building blocks for the majority of applications in statistics, but there is no purely mathematical or logical reason to suppose them. Rather, it is especially important that $\Omega$ is *defined* in way that characterizes the set of possibilities for a given problem. The set $\Omega$ could special kinds of numbers such the extended reals, the hyperreals, the surreals, hypercomplex numbers or neutrosophic numbers. $\Omega$ could also be a group, a ring, a vector space or any other algebraic structure. Likewise $\Omega$ could be a manifold, a function, a relation, a graph, a hypergraph, a simplicial complex, or a set of velociraptors! What I mean is that $\Omega$ really is an arbitrary set of "things" and not necessarily a particular set of numbers. 

Often we work with numbers for two reasons:
- Categorical measurements are usually isomorphic to a set of numbers
  - E.g. primary and foreign keys in a database preserve identity
  - E.g. colours have frequency/wavelength spectra
- Numerical measurements are quite common and useful
  - E.g. observed frequencies (i.e. counts)
  - E.g. distances
- Lots of operators and functions are ready-made for  (i.e. lots of tools available)
  - E.g. scalar summation/subtraction
  - E.g. scalar multiplication/division
  
We will suppose we are dealing with numbers here unless stated otherwise.

In order to make full use of formal probability, we require the notion of a $\Sigma$-algebra. A $\Sigma$-algebra is some additional structure for which $\Omega$ will be a part. It mostly for axiomatic purposes rather than calculation, and its importance is to gaurantee that such calculations make sense in the first place. Here is a formal definition of a $\Sigma$-algebra.

> **Definition** A $\Sigma$-algebra is a subset of the powerset of $\Omega$ (i.e. $\Sigma \subseteq \mathcal{P}(\Omega)$) which satisfies the following constraints:
>  - Containts the universal set: $\Omega \in \sigma$
>  - Closed under complementation: $A \in \Sigma \implies \Omega \\ A \in \Omega$
>  - Closed under countable unions: $A_1, A_2, \ldots \in \Sigma \implies \bigcup_i A_i \in \Sigma$

A $\Sigma$-algebra ensures that we can consider complements, intersections, and unions of subsets of the outcome space (almost) whenever we would like.

measurable space, measurable space, random variable, derived distribution

# Transformations of Discrete Random Variables

The probability distribution for some discrete set is simply given by
$$Pr(y) = \sum_{x, y=f(x)} Pr(x).$$

While the change of variables is conceptually quite easy to grasp, this is not always easy to calculate due to combinatorial explosion.

# Smooth

Often we like to work with $C^1$ smooth functions because 

# Non-Smooth Continuous Transformations

Weakly-smooth, using definition of CDF, finite difference approximation, function approximators

# Mixed Transformations

