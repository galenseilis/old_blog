---
title: What Are Ranks?
date: 2023-02-26 10:16:09 -0800
categories: [statistics,rank-based-statistics]
tags: [statistics,ranks,ranking]
math: true
mermaid: true
---

# Introduction

This post looks at the notion of ranking data or variables. Broadly, ranks are numbers used to describe something about the order-like properties on the elements of a set. We might think of runners arriving at the end of a marathon at different times and assigning 1st, 2nd, 3rd, etc, place to the runners in order of their arrival accross the finish line.

# Common Ranks in Statistics
A lot of folks (including myself) have often referred to "the" rank transform, but it actually it isn't a uniquely specified thing. For example, [`scipy.stats.rankdata`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rankdata.html) implements multiple ranking methods depending on how tied elements are to be handled:

> `method` : {`‘average’`, `‘min’`, `‘max’`, `‘dense’`, `‘ordinal’`}, optional
>
>    The method used to assign ranks to tied elements. The following methods are available (default is `‘average’`):
>
> -            `‘average’`: The average of the ranks that would have been assigned to all the tied values is assigned to each value.
>
> -            `‘min’`: The minimum of the ranks that would have been assigned to all the tied values is assigned to each value. (This is also referred to as “competition” ranking.)
>
> -            `‘max’`: The maximum of the ranks that would have been assigned to all the tied values is assigned to each value.
>
> -            `‘dense’`: Like `‘min’`, but the rank of the next highest element is assigned the rank immediately after those assigned to the tied elements.
>
> -            `‘ordinal’`: All values are given a distinct rank, corresponding to the order that the values occur in `a`.

Let us consider an example. Supposing a random variable $X \sim \operatorname{binomial} \left(10, \frac{1}{2} \right)$ which we can sample of size ten from and print a table using the following Python code. The binomial is suitable for this example in order to show how these ranking methods evaluate ties. In contrast, the distribution of the ranks of a continuous random variable are [almost surely](https://en.wikipedia.org/wiki/Almost_surely) uniform and would resemble the ordinal method regardless of the ranking method chosen above.

```python
import numpy as np
import pandas as pd
from scipy.stats import rankdata

np.random.seed(2018)

methods = (
  'average', 
  'min', 
  'max', 
  'dense', 
  'ordinal'
  )

d = {}
d['x'] = np.random.binomial(10, 0.5, size=10)
for method in methods:
  d[f'{method} method'] = rankdata(d['x'], method=method)

df = pd.DataFrame(d)
df = df.sort_values(by='x')
print(df.to_markdown(index=False))
```

The code above prints the following table.


|   x |   average method |   min method |   max method |   dense method |   ordinal method |
|----:|-----------------:|-------------:|-------------:|---------------:|-----------------:|
|   3 |              1.5 |            1 |            2 |              1 |                1 |
|   3 |              1.5 |            1 |            2 |              1 |                2 |
|   4 |              3   |            3 |            3 |              2 |                3 |
|   5 |              4.5 |            4 |            5 |              3 |                4 |
|   5 |              4.5 |            4 |            5 |              3 |                5 |
|   6 |              6.5 |            6 |            7 |              4 |                6 |
|   6 |              6.5 |            6 |            7 |              4 |                7 |
|   7 |              9   |            8 |           10 |              5 |                8 |
|   7 |              9   |            8 |           10 |              5 |                9 |
|   7 |              9   |            8 |           10 |              5 |               10 |

You can see above that most methods return only integers, with the exception of the "average" method. What the average method accomplishes it preserving the total rank even when ties occur. The "average" method will output rational numbers to account for ties whereas the minimum method and maximum method create spacing between the ranks. Another kind of "rank" which is non-integer-valued is the [percentile rank](https://en.wikipedia.org/wiki/Percentile_rank) which is the percentage of scores in the sample that are less than the given score. Certain percentile ranks can be calculated using [`scipy.stats.percentileofscore`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.percentileofscore.html) or by passing `pct=True` into [`pandas.DataFrame.rank`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html).

The ordinal method ignores ties altogether, but does have the advantage of being equal to the indices of a sorted array up to a translation of unity. The ordinal method is called `first` in the methods available in [`pandas.DataFrame.rank`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html).

And similarly Wikipedia lists some [methods of ranking](https://en.wikipedia.org/wiki/Ranking#Strategies_for_assigning_rankings):
- Standard competition ranking
- Modified competition ranking
- Dense ranking
- Ordinal ranking
- Fractional ranking

Many ranking procedures are what I call **count ranks** because they involve some kind of counting procedure. For example, the dense ranking method can be considered to assign a rank to an element equal to the number of other elements strictly less than it plus unity.

The above ranking procedures assume that the ranks are an order-preserving function, but we can also have order-reversing functions that are in a sense a rank. For example, we might have a weight-lifting competition where the person who lifts **the most** gets **first** place, thus assigning the largest weight lifted to value of unity. While `scipy.stats.rankdata` does not do order-reversed ranking *per se*, applying an order-reversing operation (e.g. $f(X) = - X$) before applying an order-preserving ranking will acheive the desired result. Some implementations such as `pandas.DataFrame.rank` provide a Boolean parameter `ascending` to indicate whether the ranking will be order-preserving or order-reversing.

I want to make a distinction which is not frequently made explicit, but does specify the mathematics nicely. Namely we should make the distinction between a **ranking** and a **rank** which was suggested language in [this post](https://stats.stackexchange.com/a/605359/69508) by user [Sextus Empiricus](https://stats.stackexchange.com/users/164061/sextus-empiricus).

Rank-based statistics are the use of any ranking function to either produce ranks, or a function of ranks, of random variables.

# Abstract Ranks
In [this post](https://stats.stackexchange.com/a/605350/69508) I gave the following definition of an "abstract ranking" which covers most forms of ranking.

> **Definition** Assume a collection random variables $\{X_1(\omega), \ldots, X_n(\omega) \}$ on outcome space $\Omega$, and $\leq$ is a partial order.
>
> An **abstract ranking** $$\rho: \prod_{i=1}^n X_i(\omega) \mapsto \mathbb{R}_{\geq 0}^n$$ is a function such that there exists a non-decreasing function $\kappa:\mathbb{N} \mapsto \mathbb{R}_{\geq0}$ that satisfies $\rho(\vec x)_i \leq \kappa(n)$ for all $i\in \{1, \ldots, n\}$.
>
> It must also hold that $\rho(\vec x)_i \leq \rho(\vec x)_j \iff x_i \leq x_j$ for all $i,j \in \{1, \ldots, n\}$ and for all $\omega \in \Omega$ [exor](https://en.wikipedia.org/wiki/Exclusive_or) $\rho(\vec x)_i \geq \rho(\vec x)_j \iff x_i \leq x_j$ for all $i,j \in \{1, \ldots, n\}$ and for all $\omega \in \Omega$.
>
> An component of an image element of an abstract ranking is called an **abstract rank**.

While the above definition is quite abstract, it assumes relatively little and provides an umbrella definition for various forms of ranking. I believe it has applications in [learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank) recommendations or detect inequity in addition to some of its familiar uses.

But what does this abstract definition mean? Well, in a pinch it means that a ranking is a collection of ranks that respect some order relation. Like the special cases of ranking given above, any abstract ranking takes a collection of instances of random variables and assigns a number that preserves an order within that collection. Not that this monotonicity applies to the ranks within the ranking, but ranks themselves are not monotonic functions of the outcome space due to the comparative and bounded way they are calculated.

# Ranks vs Ratings

I want to quickly share a distinct which I find valuable for avoiding certain confusions in mathematical modelling. In this post I am explicitly considering and defining ranking and ranks as functions that satisfy an order relation. This should be contrasted to asking someone to assign ordinals (e.g. Likert-like scales) or forced choice preferences to a selection of options because we often observe [intransitivity](https://en.wikipedia.org/wiki/Intransitivity) in human preferences. This intransivity violates the assumptions of a partial order that I made above, which even relaxing from a partially ordered set to a [weak ordering](https://en.wikipedia.org/wiki/Weak_ordering) will not satisfy.

When I am thinking about these mathematical transformations that are guaranteed to preserve/reverse order I use the term **ranking**, whereas observations of preferences by a human/AI/system I would instead use the term **rating**.

# Beyond Ranking Numbers

I want to share a less obvious facet of ranking as I have defined it above. When (I believe) most people study [random variables](https://en.wikipedia.org/wiki/Random_variable) they are thinking about numerical-valued observations. But consider two facts:

- Random variables can have images that are composed of just about anything.
  - Examples:
    - vectors (although there at least we often use the notation $\vec X$ for a random vector)
    - matrices
    - tensors
    - sets
    - trees
    - graphs
    - hypergraphs
    - [groups](https://en.wikipedia.org/wiki/Group_(mathematics))
- [Partial orders](https://mathworld.wolfram.com/PartiallyOrderedSet.html) can likewise be defined on just about anything.

So we can have just-about-anything-valued random variables and partial orderings on just about anything. Taking these notions together, we can rankings and ranks defined on just about anything as well. We're not restricted to numbers. We're restricted to where we are interested in describing order with numbers.

# Conclusions

Ranks are transformations of things, often numbers, to describe something about their order relationships to other things. In the context of statistics we have rankings of random variables, giving rise to the notion of rank-based statistics to help us study order in the presence of uncertainty.
