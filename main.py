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
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    numeros_sumados = sumar_2_numeros(num1,num2)
    print(numeros_sumados)


    

elif opcion == "2":
     num1 = int(input("Ingrese primer número: "))
     num2 = int(input("Ingrese segundo número: "))
     
     numeros_restados = restar_2_numeros(n1,n2)
     print(numeros_restados)
     



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

