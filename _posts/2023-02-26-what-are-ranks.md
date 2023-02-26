---
title: What Are Ranks?
date: 2023-02-26 10:16:09 -0800
categories: [statistics,rank-based-statistics]
tags: [statistics,ranks,ranking]
math: true
mermaid: true
---

This post looks at the notion of ranking data or variables. Broadly, ranks are numbers used to describe something about the order-like properties on the elements of a set. I have quite often refered to "the" rank transform, but it actually it isn't a uniquely specified thing. For example, [`scipy.stats.rankdata`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rankdata.html) implements multiple ranking methods depending on tied elements:

> method : {‘average’, ‘min’, ‘max’, ‘dense’, ‘ordinal’}, optional
>
>    The method used to assign ranks to tied elements. The following methods are available (default is ‘average’):
>
> -            ‘average’: The average of the ranks that would have been assigned to all the tied values is assigned to each value.
>
> -            ‘min’: The minimum of the ranks that would have been assigned to all the tied values is assigned to each value. (This is also referred to as “competition” ranking.)
>
> -            ‘max’: The maximum of the ranks that would have been assigned to all the tied values is assigned to each value.
>
> -            ‘dense’: Like ‘min’, but the rank of the next highest element is assigned the rank immediately after those assigned to the tied elements.
>
> -            ‘ordinal’: All values are given a distinct rank, corresponding to the order that the values occur in a.

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

You can see above that most methods return only integers, with the exception of the "average" method. The "average" method will output rational numbers to account for ties whereas the minimum method and maximum method create spacing between the ranks. Among these I find the dense method the most natural, which simply allows duplicate values to have the same rank. Some approaches attempt to avoid this, but I don't think it is a problem provided that the resulting distribution is considered in an analysis. The ordinal method ignores ties altogether, but does have the advantage of being equal to the indices of a sorted array up to a translation of unity. 

And similarly Wikipedia lists some [methods of ranking](https://en.wikipedia.org/wiki/Ranking#Strategies_for_assigning_rankings):
- Standard competition ranking
- Modified competition ranking
- Dense ranking
- Ordinal ranking
- Fractional ranking

I want to make a distinction which is not frequently made explicit, but does specify the mathematics. Namely we should make the distinction between a **ranking** and a **rank** which was suggested language in [this post](https://stats.stackexchange.com/a/605359/69508) by user [Sextus Empiricus](https://stats.stackexchange.com/users/164061/sextus-empiricus).

In [this post](https://stats.stackexchange.com/a/605350/69508) I gave the following definition of an "abstract ranking" which covers most forms of ranking.

> **Definition** Assume a collection random variables $\{X_1(\omega), \ldots, X_n(\omega) \}$ on outcome space $\Omega$, and $\leq$ is a partial order. An **abstract ranking** $$\rho: \prod_{i=1}^n X_i(\omega) \mapsto \mathbb{R}_{\geq 0}^n$$ is a function such that there exists a non-decreasing function $\kappa:\mathbb{N} \mapsto \mathbb{R}_{\geq0}$ that satisfies $\rho(\vec x)_i \leq \kappa(n)$ for all $i\in \{1, \ldots, n\}$. It must also hold that $\rho(\vec x)_i \leq \rho(\vec x)_j \iff x_i \leq x_j$ for all $i,j \in \{1, \ldots, n\}$ and for all $\omega \in \Omega$ [exor](https://en.wikipedia.org/wiki/Exclusive_or) $\rho(\vec x)_i \geq \rho(\vec x)_j \iff x_i \leq x_j$ for all $i,j \in \{1, \ldots, n\}$ and for all $\omega \in \Omega$. An component of an image element of an abstract ranking is called an **abstract rank**.

While the above definition is quite abstract, it assumes relatively little and provides an umbrella definition for various forms of ranking. I believe it has applications in [learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank) recommendations or detect inequity in addition to some of its familiar uses.

But what does this abstract definition mean? Well, in a pinch it means that a ranking is a collection of ranks that respect some order relation. Like the special cases of ranking given above, any abstract ranking takes a collection of instances of random variables and assigns a number that preserves an order within that collection. Not that this monotonicity applies to the ranks within the ranking, but ranks themselves are not monotonic functions of the outcome space due to the comparative and bounded way they are calculated.
