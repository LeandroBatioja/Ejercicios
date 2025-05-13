# 6. Calcular interés compuesto**

#Escribe un programa que permita calcular el **interés compuesto** de un capital inicial, una tasa de interés anual y un número de años.

def interes_com(prin, inte, tiem):
    return prin * (1 + inte) ** tiem



prin = float(input("Ingrese el valor principal: "))
inte = float(input("Ingrese su interes: "))
tiem = float(input("Ingrese el año destinado: "))


inte_fin = interes_com(prin, inte, tiem)
print(f"El valor de {prin} tiene un interes final de {inte_fin: .0f} en {tiem} años")