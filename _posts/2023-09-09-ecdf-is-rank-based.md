---
title: The Empirical Cumulative Distribution Function Is Rank-Based
date: 2023-09-09 02:50:15
categories: [statistics,rank-based-statistics,empirical-cumulative-distribution-function]
tags: [statistics,rank-based-statistics,cumulative-distribution-function,empirical-cumulative-distribution-function]
math: true
mermaid: true
---

There is a relationship between rank-based statistics and the notion of an empirical distribuion function. The empirical cumulative distribution function can be written as

$$\hat F (t) \triangleq \frac{1}{n} \sum_{i=1}^n \mathbb{I}_{X_i \leq t}$$


Note that $$\text{rank}(x) = \sum_{i=1}^n \mathbb{I}_{X_i \leq x}$$ is a rank, and thus we have

$$\hat F (x) = \frac{\text{rank}(x)}{n}$$

where we have restricted the parameter $t$ to the subset of the domain of $\hat F$ that are observed.

We can have cumulative distribution functions on things that are partially-ordered, not just subsets of the real numbers.

> The real numbers are totally-ordered, but note that every total order is a partial order.
{: .prompt-info}

The empirical cumulative distribution function according to [GCT](https://en.wikipedia.org/wiki/Glivenko%E2%80%93Cantelli_theorem) uniformly converges to the true cumulative distribution $F$ if it exists.
