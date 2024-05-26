#!/home/antonio/.config/virtualenvs/matemáticas/bin/python3.11
# Description: estimar el error de un polinomio interpolante
# Author: Antonio Cabrera

import numpy as np
from lagrange import interp_lagrange

'''
Estimar el error de un polinomio interpolante

Parámetros:
    - xp: nodos de interpolación
    - f: función a interpolar
    - p: polinomio interpolante con parámetros p(x, x fp)
    - n: número de puntos para evaluar el error

Retorno:
    - error: error de interpolación
'''
def error(xp, f, p, n=100):
    a = np.min(xp)
    b = np.max(xp)
    x = np.linspace(a, b, n)

    fp = f(xp)

    error = np.max(np.abs(f(x) - p(x, xp, fp)))

    return error

# Test
if __name__ == '__main__':
    xp = np.linspace(-1, 1, 10)
    f = lambda x: 1 / (1 + 25 * x**2)
    p = interp_lagrange

    print(f'Error: {error(xp, f, p)}')


