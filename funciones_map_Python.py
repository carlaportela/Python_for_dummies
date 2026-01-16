#Función map: Aplica una función a cada elemento de una lista iterable y devuelve una lista con los resultados.
class Worker:
    def __init__(self, name, cargo, salary):
        self.name = name
        self.cargo = cargo
        self.salary = salary

    def __str__(self):
        return f"{self.name} trabaja como {self.cargo} y tiene un salario de {self.salary}€"

#Creamos una lista de empleados
workerList=[
    #Creamos empleados
    Worker("Juan", "Director", 7500),
    Worker("Ana", "Presidente", 8500),
    Worker("Antonio", "Administrativo", 2500),
    Worker("Maria", "Secretaria", 2700),
    Worker("Mario", "Botones", 1500)
]

#Vamos a crear una función que calcule la comisión de cada empleado
def calculateCommission(worker):
    worker.salary = int(worker.salary * 1.10) #Devuelve el salario con un 10% más
    return worker

#Usamos la función map para aplicar la función calculateCommission a cada empleado de la lista
workerListCommission = map(calculateCommission, workerList)

#Mostramos los resultados
for worker in workerListCommission:
    print(worker)