---
title: Probability Of Min > Max Of Independent Samples
date: 2023-03-01 21:32:00 -0800
categories: [statistics,order-statistics]
tags: [statistics,order-statistics,convolution-theorem]
math: true
mermaid: true
---

# Preamble
Suppose we have two collections of random variables 

$$\{X_1, \ldots, X_n \}$$

and

$$\{Y_1, \ldots, Y_m \}$$

with $X_i \sim  F_X$ and $Y_j \sim  F_Y$ that I will assume are $C^1$ [smooth](https://en.wikipedia.org/wiki/Smoothness).


# Question
What is $Pr \left[ \min \{X_1, \ldots, X_n \} > \max \{Y_1, \ldots, Y_m \} \right]$?

# Answer

Note that 

$$Pr \left[ \min \{X_1, \ldots, X_n \} > \max \{Y_1, \ldots, Y_m \} \right] \iff Pr \left[ \min \{X_1, \ldots, X_n \} - \max \{Y_1, \ldots, Y_m \} > 0 \right]$$

so finding $Z = \min \{X_1, \ldots, X_n \} - \max \{Y_1, \ldots, Y_n \}$ puts our problem is a familiar form of cumulative distribution function.

We know from standard order statistics that $\max \{Y_1, \ldots, Y_n \} \sim \left[ F_Y(y) \right]^m$, so that is a starting point for finding the distribution of $- \max \{Y_1, \ldots, Y_n \}$. To obtain the reflection

# Applications

Probability that signal plus noise is greater than noise.

Deciding that one model is better than another one. Not a common option since samples since errors will often be dependent...

# Conclusions

It was fairly straightforward to use known results to derive this distribution. The problem gets substantially more difficult if I want to drop independence or smoothness. As is often the case, it can often be easier to start with a generative model and simulate samples than to analytically derive the distribution. But latter is an increment of progress unto itself.
