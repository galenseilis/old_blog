import sympy as sp

assert sp.__version__ == '1.12'

x = sp.Symbol('x', real=True, nonnegative=True)
lam = sp.Symbol('\\lambda', real=True, positive=True)
n = sp.Symbol('n', integer=True, positive=True)
t = sp.Symbol('t', real=True, nonnegative=True)
F = 1 - sp.exp(-lam * x)
f = lam * sp.exp(-lam * x)


G = n * sp.integrate(f * (F.subs(x, x+t) - F) ** (n-1), (x, 0, sp.oo))
print('CDF', sp.latex(sp.simplify(G)))

g = G.diff(t)
print('PDF', sp.latex(sp.simplify(g)))

Q = sp.solve(G, t)
print('Quantile', *[sp.latex(sp.simplify(_)) for _ in Q])

E = sp.integrate(t * g, (t, 0, sp.oo))
print('Expected Value', sp.latex(sp.simplify(E)))

V = sp.integrate((t - E) ** 2 * g, (t, 0, sp.oo))
print('Variance', sp.latex(sp.simplify(V)))

for _ in range(2, 11):
  MLE = sp.calculus.util.maximum(g.subs(n, _), t, sp.Interval(0, sp.oo))
  print(f'MLE when n={_}', sp.latex(sp.simplify(MLE)))
