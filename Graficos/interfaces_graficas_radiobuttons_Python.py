from tkinter import *

root=Tk()

#Creamos una variable a la que le asignaremos el valor de la opcion seleccionada
option=IntVar()

#Creamos una funcion que nos muestre el valor seleccionado
def printOption():
    if option.get()==1:
        result.config(text="Has seleccionado masculino")
    else :
        result.config(text="Has seleccionado femenino")

#Indicamos al usuario mediante una etiqueta que seleccione una opcion
Label(root, text="Selecciona tu genero:").pack()

#Creamos un radioutton para cada una de las opciones y les asignamos la variable y el valor
Radiobutton(root, text="Masculino", variable=option, value=1, command=printOption).pack()
Radiobutton(root, text="Femenino", variable=option, value=2, command=printOption).pack()

#Creamos una etiqueta para mostrar la opcion seleccionada
result=Label(root)
result.pack()

root.mainloop()