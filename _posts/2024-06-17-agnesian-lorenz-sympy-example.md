---
title: Expressing the Agnesian Equation of Order One of the Lorenz System Using SymPy
date: 2024-06-17 04:52:15
categories: [python,sympy]
tags: [sympy,python,agnesian-operator,ordinary-differential-equation,lorenz-system,operators,differential-equations]
math: true
mermaid: true
---

This post shows how to use SymPy to express the Agnesian of order one $\mathcal{A}_t^1$ of a system of ordinary differential equations. See [Seilis 2022](https://unbc.arcabc.ca/islandora/object/unbc:59312) for a description of the Agnesian operator. Briefly, it represents a form of non-statistical notion of "covariance".

In this case let us choose the [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system).

$$\frac{dx}{dt} = \sigma (y - x)$$

$$\frac{dy}{dt} = x (\rho - z) - y$$

$$\frac{dz}{dt} = xy - \beta z$$

```python
import numpy as np
from sympy import *

sigma = Symbol("\\sigma", real=True)
rho = Symbol("\\rho", real=True)
beta = Symbol("\\beta", real=True)
t = Symbol("t", real=True)

x = Function("x")(t)
y = Function("y")(t)
z = Function("z")(t)

v = [sigma * (y - x), x * (rho - z - y), x * y - beta * z]

dvdt = [i.diff(t) for i in v]
agnesian1 = latex(np.prod(dvdt))

print(agnesian1)
```

This trivially gives the result:

$$\mathcal{A}_t^1 \vec v (t) = \sigma \left(\left(- \frac{d}{d t} y{\left(t \right)} - \frac{d}{d t} z{\left(t \right)}\right) x{\left(t \right)} + \left(\rho - y{\left(t \right)} - z{\left(t \right)}\right) \frac{d}{d t} x{\left(t \right)}\right) \left(- \frac{d}{d t} x{\left(t \right)} + \frac{d}{d t} y{\left(t \right)}\right) \left(- \beta \frac{d}{d t} z{\left(t \right)} + x{\left(t \right)} \frac{d}{d t} y{\left(t \right)} + y{\left(t \right)} \frac{d}{d t} x{\left(t \right)}\right)$$
