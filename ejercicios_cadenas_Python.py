#Ejercicio 1
#Crea un programa que pida introducir una dirección de email por teclado. 
# El programa debe imprimir en consola si la dirección de email es correcta o no en función de si esta tiene el símbolo ‘@’. 
# Si tiene una ‘@’ la dirección será correcta. 
# Si tiene más de una o ninguna ‘@’ la dirección será errónea. 
# Si la ‘@’ está al comienzo de la dirección de email o al final, la dirección también será errónea

def es_email_valido():
    print("Programa para validar una dirección de email")
    email = input("Introduce una dirección de email: ")
    if "@" in email: #Comprobamos que contiene '@'
        if email.count("@") == 1: #Comprobamos que solo tiene una '@'
            if email.startswith("@") or email.endswith("@"): #Comprobamos que no empieza o termina con '@'
                print("La dirección de email " + email + " es errónea: la '@' no puede ir al comienzo o al final.")
            else:
                print("La dirección de email "+ email + " es correcta.")
        elif email.count("@") > 1: #Comprobamos que no tiene más de una '@'
            print("La dirección de email " + email + " es errónea: tiene más de una '@'.")
    else: #Si no contiene '@'
        print("La dirección de email " + email + " es errónea: no contiene '@'.")

es_email_valido()

    
    