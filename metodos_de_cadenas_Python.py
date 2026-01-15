#Métodos de cadenas/Objetos String
nombreUsuario = input("Ingrese su nombre de usuario: ")
print("Hola, " + nombreUsuario + "!")

#Para imprimirlo en mayusculas
print("Hola, " + nombreUsuario.upper() + "!")

#Para imprimirlo en minusculas
print("Hola, " + nombreUsuario.lower() + "!")

#Para imprimirlo con la primera letra en mayuscula
print("Hola, " + nombreUsuario.capitalize() + "!")

#Para imprimirlo con la primera letra de cada palabra en mayuscula
print("Hola, " + nombreUsuario.title() + "!")

#Para imprimirlo con la primera letra de cada palabra en mayuscula y el resto en minusculas
print("Hola, " + nombreUsuario.swapcase() + "!")

#Para eliminar espacios al inicio y al final
print("Hola, " + nombreUsuario.strip() + "!")

#Para eliminar espacios al inicio
print("Hola, " + nombreUsuario.lstrip() + "!")

#Para eliminar espacios al final
print("Hola, " + nombreUsuario.rstrip() + "!")

#Para reemplazar una palabra por otra
print("Hola, " + nombreUsuario.replace(" ", "_") + "!")  # Reemplaza espacios por guiones bajos

#Para dividir la cadena en una lista de palabras
print("Hola, " + str(nombreUsuario.split()) + "!")  # Convierte la lista a cadena para imprimir

#Para contar cuantas veces aparece una letra
letra = input("Ingrese una letra para contar cuantas veces aparece: ")
print("La letra '" + letra + "' aparece " + str(nombreUsuario.count(letra)) + " veces en el nombre de usuario.")

#Para saber la posición de una letra
posicion = nombreUsuario.find(letra)
if posicion != -1:
    print("La letra '" + letra + "' se encuentra en la posición " + str(posicion) + ".")
else:
    print("La letra '" + letra + "' no se encuentra en el nombre de usuario.")

#Para verificar si una cadena empieza con una letra
inicio = input("Ingrese una letra para verificar si el nombre de usuario empieza con ella: ")
if nombreUsuario.startswith(inicio):
    print("El nombre de usuario empieza con la letra '" + inicio + "'.")
else:
    print("El nombre de usuario no empieza con la letra '" + inicio + "'.")

#Para verificar si una cadena termina con una letra
fin = input("Ingrese una letra para verificar si el nombre de usuario termina con ella: ")
if nombreUsuario.endswith(fin):
    print("El nombre de usuario termina con la letra '" + fin + "'.")
else:
    print("El nombre de usuario no termina con la letra '" + fin + "'.")

#Para saber si una cadena es alfanumérica
if nombreUsuario.isalnum():
    print("El nombre de usuario es alfanumérico.")

#Para saber si una cadena es solo alfabética
if nombreUsuario.isalpha():
    print("El nombre de usuario es alfabético.")

#Para saber si una cadena es numérica
if nombreUsuario.isdigit():
    print("El nombre de usuario es numérico.")

#Para saber si una cadena es un identificador válido
if nombreUsuario.isidentifier():
    print("El nombre de usuario es un identificador válido.")

#Para saber si una cadena es un espacio en blanco
if nombreUsuario.isspace():
    print("El nombre de usuario es un espacio en blanco.")

#Para saber si una cadena es imprimible
if nombreUsuario.isprintable():
    print("El nombre de usuario es imprimible.")

#Para saber si una cadena es un título
if nombreUsuario.istitle():
    print("El nombre de usuario es un título.")

#Para saber la longitud de la cadena
print("La longitud del nombre de usuario es: " + str(len(nombreUsuario)) + " caracteres.")

#Para invertir la cadena
print("El nombre de usuario invertido es: " + nombreUsuario[::-1])

#Para concatenar dos cadenas
otraCadena = input("Ingrese otra cadena para concatenar: ")
print("La concatenación del nombre de usuario y la otra cadena es: " + nombreUsuario + " " + otraCadena)

#Para repetir la cadena
repeticiones = int(input("Ingrese cuántas veces desea repetir el nombre de usuario: "))
print("El nombre de usuario repetido " + str(repeticiones) + " veces es: " + (nombreUsuario + " ") * repeticiones)

#Para verificar si una cadena contiene otra cadena
subcadena = input("Ingrese una subcadena para verificar si está en el nombre de usuario: ")
if subcadena in nombreUsuario:
    print("La subcadena '" + subcadena + "' está en el nombre de usuario.")
else:
    print("La subcadena '" + subcadena + "' no está en el nombre de usuario.")

  
edad = input("Ingrese su edad: ")
#Si introducimos una cadena de texto que no es un número, se producirá un error.
#Para evitar esto:
while not edad.isdigit(): #Mientras no sea un número || edad.isdigit() == False
    print("Por favor, ingrese un número válido para la edad.")
    edad = input("Ingrese su edad: ")
if int(edad) < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
    


