#!/usr/bin/python3
# Description: Obtener la raíz de una función mediante el método de punto fijo

import math

# Función a la que se le buscará la raíz
def f(x):
    return x - 0.007*math.sin(x) - 0.7

# Función g(x) que se obtiene de despejar x en f(x)
def g(x):
    return 0.007*math.sin(x) + 0.7

# Método de punto fijo: x_{n+1} = g(x_n)
def iteracion_punto_fijo(fx, gx, x0):
    x1 = gx(x0)

    if abs(fx(x1)) < 1e-6:
        return x1
    else:
        return iteracion_punto_fijo(fx, gx, x1)

if __name__ == "__main__":
    x0 = 0.0
    raiz = iteracion_punto_fijo(f, g, x0)
    print(f'La raíz de la función es: {raiz}')
    print(f'f({raiz:.6f}) = {f(raiz):.6f}')


