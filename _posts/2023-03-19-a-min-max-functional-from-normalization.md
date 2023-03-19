---
title: A Functional Inspired by Min-Max Normalization
date: 2023-03-19 14:48:00
categories: [math,functions,functionals]
tags: [math,functions,normalization,truncation,functionals,addition, subtraction, multiplication, division, exponentiation,logarithms,min-max-normalization,truncated-distributions,binary-operators,normalization,python,sympy]
math: true
---

For a function $F: \mathbb{R}^n \mapsto \mathbb{R}$ we can consider the functional

$$\frac{F(x) - F(a)}{F(b) - F(a)} $$

where $$a = \arg\min_x F(x)$$ and $$b = \arg\max_x F(x)$$. You may recognize this to be the form of [min-max normalization](https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)). If we restrict $F$ to be a cumulative distribution function then this is also the form of a [truncated probability distribution](https://en.wikipedia.org/wiki/Truncated_distribution). Both of these notions are useful for certain kinds of modelling problems. For recreation rather than utility, I generalize this functional below.


We can consider a more general functional

$$g \left( f\left( F(x), F(a) \right),  f\left( F(b), F(a) \right) \right)$$

where $g$ and $h$ are suitably-defined binary operators.

Taking common operations including addition, subtraction, multiplication, division, exponentiation, and logarithms, I've tabulated various choices below.


| f        | g        | Functional                                                                                                                                                                                                                    |
|:---------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| add      | add      | $2 F{\left(a \right)} + F{\left(b \right)} + F{\left(x \right)}$                                                                                                                                                              |
| add      | subtract | $- F{\left(b \right)} + F{\left(x \right)}$                                                                                                                                                                                   |
| add      | mult     | $\left(F{\left(a \right)} + F{\left(b \right)}\right) \left(F{\left(a \right)} + F{\left(x \right)}\right)$                                                                                                                   |
| add      | divide   | $\frac{F{\left(a \right)} + F{\left(x \right)}}{F{\left(a \right)} + F{\left(b \right)}}$                                                                                                                                     |
| add      | exp      | $\left(F{\left(a \right)} + F{\left(x \right)}\right)^{F{\left(a \right)} + F{\left(b \right)}}$                                                                                                                              |
| add      | log      | $\frac{\log{\left(F{\left(a \right)} + F{\left(b \right)} \right)}}{\log{\left(F{\left(a \right)} + F{\left(x \right)} \right)}}$                                                                                             |
| subtract | add      | $- 2 F{\left(a \right)} + F{\left(b \right)} + F{\left(x \right)}$                                                                                                                                                            |
| subtract | subtract | $- F{\left(b \right)} + F{\left(x \right)}$                                                                                                                                                                                   |
| subtract | mult     | $\left(F{\left(a \right)} - F{\left(b \right)}\right) \left(F{\left(a \right)} - F{\left(x \right)}\right)$                                                                                                                   |
| subtract | divide   | $\frac{F{\left(a \right)} - F{\left(x \right)}}{F{\left(a \right)} - F{\left(b \right)}}$                                                                                                                                     |
| subtract | exp      | $\left(- F{\left(a \right)} + F{\left(x \right)}\right)^{- F{\left(a \right)} + F{\left(b \right)}}$                                                                                                                          |
| subtract | log      | $\frac{\log{\left(- F{\left(a \right)} + F{\left(b \right)} \right)}}{\log{\left(- F{\left(a \right)} + F{\left(x \right)} \right)}}$                                                                                         |
| mult     | add      | $\left(F{\left(b \right)} + F{\left(x \right)}\right) F{\left(a \right)}$                                                                                                                                                     |
| mult     | subtract | $\left(- F{\left(b \right)} + F{\left(x \right)}\right) F{\left(a \right)}$                                                                                                                                                   |
| mult     | mult     | $F^{2}{\left(a \right)} F{\left(b \right)} F{\left(x \right)}$                                                                                                                                                                |
| mult     | divide   | $\frac{F{\left(x \right)}}{F{\left(b \right)}}$                                                                                                                                                                               |
| mult     | exp      | $\left(F{\left(a \right)} F{\left(x \right)}\right)^{F{\left(a \right)} F{\left(b \right)}}$                                                                                                                                  |
| mult     | log      | $\frac{\log{\left(F{\left(a \right)} F{\left(b \right)} \right)}}{\log{\left(F{\left(a \right)} F{\left(x \right)} \right)}}$                                                                                                 |
| divide   | add      | $\frac{F{\left(b \right)} + F{\left(x \right)}}{F{\left(a \right)}}$                                                                                                                                                          |
| divide   | subtract | $\frac{- F{\left(b \right)} + F{\left(x \right)}}{F{\left(a \right)}}$                                                                                                                                                        |
| divide   | mult     | $\frac{F{\left(b \right)} F{\left(x \right)}}{F^{2}{\left(a \right)}}$                                                                                                                                                        |
| divide   | divide   | $\frac{F{\left(x \right)}}{F{\left(b \right)}}$                                                                                                                                                                               |
| divide   | exp      | $\left(\frac{F{\left(x \right)}}{F{\left(a \right)}}\right)^{\frac{F{\left(b \right)}}{F{\left(a \right)}}}$                                                                                                                  |
| divide   | log      | $\frac{\log{\left(\frac{F{\left(b \right)}}{F{\left(a \right)}} \right)}}{\log{\left(\frac{F{\left(x \right)}}{F{\left(a \right)}} \right)}}$                                                                                 |
| exp      | add      | $F^{F{\left(a \right)}}{\left(b \right)} + F^{F{\left(a \right)}}{\left(x \right)}$                                                                                                                                           |
| exp      | subtract | $- F^{F{\left(a \right)}}{\left(b \right)} + F^{F{\left(a \right)}}{\left(x \right)}$                                                                                                                                         |
| exp      | mult     | $F^{F{\left(a \right)}}{\left(b \right)} F^{F{\left(a \right)}}{\left(x \right)}$                                                                                                                                             |
| exp      | divide   | $F^{- F{\left(a \right)}}{\left(b \right)} F^{F{\left(a \right)}}{\left(x \right)}$                                                                                                                                           |
| exp      | exp      | $\left(F^{F{\left(a \right)}}{\left(x \right)}\right)^{F^{F{\left(a \right)}}{\left(b \right)}}$                                                                                                                              |
| exp      | log      | $\frac{\log{\left(F^{F{\left(a \right)}}{\left(b \right)} \right)}}{\log{\left(F^{F{\left(a \right)}}{\left(x \right)} \right)}}$                                                                                             |
| log      | add      | $\frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(x \right)} \right)}} + \frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(b \right)} \right)}}$                                               |
| log      | subtract | $\frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(x \right)} \right)}} - \frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(b \right)} \right)}}$                                               |
| log      | mult     | $\frac{\log{\left(F{\left(a \right)} \right)}^{2}}{\log{\left(F{\left(b \right)} \right)} \log{\left(F{\left(x \right)} \right)}}$                                                                                            |
| log      | divide   | $\frac{\log{\left(F{\left(b \right)} \right)}}{\log{\left(F{\left(x \right)} \right)}}$                                                                                                                                       |
| log      | exp      | $\left(\frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(x \right)} \right)}}\right)^{\frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(b \right)} \right)}}}$                                  |
| log      | log      | $\frac{\log{\left(\frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(b \right)} \right)}} \right)}}{\log{\left(\frac{\log{\left(F{\left(a \right)} \right)}}{\log{\left(F{\left(x \right)} \right)}} \right)}}$ |

> Note that notation such as $F^2(a)$ and $F^{F(a)}(b)$ denote exponentiation, not powers of function composition.
{: .prompt-warning}

If you are interested in tinkering with your own choice of functions, here is the source code to generate the above table.

```python
from itertools import product

import sympy as sp
import pandas as pd

x = sp.Symbol('x')
b = sp.Symbol('b')
a = sp.Symbol('a')
F = sp.Function('F')
F_x = F(x)
F_b = F(b)
F_a = F(a)

ops = {
    
    'add' : lambda x,y: x + y,
    'subtract': lambda x,y: x - y,
    'mult' : lambda x,y: x * y,
    'divide': lambda x,y: x / y,
    'exp': lambda x,y: x ** y,
    'log': lambda x,y: sp.log(y, x)
    }

results = []
for f,g in product(ops, ops):
    result = ops[g](ops[f](F_x, F_a), ops[f](F_b, F_a))
    result = result.simplify()
    results.append([f, g, f'${sp.latex(result)}$'])

df = pd.DataFrame(results, columns=['f', 'g', 'Functional'])
print(df.to_markdown(index=False))
```

At a glance it may appear that our original functional is absent in the table, but noting that 

$$\frac{F{\left(a \right)} - F{\left(x \right)}}{F{\left(a \right)} - F{\left(b \right)}} = \frac{-1}{-1} \frac{F(x) - F(a)}{F(b) - F(a)}$$

reveals that SymPy produced the same result but with a distinct expression.

It is easy to confirm that not all of the functionals I have tabulated above will provide a normalization onto the interval $[a,b]$.
