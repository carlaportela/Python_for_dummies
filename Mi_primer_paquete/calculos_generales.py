def sumar(op1, op2):
    print("El resultado de la suma es:", op1 + op2)

def restar(op1, op2):
    print("El resultado de la resta es:", op1 - op2)

def multiplicar(op1, op2):
    print("El resultado de la multiplicación es:", op1 * op2)
    
def dividir(op1, op2):
    if op2 != 0:
        print("El resultado de la división es:", op1 / op2)
    else:
        print("Error: No se puede dividir por cero.")

def potencia(base, exponente):
    print("El resultado de la potencia es:", base ** exponente)

def raiz_cuadrada(numero):
    if numero >= 0:
        print("El resultado de la raíz cuadrada es:", numero ** 0.5)
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")

def redondear(numero):
    print("El número redondeado es:", round(numero))