#!/usr/bin/python3
# Description: Examen cálculo numérico

import math

# Función que devuelve el signo de un número
def signo(x):
    if x > 0:
        return 1 
    elif x < 0:
        return -1
    else:
        return 0

# Método de la bisección
def biseccion(a, b, f, tol=1e-6, max_iter=100):
    iter_count = 0
    
    while iter_count < max_iter:
        c = (a + b) / 2
        f_c = f(c)
        
        if abs(f_c) < tol:
            return c, iter_count
        
        if signo(f(a)) * signo(f_c) < 0:
            b = c
        else:
            a = c
        
        iter_count += 1

    return None

# Método de la secante
def secante(f, x0, x1, tol=1e-6, max_iter=100):

    iter_count = 0

    while iter_count < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if abs(f_x0) < tol:
            return x0, iter_count
        if abs(f_x1) < tol:
            return x1, iter_count
        
        x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
        
        if abs(x1 - x0) < tol:
            return x1, iter_count
        
        x0 = x1
        x1 = x2
        
        iter_count += 1
    
    return None

# Método híbrido secante-bisección
def secant_bisection_method(f, x0, x1, tol=1e-6, max_iter=100):
    iter_count = 0

    while iter_count < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if abs(f_x0) < tol:
            return x0, iter_count
        if abs(f_x1) < tol:
            return x1, iter_count
        
        x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        if abs(x1 - x0) < tol:
            return x1, iter_count
        
        iter_count += 1
    
    return None

if __name__ == '__main__':
    f = lambda x: x**3 - 2
    x0 = 1
    x1 = 3

    root, iterations = secant_bisection_method(f, x0, x1)
    print(f'Raíz método híbrido: {root}')
    print(f'Iteraciones método híbrido: {iterations}')

    root, iterations = biseccion(x0, x1, f)
    print(f'Raíz método bisección: {root}')
    print(f'Iteraciones método bisección: {iterations}')

    root, iterations = secante(f, x0, x1)
    print(f'Raíz método secante: {root}')
    print(f'Iteraciones método secante: {iterations}')

