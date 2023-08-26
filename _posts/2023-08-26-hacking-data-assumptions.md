---
title: Hacking The Data To Meet The Assumptions
date: 2023-08-26 00:50:15
categories: [statistics,rank-based-statistics]
tags: [statistics,rank-based-statistics,]
math: true
mermaid: true
---

# Introduction

This post is an ongoing series of posts that respond to the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/qee6b7vl2O0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

There is a particular quote from near the end of the video that I would like to explore. Dustin says this about rank-based procedures:

> Quotation (Dustin Fife)
>
> You're hacking the data to meet the assumptions.

A natural question for me to start with is: *what assumptions*?

I think for a lot of people that take a statistics course they are given a collection of pre-made recipes to master. A typical frequentist course on statistics often covers an assortment of null hypothesis significance testing procedures that make particular assumptions. I already commented to an extent on the non-necessity of these procedures and assumptions for parametric statistics in [Wilcoxon's Heuristic](https://galenseilis.github.io/posts/wilcoxons-heuristic/).

I've seen some people try really hard to conform their analysis to such recipes. This often comes in the form of applying functions (AKA transformations) to obtain estimates that are [unbiased](https://en.wikipedia.org/wiki/Bias_of_an_estimator), [consistent](https://en.wikipedia.org/wiki/Consistent_estimator), [sufficient](https://en.wikipedia.org/wiki/Sufficient_statistic), or [efficient](https://en.wikipedia.org/wiki/Efficiency_(statistics)), or similarly satisfying the [Gauss-Markov theorem](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem).

Often, although not always or not to the same extent, this comes from people not having the tools and knowledge to develop their own statistical methodologies. This is in part due to not have sufficient familiarity with mathematics or computer science. I expect that we're all doing this to an extent; taking the approaches we have in hand conforming the problem to the tools. I am reminded of this quote which is purportedly from [Amos Tversky](https://en.wikipedia.org/wiki/Amos_Tversky):

> Quotation (Amos Tversky)
>
> Whenever there is a simple error that most laymen fall for, there is always a slightly more sophisticated version of the same problem that experts fall for.

But I wouldn't say that all this adjusting to meet assumptions is entirely bad, especially if it is done rigorously. It is a matter of satisfying the goals and constraints of the analysis given the tools and the data in hand. 

Functions, especially invertible functions, provide a means of making a hard problem easy. Physicists routinely apply what they call *change of coordinates*, which are just invertible functions, if it makes the problem they are working on easier. While there are complicated or sophisticated approaches involving integral transforms that are often used, I think there is a relatively simple example that we can draw on for intuition: [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system). Often our data is supposed to be embedded in [Cartesian coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinate_system), but in sometimes the mathematics (and 'shape of our data' so-to-speak) becomes simpler if we convert to polar coordinates. If our data is a sample from a manifold which is a circle in Cartesian coordinates, then our data just becomes a line in polar coordinates. Likewise, many complicated curves on the plane just become polynomials or other tractable examples in polar coordinates.

> Invertible functions are nice, but sometimes we have to do without them, or generalize what we mean by "inverse". One approach that I've seen in [Copula Theory](https://en.wikipedia.org/wiki/Copula_(probability_theory)) is to take the [infinum](https://en.wikipedia.org/wiki/Infimum_and_supremum) of the [preimage](https://mathworld.wolfram.com/Pre-Image.html) of the function. With inverting matrices, which represent linear maps, we have the [Moore-Penrose inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse). Or sometimes functions are not invertible but they are *locally invertible* via the [inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem) (IVT). And even when IVT fails because we don't have partial derivatives we can turn to [weak derivatives](https://en.wikipedia.org/wiki/Weak_derivative) and [distributional derivatives](https://en.wikipedia.org/wiki/Distribution_(mathematics)#Differentiation_of_distributions) to obtain a similar relaxation of the [Jacobian](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)s. See [Tao 2009](https://terrytao.wordpress.com/2009/04/19/245c-notes-3-distributions/) for further reference on the distributional approach.
{: .prompt-tip}

As (I think) I've mentioned before, the best use cases for rank-based statistics pertain to certain problems where the order properties of the data are of interest. While many people have used Wilcoxon's heuristic as I've described it, I don't think of them as synonymous with that approach. By all means use the Mann-Whitney U statistic if you want to quantify the strength of a stochastic ordering between two groups as the statistic itself doesn't assume very much at all. You can even compute the statistic on non-numerical data provided that the notion of order relation (i.e. what we mean by "$\leq$") is defined. You can use the classic Mann-Whitney U *test* if 

1. you can assign a non-arbitrary significance level threshold $\alpha$ and 
2. can assume the observations are soundly modelled as [IID](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) random variables and 
3. you are actually interested in what it would say about the order properties of your data.

Otherwise, don't use it. 🤷 

There's no shortage of mathematical modifications you can make to existing procedures if they don't quite match what you're going for. If a Mann-Whitney U test is almost what you want except that you cannot assume IID, then further develop a modification of the procedure that accounts for the statistical dependence. Maybe you further assume that the observations have a multivariate normal distribution, for example. Likewise, you can get out a dry eraser and whiteboard and start working out a new procedure from first principles.

Overall my impression of "you're hacking the data to meet the assumptions" is that this isn't necessarily as bad as it sounds. Sure, some people are producing [janky](https://www.merriam-webster.com/dictionary/janky) work because they're desparately trying to make something work that doesn't work. However I think that Dustin may be thinking he is [separating the wheat from the chaff](https://www.merriam-webster.com/dictionary/separate%20the%20wheat%20from%20the%20chaff) when he is actually [throwing out the baby with the bathwater](https://en.wikipedia.org/wiki/Don%27t_throw_the_baby_out_with_the_bathwater)... Figures of speech are weird. 🤔 

Anyway, my point being that provided that it is done rigorously I do not think that rank-based non-parametric statistics (including the classics) are problematic *per se*. Where Dustin and I may find some agreement is that they often *are not* applied rigorously by people. 

In my view we should challenge specific misuses of statistics when they arise rather than calling for an overly-broad abolition of what is basically a branch of math.
