---
title: A Quick Reference to Some Common Orders
date: 2024-02-27 04:49:15
authors: [galen]
categories: [math,order-theory]
tags: [math,mathematics,order,order-theory,reflexive,antisymmetric,transitive,irreflextive,asymmetric,strongly-connected,connected,product-order,pareto-order,lexicographic-order,function-induced-order,consensus-order,magnitude,proximity-order,hausdorff-distance]
math: true
mermaid: true
image:
	path: /assets/images/ce6b698c-e299-4bf5-b9e2-e0e9df66c6d9.jpg
	alt: A Quick Reference to Some Common Orders
---

## Introduction
This post is just dumping a short list of notions of order from my MSc thesis days.

## Broad Classes of Orders

There are four common classes of orders.

### Non-Strict Partial Order
- Reflexive
- Antisymmetric
- Transitive


### Strict Partial Order
- Irreflexive
- Asymmetric
- Transitive

### Non-Strict Total Order
- Reflexive
- Transitive
- Antisymmetric
- Strongly-connected

### Strict Total Order
- Irreflexive
- Transitive
- Connected

## Multidimensional Orders

There are orders which sit over tuples, which themselves may be elements of a relation.

- Product order
- Lexicographic order
- Pareto order


## Function-Induced Orders

Sometimes a collection can be assigned an order by the level sets of a function.

### Consensus Order

Suppose a collection of points $S$ where $x \leq y$ if-and-only-if there are more elements of $x$ dominated by elements of $y$ than *vice versa*.

### Proximity Order

We can define orders by their proximity to a reference element or set.

#### Point Proximity Orders
Give a choice of metric space $(X, \rho)$ and a reference element of that metric space $\psi \in X$, then we consider $x \leq y$ if-and-only-if $\rho(\psi, x) \leq \rho(\psi, y)$.

#### Set Proximity Orders

The [Hausdorff distance](https://en.wikipedia.org/wiki/Hausdorff_distance) can similarly be used to induce an order on a collection of sets given a reference set.
