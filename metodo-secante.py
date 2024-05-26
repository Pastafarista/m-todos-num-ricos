#!/usr/bin/python3
# Description: Método de la secante para encontrar raices de una función

# Función a la que se le buscará la raíz
def f(x):
    return x**3 - 2*x**2 + 4*x - 8

# Función que calcula la diferencia dividida de dos puntos
def diferencia_dividida(x0, x1, function):
    return (function(x1) - function(x0)) / (x1 - x0)

# Método de la secante
def secante(x0, x1, function):
    
    # Comprobamos si f(x1) está definido
    try:
        numerador = function(x1)
    except:
        Exception("Error: f(x1) no está definido")
    
    # Comprobamos si el denominador es igual a cero
    denominador = diferencia_dividida(x0, x1, function) 
    
    if denominador == 0:
        if function(x0) == 0:
            return x0
        else:
            Exception("Error: denominador igual a cero")
    
    # Buscamos la raíz de la recta interpolante con nodos de interpolación x0 y x1
    x2 = x1 - (numerador / denominador)

    # Comprobamos si f(x2) es igual a cero
    if (abs(function(x2)) < 1e-6):
        return x2
    else:
        return secante(x1, x2, function)

if __name__ == "__main__":
    x0 = 1
    x1 = 3
    raiz = secante(x0, x1, f)

    print(f"La raíz de la función es: {raiz}")
