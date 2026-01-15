from tkinter import *

#Importamos el módulo filedialog para abrir la ventana emergente de selección de archivo
from tkinter import filedialog

root = Tk()
root.title("Abrir archivo en Python")
root.geometry("500x200")

#Creamos una función para abrir la ventana emergente de selección de archivo cuando pulsemos un botón
def openFile():
    archivo = filedialog.askopenfilename(title="Abrir archivo", initialdir="D:/", filetypes=(("Text files", "*.txt"), ("All files", "*.*"))) #Hay que ofrecerle por lo menos dos posibilidades
    #El primer argumento es el título de la ventana emergente, el segundo es el directorio inicial que se abre y el tercero es una tupla con los tipos de archivos que queremos mostrar
    print(archivo) #Mostramos en consola la ruta del archivo seleccionado

#Creamos un botón para abrir la ventana emergente de selección de archivo
openButton = Button(root, text="Abrir archivo", command=openFile)
openButton.pack()

root.mainloop()
