---
title: Distribution of the Minimum of Sample Being Less than the Maximum of Another Sample
math: true
---



Suppose we have a collection of IID random variables $X_1, \ldots, X_n$, and we also have a second collection of IID random variables $Y_1, \ldots, Y_m$.

Suppose we would like to find $Pr \left[ \min (X_1, \ldots, X_n) \geq \max (Y_1, \ldots, Y_n) \right]$.

For the minimum of the collection of $X$ variables we can use [order statistics](https://en.wikipedia.org/wiki/Order_statistic) to obtain:

$$F_{X_{(1)}}(x) = Pr \left[ \min \{X_1, \ldots, X_n \} \leq x \right] =  1 - \left[1 - F_X(x) \right]^n.$$

Find the distribution of the maximum is likewise:

$$F_{Y_{(m)}}(y) = \left[ F_Y(y) \right]^m$$
