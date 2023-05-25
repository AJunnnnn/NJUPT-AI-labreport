from sympy import *

a,b,c,x=symbols('a,b,c,x')
f=Function('f')
# a * diff(f(x),x,2) + b * diff(f(x),x) + c * f(x) + 3
print(dsolve(a * diff(f(x),x,2) + b * diff(f(x),x) + c * f(x) + 3,f(x)))

a=1
b=-3
c=-1
print(dsolve(a * diff(f(x),x,2) + b * diff(f(x),x) + c * f(x) + 3,f(x)))