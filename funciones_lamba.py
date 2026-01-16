#Funciones lambda en Python --------------------------------------------------------------------------------------
#Una función lambda es una función anónima que se define utilizando la palabra clave "lambda".
#Se utiliza para crear funciones simples y de una sola línea sin necesidad de definir una función completa con "def".

#Función tradicional para calcular el área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

print(area_triangulo(5, 10))  #Salida: 25.0

#Función lambda equivalente
area_triangulo_lambda = lambda base, altura: (base * altura) / 2 #Podemos usar el número de parámetros que necesitemos
#Los dos puntos (:) serían el equivalente al "return" en una función tradicional

print(area_triangulo_lambda(5, 10))  #Salida: 25.0

#No se pueden emplear funciones lambda para operaciones complejas o múltiples líneas de código.
#Son ideales para funciones simples y rápidas, como en el caso de funciones de orden superior.

al_cubo=lambda numero: numero**3 #esta función lambda recibe un único parámetro y devuelve su valor al cubo
al_cubo2=lambda numero: pow(numero,3) #otra forma de definir la misma función usando pow()
print(al_cubo(3))  #Salida: 27
print(al_cubo2(4))  #Salida: 64

destacar_valor= lambda comision: "¡{}€!".format(comision)  #esta función lambda recibe un único parámetro y devuelve una cadena formateada
comision_ANA=1500
print(destacar_valor(comision_ANA))  #Salida: ¡1500€!