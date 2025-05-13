#5. Conversión de millas a kilómetros y metros**

#Desarrolla un programa que convierta una cantidad dada en **millas** a su equivalente en **kilómetros** y **metros**.

millas = float(input("Intorduce la distancia en millas: "))

kilometros = millas * 1.609
metros = millas * 1609

print(f"{millas} millas equivalen a {kilometros} kilometros")
print(f"{millas} millas equivalen a {metros} metros")