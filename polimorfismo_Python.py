#Polimorfismo:
#Permite que diferentes clases implementen el mismo método de manera diferente.

class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
        
#Creamos un objeto de cada clase y llamamos al método desplazamiento
        
miVehiculo1 = Moto()
miVehiculo1.desplazamiento() #Se desplaza utilizando dos ruedas

miVehiculo2 = Coche()
miVehiculo2.desplazamiento() #Se desplaza utilizando cuatro ruedas

miVehiculo3 = Camion()
miVehiculo3.desplazamiento() #Se desplaza utilizando seis ruedas

#Polimorfismo en una función
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)  #Le pasamos como parámetro un objeto

