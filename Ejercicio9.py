#9. Conversión de horas a días, horas, minutos y segundos**

# Escribe un programa que convierta una cantidad de **horas** ingresada por el usuario a su equivalente en **días**, **horas**, **minutos** y **segundos**.


def conversion_ho_dia_segu_min(horas):
    dias = horas // 24
    horas_restantes = horas % 24
    minutos = horas_restantes * 60
    segundos = minutos * 60

    return [dias, horas_restantes, minutos, segundos]

# Solicitar al usuario la cantidad de horas
horas = int(input("Ingresa la cantidad de horas: "))

# Convertir a días, horas, minutos y segundos
dias, horas_restantes, minutos, segundos = conversion_ho_dia_segu_min(horas)

# Imprimir los resultados
print(f"{horas} horas son:")
print(f"- {dias} días")
print(f"- {horas_restantes} horas")
print(f"- {minutos} minutos")
print(f"- {segundos} segundos")