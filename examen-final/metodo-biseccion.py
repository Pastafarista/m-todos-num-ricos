#!/usr/bin/python3
# Description: Método de Bisección para encontrar raices de una función

# Función a la que se le buscará la raiz
def f(x):
    return x**2 - 2

# Función que devuelve el signo de un número
def signo(x):
    if x > 0:
        return 1 
    elif x < 0:
        return -1
    else:
        return 0

def biseccion(a, b, function):
    # Obtenemos el punto medio
    c = (a+b)/2
    
    # Condición de parada
    if(abs(function(c)) < 0.0001):
        return c
    
    if signo(function(a)) != signo(function(c)):
        return biseccion(c, a, function)
    elif signo(function(b)) != signo(function(c)):
        return biseccion(b, c, function)

if __name__ == '__main__':
    raiz = biseccion(1, 3, f)

    print(f'La raiz de f es {raiz}')
