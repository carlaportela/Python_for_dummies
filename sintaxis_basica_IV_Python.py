#Funciones sin parámetros
def suma():
    num1=5
    num2=7  
    print("La suma de", num1, "y", num2, "es:", num1+num2)

suma()

# Funciones con parámetros
def multiplica(num1, num2):
    print("La multiplicación de", num1, "y", num2, "es:", num1*num2)

multiplica(5, 7)

#Funciones con retorno
def resta(num1, num2):
    return num1-num2
print("La resta de", 5, "y", 7, "es:", resta(5, 7))


