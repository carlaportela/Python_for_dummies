#Importamos la librería pickle
import pickle

#Creamos una clase
class Persona:
    
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con nombre", self.nombre)
        
    def __str__(self): #Este método nos devuelve un string con los atributos de cada objeto
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

#Creamos una clase para guardar objetos Persona en una lista
class ListaPersonas:
    
    personas=[] #Creamos una lista
    
    #Reamos un constructor que al instanciar un objeto de esta clase, además de crear la correspondiente lista
        #vaya guardando los datos en un archivo externo
    def __init__(self):
        
        #Creo una variable que se encargará de crear el fichero externo, con permiso para agregar información binaria
        listadePersonas=open("ficheroPersonas", "ab+")
        #Y desplazamos el cursor a la primera posición
        listadePersonas.seek(0)
        #Volcamos la información mediante la lista personas creada
        #Si es la primera vez que instanciamos, la primera vez no se van a añadir personas, por ello utilizamos un bloque try
        try:
            self.personas=pickle.load(listadePersonas)
            print("Se cargaron {} personas al fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally: #Estas sentencias se ejecuten siempre
            #Cerramos el archivo externo y borramos la variable con la que lo hemos abierto
            listadePersonas.close()
            del(listadePersonas)
           
    
    def agregarPersonas(self, p): #Método para agregar objetos Persona a la lista
        self.personas.append(p)
        #Una vez guardados los objetos en la lista, llamamos al método que guardará dichos objetos en el archivo externo
        self.guardarPersonasEnFicheroExterno()
        
    def mostrarPersonas(self):
        for p in self.personas:
            print("La información de la lista es:", p)
    #Creamos un método que añada personas al archivo externo desde la lista de personas
    def guardarPersonasEnFicheroExterno(self):
        #Abre el fichero externo con permiso para escribir en binario
        listaDePersonas=open("ficheroPersonas", "wb")
        #Volcamos toda la anformación de la lista personas en el fichero externo (Pueden ser uno o varios objetos Persdona)
        pickle.dump(self.personas, listaDePersonas) 
        #Una vez realizado el volcado, cerramos el archivo externo y borramos la variable con la que lo hemos abierto
        listaDePersonas.close()
        del(listaDePersonas)
        
    #Método para ver los objetos Persona que se han cargado en el fichero externo
    def mostrarInforFicheroExterno(self):
        print("La información del fichero externo es:")
        for persona in self.personas:
            print(persona)
#Instanciamos un objeto de clase ListaPersonas
miLista=ListaPersonas()

#Instanciamos objetos
persona=Persona("Sandra", "Femenino", 29)

#Agregamos un objeto de Persona a la lista que hemos creado
miLista.agregarPersonas(persona)

#Mostramos el contenido de la lista
miLista.mostrarPersonas()

#Mostramos la información guardada en el fichero externo
miLista.mostrarInforFicheroExterno()

#Agregamos mas instancias de Persona y las subimos al fichero externo
persona=Persona("Antonio", "Masculino", 46)
miLista.agregarPersonas(persona)
persona=Persona("Ana", "Femenino", 35)
miLista.agregarPersonas(persona)

#Visualizamos que las nuevas instancias se hayan cargado
miLista.mostrarInforFicheroExterno()






