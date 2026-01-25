# We’ll use a simple numerical technique called the difference method:
# f′(x) ≈ f(x+h) − f(x) / h    
# This is called the forward difference method, where h is a very small number.

import math

def approx_derivative(func, x, h):
    return (func(x + h) - func(x)) / h

def square(x):
    return x * x

def cube(x):
    return x * x * x

def sin():
    return math.sin

def log():
    return math.log

print(approx_derivative(sin(), math.pi/4, .0001))
print(approx_derivative(square, 3, .0001 ))
print(approx_derivative(cube, 3, .0001))
print(approx_derivative(log(), 2, .0001))