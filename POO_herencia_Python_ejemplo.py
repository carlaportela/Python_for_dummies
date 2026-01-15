class Persona():
    
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Lugar de residencia: {self.residencia}")
        
class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} \nAntigüedad: {self.antiguedad} años")

antonio = Persona("Antonio", 30, "Madrid")
antonio.descripcion()
maria = Empleado(3000, 5, "María", 28, "Barcelona")
maria.descripcion()

#Principio de sustitución: una instancia de una subclase es siempre una instancia de la superclase; pero no al revés
#Este principio se usa para comprobar que una herencia se ha creado correctamente
#Se comprueba mediante isinstance()
print(isinstance(maria, Persona))  # True
print(isinstance(antonio, Empleado))  # False Un empleado no siempre es una persona
print(isinstance(maria, Empleado))  # True

