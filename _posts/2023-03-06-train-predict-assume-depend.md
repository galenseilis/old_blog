---
title: Training Predictive Models Doesn't Assume Statistical Dependence
date: 2023-03-06 20:10:00
categories: [statistics,statistical-independence]
tags: [statistics,statistical-independence,predictive-model,assumptions,conditional-expectation,python,numpy]
math: true
---

It was suggested to me recently that to fit a predictive model supposes that the domain variables cause the image variables. This is not the case.

Predictive models assume nothing about causality *per se*. You can fit predictive models that are quite successful in making predictions with observational data but perform quite poorly at counterfactual inference. Worse still, the converse doesn't hold either. If a model is excellent predicting the outcome of an intervention, this does not mean the model will succeed at predicting observational data.

Let us say we retreat to a position invoking a statistical assumption without causal inference: does training a predictive model assume that the variables are statistically dependent? Again, no. A relevant mathematical fact is that if $X$ and $Y$ are random variables and $f,g$ are Borel-measurable functions that $f(X)$ and $g(Y)$ will also be independent. See these links for guidance in understanding this result:
- [Functions of independent Random Variables](https://stats.stackexchange.com/questions/94872/functions-of-independent-random-variables)
- [Are functions of independent variables also independent](https://math.stackexchange.com/questions/8742/are-functions-of-independent-variables-also-independent)

So what happens if you train a model 

$$Y = f(X; \theta) + \epsilon$$ 

when 

$$X,Y,\epsilon$$ 

are independent? I encourage you to try it out. You'll observe that the sample estimates of $\mathbb{E}[Y | X]$ and $\mathbb{E}[Y]$ are equal up to sampling variation. Let's see an example with coins (i.e. Bernoulli trials):

```python
import numpy as np

x = np.random.randint(0,2,size=10**4)
y = np.random.randint(0,2,size=10**4)

print(np.mean(y[x == 0]), np.mean(y[x == 1]), np.mean(y))
```

Not that this computational experiment of computing the conditional expectation didn't assume anything about a dependence between $X$ and $Y$. And yet this conditional expectation is a choice of $Y = f(X; \theta) + \epsilon$ where the parameter $\theta$ doesn't come into the picture. Is that cheating that we didn't even talk about some $\theta$ in the example? Not really. We could have assigned it anything we like by declaring it `theta = 3` for example, but it wouldn't participate in the computation. Go ahead with trying an example like $Y = X + \beta$ and you'll find again that it doesn't make much of difference, and the tiny bit of difference it makes will not generalize to future samples well. We were also being pretty charitable in assuming that $\epsilon$ was a degenerate random variable centered at zero because adding noise would just make any correspondence you would have hoped to find come out as even weaker.

The intuitive phrasing is that if $X$ and $Y$ are independent than any model that conditions $Y$ on $X$ will not have any effect in theory, and very little if any in practice. When you train a model on variables for which you do not know if they are independent you are not committing any kind of fallacy. The model will fit better or worse. If it consistently predicts test examples then there is likely some statistical dependence. If not, there *could* statistical independence or the form of statistical dependence is not one in which your choice of model captured very well.


