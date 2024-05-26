#!/home/antonio/.config/virtualenvs/matemáticas/bin/python3.11
# Description: Ver los problemas de la aritmética en coma flotante
# Athor: Antonio Cabrera

import math

def x_1(a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

def x_2(a, b, c):
    return (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

def y_1(a, b, c):
    return 2*c / (-b - math.sqrt(b**2 - 4*a*c))

def y_2(a, b, c):
    return 2*c / (-b + math.sqrt(b**2 - 4*a*c))

def test(a, b, c):

    print(f"a = {a}, b = {b}, c = {c}")

    try:
        print(f"x_1 = {x_1(a, b, c)}")
    except Exception as e:
        print(f"Error x_1: {e}")

    try:
        print(f"x_2 = {x_2(a, b, c)}")
    except Exception as e:
        print(f"Error x_2: {e}")

    try:
        print(f"y_1 = {y_1(a, b, c)}")
    except Exception as e:
        print(f"Error y_1: {e}")

    try:
        print(f"y_2 = {y_2(a, b, c)}")
    except Exception as e:
        print(f"Error y_2: {e}")

if __name__ == "__main__":
    a = 1
    b = 9**12
    c = -3

    test(a, b, c)

    b = -9**12

    test(a, b, c)

