#3. Perímetro y área de un rectángulo**

#Escribe un programa que calcule el **perímetro** y el **área** de un rectángulo, dados su largo y ancho. El programa debe validar que ambos valores sean positivos.



import math
def cal(rec):
    if rec < 0:
        raise AssertionError ("radio Negativo")
    elif rec == 0:
        raise AssertionError ("radio Negativo")
    
    rec = rec * rec
    per = 2 * math.pi * ra
    
    return ar, per

ra = float(input("Ingrese su radio: "))
ar, per = cal(ra)
print("area: ", ar)
print("perimetro: ", per)