#Creación de una clase en Python ----------------------------------------------------------------------------
class Coche():
    #Atributos/Propiedades comunes a todos los objetos de la clase:
        #largoChasis = 250 
        #anchoChasis = 120
        #ruedas = 4 
        #enmarcha = False 
    #Todos eestos atributos podemos meterlos en el contructor, pero no es obligatorio
    
    #Constructor (se ejecuta al crear un objeto de la clase y le proporciona su estado inicial):
    def __init__(self, marca="Desconocida", modelo="Desconocido", color="Desconocido"):
        self.__largoChasis = 250  #Atributo privado, no se puede acceder desde fuera de la clase
        self.__anchoChasis = 120  #Atributo privado, no se puede acceder desde fuera de la clase
        self.__ruedas = 4  #Atributo privado, no se puede acceder desde fuera de la clase
        self.__enmarcha = False #Estado del coche, por defecto es False (apagado). Estado inicial
        self.marca = marca
        self.modelo = modelo
        self.color = color
        print(f"Se ha creado un coche {self.marca} {self.modelo} de color {self.color}.")

    #Metodos/Comportamientos de la clase (Funciones dentro de la clase):
    def estado(self):
        if self.__enmarcha:
            return "El coche está en marcha."
        else:
            return "El coche está detenido."
    
    def estadoCompleto(self):
        print("El coche tiene ", self.__ruedas, " ruedas, un largo de ", self.__largoChasis, " cm y un ancho de ", self.__anchoChasis, " cm.")
    
    def arrancar(self): #self hace referencia al objeto que llama al método. PRIMER PARÁMETRO OBLIGATORIO
        self.__enmarcha = True
        if self.__enmarcha:
            print(f"El coche {self.marca} {self.modelo} está arrancando.")

    def detener(self):
        self.__enmarcha = False
        print(f"El coche {self.marca} {self.modelo} se ha detenido.")
    
    #Encapsulación de atributos ----------------------------------------------------------------------
        #__nombreAtributo = valor
        #__nombreAtributo es privado y no se puede acceder directamente desde fuera de la clase.
        #Si intentamos modificarlo o acceder a él desde fuera, no se modificará el atributo original.
        #Para acceder a estos atributos privados, se deben crear métodos dentro de la clase que permitan su acceso o modificación.
        #Por ejemplo, para modificar el número de ruedas del coche, podemos crear un método específico
    def modificaRuedas(self,nuevasRuedas):
        self.__ruedas = nuevasRuedas
        
    #Encapsulación de métodos ----------------------------------------------------------------------
        #Los métodos también pueden ser privados, lo que significa que no se pueden llamar desde fuera
        #de la clase. Se definen con un nombre que comienza con dos guiones bajos (__).
        #No tiene sentido que se realice un chequeo interno si el coche no está en marcha, pero se ha implementado para mostrar el concepto de encapsulación y métodos privados.
        #Si no está encapsulado el método chequeo interno, se le puede llamar desde fuera de la clase.
        #miCoche2.chequeoInterno()  
        #Para evitarlo encapsulamos el método chequeoInterno, de modo que no se pueda llamar desde fuera de la clase.
        #Y accederemos a él únicamente desde otros métodos de la clase, como arrancarConChequeo.   
    def __chequeoInterno(self):
        print("Realizando chequeo interno del coche")
        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"
        
        if(self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas"):
            print("Chequeo interno completado con éxito.")
            return True
        else:
            print("Chequeo interno fallido.")
            return False
        #A este método se le llamaría justo antes de arrancar el coche
        
    def arrancarConChequeo(self):
        self.__enmarcha = True  #Intentamos arrancar el coche
        if (self.__enmarcha):
            chequeo = self.__chequeoInterno()  #Llamada al método privado de chequeo interno
        if self.__enmarcha and chequeo:
            print(f"El coche {self.marca} {self.modelo} está en marcha.")
        elif self.__enmarcha and not chequeo: #||chequeo == False
            print(f"El coche {self.marca} {self.modelo} no puede arrancar debido a un fallo en el chequeo interno.")
        else:
            print("El coche está apagado")
            
#Creación de instancias ------------------------------------------------------------------------------
#nombreObjeto = Objeto("parametro1", "parametro2", "parametro3"):
miCoche = Coche("Toyota", "Corolla", "Azul")  #No se emplea el operador new como en otros lenguajes

#Acceso a los atributos públicos del objeto:
print("Modelo: " + miCoche.modelo)
print("Color: " + miCoche.color)
print("Marca: " + miCoche.marca)

#Llamada a los métodos públicos del objeto:
print(miCoche.estado())
print(miCoche.arrancar()) 
print(miCoche.estado())
print(miCoche.detener())
print(miCoche.estado())

#Creación de una segunda instancia de la clase Coche:
miCoche2 = Coche("Honda", "Civic", "Rojo") #NO puede haber dos objetos con el mismo nombre, se debe usar otro nombre de variable
print("Modelo: " + miCoche2.modelo)
print("Color: " + miCoche2.color)
print("Marca: " + miCoche2.marca)

#Intento de acceso y modificación de atributos privados desde fuera de la clase.
miCoche2.__ruedas = 5  #La modificación no tendrá efecto, ya que __ruedas es un atributo privado.

#Visualizamos el estado completo de ambos coches:
print(miCoche.estadoCompleto())
print(miCoche2.estadoCompleto()) 

#Acceso y modificación de atributos privados mediante métodos de la clase:
miCoche2.modificaRuedas(5)  #Modificamos el número de ruedas del coche 2
print(miCoche2.estadoCompleto())  #Visualizamos el estado completo del coche 2 tras la modificación

#Acceso a métodos privados de la clase mediante métodos públicos:
miCoche2.arrancarConChequeo()  #El método público accede al método privado __chequeoInterno
miCoche2.estado()



