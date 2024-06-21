---
title: DRAFT - Gutsick Gibbon and Dr. Carter on Normality and Weighted Averages
date: 2024-06-20 04:51:15
categories: [statistics]
tags: [statistics,probability,normal-distribution,mathematical-statistics,math,maths,moments,expectation,expected-value,average,weighted-average,weighted-arithmetic-mean,arithmetic-mean]
math: true
mermaid: true
---

This post was prompted by the following video by the YouTube channel Gutsick Gibbon:

<iframe width="560" height="315" src="https://www.youtube.com/embed/zzkYmKJ6Sk8?si=WJL1G98hEJaMhzZt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Some of the topics that were discussed in that video were about statistics, a subject that I'm passionate about. I'll give some commentary around that topic in this post, but I'm going to try to avoid diving into the full context of what Gutsick Gibbon is talking about. There are just too many tangents.


<a href="https://imgflip.com/i/8uj5re"><img src="https://i.imgflip.com/8uj5re.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>


## How good was the sample?

I won't try to cover every aspect of the sample that was under discussion, but both Roohif (embedded below) and Gutsick Gibbon (embedded above) give extensive critiques of various aspects of the studies by Tomkins.

<iframe width="560" height="315" src="https://www.youtube.com/embed/j9XbeckuzwY?si=KKtSOg9vFC6V_rNo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<a href="https://imgflip.com/i/8uj598"><img src="https://i.imgflip.com/8uj598.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>

I will just echo that it is imperative that the right statistical population has been sampled from (or at least close enough) in order for the accurate inferences to be made.

### Accuracy in Distribution

<a href="https://imgflip.com/i/8uj5w0"><img src="https://i.imgflip.com/8uj5w0.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>

All statistical properties of a statistical population are captured in its [joint cumulative distribution function](https://en.wikipedia.org/wiki/Joint_probability_distribution#Joint_cumulative_distribution_function), including for categorical variables up to a choice of ordering. 

According to the univariate [DKW(M) inequality](https://en.wikipedia.org/wiki/Dvoretzky%E2%80%93Kiefer%E2%80%93Wolfowitz_inequality), an [IID](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) sample of size $n$ has a bounded probability of exceeding a given absolute difference between the [empirical cumulative distribution](https://en.wikipedia.org/wiki/Empirical_distribution_function) and the (population) [cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function).

$$\Pr \left( \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| > \epsilon \right) \leq 2 e^{-2n\epsilon^2}$$

We can convert from this [survival function](https://en.wikipedia.org/wiki/Survival_function) (i.e. the probability of exceedance) to the cumulative probability that the error will not exceed $\epsilon$ by simply taking the complement. This complement rule is a logical consequence of [Kolmogorov's axioms of probability](https://en.wikipedia.org/wiki/Probability_axioms#Kolmogorov_axioms).

$$\Pr \left( \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| > \epsilon \right) \leq 2 e^{-2n\epsilon^2} \iff 1 - 2 e^{-2n\epsilon^2}  \leq \Pr \left( \sup_{x \in \mathbb{R}} \left| F_n(x) - F(x) \right| \leq \epsilon \right)$$


Here is the calculation, taking $\epsilon := \frac{1}{100}$ for the sake of example:

```python
# Python 3.10.12 [GCC 11.4.0] on linux
>>> import numpy as np
>>> 2 * np.exp(-2 * (18000) * (1 / 100)**2)
0.05464744489458512
>>> 1 - _
0.9453525551054149
```

So when the univariate DKW(M) inequality holds, we can say that a sample size of 18 000 would tells us the probability of our estimate of the cumulative distribution function anywhere being within 1% absolute difference from the population cumulative distribution function is no less than 94.54%.

However, the key assumption that may not hold here is the sample variables being [IID](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables). Some of the other concerns that Roohif and Gutsick Gibbon had with Tomkin's work may substantially invalidate this assumption.


## Averages

A part of the what was discussed in the video linked by Gutsick Gibbon was about averages.

### Is the average of a ratio the same as the ratio of the averages?

In short, no, the average of a ratio is not the same as the ratio of the averages in general. The [expectation operator is linear](https://en.wikipedia.org/wiki/Expected_value#Properties), so it distributions over [linear combinations](https://en.wikipedia.org/wiki/Linear_combination). A ratio of two random variables is not a linear combination.

$$\mathbb{E} \left[ \frac{Y}{X} \right] \neq \frac{\mathbb{E}[Y]}{\mathbb{E}[X]}$$

Neither of this expectations are always defined in the population, but there are also many cases where they will be. It depends on what we're willing to assume about the joint distribution of $(X,Y)$.

Even more generally, if $g$ is a non-linear measurable function of the outcome space, then $$\mathbb{E}[f(X)] \neq f(\mathbb{E}[X]).$$

### Can you take an average when distributions are non-normal?

First, you can always take an average of a finite set of numbers. So whenever you have a sample of a random variable suitably-equipped with summation and scale, and notwithstanding other issues like missing data, you can take an average. This comprises a description of the sample.

When it comes to the population the answer is "usually, but not always". The expected value exists for many, but not all distributions. A counterexample is the [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution) whose expectations do not exist. Sometimes there are mathematical techniques available that give us something as close as possible to an expected value as we can even though the expected value itself does not exist. For example, the [odd momments](https://stats.stackexchange.com/a/569486/69508) of a standard Cauchy distribution are zero.

### Weighted Average

#### What are weighted averages?

A [weighted (arithmetic) mean](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean#Mathematical_definition) is a [convex combination](https://en.wikipedia.org/wiki/Convex_combination) which we can write in vector form as 

$$\bar x_{\vec w} \triangleq \frac{\vec w \cdot \vec x}{\Vert \vec w \Vert_1} = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}$$

where I have used a [1-norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#Taxicab_norm_or_Manhattan_norm) to collapse the weights vector in the denominator into a scalar. Indeed, we can recognize this as being a [scalar projection](https://en.wikipedia.org/wiki/Scalar_projection#Definition_in_terms_of_a_and_b). We'll return to that point soon.

#### Can we weight six ways to Sunday to get the right answer from a biased sample?

<a href="https://imgflip.com/i/8uj64n"><img src="https://i.imgflip.com/8uj64n.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>

Dr. Carter suggests that we can weight as much as we like and we will not get the right answer from a biased sample. That's right, especially in practice, but I want to shine some light a couple of nuances.

Even if I have a [unbiased estimator](https://en.wikipedia.org/wiki/Bias_of_an_estimator) for the [expected value](https://en.wikipedia.org/wiki/Expected_value) of a [continuous random variable](https://en.wikipedia.org/wiki/Random_variable#Continuous_random_variable), it will still [almost-never](https://en.wikipedia.org/wiki/Almost_surely) equal the population parameter exactly. This is due to sampling variation, and that will be lurking in real applications whether you use weighted averages or not. Matt Parker provides some real examples of this in the following video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/NbiveCNBOxk?si=CpxDh-py1fumrTD3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Remember I mentioned that weighted averages can be represented as scalar projections? Well, we can ask what range of values we can obtain for $\bar x_{\vec w}$ assuming that $\vec x$ is fixed and we can choose any $\vec w$ we like as long as $\vec 1 \cdot \vec w = 1$. In terms of scaling the componets of $\vec x$ this is equivalent to asking a special case of [linear span](https://en.wikipedia.org/wiki/Linear_span#Definition) where we are limited to convex combinations (recall that all convex combinations are linear combinations). Such a "convex span" will reach any point in the [convex hull](https://en.wikipedia.org/wiki/Convex_hull) of $\vec x$, but since we would subsequently [linearly project](https://en.wikipedia.org/wiki/Projection_(linear_algebra)) (a special case of what I sometimes call ["abstract projection"](https://en.wikipedia.org/wiki/Projection_(mathematics)#Definition)) down onto the real number line there will be some *interval* of reachable points. These extreme points turn out to simply be the [minimum and maximum](https://en.wikipedia.org/wiki/Sample_maximum_and_minimum) of $\vec x$.

We know that the minimum and maximum of a collection of [exchangeable random variables](https://en.wikipedia.org/wiki/Exchangeable_random_variables#Definition) $S = \{ X_1, \ldots, X_n \}$ grows in size because the prediction interval for some random variables $Y$, also exchangeable with the elements of $S$, satisfies 

$$\Pr \left[ Y \in  \right [\min S, \max S]] = \frac{n-1}{n+1}$$

where $n$ is the sample size. This is clearly an increasing function in $n$, so the interval will get wider with sample size.

So provided that the true distribution eventually overlaps with the biased distribution, and our samples from the biased distribution are exchangeable, then with a sufficiently large sample there will exist a weighting function which corrects for the bias. However, if you are just starting with a sample then you will magically know whether you have enough data. Nor will you always have the experimental standards (e.g. [chemical standards](https://www.chemicool.com/definition/standards.html)). So while Dr. Carter's claim is technically false, there is a lot of truth to it in practice.

#### Are weighted averages about non-normality?

<a href="https://imgflip.com/i/8uj6bw"><img src="https://i.imgflip.com/8uj6bw.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>

Given a sample of real numbers $x_1, \ldots, x_n$ and (non-negative) weights $w_1, \ldots, w_n$ the quantity is always defined. It doesn't matter if we're talking about normal distributions, Poisson distributions, or some other distribution whose support is a subset of the real numbers.

Such a quantity may not be defined in the population for similar reasons that the ordinary average may not exist in the population: lack of convergence. The [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy_distribution) and [Pareto distribution](https://en.wikipedia.org/wiki/Pareto_distribution) are examples of distributions where the average does not exist in the population, and I suspect that under mild assumptions that a weighted mean would not either.

Beyond the edge/corner cases, weighted averages are often well-defined. In general they are not about non-normality. Due to normal distributions being [Lévy alpha-stable](https://en.wikipedia.org/wiki/Stable_distribution), weighted averages of independent normal variables has a change of variables that gives us a new normal variable (e.g. see [The Book of Statistical Proofs](https://statproofbook.github.io/P/norm-lincomb.html)). Weighted averages will be defined for many continuous random variables via well-understood [change of variable](https://en.wikipedia.org/wiki/Probability_density_function#Function_of_random_variables_and_change_of_variables_in_the_probability_density_function) formulae, and if you're more advanced with mathematics you can tackle some of the trickier cases using [certain theorems from measure theory](https://en.wikipedia.org/wiki/Integration_by_substitution#Substitution_for_multiple_variables) like the [coarea formula](https://en.wikipedia.org/wiki/Coarea_formula). Discrete random variables are often quite straightforward in their change of variables (see [here](https://en.wikipedia.org/wiki/Probability_mass_function#Measure_theoretic_formulation)) via the [pushforward measure](https://en.wikipedia.org/wiki/Pushforward_measure#Main_property:_change-of-variables_formula).

Overall there's nothing about weighted averages that is special to non-normality as it applies readily to a variety of normal distributions in addition to many non-normal distributions.

#### What are weighted averages good for?

The primary reason I would use a weighted average is to produce a [shrunk estimate](https://en.wikipedia.org/wiki/Shrinkage_(statistics)) of the parameter of interest. Wikipedia gives a nice informal description:

> A shrinkage estimator is an estimator that, either explicitly or implicitly, incorporates the effects of shrinkage. In loose terms this means that a naive or raw estimate is improved by combining it with other information. The term relates to the notion that the improved estimate is made closer to the value supplied by the 'other information' than the raw estimate. In this sense, shrinkage is used to regularize ill-posed inference problems.

Additionally, special cases of weighted averaging can formulated as the [law of total expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation), which is sometimes useful.

#### Are weighted averages sufficient for controlling for sequence length?

#### Are weighted averages only applied to data?

No. There are also theoretical constructs that we can take weighted averages of. A special case of [mixture models](https://en.wikipedia.org/wiki/Mixture_model) are [mixture distributions](https://en.wikipedia.org/wiki/Mixture_distribution). These types of probability models are valuable for modelling certain structures like multimodality even when we do not have explicit labels for subpopulations to condition on. 

A finite mixture distribution is a convex combination of probability mass functions and/or probability density functions:

$$F(x) = \vec w \cdot \vec \Pr(x)$$

$$f(x) = \vec w \cdot \vec p(x)$$

An infinite, but countable, mixture is a similar series expansion in form:

$$F(x) = \sum_{i=1}^{\infty} w_i \Pr_i(x)$$

$$f(x) = \sum_{i=1}^{\infty} w_i p_i(x)$$

We can also have [uncountable mixtures](https://en.wikipedia.org/wiki/Mixture_distribution#Uncountable_mixtures):

$$f(x) = \int_{\Omega} w(a) p(x;a) da$$

[Marginal distributions](https://en.wikipedia.org/wiki/Marginal_distribution#Definition) can be understood as mixtures.

## Similarity Measures

### What are similarity measures?

### What makes a good similarity measure?
