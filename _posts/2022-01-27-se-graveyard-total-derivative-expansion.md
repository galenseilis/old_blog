---
title: Series expansion for total derivative of finite order?
date: 2022-01-27 00:40:00 -0800
categories: [math,calculus,derivatives,total-derivatives]
tags: [math,stack-exchange,stack-exchange-post-mortem,calculus,derivatives,total-derivatives,partial-derivatives,chain-rule]
math: true
mermaid: true
---

> [This question](https://math.stackexchange.com/questions/4371576/what-is-dyadic-sampling-in-the-context-of-a-wavelet-transform) was automatically deleted from `math.stackexchange.com`.
{: .prompt-info}

# Question

Given a function $L(t, x_1(t), \cdots, x_n(t))$, its [total derivative](https://en.wikipedia.org/wiki/Total_derivative) with respect to $t$ is given by

$$\frac{dL}{dt} = \frac{\partial L}{\partial t} + \sum_{j=1}^{n} \frac{\partial L}{\partial x_j} \frac{dx_j}{dt}$$

which is a consequence of the [chain rule](https://en.wikipedia.org/wiki/Chain_rule). Note that I have dropped the function notation reminding us that we're considering a collection of functions of $t$.

Is there a similar-ish expansion for the $k$th order derivative of $L(t, x_1(t), \cdots, x_n(t))$, denoted $\frac{d^k L}{dt^k}$?

For starters, we could look at the second application of the total derivative:

$$\begin{align}
\frac{d}{dt} \frac{dL}{dt} = \frac{d^2L}{dt^2} &= \frac{d}{dt} \left[ \frac{\partial L}{\partial t} + \sum_{j=1}^{n} \frac{\partial L}{\partial x_j} \frac{dx_j}{dt} \right] \\
 &= \frac{d}{dt} \left[ \frac{\partial L}{\partial t} \right] + \frac{d}{dt} \left[ \sum_{j=1}^{n} \frac{\partial L}{\partial x_j} \frac{dx_j}{dt} \right] \\
 &= \frac{d}{dt} \left[ \frac{\partial L}{\partial t} \right] +  \sum_{j=1}^{n} \frac{d}{dt} \left[\frac{\partial L}{\partial x_j} \frac{dx_j}{dt} \right] \\
&= \frac{d}{dt} \left[ \frac{\partial L}{\partial t} \right] +  \sum_{j=1}^{n}  \left(\frac{d}{dt} \left[\frac{\partial L}{\partial x_j} \right] \frac{dx_j}{dt} +  \frac{\partial L}{\partial x_j} \frac{d}{dt} \left[\frac{dx_j}{dt} \right] \right) \\
\end{align}$$

but I have not seen a way to simplify the above and generalize to finite $k$.
