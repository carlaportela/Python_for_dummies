#Creación de clase padre o superclase
class Vehiculos():
    
    #Constructor de la clase Vehiculos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        print("Se ha creado un vehículo",self.marca, self.modelo)
        
    #Comportamientos de la clase:
    def arrancar(self):
        self.enmarcha = True
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")
        
    def acelerar(self):
        self.acelera = True
        print(f"El vehículo {self.marca} {self.modelo} está acelerando.")
    
    def frenar(self):
        self.frena = True
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")
    
    #Estado del vehículo
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
    

#Creación de clase hija que hereda de Vehiculos
class Furgoneta(Vehiculos):
    capacidadCarga = 0  #Atributo específico de la clase Furgoneta
    cargada = False
    cargaActual = 0  #Atributo para la carga actual
    
    #Constructor de la clase Furgoneta
    def __init__(self, marca, modelo, carga):
        super().__init__(marca, modelo)  #Llamada al constructor de la clase padre Vehiculos
        self.capacidadCarga = carga
        print(f"Se ha creado una furgoneta {self.marca} {self.modelo} con capacidad de carga {self.capacidadCarga} kg.")
    
    #Sobrescritura del método estado para incluir la capacidad de carga
    def estado(self):
        super().estado()  #Llamada al método estado de la clase padre Vehiculos
        print("Capacidad de carga: ", self.capacidadCarga, "kg")
        
    #Comportamientos específicos de la clase Furgoneta
    def cargar(self, carga):
        self.cargaActual = int(carga)
        self.cargada = True
        print(f"La furgoneta {self.marca} {self.modelo} está cargando {self.cargaActual} kg.")
    
        
class Moto(Vehiculos):
    hacerCaballito = False  #Atributo específico de la clase Moto
    
    #Constructor de la clase Moto
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  #Llamada al constructor de la clase padre Vehiculos
        self.tipo = tipo
        print(f"Se ha creado una moto {self.marca} {self.modelo} de tipo {self.tipo}.")
    
    #Comportamientos específicos de la clase Moto
    def hacerCaballito(self):
        if self.enmarcha:
            self.hacerCaballito = True
            print(f"La moto {self.marca} {self.modelo} está haciendo un caballito.")
        else:
            print("La moto debe estar en marcha para hacer un caballito.")

    #Sobrescritura del método estado para incluir el tipo de moto
    def estado(self):
        super().estado()  #Llamada al método estado de la clase padre Vehiculos
        print("Tipo de moto: ", self.tipo)


    
#Creación de instancia de la clase Moto
miMoto = Moto("Yamaha", "MT-07", "Deportiva") #Se hereda el constructor de Vehiculos
miMoto.arrancar()  #Se heredan los métodos de Vehiculos
miMoto.acelerar()  
miMoto.hacerCaballito()
miMoto.estado()  

#Creación de instancia de la clase Furgoneta
miFurgoneta = Furgoneta("Mercedes", "Sprinter", 1200)  #Se hereda el constructor de Vehiculos
miFurgoneta.arrancar()  #Se heredan los métodos de Vehiculos
miFurgoneta.cargar(800)  #Método específico de Furgoneta
miFurgoneta.estado()  #Se hereda el método estado de Vehiculos

#miMoto.cargar(500)  #Da error. Ya que aunque ambas clases heredan de Vehiculos, no tienen relación directa entre ellas.
#Una furgoneta puede cargar, pero una moto no.

#Herencia múltiple
class Electricos():
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)  #Llamada al constructor de la clase padre Vehiculos
        self.autonomia = 100  #Atributo específico de la clase Electricos
        self.cargando = False 
    def recargar(self):
        self.cargando = True
        print("El vehículo eléctrico está recargando.")
    
        
class BicicletaElectrica(Vehiculos, Electricos): #Heredan métodos y caracteristicas de ambas clases
    def estado(self):
        super().estado()  #Llamada al método estado de la clase padre Vehiculos
        print("Autonomía: ", self.autonomia, "km")

miBiciElectrica = BicicletaElectrica("Giant", "Explore E+")  #Se hereda el constructor de Vehiculos por encontrarse primero en el orden de argumentos de la clase BicicletaElectrica
miBiciElectrica.autonomia = 150  #Hereda el atributo específico de Electricos
miBiciElectrica.arrancar()  #Se heredan los métodos de Vehiculos
miBiciElectrica.recargar()  #Se heredan los métodos de Electricos
miBiciElectrica.estado()  #Se hereda el método estado de Vehiculos      
