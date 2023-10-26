---
title: Derivative of a Capacitance Function Using SymPy
date: 2023-10-25 00:50:15
categories: [programming,computer-algebra-system,sympy]
tags: [programming,computer-algebra-system,sympy,computer-programming,python,calculus,derivatives,partial-derivatives,mathematics]
math: true
mermaid: true
---

Suppose we have the following function $C : \mathbb{C} \mapsto \mathbb{C}$:
$$C(w_0) = \frac{2 \epsilon_{0} a b \left(\frac{\operatorname{atan}{\left(\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}} \right)}}{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}} + \frac{\operatorname{atan}{\left(\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{\sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}} \right)}}{\sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}}\right)}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}$$

Now we are asked to compute the second partial derivative with respect to $w_0$:

$$\frac{\partial^2}{\partial w_0^2} C(w_0)$$

In my early undergraduate days we would have gotten out our chain rule and applied it again and again and again until a result yielded. But we're busy, so let's compute this using the SymPy computer algebra system.

```python
from sympy import *
from sympy.abc import a,b

# Define the basic variables we need.

w_0 = Symbol('w_0')
d_0 = Symbol('d_0')
d_i = Symbol('d_i')
epsilon_r = Symbol('\\epsilon_r')
epsilon_0 = Symbol('\\epsilon_0')

# First layer of variables defined
g = d_0 + d_i / epsilon_r
y = w_0 / g

# Some square rooty stuff
sqrty = sqrt(y)
sqrtym = sqrt(sqrty - y)
sqrtyp = sqrt(sqrty + y)

# Some arctan and plus-minus stuff
left_inner = atan(sqrty / sqrtym) / sqrtym
right_inner = atan(sqrty / sqrtyp) / sqrtyp

# A leading coefficient
coef = 2 * a * b * epsilon_0 / g

# Target variavle

C = coef * (left_inner + right_inner)

# Second derivative
d2Cdw_02 = C.diff('w_0', order=2)

print(latex(d2Cdw_02)) # print a latex representation to copy-paste into MathJax.
```

The above prints the rather terrifying $\LaTeX$ expression representing $\frac{\partial^2}{\partial w_0^2} C(w_0)$:

```python
\frac{2 \epsilon_{0} a b \left(\frac{\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}} \left(- \frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right)}{\left(\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}} + \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{2 w_{0} \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}}}{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}} \left(\frac{w_{0}}{\left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right) \left(\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)} + 1\right)} + \frac{\left(- \frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right) \operatorname{atan}{\left(\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}} \right)}}{\left(\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}} + \frac{\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}} \left(\frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right)}{\left(- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}} + \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{2 w_{0} \sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}}}{\sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}} \left(\frac{w_{0}}{\left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right) \left(- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)} + 1\right)} + \frac{\left(\frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right) \operatorname{atan}{\left(\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{\sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}} \right)}}{\left(- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}}\right)}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}
```

When we render it in MathJax we have:

$$\frac{2 \epsilon_{0} a b \left(\frac{\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}} \left(- \frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right)}{\left(\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}} + \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{2 w_{0} \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}}}{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}} \left(\frac{w_{0}}{\left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right) \left(\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)} + 1\right)} + \frac{\left(- \frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right) \operatorname{atan}{\left(\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}} \right)}}{\left(\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}} + \frac{\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}} \left(\frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right)}{\left(- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}} + \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{2 w_{0} \sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}}}{\sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}} \left(\frac{w_{0}}{\left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right) \left(- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)} + 1\right)} + \frac{\left(\frac{1}{2 \left(d_{0} + \frac{d_{i}}{\epsilon_{r}}\right)} - \frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{4 w_{0}}\right) \operatorname{atan}{\left(\frac{\sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}{\sqrt{- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}}} \right)}}{\left(- \frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}} + \sqrt{\frac{w_{0}}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}}\right)^{\frac{3}{2}}}\right)}{d_{0} + \frac{d_{i}}{\epsilon_{r}}}$$
This is the type of expression that is complicated enough that I would not do anything further with it manually, and what we do with it will determine what tools we use. For further mathematical operations we might use SymPy, or parse the $\LaTeX$ into some other computer algebra system such as Mathematica. Or we might [lambdify](https://docs.sympy.org/latest/modules/utilities/lambdify.html)the symbolic expression in order to let us quickly do numerical calculations with the expression.

> I think `lambdify` gets cranky with backslashes. Using symbols other than `\epsilon` might help avoid issues with escape characters.
{: .prompt-warning }

In this post I showed how to get started with loading a symbolic expression into SymPy and applying some basic calculus to it. When using `Symbol` I did not pass any further constraints such as `real=True` or `positive=True` that may apply to some of the variables when considered for a real application. Assumptions about variables is discussed in the documentation [here](https://docs.sympy.org/latest/guides/assumptions.html). 

Happy deriving.

