#Conversión de temperatura (Celsius a Fahrenheit o Fahrenheit a Celsius)**

#Crea un programa que convierta una temperatura de **Celsius a Fahrenheit** o de **Fahrenheit a Celsius**, dependiendo de la elección del usuario.

def fahrenheit_a_celsius(f):
    return (f - 32) / 1.8


def celsius_a_fahrenheit(c):
    return (c * 1.8) + 32


# Modo de uso
f = float(input("Ingresa los grados Fahrenheit: "))
c = fahrenheit_a_celsius(f)
print(f"Los {f} grados Fahrenheit son {c} grados celsius")

c = float(input("Ingresa los grados Celsius: "))
f = celsius_a_fahrenheit(c)
print(f"Los {c} grados Celsius son {f} grados Fahrenheit")