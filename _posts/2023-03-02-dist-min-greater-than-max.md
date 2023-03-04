---
title: Probability of Min of X Greater than Max of Y
date: 2023-03-02 21:21:09 -0800
categories: [statistics,probability-distribution]
tags: [statistics,probability-distribution,derivation,change-of-variables,transformation,stochastic-order,identical-and-independently-distributed,random-variables,statistical-independence,smooth-function,minimum,maximum,probability,order-statistics,convolution,convolution-theorem,fourier-transform]
math: true
---

Suppose we have a collection of IID random variables $\{ X_1, \ldots, X_n \}$, and we also have a second collection of IID random variables $\{ Y_1, \ldots, Y_m \}$. Each $X_i \sim F_X$ and $Y_i \sim F_Y$ and we will assume that all these variables are statistically independent. Let us also assume that that $F_X$ and $F_Y$ are in the $\mathcal{C}^1$ smoothness class.

Suppose we would like to find $Pr \left[ \min (X_1, \ldots, X_n) > \max (Y_1, \ldots, Y_n) \right]$, which is equal to $Pr \left[ \min (X_1, \ldots, X_n) - \max (Y_1, \ldots, Y_n) > 0 \right]$. The relevance of this observation is that $\min (X_1, \ldots, X_n) - \max (Y_1, \ldots, Y_n)$ is an expression for which we can derive the distribution

For the minimum of the collection of $X$ variables we can use [order statistics](https://en.wikipedia.org/wiki/Order_statistic) to obtain:

$$F_{X_{(1)}}(x) = Pr \left[ \min \{X_1, \ldots, X_n \} \leq x \right] =  1 - \left[1 - F_X(x) \right]^n.$$

Likewise, the maximum of the $Y$ variables comes from order statistics:

$$\max (Y_1, \ldots, Y_m) \sim \left[ F_Y \right]^m$$

We would like to put our problem into the form of adding two independent random variables $U + V$ because then we can convolve them to obtain the distribution of the sum. Taking $U = X_{(1)}$ as our minimum of the $X$ variables, and $V = - Y_{(m)}$ of the $Y$ variables, we can next consider the distribution of $V$ to be a reflection of $Y_{(m)}$. The smooth change in variables works out to be

$$f_V(v) = m f_Y(-y) \left[ F_Y(-y)\right]^{m-1}.$$

To compute the convolution of the densities $f_U \star f_V$ we need the density $f_U$:

$$f_U(u) = \frac{d}{dx} F_X(x) = n \left[ 1 - F_X(x) \right]^{n-1}f_X(x)$$

We can use the convolution theorem to obtain the result via the Fourier transform $\mathcal{F}$ and its inverse $\mathcal{F}^{-1}$.

$$f_{X_{(1)} - Y_{(m)}} = \mathcal{F}^{-1} \left\{ \mathcal{F} \left\{ n \left[ 1 - F_X(x) \right]^{n-1} f_X(x) \right\} \mathcal{F} \left\{ m f_Y(-y) \left[ F_Y(-y) \right]^{m-1} \right\}  \right\}$$


Finally, we can obtain the cumulative distribution by integrating:

$$F_{X_{(1)} - Y_{(m)}}(x,y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X_{(1)} - Y_{(m)}}(x,y) dx dy$$
