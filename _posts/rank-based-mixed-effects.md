---
title: A Rank-Based Mixed Effects Model
date: 2023-03-04 08:48:12 -0800
categories: [statistics,rank-based-statistics]
tags: [statistics,math,ranks,ranking,rank-based-statistics]
math: true
mermaid: true
---

# Introduction

This post is a response to particular claim made in the following video:

{% include embed/youtube.html id='qee6b7vl2O0' %}

The claim in the video is this:

> **Quotation** (Dustin Fife)
> The original rank-base procedures were modelled after t-tests, ANOVA's, and regressions. They're not designed for these really complicated situations.

These claims are essentially correct *per se*. As far as I have read, many (albeit not all), of the earlier contributors (especially Wilcoxon) to rank-based statistics were motivated by replacing common parametric procedures. I won't dig further into the history here. What struck me is the omission of using modern techniques alongside rank-based statistics.

> The claim I am quoting above was in the context of whether there are "rank-based equivalents" to more complicated models. I discuss this claim in that context in one of my other posts, so I won't re-hash that here.
{: .prompt-tip}

In this post I want to present *an* example. It is far from the only example that could be produced as mathematical functions can be composed together in more ways than I can itemize or enumerate. Much more complicated examples could be constructed by automatically generating large computation graphs on the random variables. My goal is to show a rank-based model that is more complicated than [simple linear regression](https://en.wikipedia.org/wiki/Simple_linear_regression) but also understandable without unsurmountable effort.

# Example

While I've never participated in a full marathon, my understanding is a set of participants run for 42.195 kilometres. It is a form of competetion where there is a first, second, and third place based on ranking participant arrival times. Below I will assume that we are using the *dense ranking method*.

For each $i$th participant we can consider take their arrival time in the $j$th race to be $T_{ij}$. We can compute the participants' ranking across the races:

$$\operatorname{ranking}_j(T_{1j}, \dots,  T_{ij}, \ldots, T_{mj}) = \begin{bmatrix} \operatorname{rank}(T_{1j}) \\ \vdots \\ \operatorname{rank}(T_{mj}) \end{bmatrix}$$


> What if we are just given the ranks/rankings? In that case we would have [missing data](https://en.wikipedia.org/wiki/Missing_data) since the scores $T_{ij}$ would be unknown. If the underlying arrival times $T_{ij}$ are all continuous random variables, then the distribution of ranks within a ranking will be almost-surely uniform. In such a case the underlying distributions for $T_{ij}$ may not be important to the analysis. Otherwise we might perform various forms of imputation (e.g. Bayesian imputation) to account for the missing values.
{: .prompt-tip}

> For simplicity, I am assuming that each runner participates in every race. This is an unrealistic assumption, but fortunately it can be accounted for in a real application. It involves using tricks such as masking, or coding a custom computation graph, such that not all study participants are used in every competition.
{: .prompt-info}


While runners do not always get a monitary (i.e. numerical) reward, we will suppose there is a numerical reward $Y$.

We can take advantage of the identity 

$$\prod_{j=\ell}^k  \mathbb{I}(\operatorname{rank} \leq j) = \mathbb{I}(\operatorname{rank} \leq \ell)$$ 

which holds because for arbitrary $a \leq b$ that $\mathbb{I}(\operatorname{rank} \leq a) \implies \mathbb{I}(\operatorname{rank} \leq b)$. I won't formally prove the identity here, but to get some intuition consider the following table.

|   rank |   $\mathbb{I}(\operatorname{rank} \leq 1)$ |   $\mathbb{I}(\operatorname{rank} \leq 2)$ |   $\mathbb{I}(\operatorname{rank} \leq 3)$ |   $\mathbb{I}(\operatorname{rank} \leq 4)$ |   $\mathbb{I}(\operatorname{rank} \leq 5)$ |   $\mathbb{I}(\operatorname{rank} \leq 6)$ |   $\mathbb{I}(\operatorname{rank} \leq 7)$ |   $\mathbb{I}(\operatorname{rank} \leq 8)$ |   $\mathbb{I}(\operatorname{rank} \leq 9)$ |   $\mathbb{I}(\operatorname{rank} \leq 10)$ |
|-------:|-------------------------------------------:|-------------------------------------------:|-------------------------------------------:|-------------------------------------------:|-------------------------------------------:|-------------------------------------------:|-------------------------------------------:|-------------------------------------------:|-------------------------------------------:|--------------------------------------------:|
|      1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                           1 |
|      2 |                                          0 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                           1 |
|      3 |                                          0 |                                          0 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                           1 |
|      4 |                                          0 |                                          0 |                                          0 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                           1 |
|      5 |                                          0 |                                          0 |                                          0 |                                          0 |                                          1 |                                          1 |                                          1 |                                          1 |                                          1 |                                           1 |
|      6 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          1 |                                          1 |                                          1 |                                          1 |                                           1 |
|      7 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          1 |                                          1 |                                          1 |                                           1 |
|      8 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          1 |                                          1 |                                           1 |
|      9 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          1 |                                           1 |
|     10 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                          0 |                                           1 |

From the above table it should be clear that multiplying two columns together always has one of the two input columns as the output. Specifically, it is the column $\mathbb{I}(\operatorname{rank} \leq a)$  such that $a \leq b$. This reveals that $0 \land 1 = 0$, which can be represented as $0 \times 1$, is part of why we get this absorbing property.

The following code produces the previous table if you want to tinker.

```python
import pandas as pd

d = {}
d['rank'] = list(range(1,11))

for i in range(1,11):
    d[f'$\\mathbb{{I}}(\\operatorname{{rank}} \\leq {i})$'] = [int(j <= i) for j in d['rank']]

df = pd.DataFrame(d)

print(df.to_markdown(index=False))
```

The above identity substantially simplifies our model to something that may not even appear to be a mixed model. But it is a mixed model! The nested effects are in getting a better ranking in a partial order of runners.

The final model is given by

$$Y_i = \gamma_{\infty} + \sum_{j=1}^n \gamma_{j} \mathbb{I}(\operatorname{rank} \leq j) + \epsilon_i$$

Further effects can be put into such a model to account for different ranking methods and rules for assigning reward. I took marathons as an example, but there is nothing about this model that truly depends us considering marathons. What was required was a collection of random variables that could be ranked, and a numerical reward $Y$, in order to fit this model. The mixed effect achieves the notion *cumulative reward* for ranking better in competition.

# Conclusions
