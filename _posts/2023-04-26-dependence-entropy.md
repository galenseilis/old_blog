---
title: Dependence Entropy
date: 2023-04-26 12:12:00
categories: [statistics,mathematical-statistics]
tags: [statistics,mathematical-statistics,dependence,statistical-dependence,mutual-dependence,shannon-entropy,information-theory,calculus,probability-theory]
math: true
---

I want to share an update in my thinking since asking and answering [A formal definition of a "measure of association"](https://stats.stackexchange.com/q/534454/69508){:target="_blank"}. I've developed a functional which assigns how balanced the positive and negative statistical independence will be for a given probability distribution. It is not without assumptions, of course, but it is quite general all the same.

Let the **independence gap** be defined as 

$$\phi(x_1, \ldots, x_n) \triangleq F_{X_1, \ldots, X_n}(x_1, \ldots, x_n) - \prod_{j=1}^n F_{X_j}(x_j)$$

where 

$$F_{X_1, \ldots, X_n}$$

is the joint [CDF](https://en.wikipedia.org/wiki/Cumulative_distribution_function){:target="_blank"}over the random variables 

$$X_1, \ldots, X_n$$ 

and 

$$F_{X_j}(x_j)$$

is the marginal CDF of the $j$th variable. That is, the independence gap directly quantifies (in a signed way) the statistical dependence about a point $$(x_1, \ldots, x_n)$$ based on the definition of statistical independence.

The independence gap whose range can be generally taken to be the real-interval $$[-1,1]$$. As such, it has [positive and negative parts](https://en.wikipedia.org/wiki/Positive_and_negative_parts){:target="_blank"}:

$$\phi^+(x_1, \ldots, x_n) = \frac{\|\phi(x_1, \ldots, x_n)\| + \phi(x_1, \ldots, x_n)}{2}$$

$$\phi^-(x_1, \ldots, x_n) = \frac{\|\phi(x_1, \ldots, x_n)\| - \phi(x_1, \ldots, x_n)}{2}$$

It follows immediately that 

$$0 \leq \phi^+(x_1, \ldots, x_n) \leq \|\phi(x_1, \ldots, x_n)\|$$

and

$$0 \leq \phi^-(x_1, \ldots, x_n) \leq \|\phi(x_1, \ldots, x_n)\|.$$

which allows us to normalize (when the denominator is non-zero) the totality of the positive and negative parts of the independence gap:

$$\rho_+ = \frac{\int_{\Omega} \phi^+(x_1, \ldots, x_n) d \Omega}{\int_{\Omega} \|\phi(x_1, \ldots, x_n)\| d \Omega}$$

$$\rho_- = \frac{\int_{\Omega} \phi^-(x_1, \ldots, x_n) d \Omega}{\int_{\Omega} \|\phi(x_1, \ldots, x_n)\| d \Omega}$$

which I'll call the **positive dependence measure** and **negative dependence measure** respectively. These functions quantify the amount of positive and negative statistical dependence as ratios.

Now I can define the **dependence entropy** to be

$$H\left(F_{X_1, \ldots, X_n}\right) \triangleq -\left( \rho_- \log \rho_- + \rho_+ \log \rho_+ \right)$$

which is [Shannon's entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)){:target="_blank"} of the dependence ratios.

Similarly, the **normalized dependence entropy** can be computed as 

$$\mathcal{H}\left(F_{X_1, \ldots, X_n}\right) \triangleq \frac{H\left(F_{X_1, \ldots, X_n}\right)}{\log 2}.$$
