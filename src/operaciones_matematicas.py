

def sumar_2_numeros(num1,num2):

    resultado = num1 + num2
    return  resultado


def restar_2_numeros(num1,num2):
    resultado = num1 - num2
    return resultado 

   
def multiplicar_2_numeros(num1,num2):
    resultado = num1 * num2
    return resultado


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
