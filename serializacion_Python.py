#Primero debemos importar la bibilioteca de Python, Pickle (métodos dump() para volcar datos a archivo binario externo y load() para cargarlo)
import pickle

#Serialización de listas/diccionarios/colecciones ---------------------------------------------------------------------------------------------
#Creamos una lista
lista_nombre=["Pedro", "Ana", "María", "Isabel"]

#Creamos un fichero externo con acceso de escritura binaria
fichero_binario=open("lista_nombres", "wb")

#Volcado de la lista al fichero externo mediante el método dump()
#Recibe dos argumentos: el nombre de la lista/diccionario/colección que deseamos guardar y el archivo en el que lo vamos a guardar
pickle.dump(lista_nombre, fichero_binario)

#Una vez realizado el volcado, cerramos el fichero con el método close()
fichero_binario.close()

#Una vez guardada la lista en el fichero externo, incluso podríamos borrar la lista para liberar memoria con el método del()
del(fichero_binario)

#Vamos intentar rescatar la información del fichero binario
#Para ello creamos una nueva lista con permiso de lectura binaria
fichero_carga=open("lista_nombres", "rb")

#Creamos una variable lista para guardar la información del archivo externo
lista_cargada_nombre=pickle.load(fichero_carga)
fichero_carga.close()

print(lista_cargada_nombre)

#Serialización de objetos ---------------------------------
#Declaramos clase, constructores y métodos

class Coche():
    
    def __init__(self, marca="desconocida", modelo="desconocido", color="desconocido"):
        self.__largoChasis = 250  #Atributo privado, no se puede acceder desde fuera de la clase
        self.__anchoChasis = 120  #Atributo privado, no se puede acceder desde fuera de la clase
        self.__ruedas = 4  #Atributo privado, no se puede acceder desde fuera de la clase
        self.__enmarcha = False #Estado del coche, por defecto es False (apagado). Estado inicial
        self.marca = marca
        self.modelo = modelo
        self.color = color
        print(f"Se ha creado un coche {self.marca} {self.modelo} de color {self.color}.")

    def estado(self):
        print(f"Coche {self.marca} {self.modelo} de color {self.color}.")

#Creamos varios objetos de la clase Coche
coche1=Coche("Mazda", "MX5")
coche2=Coche("Seat", "Ibiza")
coche3=Coche("Renault", "Megane")

#Los metemos en una colección
coches=[coche1,coche2,coche3]

#Creamos el fichero para serializar la colección
fichero=open("Coches", "wb")

#Volcamos la información en este fichero, cerramos el fichero y lo borramos de la memoria
pickle.dump(coches,fichero)
fichero.close()
del(fichero)

#Ahora vamos a realizar el paso inverso que es a partir de un fichero externo, rescatar la información
fichero_apertura=open("Coches", "rb")

#Creamos una variable donde cargar la información del fichero experto
coches_cargados=pickle.load(fichero_apertura)
fichero_apertura.close()

#Mostramos la información cargada del fichero externo en la variable "coches_cargados"
for coche in coches_cargados:
    print (coche.estado())

#Para que pueda leer un objeto de una determinada clase es necesario que esa clase este definida en el archivo en el que se realiza la serialización
#o que se importe dicha clase.



    
    





