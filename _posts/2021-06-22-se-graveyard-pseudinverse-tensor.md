---
title: Is there a pseudoinverse for tensors of finitary rank?
date: 2021-06-22 22:29:00 -0800
categories: [math,tensors]
tags: [math,stack-exchange,stack-exchange-post-mortem,inverse-functions,tensors,pseudoinverse-functions]
math: true
mermaid: true
---

> [This question](https://math.stackexchange.com/questions/4180383/is-there-a-pseudoinverse-for-tensors-of-finitary-rank) was automatically deleted from `math.stackexchange.com`.
{: .prompt-info}

# Question

Matrices estimated from data, even when, are not always invertible. Fortunately a 'nearest inverse' can be calculated with the [Moore-Penrose inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse). Recently I have been taking [inverses](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html) of tensors of rank greater than two that are calculated from real-world data, but I am finding that they are often non-invertible.

Is there a pseudoinverse for finitary [rank](https://mathworld.wolfram.com/TensorRank.html) [tensors](https://mathworld.wolfram.com/Tensor.html) in a similar sense to the Moore-Penrose pseudoinverse?
