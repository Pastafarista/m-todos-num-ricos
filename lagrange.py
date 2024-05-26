#!/home/antonio/.config/virtualenvs/matemáticas/bin/python3.11
# Description: diferentes implementaciones del polinomio de Lagrange
# Author: Antonio Cabrera

import numpy as np
import matplotlib.pyplot as plt
from horner import horner

'''
Calcular los coeficientes del polinomio de Lagrange mediante el método de coeficientes indeterminados

Parámetros:
    - x: vector de nodos de interpolación
    - fx: vector de valores de la función en los nodos de interpolación

Retorno:
    - coeficientes: vector de coeficientes del polinomio de Lagrange de la forma [an, an-1, ..., a1, a0]: p(x) = an*x^n + an-1*x^(n-1) + ... + a1*x + a0
'''
def coeficientes_lagrange(x, fx):
    matriz_vander = np.vander(x)
    coeficientes = np.linalg.solve(matriz_vander, fx)
    
    return coeficientes

'''
Evaluar el polinomio de Lagrange en un punto z mediante el método de coeficientes indeterminados

Parámetros:
    - x: vector de nodos de interpolación
    - fx: vector de valores de la función en los nodos de interpolación
    - z: vector de puntos en los que se evaluará el polinomio de Lagrange

Retorno:
    - p: vector de valores del polinomio de Lagrange en los puntos de z
'''
def evaluar_coeficientes_indeterminados(z, x, fx):
   
    coeficientes = coeficientes_lagrange(x, fx)
    p = np.zeros(len(z))

    for i in range(len(z)):
        p[i] = horner(coeficientes, z[i])

    return p

'''
Calcular las bases de Lagrange

Parámetros:
    - x: vector de nodos de interpolación
    - z: vector de puntos en los que se evaluará el polinomio de Lagrange

Retorno:
    - L: matriz de bases de Lagrange de dimensiones (m, n) donde m es la longitud de z y n la longitud de x
'''
def base_lagrange(z, x):
    n = len(x)
    m = len(z)
    L = np.zeros((m, n))

    for i in range(n):
        numerador = np.ones(m)
        denominador = np.ones(m)

        for j in range(n):
            if i != j:
                numerador *= z - x[j]
                denominador *= x[i] - x[j]

        L[:, i] = numerador / denominador

    return L)

    for i in range(n):
        numerador = np.ones(m)
        denominador = np.ones(m)



'''
Evaluar el polinomio de Lagrange en un punto z mediante el método de bases de Lagrange

Parámetros:
    - fx: vector de valores de la función en los nodos de interpolación
    - x: vector de nodos de interpolación
    - z: vector de puntos en los que se evaluará el polinomio de Lagrange

Retorno:
    - p: vector de valores del polinomio de Lagrange en los puntos de z
'''
def evaluar_lagrange(z, x, fx):
    L = base_lagrange(z, x)

    return np.dot(L, fx)

'''
Calcular las diferencias divididas de la forma de Newton mediante la tabla del polinomio de Lagrange

Parámetros:
    - fx: vector de valores de la función en los nodos de interpolación
    - x: vector de nodos de interpolación

Retorno:
    - diferencias_divididas: vector con las diferencias divididas de la forma de Newton
'''plt.plot(z, evaluar_diferencias_divididas(z, x, fx), label='Diferencias divididas')
def tabla_lagrange(x, fx):

    # Inicializar la tabla
    tabla = np.zeros((len(x), len(x)))
    
    # Damos los valores iniciales de la tabla
    for i in range(len(x)):
        tabla[i, 0] = fx[i]

    # Calcular la tabla
    for j in range(1, len(x)):
        for i in range(j, len(x)):
            tabla[i, j] = (tabla[i, j - 1] - tabla[i - 1, j - 1]) / (x[i] - x[i - j])

    # Extraer la diagonal principal de la tabla
    diferencias_divididas = np.diag(tabla)

    return diferencias_divididas
   
'''
Evaluar el polinomio de Lagrange en el vector z mediante las diferencias divididas de la forma de Newton

Parámetros:)

    for i in range(n):
        numerador = np.ones(m)
        denominador = np.ones(m)


    - z: vector de puntos en los que se evaluará el polinomio de Lagrange
    - x: vector de nodos de interpolación
    - fx: vector de valores de la función en los nodos de interpolación

Retorno:
    - p: vector de valores del polinomio de Lagrange en los puntos de z
'''
def evaluar_diferencias_divididas(z, x, fx):
    diferencias_divididas = tabla_lagrange(x, fx) 
    p = np.zeros(len(z))

    for i in range(len(z)):
        for j in range(len(x)):
            p[i] += diferencias_divididas[j] * np.prod(z[i] - x[:j])

    return p

'''
Interpolación de Lagrange mediante la función polyfit de numpy

Parámetros:
    - x: vector de puntos en los que se evaluará el polinomio de Lagrange
    - xp: vector de nodos de interpolación
    - fp: vector de valores de la función en los nodos de interpolación

Retorno:
    - result: vector de valores del polinomio de Lagrange en los puntos de x
'''
def interp_lagrange(x, xp, fp):
    polinomio = np.polyfit(xp, fp, len(xp) - 1)
    result = np.polyval(polinomio, x)

    return result

# Test
if __name__ == '__main__':
    x = np.array([1, 2, 3, 4])
    fx = np.array([1, 1, 2, 6])
    z = np.linspace(1, 4, 100)

    print('Forma de newton:', evaluar_diferencias_divididas(z, x, fx))

    # Mostrar gráficamente los polinomios de Lagrange obtenidos mediante los diferentes métodos
    plt.plot(z, evaluar_coeficientes_indeterminados(z, x, fx), label='Coeficientes indeterminados')
    plt.plot(z, evaluar_lagrange(z, x, fx), label='Bases de Lagrange')
    plt.plot(z, evaluar_diferencias_divididas(z, x, fx), label='Diferencias divididas')
    plt.plot(z, interp_lagrange(z, x, fx), label='Polyfit')
    
    # Mostrar los nodos de interpolación
    plt.scatter(x, fx, color='red')

    # Mostrar la leyenda
    plt.legend()

    # Mostrar la gráfica
    plt.show() 



