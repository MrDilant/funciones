from src.operaciones_matematicas import *


print("Calculadora en consola")

print("1. Sumar 2 números")
print("2. Restar 2 números")
print("3. Multiplicar 2 números")
print("4. dividir 2 números")
print("5. Exponenciación de números")
print("0. Salir")

opcion = input("Ingrese la opción: ")


if opcion == "1":
    sumar_2_numeros()
    


elif opcion == "2":
     restar_2_numeros()



elif opcion == "3":
    multiplicar_2_numeros()
    


elif opcion == "4":
    dividir_2_numeros()
   


elif opcion == "5":
    num = int(input("Ingrese un número: "))
    numero_transformado = exponenciar_numero(num)
    print(numero_transformado)

elif opcion == "0":
    print("Saliendo...")

