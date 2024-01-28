---
title: The Curvature of the Graph of the Expectation of a Random Scalar
date: 2024-01-28 06:30:15
categories: [mathematics,mathematical-statistics]
tags: [mathematics,statistics,mathematical-statistcs,calculus,curvature,curvature-of-a-graph,expectation,expectation-operator,functions,random-variable,random-element,random-scalar,exponential-distribution]
math: true
mermaid: true
---


In this post we'll apply some basic definitions to obtain the curvature of the expected value of a random variable assuming that its cumulative distribution function is in the set of second-differentiable function ($\mathcal{C}^2$). The curvature of the graph of the expectation will describe the direction that the expectation operator is bending when the instance variable is changed an arbitrarily small (but non-zero) amount.

One of the simpler notions of curvature is given by the curvature of a graph of a function in some choice of coordinates:

$$\kappa(y) \triangleq \frac{\frac{d^2}{d y^2} g(y)}{\left( 1 + \left( \frac{d}{dy}g(y) \right)^2 \right)^{\frac{3}{2}}}$$

We can consider this notion of curvature for expectation operators first noting the derivatives. The first derivative of the expectation with respect to the instance variable $y$ comes as a result of the integral definition of an expectation operator and the Fundamental Theorem of Calculus.

$$\frac{d}{dy} \mathbb{E}[Y] = \frac{d}{dy} \int y f_Y(y) dy = yf_Y(y)$$

The second derivative can be obtained from the first derivative which involves applying the product rule of derivatives. 

$$\frac{d^2}{dy^2} \mathbb{E}[Y] = \frac{d}{dy} \frac{d}{dy} \mathbb{E}[Y] = \frac{d}{dy} \left[y f_Y(y) \right] = f_Y(y) + y \frac{d}{dy} f_Y(y)$$

Above the expression $f_Y(y)$ is a probability density function over $y$.

Replacing $g(y)$ above in the generic definition of curvature of the graph of a curve with the expectation $\mathbb{E}[Y]$ we have:

$$k(y) = \frac{f_Y(y) + y \frac{d}{dy} f_Y(y)}{\left( 1 + \left[ y f_Y(y) \right]^2 \right)^{\frac{3}{2}}}$$

Let us take the exponential distribution as an example. Assuming a random variable $$X \sim \operatorname{Exponential}(\lambda)$$
then $$f_X(x) = \lambda \exp \left( -\lambda x \right).$$
Plugging these variables into our curvature of the expectation formula we have

$$k(x) = \lambda \frac{\exp \left( -\lambda x \right) + x \exp \left( -\lambda x \right)}{\left( 1 + x^2 \lambda^2 \exp \left( -2 \lambda x \right) \right)^{\frac{3}{2}}}$$

