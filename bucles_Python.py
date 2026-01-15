#Bucle for determinado (Número de iteraciones determinado)
for i in [1,2,3]: #Se itera 3 veces ya que en la lista existen 3 elementos
    print(i)
#Cuando el flujo de ejecución llega a i, i=1, y ejecuta e imprime i; y esto lo repite hasta finalizar la lista

#El bucle for también puede iterar sobre cadenas de texto
for letra in "Hola, mundo!":
    print(letra) #Imprime cada letra en una linea

#Evaluar si una dirección de correo electrónico es válida mediante un bucle for
email=False #Iniciamos la variable en false para que sea evaluada después
email_input = input("Introduce tu dirección de correo electrónico: ")   
for i in email_input: #Recorre cada caracter de la dirección de correo electrónico
    if i == "@":
        email = True

if email == True: #if email:
    print("La dirección de correo electrónico es válida")
else:
    print("La dirección de correo electrónico no es válida")

#Añadimos un contador para verificar una dirección de correo electrónico si contiene @ o "."
contador=0 #Inicializamos un contador
email_input = input("Introduce tu dirección de correo electrónico: ")   
for i in email_input: #Recorre cada caracter de la dirección de correo electrónico
    if i == "@" or i==".":
       contador+=1 #contador = contador + 1

if contador >= 2: #Una dirección de correo válida sería aquella que como mínimo contenga una @ y un punto
    print("La dirección de correo electrónico es válida")
else:
    print("La dirección de correo electrónico no es válida")

#El tipo range permite hacer conteos numéricos en un rango determinado (crea un array/lista de números)
for i in range(5): #Comienza en 0 y termina en 5 (no incluye 5)
    print(f"Valor de la variable {i}") #Notación para encadenar variables en strings

for i in range(1, 6): #Se itera 5 veces, del 1 al 6 (no incluye 6)
    print(i)

for i in range(5,50,3): #El tipo range permite un tercer argumento para especificar el incremento
    print(i) #Comienza en 5, termina en 50 (no incluye 50), y se incrementa de 3 en 3
    
email_valido=False
email_input = input("Introduce tu dirección de correo electrónico: ")
for i in range(len(email_input)):
    if email_input[i] == "@":
        email_valido = True
if email_valido:
    print("La dirección de correo electrónico es válida")
else:
    print("La dirección de correo electrónico no es válida")

#---------------------------------------------------------------------------------------------------------------
#Bucle while indeterminado (No se conoce el número de iteraciones)
i=1
while i<=10:
    print("Ejecución" + str(i))
    i+=1
print("Fin del bucle")

edad=int(input("Introduce tu edad: "))
while edad<0 or edad>100: #Mientras la edad sea negativa o superior a 100, lo indicará y se pedirá de nuevo introducir la edad
    print("Edad incorrecta. Introduce una edad válida")
    edad=int(input("Introduce tu edad: "))
print("Edad correcta")
print("Edad del aspirante"+str(edad))

#Instruccion break
import math #Importamos la librería math para calcular la raíz cuadrada
print("Programa de cálculo de raíz cuadrada")
numero_input=int(input("Introduce un número: "))
intentos=0
while numero_input<0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos==2:
        print("Has superado el número de intentos permitidos")
        break #Salimos del bucle while y se continua con la ejecución de la lineas que le siguen
    numero_input=int(input("Introduce un número: "))
    if numero_input<0:
        intentos+=1
if intentos<2:
    raiz_cuadrada=math.sqrt(numero_input)
    print("La raíz cuadrada de", numero_input, "es", raiz_cuadrada)

#Instrucción continue (salta a la siguiente iteración del bucle)
for letra in "Python":
    if letra=="h":
        continue #Saltamos a la siguiente iteración del bucle (no imprime la letra h)
    print("Viendo la letra:", letra)#Esta linea es ignorada si encuentra la letra h

nombre="Maldita Carlita"
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1 #No se cuentan los espacios en el nombre
print("El nombre tiene", contador, "letras")

#Instrucción pass (devuelve null, como si el bucle no se ejecutara)
#while True:
    #pass #Este bucle nunca terminará, pero se puede salir de él mediante Ctrl+c

#class MiClase:
    #pass #Para implementar más tarde

#Instrucción else en bucles
email_input = input("Introduce tu dirección de correo electrónico: ")
for i in email_input:
    if i == "@":
        arroba="El correo electrónico tiene una arroba"
        break
else:
        arroba="El correo electrónico no tiene una arroba"
print(arroba)


