---
title: Is the Verhulst (logistic) growth function convex over its parameters?
date: 2021-11-02 05:49:00 -0800
categories: [math,functions,convex-functions]
tags: [math,functions,convex-functions,parameters,stack-exchange,stack-exchange-post-mortem]
math: true
mermaid: true
---

> [This question](https://math.stackexchange.com/questions/4294174/is-the-verhulst-logistic-growth-function-convex-over-its-parameters) was automatically deleted from `math.stackexchange.com`.
{: .prompt-info}

# Question

Considering the Verhulst growth model to be the following:
$$p(t) = \frac{k}{1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}}$$

I would like to know if $p(t)$ is non-convex with respect to $k, p_0$, and $r$ under the constraints that these parameters are themselves positive. I suspect that it isn't convex because of looking at plots of the graph of the function over single choices of parameters. I would like something more symbolic/algebraic.

It has the following Hessian with respect to $k, p_0$, and $r$ is given by

$$\left[\begin{matrix}\frac{k \left(- \frac{2 e^{- r t}}{p_{0}^{2}} - \frac{2 \left(k - p_{0}\right) e^{- r t}}{p_{0}^{3}}\right)}{\left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} + \frac{k \left(\frac{e^{- r t}}{p_{0}} + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}\right) \left(\frac{2 e^{- r t}}{p_{0}} + \frac{2 \left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}\right)}{\left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}} & - \frac{2 k \left(\frac{e^{- r t}}{p_{0}} + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}\right) e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}} + \frac{k e^{- r t}}{p_{0}^{2} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} + \frac{\frac{e^{- r t}}{p_{0}} + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}}{\left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} & \frac{k \left(- \frac{t e^{- r t}}{p_{0}} - \frac{t \left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}\right)}{\left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} + \frac{2 k t \left(k - p_{0}\right) \left(\frac{e^{- r t}}{p_{0}} + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}\right) e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}}\\- \frac{k \left(\frac{2 e^{- r t}}{p_{0}} + \frac{2 \left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}\right) e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}} + \frac{k e^{- r t}}{p_{0}^{2} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} + \frac{\frac{e^{- r t}}{p_{0}} + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}}{\left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} & \frac{2 k e^{- 2 r t}}{p_{0}^{2} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}} - \frac{2 e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} & \frac{k t e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} - \frac{2 k t \left(k - p_{0}\right) e^{- 2 r t}}{p_{0}^{2} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}} + \frac{t \left(k - p_{0}\right) e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}}\\- \frac{k t e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} + \frac{k t \left(k - p_{0}\right) \left(\frac{2 e^{- r t}}{p_{0}} + \frac{2 \left(k - p_{0}\right) e^{- r t}}{p_{0}^{2}}\right) e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}} - \frac{k t \left(k - p_{0}\right) e^{- r t}}{p_{0}^{2} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} & \frac{k t e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} - \frac{2 k t \left(k - p_{0}\right) e^{- 2 r t}}{p_{0}^{2} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}} + \frac{t \left(k - p_{0}\right) e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} & - \frac{k t^{2} \left(k - p_{0}\right) e^{- r t}}{p_{0} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{2}} + \frac{2 k t^{2} \left(k - p_{0}\right)^{2} e^{- 2 r t}}{p_{0}^{2} \left(1 + \frac{\left(k - p_{0}\right) e^{- r t}}{p_{0}}\right)^{3}}\end{matrix}\right]$$

Up until this point can be obtained readily with the following Python:
```python
import numpy as np
from sympy import *

t, p0, k, r = Symbol('t'), Symbol('p0'), Symbol('k'), Symbol('r')

p = k / (1 + ((k-p0)/p0) * exp(-r*t))

H = np.zeros((3,3), dtype=object)
for i, xi in enumerate((p0, k, r)):
    for j, xj in enumerate((p0, k, r)):
        H[i,j] = diff(diff(p, xi), xj)
H = Matrix(H)
```

To get the eigenvalues one would simply need to additionally call:
```python
H.eigenvals()
```
which seems to work... except that output is enormous. While I might just throw a bunch of randomly-selected values along with the usual corner cases (zero, $\pm$one, $\pm$infinity) into the eigenfunctions to look for negative values, I am hoping that asking here yields something more elegant.

