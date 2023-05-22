---
title: Quick Review of the Graphoid Axioms
date: 2023-05-20 00:00:00 -0800
categories: [statistics,mathematical-statistics]
tags: [statistics,mathematical-statistics,graphoid-axioms,probability-theory]
math: true
mermaid: true
---

Consider the following definition:

> **Definition** (Pearl 2009)
>
> Let $V = \{V_1, V_2, \ldots \}$ be a finite set of variables.
> 
> Let $P(\cdot)$ be a joint probability function over the variables in $V$, and let $X$, $Y$, $Z$ stand for any three subsets of the variables in $V$. 
>
> The sets $X$ and $Y$ are said to be **conditionally independent** given $Z$ if
>
> $$P(x | y, z) = P(x|z)$$
> whenever $P(y,z) > 0$.


Denoting this ternary relation as $$(X \mathrel{\unicode{x2AEB}} Y \vert Z)$$, whe have the following properties below.

The first property is **symmetry**.

$$(X \mathrel{\unicode{x2AEB}} Y \vert Z) \implies (Y \mathrel{\unicode{x2AEB}} X \vert Z)$$

> While this is a form of symmetry, it is not the same as [**strongly symmetric**](https://www.sciencedirect.com/science/article/pii/S0195669809001589) when describing any given $n$-ary relation. If it were, we would have to accept propositions such as $$(X \mathrel{\unicode{x2AEB}} Y \vert Z) \implies (Y \mathrel{\unicode{x2AEB}} Z \vert Y)$$. But this can not be so for the same type of reason as to why $Pr(A\vert B) \neq Pr(B \vert A)$ for at least some probability measure $Pr$ on events $A$ and $B$.
{: .prompt-warning }

The second property is **decomposition**,

$$(X \mathrel{\unicode{x2AEB}} (Y, W) \vert Z) \implies (Y \mathrel{\unicode{x2AEB}} X \vert Z)$$,

> Pearl 2009 seems to use $YW$ instead of $(Y,W)$, giving a false impression that we might be considing some kind of multiplication. See [*Notational confusion about conditional independence in Pearl 2009*](https://stats.stackexchange.com/q/605959/69508) for more information.
{: .prompt-warning }

The third property is **weak union**.

$$(X \mathrel{\unicode{x2AEB}} (Y, W) \vert Z) \implies (Y \mathrel{\unicode{x2AEB}} X \vert (Z,W))$$

The fourth property is **contraction**.

$$(X \mathrel{\unicode{x2AEB}} Y | Z) \land (X \mathrel{\unicode{x2AEB}} W | (Z,Y)) \implies (X \mathrel{\unicode{x2AEB}} (Y,W) \vert Z)$$

Finally the fifth property is **intersection**.

$$(X \mathrel{\unicode{x2AEB}} W \vert (Z, Y)) \land (X \mathrel{\unicode{x2AEB}} Y \vert (Z, W)) \implies (X \mathrel{\unicode{x2AEB}} (Y,W) \vert Z)$$
