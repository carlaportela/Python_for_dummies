#Ejercicio 1
#Crea un programa que muestre los números impares del 1 al 100. Los números deberán aparecer una al lado del otro sin salto de línea.
def mostrar_numeros_impares():
    for i in range(100):
        if i%2 != 0:
            print(i, end=" ")

mostrar_numeros_impares()

#Ejercicio 2
#Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña errónea”
def validar_contrasena():
    contrasena_input = input("Introduce una contraseña: ")
    contador_caracteres=0
    contador_espacios=0
    for i in contrasena_input:
        contador_caracteres += 1
        if i == " ":
            contador_espacios += 1
    if contador_caracteres>=8 and contador_espacios==0:
        print("La contraseña es correcta")
    elif contador_caracteres<8 and contador_espacios==0:
        print("La contraseña es incorrecta ya que sólo tiene", contador_caracteres, "caracteres")
    elif contador_caracteres<8 and contador_espacios==1:
        print("La contraseña es incorrecta ya que sólo tiene", contador_caracteres, "caracteres y", contador_espacios, "espacio en blanco")
    elif contador_caracteres<8 and contador_espacios>1:
        print("La contraseña es incorrecta ya que sólo tiene", contador_caracteres, "caracteres y", contador_espacios, "espacio en blanco")
    else:
        print("La contraseña es incorrecta ya que tiene", contador_espacios, "espacio en blanco")

validar_contrasena()

#Ejercicio 3
#Crea un programa que evalúe si una dirección de correo electrónico es válida o no en función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera correcta si solo tiene una “@” y si tiene uno o más “.”
def validar_correo():
    correo_input = input("Introduce una dirección de correo electrónico: ")
    contador_arroba=0
    contador_punto=0
    for i in correo_input:
        if i == "@":
            contador_arroba += 1
        elif i == ".":
            contador_punto += 1
    if contador_arroba==1 and contador_punto>0:
        print("La dirección de correo electrónico es válida")
    else:
        print("La dirección de correo electrónico es inválida")

validar_correo()
