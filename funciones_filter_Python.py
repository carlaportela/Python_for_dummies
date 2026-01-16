#Funciones filter: funciones de uso superior que reciben otra función como argumento y devuelven un iterable filtrado.
#Comprueba que unos elementos de una lista cumplen una condición determinada.

#Definimos una función que verifica si un número es par
def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

#Definimos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Usamos la función filter para filtrar los números pares de la lista
print(filter(es_par, numeros))  #Usamos la función filter para llamar a la función es_par y filtrar los números pares de la lista
#La función funciona pero no se ve el resultado ya que esta función devuelve un objeto filter, por lo que debemos convertirlo a una lista para ver los resultados
numeros_pares = list(filter(es_par, numeros))  #Convertimos el objeto filter a una lista
print(numeros_pares)  #Imprimimos la lista de números pares

#Podríamos resumir lo anterior en una sola línea
print(list(filter(es_par, numeros)))  #Usamos la función filter y convertimos el resultado a una lista en una sola línea

#También podríamos resumirlo usando una función lambda
numeros_pares_lambda = list(filter(lambda x: x % 2 == 0, numeros))  #Usamos una función lambda para filtrar los números pares de la lista
print(numeros_pares_lambda)  #Imprimimos la lista de números pares obtenida
#Podríamos resumirlo en una sola línea
print(list(filter(lambda x: x % 2 == 0, numeros)))  #Usamos una función lambda y convertimos el resultado a una lista en una sola línea

#Otra forma de hacerlo es usando una lista por comprensión
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return f"{self.nombre} trabaja como {self.cargo} y tiene un salario de {self.salario}"

#Creamos una lista de empleados
listaEmpleados=[
    #Creamos empleados
    Empleado("Juan", "Director", 7500),
    Empleado("Ana", "Presidente", 8500),
    Empleado("Antonio", "Administrativo", 2500),
    Empleado("Maria", "Secretaria", 2700),
    Empleado("Mario", "Botones", 1500)
]

#Filtramos los empleados que ganan más de 3000 usando filter
salarios_altos = list(filter(lambda empleado: empleado.salario > 3000, listaEmpleados))
for empleado_salario in salarios_altos:
    print(empleado_salario)
        