#Expresiones regulares en Python ------------------------------------------------------------------------------------------------------
#Secuencia de caracteres que forman un patrón que sirve para:
# - Realizar búsquedas de un texto que se ajusten a dicho patrón (correo electrónico).
# - Reemplazar partes de un texto que se ajusten a dicho patrón.
# - Buscar si existe una cadena de caracteres dentro de un texto.
# - Extraer partes de un texto que se ajusten a dicho patrón.
# - Contar el número de coincidencias dentro de un texto.

#La documentación oficial de Python sobre expresiones regulares está en:
#https://docs.python.org/3/library/re.html

#Para trabajar con expresiones regulares en Python, se utiliza el módulo re.
import re

#Creamos una variable con una cadena de texto.
cadena = "En un lugar de La Mancha, de cuyo nombre no quiero acordarme..." 

#Ejemplos de métodos del módulo re ------------------------------------------------------------------------------------------------------
#Usamos la función search del módulo re para buscar la palabra "lugar" en la cadena.
resultado = re.search("lugar", cadena) #Pasamos como parámetros la palabra que buscamos y la cadena de texto donde buscarla.
print(resultado) #Mostramos el resultado de la búsqueda.
#Devuelve un objeto Match si encuentra la palabra, o None si no la encuentra.

textoBuscar="nombre" #Creamos una variable con la palabra que queremos buscar.
#Usamos la función search del módulo re para buscar la palabra almacenada en la variable texto
if re.search(textoBuscar, cadena) is not None: #Si la función search devuelve un objeto Match (es decir, encuentra la palabra)  
    print(f'Se ha encontrado la palabra "{textoBuscar}" en la cadena de texto.')
else:
    print(f'No se ha encontrado la palabra "{textoBuscar}" en la cadena de texto.')
    
#Si queremos obtener la posición de la palabra encontrada, podemos usar los métodos start() y end() del objeto Match.
textoEncontrado = re.search(textoBuscar, cadena) #Buscamos la palabra almacenada en la variable textoBuscar en la cadena.
print(textoEncontrado.start()) #Devuelve la posición inicial de la palabra encontrada.
print(textoEncontrado.end())   #Devuelve la posición final de la palabra encontrada.

#El método span() devuelve una tupla con la posición inicial y final de la palabra encontrada.
print(textoEncontrado.span())  #Devuelve una tupla (inicio, fin).

#El método findall() devuelve una lista con todas las coincidencias encontradas en el texto.
coincidencias = re.findall("de", cadena) #Buscamos todas las apariciones de la palabra "de" en la cadena.
print(coincidencias) #Mostramos la lista de coincidencias. Devuelve ['de', 'de', 'de'].

#El método len() nos permite contar el número de elementos en una lista.
print(len(coincidencias)) #Mostramos el número de coincidencias encontradas. Devuelve 3.

#Metacaracteres -----------------------------------------------------------------------------------------------------------------------
#son caracteres especiales que tienen un significado especial en las expresiones regulares.

#Ejemplos de metacaracteres:
# . (punto): coincide con cualquier carácter excepto una nueva línea.
# ^ (circunflejo): coincide con el inicio de una cadena.
# $ (dólar): coincide con el final de una cadena.
# * (asterisco): coincide con cero o más repeticiones del carácter anterior.
# + (más): coincide con una o más repeticiones del carácter anterior.
# ? (interrogación): coincide con cero o una repetición del carácter anterior.
# ! (signo de exclamación): niega el patrón que le sigue.
# [] (corchetes): define un conjunto de caracteres a buscar.
# | (barra vertical): actúa como operador OR.
# & (ampersand): actúa como operador AND.

#Las anclas son metacaracteres que permiten buscar coincidencias en posiciones específicas dentro de una cadena.
#Ejemplos de anclas:
# ^ (circunflejo): coincide con el inicio de una cadena.
# $ (dólar): coincide con el final de una cadena.
# \b: coincide con un límite de palabra (inicio o fin de una palabra).
# \B: coincide con una posición que no es un límite de palabra.

#Ejemplos de uso de metacaracteres y anclas ---------------------------------------------------------------------------------------------
listaNombresApellidos = ["Ana Gómez", "Antonio Pérez", "Maria Gómez", "Mario Casas", "Juan Vacas", "Julian Pérez", "Alberto Rey"]
#recorremos la lista de nombres, elemento a elemento, y buscamos los nombres que empiezan por "A"
for nombre in listaNombresApellidos:
    if re.findall('^Ana', nombre):
        print(nombre) #Devuelve "Ana Gómez"

for nombre in listaNombresApellidos:
    if re.findall('Pérez$', nombre):
        print(nombre) #Devuelve "Antonio Pérez" y "Julian Pérez"
        
listaDominios = ["http://example.com", "https://secure-site.org", "ftp://fileserver.net", "http://mywebsite.es"]
#recorremos la lista de dominios, elemento a elemento, y buscamos los que empiezan por "http"
for dominio in listaDominios:
    if re.findall('^http', dominio):
        print(dominio) #Devuelve "http://example.com" y "http://mywebsite.es"

#Clases de caracteres son conjuntos de caracteres que permiten definir patrones de búsqueda más específicos y van entre corchetes [].
#Ejemplos de clases de caracteres:
# \d: coincide con cualquier dígito (0-9).
# \D: coincide con cualquier carácter que no sea un dígito.
# \w: coincide con cualquier carácter alfanumérico (letras, dígitos y guiones bajos).
# \W: coincide con cualquier carácter que no sea alfanumérico.
# \s: coincide con cualquier carácter de espacio en blanco (espacios, tabulaciones, saltos de línea).
# \S: coincide con cualquier carácter que no sea un espacio en blanco.

#Ejemplos de uso de clases de caracteres -----------------------------------------------------------------------------------------------
listaUsuarios = ["Usuario123", "admin_456", "guest!@#", "root$%^", "test_user789"]
#Buscamos todas las secuencias de dígitos en el texto
for usuario in listaUsuarios:
    if re.findall('[@]', usuario):
        print(usuario) #Devuelve "guest!@#"

listaPersonas = ['hombres', 'mujeres', 'niños', 'niñas', 'adultos', 'adolescentes', 'tio', 'tío', 'tía', 'tia']
#Buscamos niños y niñas en la lista
for persona in listaPersonas:
    if re.findall('niñ[oa]s', persona): #Lo que aparece entre corchetes indica que puede ser una 'o' o una 'a'
        print(persona) #Devuelve "niños" y "niñas"

#Buscamos palabras con acento y sin acento en la lista
for persona in listaPersonas:
    if re.findall('t[íioa]', persona): #Lo que aparece entre corchetes indica que puede ser una 'í' o una 'i'
        print(persona) #Devuelve "tio", "tío", "tía" y "tia"

#Rangos de caracteres ---------------------------------------------------------------------------------------------------------------
#Los rangos nos permiten definir un conjunto de caracteres especificando un rango entre dos caracteres utilizando el guion (-).

#Ejempls de uso de rango de caracteres
listaNombres = ["Ana", "Antonio", "Maria", "Mario", "Juan", "Julian", "Alberto", "Beatriz", "Carmen"]
#Buscamos los nombres que empiezan por una letra entre la A y la M
print("Nombres que contienen caracteres entre la o y la t:")
for nombre in listaNombres:
    if re.findall('[o-t]', nombre): 
        print(nombre) #Devuelve "Antonio", "Maria", "Mario", "Alberto", "Beatriz" y "Carmen"

#Distingue entre mayúsculas y minúsculas, por lo que si hacemos la misma búsqueda pero en mayúsculas, no devolverá ningún resultado.
print("Nombres que contienen caracteres entre la O y la T:")
for nombre in listaNombres:
    if re.findall('[O-T]', nombre): 
        print(nombre) #No devuelve nada
    else:
        print("No hay nombres con caracteres entre la O y la T.")

#Buscamos nombres que empiezan por la A hasta la M
print("Nombres que empiezan por la A-M:")
for nombre in listaNombres:
    if re.findall('[^A-M]', nombre): 
        print(nombre) #Devuelve "Ana", "Antonio", "Maria", "Mario", "Juan", "Julian", "Alberto", "Beatriz" y "Carmen"

#Buscamos nombres que terminen por la letra 0 hasta la t
print("Nombres que terminan por la o-t:")
for nombre in listaNombres:
    if re.findall('[o-t]$', nombre): 
        print(nombre) #Devuelve "Antonio", "Mario" y "Alberto"
        
#Buscamos los 3 primeros pedidos de una lista de pedidos
listaPedidos = ["Madrid1", "Barcelona2", "Malaga1", "Madrid2", "Valencia3", "Sevilla4", "Malaga3", "Valencia2", "Zaragoza5", "Bilbao6", "Madrid3"]
print("Primer y segundo pedido de Madrid:")
for pedido in listaPedidos:
    if re.findall('^Madrid[1-2]', pedido): 
        print(pedido) #Devuelve "Madrid1" y "Madrid2"

#Con el acento circunflejo (^) delante del rango (dentro de los corchetes), negamos el rango de caracteres.
print("lista de pedidos de Madrid que no sean el 1 o el 2:")
for pedido in listaPedidos:
    if re.findall('^Madrid[^1-2]', pedido): 
        print(pedido) #Devuelve "Madrid3"
        
print("lista de pedidos de Madrid que no sean el 1 o el 2:")
for pedido in listaPedidos:
    if re.findall('^Madrid^[1-2]', pedido): 
        print(pedido) #No funciona, no devuelve nada
        
#Buscamos lista de pedidos que no sean de Madrid ni Barcelona
print("Lista de pedidos que no sean de Madrid ni Barcelona:")
for pedido in listaPedidos:
    if re.findall('^(?!Madrid|Barcelona).*', pedido): #Que empiece por algo que no sea Madrid o Barcelona y que continue con cualquier número de caracteres (.*) que no sea salto de línea
        print(pedido) #Devuelve "Valencia3", "Sevilla4", "Valencia2", "Zaragoza5", "Bilbao6" y "Madrid3"

print("lista de pedidos que empiecen por Ma y que contengan letras entre la f y la l:")
for pedido in listaPedidos:
    if re.findall('^Ma[f-l]', pedido): #Que empiece por algo que no sea Madrid o Barcelona y que continue con una M y cualquier número de caracteres (.*) que no sea salto de línea
        print(pedido) #Devuelve "Malaga1" y "Malaga3"

#Función match --------------------------------------------------------------------------------------------------------------------------
#El método match() busca una coincidencia sólo al inicio de la cadena.

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"
nombre4="Yara López"
nombre5="Lara Gómez"
nombre6="5458100454"
nombre7="abc5458100"

#Buscamos coincidencias en nombres al principio de la cadena
patronBusqueda1="Sandra"
print(f'Buscando el nombre "{patronBusqueda1}" en las cadenas "{nombre1}" y "{nombre2}":')
if re.match(patronBusqueda1, nombre1): #Busca el patrón "Sandra" al inicio de la cadena nombre1
    print(f'Hemos encontrado el nombre "{patronBusqueda1}" en la cadena nombre1') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre1') #Devuelve el mensaje

if re.match(patronBusqueda1, nombre2): #Busca el patrón "Sandra" al inicio de la cadena nombre2
    print(f'Hemos encontrado el nombre "{patronBusqueda1}" en la cadena nombre2') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre2') #Devuelve el mensaje

#La función match distingue entre mayúsculas y minúsculas.
patronBusqueda2="maría"
print(f'Buscando el nombre "{patronBusqueda2}" en la cadena "{nombre3}":')
if re.match(patronBusqueda2, nombre3): #Busca el patrón "maría" al inicio de la cadena nombre3
    print(f'Hemos encontrado el nombre "{patronBusqueda2}" en la cadena nombre3') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre3') #Devuelve el mensaje

#Si queremos que no distinga entre mayúsculas y minúsculas, podemos usar un tercer parámetro, re.IGNORECASE
print(f'Buscando el nombre "{patronBusqueda2}" en la cadena "{nombre3}" sin distinguir entre mayúsculas y minúsculas:')
if re.match(patronBusqueda2, nombre3, re.IGNORECASE): #Busca el patrón "maría" al inicio de la cadena nombre3 sin distinguir entre mayúsculas y minúsculas
    print(f'Hemos encontrado el nombre "{patronBusqueda2}" en la cadena nombre3') #Devuelve el mensaje  
else:
    print(f'No lo hemos encontrado en la cadena nombre3') #Devuelve el mensaje

#Podemos utilizar comodines para buscar nombres que se parezcan al patrón que buscamos.
patronBusqueda3=".*ara" #El punto (.) representa cualquier carácter y el asterisco (*) representa cero o más repeticiones del carácter anterior.
print(f'Buscando nombres que terminen en "ara" en las cadenas "{nombre4}" y "{nombre5}":')
if re.match(patronBusqueda3, nombre4): #Busca el patrón ".*ara" al inicio de la cadena nombre4
    print(f'Hemos encontrado un nombre que termina en "ara" en la cadena nombre4, {nombre4}') #Devuelve el mensaje         
else:
    print(f'No lo hemos encontrado en la cadena nombre4, {nombre4}') #Devuelve el mensaje
if re.match(patronBusqueda3, nombre5): #Busca el patrón ".*ara" al inicio de la cadena nombre5
    print(f'Hemos encontrado un nombre que termina en "ara" en la cadena nombre5, {nombre5}') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre5, {nombre5}') #Devuelve el mensaje
    
patronBusqueda1 = "\d{10}" #Busca una secuencia de 10 dígitos
print(f'Buscando una secuencia de 10 dígitos en las cadenas "{nombre6}" y "{nombre7}":')
if re.match(patronBusqueda1, nombre6): #Busca el patrón "\d{10  }" al inicio de la cadena nombre6
    print(f'Hemos encontrado una secuencia de 10 dígitos en la cadena nombre6, {nombre6}') #Devuelve el mensaje     
else:
    print(f'No lo hemos encontrado en la cadena nombre6, {nombre6}') #Devuelve el mensaje
if re.match(patronBusqueda1, nombre7): #Busca el patrón "\d{10  }" al inicio de la cadena nombre7
    print(f'Hemos encontrado una secuencia de 10 dígitos en la cadena nombre7, {nombre7}') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre7, {nombre7}') #Devuelve el mensaje
    
#Función search -------------------------------------------------------------------------------------------------------------------------
#El método search() busca una coincidencia en toda la cadena.
#Buscamos coincidencias en apellidos, que no están al principio de la cadena.  
patronBusqueda4="López"
print(f'Buscando el apellido "{patronBusqueda4}" en las cadenas "{nombre1}" y "{nombre2}":')
if re.search(patronBusqueda4, nombre1): #Busca el patrón "López"
    print(f'Hemos encontrado el apellido "{patronBusqueda4}" en la cadena nombre1') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre1') #Devuelve el mensaje
if re.search(patronBusqueda4, nombre2): #Busca el patrón "López"
    print(f'Hemos encontrado el apellido "{patronBusqueda4}" en la cadena nombre2') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre2') #Devuelve el mensaje
    
#La función search también distingue entre mayúsculas y minúsculas. Para lo que usaríamos el tercer parámetro re.IGNORECASE
patronBusqueda5="gómez"
print(f'Buscando el apellido "{patronBusqueda5}" en las cadenas "{nombre1}" y "{nombre2}" sin distinguir entre mayúsculas y minúsculas:')
if re.search(patronBusqueda5, nombre1, re.IGNORECASE): #Busca el patrón "gómez" en la cadena nombre1 sin distinguir entre mayúsculas y minúsculas
    print(f'Hemos encontrado el apellido "{patronBusqueda5}" en la cadena nombre1') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre1') #Devuelve el mensaje
if re.search(patronBusqueda5, nombre2, re.IGNORECASE): #Busca el patrón "gómez" en la cadena nombre2 sin distinguir entre mayúsculas y minúsculas
    print(f'Hemos encontrado el apellido "{patronBusqueda5}" en la cadena nombre2') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en la cadena nombre2') #Devuelve el mensaje
    
#Se suele utilizar la función para texto más largos donde no sabemos dónde puede aparecer la coincidencia.

texto1="En un lugar de La Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
texto2="Había una vez un reino muy lejano donde vivía un valiente caballero que luchaba contra dragones y rescataba princesas."
patronBusqueda6="princesas"
print(f'Buscando la palabra "{patronBusqueda6}" en los textos:')    
if re.search(patronBusqueda6, texto1): #Busca el patrón "princesas" en el texto1
    print(f'Hemos encontrado la palabra "{patronBusqueda6}" en el texto1') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en el texto1') #Devuelve el mensaje
if re.search(patronBusqueda6, texto2): #Busca el patrón "princesas" en el texto2
    print(f'Hemos encontrado la palabra "{patronBusqueda6}" en el texto2') #Devuelve el mensaje
else:
    print(f'No lo hemos encontrado en el texto2') #Devuelve el mensaje

