from sympy import *

a,b,c,x,y=symbols('a,b,c,x,y')
print(solve(a*x**2+b*x+c, x))


a=1
b=3
c=1
print(solve(a*x**2+b*x+c, x))


print(solve((x**2+x*y+1,y**2+x*y+2),x,y))