
from sympy import Derivative, symbols

x = symbols("x")
fx = 4*(x**4)+3*x

fprime = Derivative(fx, x).doit() # x라는 문자에 대해 미분을 한다.
print(f"fprime의 도함수 = {fprime}")

value = fprime.subs({x:3})
print(f"x=3에서의 도함수 값은 {value}")

sprime = Derivative(fprime, x).doit()
print(f"fprime의 2계도함수 = {sprime}")



