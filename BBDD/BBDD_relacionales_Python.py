#Las bases de datos relacionales contienen un campo clave primaria (Primary Key) que identifica de forma única cada fila de una tabla.
#Creación de campo clave primaria en SQLite:

#Importar librería sqlite3
import sqlite3

#1.Abrir/Crear conexión con la BBDD (si no existe, la crea)
myConnection = sqlite3.connect("D:\Ciclo Desarrollo Web\Curso_Python\BBDD\MyRelationalDatabase") #Como argumento se pasa el nombre del archivo de la BBDD

#2.Crear cursor/puntero
myCursor = myConnection.cursor() #El cursor permite ejecutar sentencias SQL y recuperar resultados

#3.Ejecutar consultas SQL(Query)
myCursor.execute("CREATE TABLE IF NOT EXISTS empleados (dni VARCHAR(9) PRIMARY KEY, nombre VARCHAR(100), sueldo INTEGER)")
#Por convención, los campos clave primaria se suelen llamar ID, y si queremos que se gestionen sólos debemos añadir AUTOINCREMENT después de PRIMARY KEY
#ID INTEGER PRIMARY KEY AUTOINCREMENT p.e.

#En este caso, el campo "dni" es la clave primaria de la tabla "empleados", lo que significa que cada valor en este campo debe ser único y no nulo.

#4.Introducir datos
workers = [
    ('12345678A', 'Juan', 3000),
    ('23456789B', 'Ana', 3500),
    ('34567890C', 'Pedro', 2800),
    ('45678901D', 'Marta', 3200),
    ('56789012E', 'Lucia', 4000),
    ('67890123F', 'Javier', 2900)
]
myCursor.executemany("INSERT INTO empleados VALUES (?, ?, ?)", workers) #Se insertan tantos interrogantes como parametros tenga la tupla
#En caso de que el campo clave primaria sea AUTOINCREMENT, se puede omitir en la inserción de datos:
#myCursor.executemany("INSERT INTO empleados VALUES (NULL, ?, ?)", workers) NULL indica que el valor lo genera SQLite

#5.Confirmamos los cambios en la BBDD
myConnection.commit()

#Si introducimos un valor duplicado en el campo clave primaria, se genera un error de tipo UNIQUE
myCursor.execute("INSERT INTO empleados VALUES ('12345678A', 'Carlos', 3100)") #Error UNIQUE constraint failed: empleados.dni

#6.Cerrar conexión con la BBDD
myConnection.close()

