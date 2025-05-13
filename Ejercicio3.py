#3. Perímetro y área de un rectángulo**

#Escribe un programa que calcule el **perímetro** y el **área** de un rectángulo, dados su largo y ancho. El programa debe validar que ambos valores sean positivos.



ladoa = int(input("Dame un lado: "))
ladob = int(input("dame el otro lado:"))

area = ladoa * ladob
perimetro = 2*ladoa + 2*ladob

print("El valor del area es: ", area)
print("El valor del perimetro es: ", perimetro)