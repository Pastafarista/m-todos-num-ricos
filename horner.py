#!/home/antonio/.config/virtualenvs/matemáticas/bin/python3.11
# Description: Evaluar un polinomio en un punto x con el método de Horner
# Author: Antonio Cabrera

import numpy as np

'''
Evaluar un polinomio en un punto x con el método de Horner

Parámetros:
    - poly: lista de coeficientes del polinomio [an, an-1, ..., a1, a0] : P(x) = an*x^n + an-1*x^(n-1) + ... + a1*x + a0
    - x: punto en el que se evaluará el polinomio

Retorno:
    - result: resultado de evaluar el polinomio en x
'''
def horner(poly, x):
    result = poly[0]
    n = len(poly)
 
    for i in range(1, n): 
        result = result*x + poly[i]
 
    return result

'''
Mostrar el polinomio en potencias de (x - a)

Parámetros:
    - poly: lista de coeficientes del polinomio [an, an-1, ..., a1, a0] : P(x) = an*x^n + an-1*x^(n-1) + ... + a1*x + a0
    - a: valor de a en (x - a)

Retorno:
    - coeficientes: lista de coeficientes del polinomio en potencias de (x - a) [bn, bn-1, ..., b1, b0] : P(x) = bn*(x - a)^n + bn-1*(x - a)^(n-1) + ... + b1*(x - a) + b0
'''
def polinomio_potencias(poly, a):
    coeficientes = []
    n = len(poly)
    old_poly = poly.copy()
    new_poly = np.zeros(n - 1)
    
    for i in range(n - 1):
        
        new_poly[0] = old_poly[0]

        for j in range(1, n - 1 - i):
            new_poly[j] = old_poly[j] + a * new_poly[j - 1]

        coeficientes.append(old_poly[-1] + a * new_poly[-1])

        old_poly = new_poly.copy()
        new_poly = np.zeros(n - 2 - i)

    coeficientes.append(old_poly[0])

    return coeficientes[::-1]
  
'''
Mostrar un polinomio por pantalla

Parámetros:
    - coeficientes: lista de coeficientes del polinomio [an, an-1, ..., a1, a0] : P(x) = an*x^n + an-1*x^(n-1) + ... + a1*x + a0
    - x: variable del polinomio

Retorno:
    - None
'''
def mostrar_polinomio(coeficientes, x: str):
    
    print("P(x) = ", end="")

    for i in range(n):
        if (n - i - 1) == 0:
            print(coeficientes[i], end=i < n - 1 and " + " or "\n")
        elif (n - i - 1) == 1:
            if coeficientes[i] == 1:
                print(f"{x}", end=i < n - 1 and " + " or "\n") 
            elif coeficientes[i] != 0:     
                print(f"{coeficientes[i]}{x}", end=i < n - 1 and " + " or "\n")
        else:
            if coeficientes[i] == 1:
                print(f"{x}^{n - i - 1}", end=i < n - 1 and " + " or "\n") 
            elif coeficientes[i] != 0:     
                print(f"{coeficientes[i]}{x}^{n - i - 1}", end=i < n - 1 and " + " or "\n")

# Test
if __name__ == "__main__":
    poly = [5/24, 2/3, 3/2, 2, 1]
    x = 3
    n = len(poly)

    print(f"El resultado de evaluar el polinomio {poly} en x = {x} es: {horner(poly, x)}")
    
    a = 1
    print(f"\nPolinomio en potencias de (x - {a}):")
    mostrar_polinomio(polinomio_potencias(poly, a), f"(x - {a})")
