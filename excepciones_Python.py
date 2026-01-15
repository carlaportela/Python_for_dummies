#Bloque try/except --------------------------------------------------------------------------------------------------------------------
#Las excepciones son errores que ocurren durante la ejecución de un programa.
#Cuando se produce un error, el programa se detiene y muestra un mensaje de error.
#Para evitar que el programa se detenga, podemos manejar las excepciones utilizando bloques try/except.
 
#Este es el código de un programa que calcula el resultado de sumar, restar, multiplicar y dividir dos números.

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
#Mediante el manejo o control de excepción, para que aunque se produzca un error, el resto del programa se ejecute
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir ningún número entre 0")
		return "Operación errónea"

#Pedimos al usuario que introduzca los operandos y la operación a realizar
#Si el valor introducido no es el que se espera podemos colocar una excepción
while True:
    try:
        op1=(int(input("Introduce el primer número: ")))

        op2=(int(input("Introduce el segundo número: ")))	
        break	#Si tiene éxito el try, sale con el break y no lee el except; sino salta al error y volverá a pedir los valores
    except ValueError:
        print("Los valores introducidos no son correctos. Inténtalo de nuevo")
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa")

#Posibles errores:

    #Si introducimos dos números 0 y seleccionamos "divide" se producen los siguiente mensaje de error de ejecución
        #Traceback (most recent call last): (Pila de llamadas)
            #File "d:\Ciclo Desarrollo Web\Curso_Python\excepciones_Python.py", line 33, in <module>
                #print(divide(op1,op2))
            #File "d:\Ciclo Desarrollo Web\Curso_Python\excepciones_Python.py", line 12, in divide      
                #return num1/num2
        #ZeroDivisionError: division by zero (Descripción de error: Error de división por cero)

    #Para poder controlarlo, la instruccion susceptible de comerte el error la metemos en un bloque try/except y el nombre del error

    #Si introducimos una cadena de texto en lugar de valores numéricos nos da el siguiente error
        # Traceback (most recent call last): (Pila de llamadas)
            #File "d:\Ciclo Desarrollo Web\Curso_Python\excepciones_Python.py", line 37, in <module>
                #print(divide(op1,op2))
            #File "d:\Ciclo Desarrollo Web\Curso_Python\excepciones_Python.py", line 12, in divide      
                #return num1/num2
        #TypeError: unsupported operand type(s) for /: 'int' and'str' (Descripción de error: Operando de tipo no compatible para la división)
    #Si introducimos un valor cuyo tipo no se corresponde con lo esperado nos dará eñl siguiente error de tipo ValueError
        #Al colocar una excepción, el programa continua su ejecución, lo cual no tiene sentido ya que la variable op1 nunca estará definida (NameError). 
        #Para ello usamos un bucle infinito (while true) poniendo un break para poder salir de el en caso de que se establezcan las variables

#Clausula finally --------------------------------------------------------------------------------------------------------------------------------------------

def divide():
    while True:
        try:
            #Intentamos realizar la división
            op1=(float(input("Introduce el primer número: ")))
            op2=(float(input("Introduce el segundo número: ")))
            print("Resultado de la división:", op1 / op2)
            break  # Salimos del bucle si la división se realiza correctamente
        except ValueError:
            print("El valor introducido no es un número válido")
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
        finally:
            # Este bloque se ejecuta siempre, independientemente de si hubo un error o no
            print("Intento de división finalizado")
    print("Fin de la ejecución del programa")

divide()

#Al no colocar un bloque try/except, si introducimos un valor 0 en segundo lugar o un valor no numérico, el programa se detiene dando los siguientes errores respectivamente:
    #- ZeroDivisionError: float division by zero
    #- ValueError: could not convert string to float: 'texto'
#Si colocamos un bloque try/except, el programa no se detiene y se ejecuta la instrucción print de la línea 48, aunque no se haya realizado la división correctamente
#En Python podemos poner varias clausulas except consecutivas para manejar diferentes tipos de errores, o una sola que maneje todos los errores posibles.

#Lanzamiento de excepciones con raise------------------------------------------------------------------------

def evaluaEdad(edad):
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"  
    elif edad<65:
        return "Eres maduro"
    else:
        return "Eres un anciano"
    
print(evaluaEdad(18))  #Eres muy joven
print(evaluaEdad(25))  #Eres joven
print(evaluaEdad(50))  #Eres maduro
print(evaluaEdad(70))  #Eres un anciano

#Si introducimos una edad negativa, no tiene sentido, por lo que podemos lanzar una excepción personalizada con raise

def evaluaEdad():
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise TypeError("La edad no puede ser negativa")
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"  
    elif edad<65:
        return "Eres maduro"
    else:
        return "Eres un anciano"

evaluaEdad()

#Lanzamiento de una excepción con raise y personalizando el error con as -----------------------------------------------------------------
import math

def calculaRaiz(num):
    if num < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    else: 
        return math.sqrt(num)

numero=int(input("Introduce un número para calcular su raíz cuadrada: "))
try:
    print(calculaRaiz(numero))
except ValueError as errorNumeroNegativo:
    print(errorNumeroNegativo)
print("Fin del programa")

#Si introducimos un número negativo, se lanza una excepción ValueError con el mensaje "No se puede calcular la raíz cuadrada de un número negativo"
#es uy útil para el usuario ver un mensaje claro sobre el error que ha cometido, en lugar de un mensaje genérico de error de Python.