#!/home/antonio/.config/virtualenvs/matemáticas/bin/python3.11
# Description: Cálculo de los nodos de Chebyshev
# Author: Antonio Cabrera

from math import cos, pi

def chebyshev(n):
    return [cos((2*k+1)*pi/(2*n)) for k in range(n)]

if __name__ == '__main__':
    n = 4

    print(f"Los nodos de Chebyshev de grado {n} son: {chebyshev(n)}")
