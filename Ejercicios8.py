# 8. Cálculo de descuento con validación**

#Desarrolla un programa que calcule el **precio final de un producto** después de aplicarle un porcentaje de descuento. El programa debe validar que el porcentaje esté entre 0 y 100.


def calc_pre_descuento(pre, desc):
    pre_desc = pre - (pre * desc / 100)
    return pre_desc

pre = float(input("Ingrese el precio del producto: "))
desc = float(input("Ingrese el procentaje de descuento: "))

pre_fin = calc_pre_descuento(pre, desc)

print(f"El precio final con el descuento incluido es de:  {pre_fin:.2f}")