---
title: Beyond Studying Order With Ranks
date: 2023-08-26 00:50:15
categories: [statistics,rank-based-statistics]
tags: [statistics,rank-based-statistics]
math: true
mermaid: true
---

# Introduction
This post is an ongoing series of responses to the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/qee6b7vl2O0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


While Dustin and I have a disagreement about the usefulness of classic rank-based statistics, I will offer a point of potential agreement that they are simplistic (i.e. not just simple but *too simple*) for many modern research problems. There are sophisticated ways of using ranks that are suitable for complex problems, but I wanted to offer (what may seem like a [weird flex](https://www.dictionary.com/e/slang/weird-flex-but-okay/)) that we can study order *without* ranks. I believe that there are, and will be more, ways to study order that do not involve excplit use of ranks. In this post I want to very briefly outline an idea of how to study order without ranks.

# What Is Order?

First of all, we need more rigorous tools. Thinking intuitively about order will eventually lead to confusion and fuzzy thinking that is difficult to translate into methods of analysis. Fortunately, there is [Order Theory](https://en.wikipedia.org/wiki/Order_theory), which is a branch of mathematics that makes order its explicit target of study. I've been (very slowly) making my way through [these lectures](https://www.youtube.com/playlist?list=PL5rqYzyihIQ0nzfnsEKxxedCpbNQoifgg) provide a mathematical introduction. What is the first thing to know about order from this perspective?

Order in conventional mathematics is **not** about numbers *per se*. Rather orders are binary relations, which are subsets of [Cartesian products](https://en.wikipedia.org/wiki/Cartesian_product). An order is a binary relation with certain properties, and there are actually different classes of orders. 

> I found that n-ary orders are readily definable but I won't explore that generalization here. It requires generalizing some of the specific properties such as reflexivty, asymmetry/antisymmetry, and transitivty. For example, see [Cristea and Ştefănescu 2010](https://www.sciencedirect.com/science/article/pii/S0195669809001589) that describe existing definitions of reflexivity and transitivty for n-ary relations.
{: .prompt-tip}

In my opinion the 'first' (see how I am using order there 😉) type of order to become familiar with the notion of a [partial order](https://en.wikipedia.org/wiki/Partially_ordered_set). They come in a non-strict variety where the relation is [reflexive](https://en.wikipedia.org/wiki/Reflexive_relation), [antisymmetric](https://en.wikipedia.org/wiki/Antisymmetric_relation), and [transitive](https://en.wikipedia.org/wiki/Transitive_relation). A strict partial order has [irreflexivity](https://en.wikipedia.org/wiki/Reflexive_relation#Irreflexive_relation) instead of reflexivity and [asymmetry](https://en.wikipedia.org/wiki/Asymmetric_relation) instead of antisymmetry.

What is particularly noteworthy is the fact that order is representable without not only ranks but numbers altogether! Order from an Order Theory perspective is not about numbers so much as patterns about how things are paired together. This offers an approach to studying order in the empirical world by looking at patternsin how data are paired together.

> It is a common misconception that mathematics is inherently or only about numbers or about calculation.
{: .prompt-danger}

# A Non-Rank-Based Approach
So what's the entrypoint for data analysis? Network analysis. Network analysis is the study of empirical [graphs](https://en.wikipedia.org/wiki/Graph_theory). Note that the edge set of a graph is relation, and also notice that it can be *any* (homogenous) relation on the vertex set including orders. So some graphs have edge sets that are orders.

What sort of graphs can we study through network analysis with order theory in mind?

Suppose we have observed a collection of pairs. We can take those pairs to be the edges of a [directed graph (digraph)](https://en.wikipedia.org/wiki/Directed_graph). With this directed graph we can consider a [reachability relation](https://en.wikipedia.org/wiki/Reachability) on its nodes which is a partial order when the digraph is acyclic and otherwise will be a [preorder](https://en.wikipedia.org/wiki/Preorder). With this reachability relation in hand we can compute various counting, probability, or other measures/functions on it that describe how orderly the structure of the network is.

Okay, but networks often change structure. Some of these changes may be quite predictable while others are random with respect to what we know. We need statistics once again! The formal definition of a [random variable](https://en.wikipedia.org/wiki/Random_variable#Definition) says nothing about whether its image or domain are numbers or not. The pure math only supposes any set with certain operations (the [ZFC](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) axioms are more than enough). Indeed, we can have random *things* which are not numbers. This naturally brings us to the notion of random networks. Explicitly assigning a probability to each possible network is often infeasible except on a relatively small space of networks. Instead it can be more feasible to model a conditional likelihood for when the edges or vertices are observed. Richard McElreath has a delightful example which I've been able to adapt to a healthcare setting:

<iframe width="560" height="315" src="https://www.youtube.com/embed/hnYhJzYAQ60?si=YDV2s3ocyNZ5fZDD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

With a random network we should expect our descriptions of the ordinliness of our data to vary according to some distribtuion.

> I have the skills to build this type of model, but I don't have an interesting data set for it. If someone is interested in a collaboration, and can provide data and domain knowledge, feel free to reach out.
{: .prompt-tip}

# Concluding Thoughts
Personally, I think we've barely scratched the surface of studying order in an empirical setting. I'm excited by the possiblities for applications of order theory. Order can be studied without ranks, but I don't think ranks are inherently problematic either and may enhance certain analyses. I tried to specifically *not* use ranks in this post, but there are some additional things we can add to that random/dynamic network analysis that *do* involve ranks.
