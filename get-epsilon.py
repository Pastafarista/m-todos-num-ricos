# Description: Calcular el limite de la función f(x) = (1 - cos(x)) / x^2 cuando x tiende a 0
# Author: Antonio

from numpy import cos, power

def get_epsilon():
    epsilon = 1.0
    
    while True:
        if 1.0 + epsilon/2 == 1.0:
            break
        epsilon /= 2
    return epsilon

if __name__ == "__main__":

    print(f"El epsilon de la máquina es: {get_epsilon()}")
    print("1+epsilon = ", 1+get_epsilon() == 1.0)

    for i in range(1, 11):
        x =  1 / power(10, i)

        print(f"Para x = {x}, f(x) = {(1 - cos(x)) / power(x, 2)}")
