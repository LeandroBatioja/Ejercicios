# 4. Potencia de un número con opción de repetir**

#Crea un programa que calcule la **potencia de un número**, dados una base y un exponente ingresados por el usuario. El programa debe permitir al usuario realizar múltiples cálculos sin reiniciar.

def calcular_potencia(base, exponente):
  return base ** exponente

while True:
  base_str = input("Ingrese la base (o 'salir'): ")
  if base_str.lower() == 'salir':
    break
  try:
    base = float(base_str)
    exponente_str = input("Ingrese el exponente: ")
    exponente = float(exponente_str)
    resultado = calcular_potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado}")
  except ValueError:
    print("Entrada inválida. Ingrese números.")