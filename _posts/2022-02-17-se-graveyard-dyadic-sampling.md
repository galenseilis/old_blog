---
title: What is dyadic sampling in the context of a wavelet transform?
date: 2022-02-01 17:35:00 -0800
categories: [math,integral-transforms,wavelets]
tags: [math,stack-exchange,stack-exchange-post-mortem,geometry,machine-learning,integral-transforms,wavelets]
math: true
mermaid: true
---

> [This question](https://math.stackexchange.com/questions/4371576/what-is-dyadic-sampling-in-the-context-of-a-wavelet-transform) was automatically deleted from `math.stackexchange.com`.
{: .prompt-info}

# Question

In [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) the authors introduce to the reader (page 24) the notion of wavelet transforms as a way of having multiscale representations (of a group, I suspect). Here is the relevant quote that prompted me to ask:

> The translated and dilated filters are called *wavelet atoms*; their spatial position and ilation correspond to the coordinates $u$ and $\xi$ of the wavelet transform. These coordinates are usually sampled dyadically ($\xi=2^{-j}$ and $u=2^{-j}k$), with $j$ referred to as scale.

So is this to say that we often reparametrize $u$ and $\xi$ in terms of $j$ and $k$, and then compute the various wavelet transforms with varying combinations of $j$ and $k$?
