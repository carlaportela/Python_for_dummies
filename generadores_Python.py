#Sintaxis de generador de pares a partir de una función
def generaPares(limite):
    numero=1
    miLista=[]
    while numero<limite:
        miLista.append(numero*2)
        numero+=1
    return miLista

print(generaPares(10))

#A partir de la función anterior, implementamos un generador
def generaParesGenerador(limite):
    numero=1
    #No necesitamos almacenar los valores en una lista
    while numero<limite:
        yield numero*2 #Con esta instrucción (yield) cada valor se almacena en el generador
        numero+=1

devuelvePares=generaParesGenerador(10) #Guardamos en la variable devuelvePares el objeto iterable creado por el generador
#for par in devuelvePares: #Creamos un bucle para recorrer los valores devueltos por el generador
    #print(par)

#Con el método next() podemos obtener cada valor del generador, en lugar de usar un bucle for
print(next(devuelvePares)) #Devuelve los valores de uno en uno
print("Aquí habría más código... Continuaría el programa")
print(next(devuelvePares)) #Y nos devuelve el siguiente valor
print("Aquí habría más código... Continuaría el programa")
print(next(devuelvePares)) #Y nos devuelve el siguiente valor
    #De esta manera nos devuelve los tres primeros valores del generador
    #Entre llamada y llamada, el generador se encuentra en estado de suspensión, esperando que se llame

#yield from se utiliza para simplificar código en caso de bucles anidados (arrays de dos dimensiones, acceso a subelementos)
def generaElementos(limite): #Implementamos un generador de elementos
    for elemento in range(limite):
        yield elemento

elementos=generaElementos(10) #Guardamos en la variable elementos el objeto iterable creado por el generador

def generaSubelementos(): #Implementamos un generador que extrae de cada elemento los subelementos anidando dos bucles for
    for elemento in elementos:
        for subelemento in elemento:
            yield elemento*subelemento

subelementos=generaSubelementos()

#Ahora utilizamos yield from para simplificar el código
def devuelveCiudades(*ciudades): #El asterisco delante del argumento indica que va a proporcionarse un número indeterminado de argumentos en forma de tupla
    for ciudad in ciudades:
        yield ciudad

ciudades=devuelveCiudades("Madrid", "Barcelona", "London", "Paris")

print(next(ciudades)) #Devuelve solo Madrid

 #Para acceder a las letras de cada ciudad utilizamos un bucle for
def devuelveLetrasCiudades(*ciudades):
    for ciudad in ciudades:
        #for letra in ciudad:
        yield from ciudad 
            #yield letra

letras=devuelveLetrasCiudades("Madrid", "Barcelona", "London", "Paris")

print(next(letras)) #Devuelve M
print(next(letras)) #Devuelve a