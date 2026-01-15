#Función format: Permite dar formato, concatenar cadenas...

print ("{} {} {}".format(var1, var2, var3))

#Versión 3.6 - f-strings

print (f"{var1} {var2} {var3}")

#Ventajas f-strings:
    # - Son más legibles.
    # - Son más concisas.
    # - Las {} tienen soporte para expresiones complejas: cálculos, funciones, métodos (sin definir variables adicionales)

x, y = 10, 20
print(f"La suma de {x} y {y} es {x+y}.")

    # - Son máseficientes: el código se ejecuta con mayor rapidez. Lo podemos medir mediante timeit

import timeit

nombre = "Juan"
edad = 30

calculo_f_string = timeit.timeit('f"Hola {nombre} tienes {edad} años."', globals=globals(), number=1000000)

calculo_format = timeit.timeit('"Hola {} tienes {} años.".format(nombre, edad)', globals=globals(), number=1000000)

print(f"Tiempo usando f-strings: {calculo_f_string} segundos.")
print(f"Tiempo usado con método format: {calculo_format} segundos.")

    # - Son más directas con especificaciones de formato.
    

