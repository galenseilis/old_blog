---
title: A Generalization of Subindependence
date: 2024-02-09 06:30:15
categories: [mathematics,mathematical-statistics,subindependence]
tags: [mathematics,math,statistics,mathematical-statistic,independence,subindependence,characteristic-function,random-variable,sum,summation,binary-operator,function,collection,copula-theory,copula]
math: true
mermaid: true
---

## Background
I was contemplating the notion of [subindependence](https://en.wikipedia.org/wiki/Subindependence).  It states that for two random varaibles on a shared probability space that the characteristic function of their sum is equal to their the scalar product of their individual characteristic functions:

$$\phi_{X+Y} = \phi_{X}(t) \phi_{Y}(t).$$

## Multiple Variables

The first obvious generalization of this definition is to go to a collection of random variables $\{X_1, \ldots, X_n \}$:

$$\phi_{\{X_1 + X_2 + \cdots +  X_n \}}(t) = \prod_{j=1}^n \phi_{X_{j}}(t)$$

## Choice of Operator

Instead of just considering the sum of random variables, we could generalize to a measurable function $\odot: \mathcal{X} \times \mathcal{Y} \mapsto \mathcal{Z}$.

$$\phi_{\{X_1 \odot X_2 \odot \cdots \odot X_n \}}(t) = \prod_{j=1}^n \phi_{X_{j}}(t).$$

This has a familiarity to it. Like how Fourier transforms are related to sums of independent random variables or Mellin transforms under certain assumptions are related to products of independent random variables. I have not thought about this enough lately, but perhaps one can formalize this as a class of diagonalization decompositions in a function space.

## Copula Theory
Also, I wonder how subindependence relates to copula theory. Sklar's theorem gives us general conditions for mapping the marginal probabilities to their joint probabilities via a copula. So in a sense copulae specify *how* collections of random variables are dependent (or independent, in the case of the independence copula). Anyway, I intuit that there is a connection here.

## Conclusions

Just sharing passerby impressions of the notion of independence. It seems like something that can readily be generalized, although I did not cover any mathematical or practical application.
