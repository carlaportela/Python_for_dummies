#Persistencia de datos mediante archivos externos de texto plano
#1º imporamos el módulo io de la biblioteca estándar de Python
from io import open #El método open() permite abrir archivos externos

#Creamos un archivo externo de texto plano
archivo_texto=open("archivo.txt", "w") #El método open() recibe como parámetros el archivo y el modo de apertura ('r' para lectura (read), 'w' para escritura (write), 'a' para añadir contenido (append))
#Al ejecutar el código anterior se creará un archivo llamado "archivo.txt" en el directorio actual

#Escribimos en el archivo externo de texto plano
frase="Hola, soy un archivo de texto plano.\nHoy es miércoles.\n"
archivo_texto.write(frase) #El método write() escribe el contenido de la variable frase en el archivo externo

#Cerramos el archivo externo de texto plano
archivo_texto.close() #El método close() cierra el archivo externo, liberando los recursos asociados a él
                                                                                                                                                                                                                                                        
#Abrir un archivo externo de texto plano en modo lectura
archivo_texto=open("archivo.txt", "r") #Abrimos el archivo en modo lectura
#Leemos el contenido del archivo externo de texto plano
texto=archivo_texto.read() #El método read() lee todo el contenido del archivo y lo almacena en la variable texto
#Cerramos el archivo externo de texto plano
archivo_texto.close() #Cerramos el archivo externo
#Mostramos el contenido del archivo externo de texto plano a pesar de haber cerrado el archivo externo
print(texto)

#También podemos leer el archivo línea por línea
archivo_texto=open("archivo.txt", "r") #Abrimos el archivo en modo lectura
lineas=archivo_texto.readlines() #El método readlines() lee todas las líneas del archivo y las almacena en una lista manipulable
archivo_texto.close() #Cerramos el archivo externo
#Mostramos el contenido del archivo externo de texto plano línea por línea
for linea in lineas:
    print(linea[0]) #Imprimimos la primera línea de texto ya que cada una es un elemento de una lista

#Abrimos el archivo externo de texto plano para añadir contenido
archivo_texto=open("archivo.txt", "a") #Abrimos el archivo en modo añadir
#Añadimos una nueva línea al archivo externo de texto plano
archivo_texto.write("\nEsta es una nueva línea añadida al archivo.") #Escribimos una nueva línea en el archivo externo
#Cerramos el archivo externo de texto plano
archivo_texto.close() #Cerramos el archivo externo

#Manejo de punteros en archivos externos de texto plano
archivo_texto=open("archivo.txt", "r") #Abrimos el archivo en modo lectura
#Al abrir el archivo, si no especificamos la posición del puntero, este se posiciona al inicio del archivo por defecto
#En cambio si lo leemos, el puntero se desplaza al final del contenido leído
print(archivo_texto.read())
#Por lo que si volvemos a leer el archivo, no obtendremos el contenido completo
print(archivo_texto.read()) #No se mostrará nada porque el puntero está al final del archivo
#Para desplazar la posición del puntero por defecto utilizamos el método seek() permite desplazar el puntero a una posición específica del archivo (Número de caracteres desde el inicio del archivo)
archivo_texto.seek(0) #Coloca el puntero al inicio del archivo de nuevo
#También podemos utilizar el método read() y pasarle como parámetro el número de caracteres que queremos leer
print(archivo_texto.read(5)) #Leerá los primeros 5 caracteres del archivo
print(archivo_texto.read(10)) #Leerá los siguientes 10 caracteres del archivo
print(archivo_texto.read()) #Leerá el resto de caracteres del archivo desde la posición actual del puntero
#Para colocar el puntero en mitad del archivo:
archivo_texto.seek(len(archivo_texto.read())/2)
#Cerramos el archivo externo de texto plano
archivo_texto.close() 

#También podemos abrir el archivo en modo lectura y escritura al mismo tiempo
archivo_texto=open("archivo.txt", "r+") #Modo lectura y escritura
#Al abrir el archivo el puntero se encuentra al inicio, por lo que si añadimos contenido con el método write() lo hará al inicio del archivo
archivo_texto.write("Comienzo de texto")
#Incluimos una linea en mitad del archivo
lista_texto=archivo_texto.readlines()
posicion=int(len(lista_texto)/2)
print(posicion)
lista_texto[posicion]="Esta linea ha sido incluida desde el exterior y en mitad del archivo \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()


