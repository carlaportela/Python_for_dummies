#Para importar funciones específicas de un módulo (de una en una o varias separadas por comas)
from Mi_primer_paquete.calculos_generales import dividir

dividir(10, 2) # El resultado de la división es: 5.0
dividir(10, 0) # Error: No se puede dividir por cero.

from Mi_primer_paquete.calculos_generales import potencia
potencia(2, 3) # El resultado de la potencia es: 8
potencia(5, 0) # El resultado de la potencia es: 1

#Para importar todo el módulo
from Mi_primer_paquete.calculos_generales import *
raiz_cuadrada(16) # El resultado de la raíz cuadrada es: 4.0
redondear(3.14159) # El número redondeado es: 3
#O también
from Mi_primer_paquete import calculos_generales
calculos_generales.raiz_cuadrada(16) # El resultado de la raíz cuadrada es: 4.0
calculos_generales.redondear(3.14159) # El número redondeado es: 3

#Importar funciones de un subpaquete
from Mi_primer_paquete.Subpaquete_modulos.operaciones_cadenas import unirCadenas, longitudCadena
unirCadenas("Hola", "Mundo")  # Unión de cadenas: Hola Mundo
longitudCadena("Hola Mundo")  # Longitud de la cadena: 10

