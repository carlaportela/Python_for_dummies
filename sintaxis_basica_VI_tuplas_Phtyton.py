#Son listas inmutables; se pueden extraer porciones (da como resultado una tupla nueva)
#Sintaxis de tuplas
mitupla = (1, 2, 3, 4, 5) #Se pueden obviar los paréntesis (Recomendable usarlos)

#Acceso a un elemento de la tupla
print(mitupla[1])

#Acceso a un rango de elementos de la tupla
print(mitupla[1:3]) #Última posición excluida

#Conversión de tupla a lista
milista = list(mitupla)

#Conversión de lista a tupla
mitupla2 = tuple(milista)

#Comprobar si existe un elemento en una tupla
print(1 in mitupla) #Devuelve True

#Contar el número de elementos en una tupla
print(mitupla.count(1)) #Devuelve 1

#Contar la longitud de una tupla
print(len(mitupla)) #Devuelve 5

#Tupla unitaria
tuplaunitaria = (1,)

#Empaquetado en una tupla
mitupla="Juan",13,1,1995

#Desempaquetado en una tupla
mitupla=("Juan",13,1,1995)
nombre, dia, mes, agno=milista
print(nombre, dia, mes, agno) #Devuelve Juan 1 1 1995

#No se puede agregar un elemento a una tupla con añadir() o append






