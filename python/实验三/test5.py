from sympy import *


a,b,c,x=symbols('a,b,c,x')
f = a*x**2+b*x+c


print(integrate(f,x))

print(integrate(f,(x,0,1)))