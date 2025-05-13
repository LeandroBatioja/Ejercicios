#1. Área y perímetro de un círculo**

#Escribe un programa que calcule el **área** y el **perímetro** de un círculo, dado el valor de su radio. El programa debe validar que el radio sea un valor positivo.

import math
def cal(ra):
    if ra < 0:
        raise AssertionError ("radio Negativo")
    elif ra == 0:
        raise AssertionError ("radio Negativo")
    
    ar = math.pi * ra ** 2
    per = 2 * math.pi * ra
    
    return ar, per

ra = float(input("Ingrese su radio: "))
ar, per = cal(ra)
print("area: ", ar)
print("perimetro: ", per)