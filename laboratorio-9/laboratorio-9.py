#!/usr/bin/python3
# Description: Laboratorio 9 - Implementación problema 1 apartado 3

import math
from scipy.optimize import bisect

def f(x):
    return x - 0.5 * math.sin(x) - 0.7

def g(x):
    return x - (x - 0.5 * math.sin(x) - 0.7 ) / (1 - 0.5 * math.cos(x))

def iteracion_punto_fijo(fx, gx, x0, n):
    try:
        x1 = gx(x0)
    except:
        raise ZeroDivisionError("Error: División por cero")

    alpha = bisect(fx, 0, 2)

    for i in range(n):
        x0 = x1
        x1 = gx(x0)
        print(f"Iteración {i+1}: {x1}")
        print(f"Error: {abs(x1 - alpha)}")

if __name__ == "__main__":
    iteracion_punto_fijo(f, g, x0=0, n=3)


