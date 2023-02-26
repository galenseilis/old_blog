---
title: What Are Ranks?
date: 2023-02-23 21:23:30
categories: [statistics,rank-based-statistics]
tags: [statistics,ranks,ranking]
math: true
mermaid: true
---

This post looks at the notion of ranking data or variables. I have quite often refered to "the rank transform", but it actually it isn't a uniquely specified thing.

> **Definition** Assume a collection random variables $\{X_1(\omega), \ldots, X_n(\omega) \}$ on outcome space $\Omega$. An **abstract ranking** $$\rho: \prod_{i=1}^n X_i(\omega) \mapsto \mathbb{R}_{\geq 0}^n$$ is a function such that there exists a non-decreasing function $\kappa:\mathbb{N} \mapsto \mathbb{R}_{\geq0}$ that satisfies $\rho(\vec x)_i \leq \kappa(n)$ for all $i\in \{1, \ldots, n\}$. It must also hold that $\rho(\vec x)_i \leq \rho(\vec x)_j \iff x_i \leq x_j$ for all $i,j \in \{1, \ldots, n\}$ and for all $\omega \in \Omega$ [exor](https://en.wikipedia.org/wiki/Exclusive_or) $\rho(\vec x)_i \geq \rho(\vec x)_j \iff x_i \leq x_j$ for all $i,j \in \{1, \ldots, n\}$ and for all $\omega \in \Omega$. An component of an image element of an abstract ranking is called an **abstract rank**.

I want to make a distinction which is not frequently made explicit, but does specify the mathematics. Namely we should make the distinction between a **ranking** and a **rank** which was suggested language in [this post](https://stats.stackexchange.com/a/605359/69508) by user [Sextus Empiricus](https://stats.stackexchange.com/users/164061/sextus-empiricus). Given a random vector
