from sympy import *

x = Symbol('x', real=True)
y = Symbol('y', real=True)

expr = Max(Min(y, (1+x) * y), (1-x)*y)

print(expr.diff(x,2))
