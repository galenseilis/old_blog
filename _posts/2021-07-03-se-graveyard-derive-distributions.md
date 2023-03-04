---
title: How do I derive the distribution of a real-valued statistic from real-valued random variables with known univariate distributions?
date: 2021-07-03 19:15:00 -0800
categories: [statistics,probability-distributions]
tags: [math,stack-exchange,stack-exchange-post-mortem,statistics,probability-distributions]
math: true
mermaid: true
---

> [This question](https://math.stackexchange.com/questions/4189544/how-do-i-derive-the-distribution-of-a-real-valued-statistic-from-real-valued-ran) was automatically deleted from `math.stackexchange.com`.
{: .prompt-info}

# Question

I want to improve my skills at finding the distribution of functions of real-valued functions of real-valued random variables. I'm familiar with the basics of the [algebra of random variables](https://en.wikipedia.org/wiki/Algebra_of_random_variables) as far as manipulating expectations, and also understanding the expectation as an integral. I also think I understand that a [sum of two random variables is a convolution](https://en.wikipedia.org/wiki/Convolution_of_probability_distributions), and a [product of two random variables](https://en.wikipedia.org/wiki/Product_distribution) has a distribution that can be derived from their cumulative distribution function. But, let me formalize what I am interested in.

Let there exist a collection of real-valued random variables $\{X_j \sim f_j\}_{j=1}^{n}$ where the univariate distributions $f_i$ are known, and let there be a population parameter $\theta$ that is estimated by $\hat{\theta}$ which is a function $g$ of the random variables:

$$\hat{\theta} = g\left( X_1, \cdots, X_n \right)$$

Let's also assume that $g$ and $f_i$ are sufficiently smooth. But let us not assume that any subset of $\{X_j \sim f_j\}_{j=1}^{n}$ is necessarily independent.

While this description is not sufficient to provide an exact algorithm, I would like to know if there are some common approaches or procedures to deriving the distribution of $\hat{\theta}$.
