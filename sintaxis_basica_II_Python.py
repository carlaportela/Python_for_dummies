#Operadores aritméticos
suma=5+6
print(suma)
modulo=5%3
print(modulo)
exponente=2**3
print(exponente)
division_entera=9//2
print(division_entera)

#Declaración de variables
nombre="Juan"
apellido="Perez"
edad=30
print(nombre, apellido, edad)

#En Python, el tipo de variable no la establece el contenedor sino el contenido; y toda variable es un objeto (Class
#La función type() devuelve el tipo de un objeto/variable
print(type(nombre))
#Nos devuelve <class 'str'> para nombre

#""" sirve para incluir saltos de línea en un texto largo
comentario_multilinea = """
Este es un
comentario
multilínea
"""
print(comentario_multilinea)

#Operadores de comparación y condicionales
numero1=5
numero2=7
if numero1 > numero2:
    print("El número 1 es mayor que el número 2")
else:
    print("El número 2 es mayor que el número 1")

