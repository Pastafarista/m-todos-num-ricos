#!/home/antonio/.config/virtualenvs/matemáticas/bin/python3.11
# Description: Polinomio interpolador de Lagrange a trozos
# Author: Antonio Cabrera

import numpy as np
import matplotlib.pyplot as plt

'''
Calcular el parámetro alpha_i del polinomio de Lagrange a trozos

Parámetros:
    - fp: imagen de los nodos de interpolación
    - i: índice del nodo de interpolación

Retorno:
    - alpha_i: parámetro alpha_i
'''
def get_alpha_i(fp, i):
    alpha_i = fp[i - 1]

    return alpha_i

'''
Calcular el parámetro beta_i del polinomio de Lagrange a trozos

Parámetros:
    - xp: nodos de interpolación
    - fp: imagen de los nodos de interpolación
    - i: índice del nodo de interpolación

Retorno:
    - beta_i: parámetro beta_i
'''
def get_beta_i(xp, fp, i):
    beta_i = (fp[i] - fp[i - 1]) / (xp[i] - xp[i - 1])

    return beta_i

'''
Evaluar los puntos x en el polinomio de Lagrange a trozos con nodos de interpolación xp y su imagen fp

Parámetros:
    - x: puntos a evaluar
    - xp: nodos de interpolación
    - fp: imagen de los nodos de interpolación

Retorno:
    - result: imagen de los puntos x en el polinomio de Lagrange a trozos
'''
def interp_lagrange_trozos(x, xp, fp):
    result = []
    
    # Se recorren los puntos x que se quieren evaluar
    for x_i in x:
        i = 0
        
        # Primero hay que encontrar el i tal que x esté en el intervalo [xp[i-1], xp[i]]
        for j in range(1, len(xp)):
            if xp[j - 1] <= x_i <= xp[j] and x_i <= xp[j]:
                i = j
                break
        
        # Ahora calculamos los coeficientes alpha_i y beta_i
        alpha_i = get_alpha_i(fp, i)
        beta_i = get_beta_i(xp, fp, i)

        # Ahora se evalúa el polinomio de Lagrange en x
        s_x = alpha_i + beta_i * (x_i - xp[i - 1])

        result.append(s_x)

    return result

if __name__ == "__main__":
    
    # Vamos a comprobar que la implementación de la función interp_lagrange_trozos es correcta comparándola con la implementación de numpy
    xp = np.array([0, 1, 2, 3, 4])
    fp = np.array([0, 1, 8, 27, 64])
    x = np.linspace(0, 4, 100)

    plt.plot(x, interp_lagrange_trozos(x, xp, fp), label="Implementación original", color="red")
    plt.plot(x, np.interp(x, xp, fp), label="Implementación de numpy", color="blue")
    plt.scatter(xp, fp, color="black")

    plt.legend()
    plt.show()
