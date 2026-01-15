#En Python se pueden alamacenar diferentes tipos de datos en la misma lista
#Declaración de listas
miLista=["María", "Pedro", "Juan"]

#Impresión de la lista
print(miLista[:])

#Acceso a un elemento de la lista
print(miLista[1])

#Acceso a un rango de elementos de la lista
print(miLista[1:3]) #Última posición excluida
print(miLista[:3]) #Si se omite el inicio, se toma desde el 0
print(miLista[2:]) #Si se omite el final, se toma hasta el último

#Agregar un elemento a la lista
miLista.append("Marco") #Lo agrega al final de la lista
miLista.insert(1, "José") #Lo agrega en la posición indicada
miLista.extend(["Ana", "Antonio"]) #Agrega varios elementos al final de la lista

#Conocer el índice de un elemento
print(miLista.index("Pedro")) #Devuelve el índice del primer elemento encontrado

#Comprobar si un elemento está en la lista
print("María" in miLista) #Devuelve True si el elemento está en la lista

#Remover un elemento de la lista
miLista.remove("Pedro") #Remueve el primer elemento encontrado
miLista.pop(1) #Remueve el elemento en la posición indicada

#sumar diferentes listas
miLista2=["Luis", "Sofía"]
miLista3=miLista+miLista2
print(miLista3)

#Repetir lista
print(miLista*3)


