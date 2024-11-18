from sumar import sumar
from resta import resta
from multplicacion import multiplicar
from dividir import dividir
from suma_avanzada import sumar_numeros

def mostrar_menu():
  print("Seleccione una opción:")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Salir")

def main():
  while True:
    mostrar_menu()
    opcion = input("Ingrese su opción: ")

    if opcion == '5':
      print("Saliendo...")
      break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
      print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == '2':
      print(f"Resultado: {resta(num1, num2)}")
    elif opcion == '3':
      print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == '4':
      print(f"Resultado: {dividir(num1, num2)}")
    elif opcion == '5':
      print(f"Resultado: {sumar_numeros(num1, num2)}")
    else:
      print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
  main()