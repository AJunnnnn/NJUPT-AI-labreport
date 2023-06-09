from sympy import *

x = symbols('x')
y = symbols('y')
f = Function("f")
f1 = simplify((x+2)**2-(x+1)**2)
print(f1)
f2 = simplify((x**2-1)/(x+1))
print(f2)
f3 = simplify((f(x)**2-1)/(f(x)+1))
print(f3)
f4 = simplify(sin(x)**2+2*sin(x)*cos(x)+cos(x)**2)
print(f4)
f5 = simplify(f(sin(x)**2+2*sin(x)*cos(x)+cos(x)**2))
print(f5)
f6 = expand(sin(2*x+y), trig=True)
print(f6)
f7 = factor(15*(x**2)+2*y-3*x-10*x*y)
print(f7)
