---
title: A Biology Guy Divided By Zero
date: 2023-02-28 14:15:02
categories: [math,algebra,division]
tags: [math,biology,evolutionary-biology,narrow-sense-heritability,heritability,algebra,division,zero]
math: true
---

I want to share a recollection of an amusing argument I had back in my undergraduate days. A biology professor explained a definition of *narrow sense heritability* in the sense of a [parent-offspring regression](https://en.wikipedia.org/wiki/Heritability#Parent-offspring_regression). In this approach the heritability is being estimated via the slope of the regression line. Our professor further claimed that if there is no variability in parent phenotype, then the heritability is zero. Herein lies the problem.

Supposing least-squares estimation, the slope $\beta$ can be written as the ratio $\frac{\operatorname{Cov}[X,Y]}{\operatorname{Var}[X]}$. In our estimate of the slope from a sample, $\hat \beta$, we can represent it as

$$\hat \beta = \frac{\sum_{i=1}^n \left(x_i - \frac{1}{n} \sum_{i=1} x_i \right) \left(y_i - \frac{1}{n} \sum_{i=1} y_i \right)}{\sum_{i=1}^n \left(x_i - \frac{1}{n} \sum_{i=1} x_i \right)^2}.$$

Notice that if all $x$ values are equal, then $\hat \beta$ would be partially evaluated to $\frac{a}{0}$ for some real number $a$. Most students will recognize that this is an undefined expression in standard algebra. Here is a Numberphile video that explains this perspective.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BRRolKTlF6Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

If we were to allow 
$$\frac{a}{0} = 0$$
and 
$$\frac{b}{0} = 0$$
then we have
$$\frac{a}{0} = \frac{b}{0}$$
or 
$$a = b$$ for any arbitrary $a$ and $b$. Since $a$ and $b$ were arbitrary, this is tantamount to saying that all numbers are the same number. In other words $1=2=3=\pi=\frac{5}{9}$ would be taken to be true. But this violates our assumption (or construction in standard math) that these numbers are distinct. What we've found is *nonsense*.

You cannot count or quantify nonsense. It is not that there are zero beds made of sleep but rather that it isn't sufficiently clear what a "bed made of sleep" is meant to be in order to start counting them.

If you're going to define a concept in terms of some piece of math, then how you reason about that concept must play by the rules of that mathematics. That is, the mathematics is the specification of what you thought you were talking about it in the first place.

This isn't to say that we cannot divide by zero regardless of the algebra we are considering. The following video gives a quick indication of [Wheel algebra](https://en.wikipedia.org/wiki/Wheel_theory) that allows division by zero. There are other algebras that allow division by zero, none with obvious applications that I'm aware of, leading to it being a niche side topic that division by zero *can* be defined.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ydLTfyXaQmU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

I explained to the professor that dividing by zero leads to an issue of definition. He responded, "Galen, are you a math guy?" with a perceived framing that somehow that would be grounds for dismissing my concern. I don't recall exactly how I responsed to that question, but I recall being surprised at how irrelevant that argument was. Logicians know this as a [genetic fallacy](https://en.wikipedia.org/wiki/Genetic_fallacy). I missed the opportunity, probably to my own benefit, to retort, "I don't know `<professor's name>`, are you a biology guy?"
