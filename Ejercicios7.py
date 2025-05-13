# 7. Cálculo del promedio de N notas**

#Crea un programa que permita ingresar un número indefinido de **notas**, y al finalizar, calcule el **promedio** de todas ellas.


 
calificaciones = int(input("Ingrese la cantidad de calificaciones: "))
 
lista = []
posicion = 1
totalIngresadas = calificaciones
 
while calificaciones > 0:
    valor = float(input("Ingrese calificación {}: ".format(posicion)))
    lista.append(valor)
    calificaciones -= 1
    posicion += 1
 
print(lista)
 
sumaNotas = 0
for i in lista:
    sumaNotas = sumaNotas + i
 
promedio = round(sumaNotas/totalIngresadas,2)
 
print("El promedio de las notas ingresadas es: {}".format(promedio))