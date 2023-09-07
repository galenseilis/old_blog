---
title: A Rank-Based Mixed Effects Model
date: 2023-09-06 07:00:12 -0800
categories: [statistics,rank-based-statistics]
tags: [statistics,math,ranks,ranking,rank-based-statistics,rank-based-mixed-effects,mixed-effects]
math: true
mermaid: true
---

# Introduction

This post is a response to a particular claim made in the following video:

{% include embed/youtube.html id='qee6b7vl2O0' %}

The claim in the video is this:

> **Quotation** (Dustin Fife)
> The original rank-base procedures were modelled after t-tests, ANOVA's, and regressions. They're not designed for these really complicated situations.

These claims are correct. As far as I have read, many (albeit not all), of the earlier contributors (especially Wilcoxon) to rank-based statistics were motivated by using certain rank-based nonparametric procedures *in leu* of certain parametric procedures.

> The claim I am quoting above was in the context of whether there are "rank-based equivalents" to more complicated models. I discuss this claim in that context in one of my other posts, so I won't re-hash that here.
{: .prompt-tip}

In this post I want to present *an* example. It is far from the only example that could be produced as mathematical functions can be composed together in more ways than I can itemize or enumerate. Much more complicated examples could be constructed by automatically generating large computation graphs on the random variables. Furthermore, I don't claim that this model structure is optimal for any current applications. I wouldn't know. I just made it up. My goal is to show a rank-based model that is more complicated than [simple linear regression](https://en.wikipedia.org/wiki/Simple_linear_regression) but also understandable without unsurmountable effort.

# Example

While I've never participated in a full marathon, my understanding is a set of participants run for 42.195 kilometres. It is a form of competition where there is a first, second, and third place based on ranking participant arrival times. Below I will assume that we are using the *dense ranking method*.

For each $i$th participant we can take their arrival time in the $j$th race to be $T_{ij}$. We can compute the participants' ranking across the races:

$$\operatorname{ranking}_j(T_{1j}, \dots,  T_{ij}, \ldots, T_{mj}) = \begin{bmatrix} \operatorname{rank}(T_{1j}) \\ \vdots \\ \operatorname{rank}(T_{mj}) \end{bmatrix}$$


> What if we are just given the ranks/rankings? In that case we would have [missing data](https://en.wikipedia.org/wiki/Missing_data) since the scores $T_{ij}$ would be unknown. If the underlying arrival times $T_{ij}$ are all continuous random variables, then the distribution of ranks within a ranking will be almost-surely uniform. In such a case the underlying distributions for $T_{ij}$ may not be important to the analysis.
{: .prompt-tip}

> For simplicity, I am assuming that each runner participates in every race. This is an unrealistic assumption, but fortunately it can be accounted for in a real application. It involves using tricks such as masking, or coding a custom computation graph, such that not all study participants are used in every competition. It is also possible to impute the counterfactual of what a runner's rank *would have been* if they had participated in the race, but the procedure would require accounting for the fact that the ranks are relative to the other racers. This would motivate modelling the arrival time distributions to estimate this counterfactual.
{: .prompt-info}


While runners do not always get a numerical (i.e. monitary) reward, we will suppose there is a numerical reward $Y$ that depends on their rank (not their arrival time *per se*) in a given race. Let us construct a sequence of models that have mixed effects with increasing complexity. The first model is just 

$$Y = \gamma_{\infty} + \epsilon$$

where $\gamma_{\infty}$ is an intercept parameter and $\epsilon$ is some exogenous noise variable. I'll explain the subscript "$\infty$" soon enough, but just take it as arbitrary fluff for the moment. In this model we have not considered the ranks. Everyone gets some amount of reward notwithstanding some unexplained variation; a participation award. Now let's say that everyone who got 3rd or better placement gets some reward.

$$Y = \gamma_{\infty} + \gamma_3 \mathbb{I}(\text{rank} \leq 3) + \epsilon $$

This model with an added term for being third-or-better place still isn't a mixed model in any clear sense, but the next iteration or two should make it clearer where we are headed. Let's *nest* the next effect within the first, although I will cheat by reusing the $\gamma$ symbols without making some explicit substitution for new variables. We can tersely take this substitution to be $$\underbrace{\gamma_3}_{\text{old}} := \underbrace{\gamma_3}_{\text{fixed}} + \underbrace{\gamma_2 \mathbb{I}(\text{rank} \leq 2)}_{\text{random}}$$:

$$\begin{align}Y &=  \gamma_{\infty} + (\gamma_3 + \gamma_2 \mathbb{I}(\text{rank} \leq 2) )\mathbb{I}(\text{rank} \leq 3) + \epsilon \\ &= \gamma_{\infty} + \gamma_3\mathbb{I}(\text{rank} \leq 3) + \gamma_2 \mathbb{I}(\text{rank} \leq 2)\mathbb{I}(\text{rank} \leq 3) + \epsilon \\ &= \gamma_{\infty} + \gamma_3\mathbb{I}(\text{rank} \leq 3) + \gamma_2 \prod_{j=2}^3 \mathbb{I}(\text{rank} \leq j) + \epsilon \end{align}$$

Hopefully you can see that the above is already a mixed effect model, where the rank 2 effect is nested within the rank 3 effect, but let's nest another random effect by making the further substitution: 

$$\underbrace{\gamma_2}_{\text{old}} := \underbrace{\gamma_2}_{\text{fixed}} + \underbrace{\gamma_1 \mathbb{I}(\text{rank} \leq 1)}_{\text{random}}.$$

This obtains the expression:

$$\begin{align}Y &=  \gamma_{\infty} + (\gamma_3 + (\gamma_2 + \gamma_1 \mathbb{I}(\text{rank} \leq 1)) \mathbb{I}(\text{rank} \leq 2) )\mathbb{I}(\text{rank} \leq 3) + \epsilon \\   &=  \gamma_{\infty} + \gamma_3\mathbb{I}(\text{rank} \leq 3) + (\gamma_2 + \gamma_1 \mathbb{I}(\text{rank} \leq 1)) \mathbb{I}(\text{rank} \leq 2)\mathbb{I}(\text{rank} \leq 3) + \epsilon \\ &=  \gamma_{\infty} + \gamma_3\mathbb{I}(\text{rank} \leq 3) + \gamma_2 \mathbb{I}(\text{rank} \leq 2)\mathbb{I}(\text{rank} \leq 3) + \gamma_1 \mathbb{I}(\text{rank} \leq 1)\mathbb{I}(\text{rank} \leq 2)\mathbb{I}(\text{rank} \leq 3) + \epsilon \\ &=  \gamma_{\infty} + \gamma_3\mathbb{I}(\text{rank} \leq 3) + \gamma_2 \prod_{j=2}^3 \mathbb{I}(\text{rank} \leq j) + \gamma_1 \prod_{j=1}^3 \mathbb{I}(\text{rank} \leq j) + \epsilon \end{align}$$

From here you can probably guess the consequence of nesting out to some finite $k$:

$$Y = \gamma_{\infty} + \sum_{q=1}^k \gamma_q \prod_{q \leq j \leq k} \mathbb{I}(\text{rank} \leq j) + \epsilon .$$

By now I hope you're convinced that we can in fact make (arbitrarily deeply) nest mixed effects models that are also rank-based. And you might further spot that $\gamma_{\infty} = \gamma_{\infty}  \mathbb{I}(\text{rank} \leq \infty)$, although that is still just kind of fluff. Unless you're generalizing to a set like the [extended real number line](https://en.wikipedia.org/wiki/Extended_real_number_line) we shouldn't really use infinity as a number. I do find it to be a nice reminder that it follows a similar rationale as the other terms even though it jumps from $k$ to $\infty$ with no terms in between. 

But we're not quite done. There is a further simplification that we can make to the mathematical form of the model.

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

From the above table it should be clear that multiplying two columns together always has one of the two input columns as the output. Specifically, it is the column $\mathbb{I}(\operatorname{rank} \leq a)$  such that $a \leq b$. This should draw our attention to the fact that $0 \land 1 = 0$, which can be represented as $0 \times 1$, as an informal explanation of the identity of interest.

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

A final model is given by

$$Y = \gamma_{\infty} + \sum_{j=1}^n \gamma_{j} \mathbb{I}(\operatorname{rank} \leq j) + \epsilon$$

Further effects can be put into such a model to account for different ranking methods and rules for assigning reward. I took marathons as an example, but there is nothing about this model that truly depends us considering marathons. What was required was a collection of random variables that could be ranked, and a numerical reward $Y$, in order to fit this model. The mixed effect achieves the notion *cumulative reward* for ranking better in competition. (Indeed, this is a special case of something I term a *cumulative mixed effects model* for which I am working on a manuscript).

The last point, which is really a concession, is that this rank-based model is perhaps better termed a [*semiparametric*](https://en.wikipedia.org/wiki/Semiparametric_regression) regression model because we would likely still consider the distribution of the rewards $Y$ even if we can get away with ignoring the distribution of the arrival times in the marathon $T$. And even then, if $T$ is not continous then we make still have to consider the distribution of $T$ explicitly as well. Nonetheless, the possiblity of this semiparametric model is notable.

You could further compute the regression on the ranks of $Y$, however I don't think that would be natural for the marathon example. We already know that a better arrival time entails getting a better reward, or at least no-worse. But a fully nonparametric form of this is possible via that route on continous random variabless.

# Conclusions

Rank-based parametric, semiparametric, and nonparametric mixed-effects models exist.
