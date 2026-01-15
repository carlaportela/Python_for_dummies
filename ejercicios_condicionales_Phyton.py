#Ejercicio 1
#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.
def DevuelveMax(num1, num2):
    if num1>num2:
        print("El número más alto es:", num1)
    elif num2>num1:
        print("El número más alto es: " +str(num2))
    else:
        print("Los números son iguales")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
DevuelveMax(num1, num2)

#Ejercicio 2
#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).
listaContactos=[]
def guardarContactos():
    print("---Lista  de contactos ---")
    nombre=input("Introduce el nombre: ")
    apellido=input("Introduce el apellido: ")
    telefono=input("Introduce el teléfono: ")
    listaContactos.append([nombre, apellido, telefono])
    print("Los datos personales son:", nombre, apellido, telefono)

guardarContactos()
print("Total de contactos:", len(listaContactos))
print("Contactos:", listaContactos)

#Ejercicio 3
#Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos.
def mediaAritmetica():
    print("--- Programa para calcular la media aritmética ---")
    num1=float(input("Introduce el primer número: "))
    num2=float(input("Introduce el segundo número: "))
    num3=float(input("Introduce el tercer número: "))
    media=(num1+num2+num3)/3
    print("La media aritmética es:", media)

mediaAritmetica()