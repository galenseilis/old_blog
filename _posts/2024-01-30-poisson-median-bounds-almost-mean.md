---
title: When do the bounds on a Poisson's median almost equal the mean?
date: 2024-01-28 06:30:15
categories: [mathematics,mathematical-statistics]
tags: [mathematics,statistics,mathematical-statistcs,random-variable,random-element,random-scalar,poisson-distribution,median,mean,bounds,inequality]
math: true
mermaid: true
---

## Question 1

When do the bounds on the median $\nu$ of a Poisson distribution equal (or nearly equal) the mean of the distribution, $\frac{1}{\lambda}$?

The bounds of the median are given as

$$\lambda - \ln 2 \leq \nu < \lambda + \frac{1}{3}$$

### Lower Bound
Let $$\lambda - \ln 2 = \frac{1}{\lambda}$$
then we can obtain the polynomial

$$\lambda^2 - \lambda \ln 2 - 1 = 0$$
for which we can then use the quadratic equation to obtain

$$\lambda = \frac{\ln2 \pm \sqrt{\left( \ln 2 \right)^2 +4}}{2}.$$

We obtain two approximate solutions for lambda:

$$\lambda_- \approx -0.7117804400329233$$

$$\lambda_+ \approx 1.4049276205928687$$

However, since we already know that $\lambda > 0$ we can exclude $\lambda_-$ and take $\lambda_+$ as the unique solution.

### Upper Bound

Let

$$\frac{1}{\lambda} = \lambda + \frac{1}{3}$$

then we can arrange to see this is a quadratic polynomial

$$\lambda^2 + \frac{\lambda}{3} - 1 = 0$$
and apply the quadratic formula:

$$\lambda = \frac{-\frac{1}{3} \pm \sqrt{\left( \frac{1}{3} \right)^2 + 4}}{2}$$

This gives two candidate solutions:

$$\lambda_- \approx -1.18046042171637$$

$$\lambda_+ \approx 0.8471270883830365$$

Like with the lower bound, we can only take the upper bound to be $\lambda_+$. But unlike the lower bound, we can only say that the median is strictly less than $\lambda_+$ even if it is really really close.

## Question 2

Assuming $\lambda$ is known, how wide a range of values can the median take?

$$\lambda + \frac{1}{3} - \lambda + \ln 2 = \frac{1}{3} + \ln 2$$

Interestingly, no matter what value $\lambda$ takes there is a constant-width interval for the values of the median.

