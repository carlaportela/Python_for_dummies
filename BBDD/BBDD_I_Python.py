#Sistemas de gestión de bases de datos: --------------------------------------------------------------------------------------------------------------------------------
#MySQL, PostgreSQL, SQLite, MongoDB, etc.
#SQLite es un sistema de gestión de BBDD relacional, escrita en C, de código abierto y se guarda como único archivo en host.
#Es una librería que implementa un motor de base de datos SQL embebido, es decir, no necesita un servidor independiente.
#Ventajas: Ocupa poco espacio en disco y memoria, es rápido, multiplataforma y es de dominio público (gratis)
#Inconvenientes: no admite clausulas anidadas (where), no permite acceso simultaneo por varios usuarios y falta de clave foranea cuando se crea en modo consola.

#Pasos a seguir para conectar con BBDD SQLite desde Python: ------------------------------------------------------------------------------------------------------------
#1. Abrir/Crear conexión con la BBDD
#2. Crear cursor/puntero
#3. Ejecutar consultas SQL(Query)
#4. Recuperar resultados (si los hay): Insertar, leer, actualizar, borrar (CRUD)
#5. Cerrar cursor/puntero
#6. Cerrar conexión con la BBDD

#Traducción a código Python: ----------------------------------------------------------------------------------------------------------------
#Importar librería sqlite3
import sqlite3

#1.Abrir/Crear conexión con la BBDD (si no existe, la crea)
myConnection = sqlite3.connect("D:\Ciclo Desarrollo Web\Curso_Python\BBDD\MyDatabase") #Como argumento se pasa el nombre del archivo de la BBDD

#2.Crear cursor/puntero
myCursor = myConnection.cursor() #El cursor permite ejecutar sentencias SQL y recuperar resultados

#3.Ejecutar consultas SQL(Query)
#Crear tabla
myCursor.execute("CREATE TABLE IF NOT EXISTS empleados (nombre VARCHAR(100), sueldo INTEGER)")

#Descargamos Visor SQLite para visualizar la BBDD creada

#Insertar datos
myCursor.execute("INSERT INTO empleados VALUES ('Juan', 3000)")
myCursor.execute("INSERT INTO empleados VALUES ('Ana', 3500)")
myCursor.execute("INSERT INTO empleados VALUES ('Pedro', 2800)")

severalWorkers = [ #Para insertar un conjunto de datos utilizamos tuplas y listas
    ('Marta', 3200),
    ('Lucia', 4000),
    ('Javier', 2900)
]
myCursor.executemany("INSERT INTO empleados VALUES (?, ?)", severalWorkers) #Se insertan tantos interrogantes como parametros tenga la tupla

#Leer datos
myCursor.execute("SELECT * FROM empleados") #Selecciona todos los campos de la tabla empleados
result = myCursor.fetchall() #Recupera todos los registros de la consulta y los guarda en una lista
print(result) #Muestra la lista completa

for worker in result: #Recorre la lista y muestra cada registro por separado
    print(worker)
    
#Actualizar datos
myCursor.execute("UPDATE empleados SET sueldo = 3500 WHERE nombre = 'Lucia'") #Actualiza el sueldo del empleado con dni 34567890C  
myConnection.commit() #Confirma los cambios en la BBDD
print("Sueldo actualizado")

#Confirmamos los cambios en la BBDD
myConnection.commit()


#Cerrar conexión con la BBDD
myConnection.close()

