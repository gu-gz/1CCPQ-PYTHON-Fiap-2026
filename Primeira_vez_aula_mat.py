import sympy as sp

x = sp.Symbol('x')
f = (x - 1) / (x - 2)
derivada = sp.diff(f, x)
print(derivada)