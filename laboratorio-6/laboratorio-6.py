import numpy as np

# Utilizando las funciones de NumPy polyfit y polyval, escribir una función llamada interp_lagrange que, dados los puntos x, los nodos de interpolación xp y los valores correspondientes de la función en cada nodo fp, evalúe el polinomio de Lagrange en los puntos x.

def get_alpha_i(fp, i):
    alpha_i = fp[i - 1]

    return alpha_i

def get_beta_i(xp, fp, i):
    beta_i = (fp[i] - fp[i - 1]) / (xp[i] - xp[i - 1])

    return beta_i

def interp_lagrange_trozos(x, xp, fp):

    result = []

    for x0 in x:
        # primero hay que encontrar el i tal que x esté en el intervalo [xp[i - 1], xp[i]]
        i = 0

        for j in range(1, len(xp)):
            if xp[j - 1] <= x0 and x0 <= xp[j]:
                i = j
                break
        
        # ahora se calculan alpha_i y beta_i
        alpha_i = get_alpha_i(fp, i)
        beta_i = get_beta_i(xp, fp, i)

        # print(f"alpha_i de {x}: {alpha_i}")
        # print(f"beta_i de {x}: {beta_i}")
        
        # ahora se evalúa el polinomio de Lagrange en x
        s_x = alpha_i + beta_i * (x0 - xp[i - 1])

        result.append(s_x)

    return result

def interp_lagrange(x, xp, fp): 
    polinomio = np.polyfit(xp, fp, len(xp) - 1)
    result = np.polyval(polinomio, x)

    return result

# Ejemplo de uso
if __name__ == "__main__":

    x = [1, 2, 3, 4, 5]
    xp = [1, 2, 3]
    fp = [2, 3, 2]

    result = interp_lagrange(x, xp, fp)

    print(result)

