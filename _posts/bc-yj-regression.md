---
title: Box-Cox and Yeo-Johnson Regression
date: 2023-03-03 19:35:09 -0800
categories: [statistics,regression]
tags: [box-cox-transform,yeo-johnson-transform,regression]
---

Both the [Box-Cox transformation](https://en.wikipedia.org/wiki/Power_transform#Box%E2%80%93Cox_transformation) and the [Yeo-Johnson transform](https://en.wikipedia.org/wiki/Power_transform#Yeo%E2%80%93Johnson_transformation) are used to monotonically transform random variables. This is usually done for the purpose of creating a new random variable with a normal distribution in preparation for an ordinary least squares regression.


I've [asked](https://stats.stackexchange.com/questions/558223/does-parametrized-box-cox-transform-take-degrees-of-freedom-away-from-subsequent) about how performing the Box-Cox transform would affect the degrees of freedom of the resulting parameters estimated in the regression model. The [answer](https://stats.stackexchange.com/questions/558223/does-parametrized-box-cox-transform-take-degrees-of-freedom-away-from-subsequent#comment1036426_558223) appears to be that the parameter uses a degree of freedom, and I suspect the same would be said for the Yeo-Johnson transform.

But what still bothers me is why the parameter $\lambda$ in these transforms is not estimated *simultaneously* with the regression parameters. Taking $\operatorname{BC}(Y;\lambda )$ to be the Box-Cox transform with parameter $\lambda$, we can formulate the following regression model:

$$\operatorname{BC}(Y;\lambda) = \beta_0 + \sum_{j=1}^n \beta_j X_j$$

for some real parameters $\beta_0, \beta_1, \ldots, \beta_n$ and random variables $X_1, \ldots, X_n$. Let us call this a *Box-Cox regression*. Estimating $\lambda$ before these beta parameters may not give the same results as simultaneously estimating all of them. Indeed, we could device various sequences of which parameters we estimate/update from the model and obtain different estimates. My intuition is that training all the parameters together helps give estimates that account for the fact that the parameters (or their estimates) are not always independent. 


We can likewise define and consider a *Yeo-Johnson regression*.
