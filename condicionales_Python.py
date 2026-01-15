#Sintaxis condicional if
def evaluacion(nota):
    valoracion="aprobado"
    if nota < 5:
        valoracion="suspenso"
    return valoracion

#Es muy importante cuidar la sangría para establecer que está dentro del condicional y que no lo está
print(evaluacion(4)) #Devuelve "suspenso"

#Introducimos nosotros el valor de la nota a través del teclado
print("Programa para evaluar calificaciones academicas\n")
calificacion =input("Introduce la calificación: ")
print(evaluacion (float(calificacion))) #Devuelve "aprobado" o "suspenso" dependiendo de la calificación introducida

#Sintaxis condicional if-else
print("Programa para evaluar calificaciones academicas\n")
nota=float(input("Introduce la calificación: "))
if nota < 5:
        print("suspenso")
else:
        print("aprobado")
print("El programa ha finalizado")

#Sintaxis condicional if-elif-else (Cuando existe más de un if, el else trabaja con el if más cercano; salvo que usemos elif)
print("Programa para evaluar calificaciones academicas\n")
nota=float(input("Introduce la calificación: "))
if nota > 10:
      print("Error: La calificación no puede ser mayor que 10")
elif nota < 5:
        print("suspenso")
else:
        print("aprobado")
print("El programa ha finalizado")

#Sintaxis condicional if-elif-else 
print("Programa para evaluar calificaciones academicas\n")
nota=float(input("Introduce la calificación: "))
if nota<5:
        print("suspenso")
elif nota<6:
        print("Aprobado")
elif nota<7:
        print("Bien")
elif nota<9:
        print("Notable")
elif nota<=10:
        print("Sobresaliente")
else:
        print("Error: La calificación no puede ser mayor que 10")      


#En Python no existe switch-case, pero:
#  - Se puede simular utilizando diccionarios
#  - Concatenación de operadores de comparación
edad=int(input("Introduce la edad: "))
if 0<edad<100:
       print("La edad es correcta")
else:
       print("Error: La edad no puede ser mayor que 100")
       
#  - Operadores lógicos AND y OR
print("Programa de becas 2025")
distancia=int(input("Introduce la distancia a la universidad (en kilómetros): "))
print(distancia)
hermanos=int(input("Introduce el número de hermanos: "))
print(hermanos)
salarioFamiliar=int(input("Introduce el salario familiar: "))
print(salarioFamiliar)
if distancia>40 and hermanos>2 and salarioFamiliar<=20000:
       print("Has sido admitido a las becas 2025")
else:
       print("No has sido admitido a las becas 2025")
#Se pueden concatenar todos los operadores AND y OR que se deseen

print("Programa de becas 2025")
distancia=int(input("Introduce la distancia a la universidad (en kilómetros): "))
print(distancia)
hermanos=int(input("Introduce el número de hermanos: "))
print(hermanos)
salarioFamiliar=int(input("Introduce el salario familiar: "))
print(salarioFamiliar)
if (distancia>40 and hermanos>2) or (salarioFamiliar<=20000):
       print("Has sido admitido a las becas 2025")
else:
       print("No has sido admitido a las becas 2025")

#  - Operador IN
print("Asignaturas optativas 2025:")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
asignatura=input("Introduce la asignatura que deseas optar: ")
if asignatura in ("Informática gráfica", "Pruebas de software", "Usabilidad y accesibilidad"):
       print("Ha seleccionado"+ asignatura)
else:
       print("La asignatura seleccionada no está disponible")

#Case sensitive: Sensible a mayúsculas y minúsculas
#Se puede solventar con las funciones lower() y upper()
print("Asignaturas optativas 2025:")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Introduce la asignatura que deseas optar: ")
asignatura=asignatura.lower() #Convierte la cadena a minúsculas para evaluar todo en minúsculas
if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
       print("Ha seleccionado"+ asignatura)
else:
       print("La asignatura seleccionada no está disponible")
