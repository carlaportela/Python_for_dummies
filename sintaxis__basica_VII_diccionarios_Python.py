midiccionario = {"clave1": "valor1", "clave2": "valor2"}
diccionariogeografico = {"México":"Ciudad de México", "Guadalajara":"Monterrey", "Canadá": "Ottawa"}

#Imprimir un valor del diccionario
print(diccionariogeografico["México"])

# Imprimir todas las claves y valores del diccionario
print(midiccionario)
for clave, valor in midiccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Añadir un nuevo par clave-valor al diccionario
diccionariogeografico["Japón"] = "Tokyo"

#Modificar un valor existente
diccionariogeografico["Guadalajara"] = "Ciudad de Guadalajara" #En Python el nuevo valor se sobreescribe el anterior

# Eliminar un par clave-valor del diccionario
del diccionariogeografico["Canadá"]

#Asignación de una tupla como claves al diccionario
mitupla=["España", "Francia", "Alemania"]
diccionariopaises={mitupla[0]: "Madrid", mitupla[1]: "París", mitupla[2]: "Berlín"}
print(diccionariopaises[mitupla[0]])
print(diccionariopaises["España"]) #Se puede acceder mediante la clave del diccionario o el valor de la tupla clave del diccionario

#Asignación de una tupla como valor al diccionario
diccionarionba={23:"Jordan", "Nombre":"Michel", "Apellido":"Jordan", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(diccionarionba[23]) #Se puede acceder mediante la clave del diccionario o el valor de la tupla clave del diccionario
print(diccionarionba["Anillos"]) #Se puede acceder mediante la clave del diccionario a los valores de la tupla

#Guardar un diccionario dentro de otro diccionario
diccionarionba={23:"Jordan", "Nombre":"Michel", "Apellido":"Jordan", "Equipo":"Chicago", "anillos":{[1991,1992,1993,1996,1997,1998]}}
diccionariototal={"Baloncesto":diccionarionba, "Paises":diccionariogeografico}

#Métodos de un diccionario
print(diccionarionba.keys()) #Imprime las claves del diccionario
print(diccionarionba.values()) #Imprime los valores del diccionario
print(diccionarionba.items()) #Imprime las claves y valores del diccionario
print(len(diccionarionba)) #Imprime el número de elementos del diccionario

