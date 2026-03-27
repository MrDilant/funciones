

def sumar_2_numeros():

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    suma = num1 + num2
    
    print(f"Resultado: {suma}")

def restar_2_numeros(): 

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    resta = num1 - num2 

    print(f"Resultado: {resta}")

def multiplicar_2_numeros():

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    multipicacion = num1 * num2

    print(f"Resultado: {multipicacion}")

def dividir_2_numeros():

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        division = num1 // num2
        print(f"Resultado: {division}")



def exponenciar_numero(num):
    resultado = num ** 2
    return resultado
