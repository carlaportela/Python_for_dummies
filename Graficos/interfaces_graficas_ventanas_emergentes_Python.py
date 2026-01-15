from tkinter import *

#Importamos la librería messagebox para mostrar ventanas emergentes
from tkinter import messagebox

root = Tk()
root.title("Menus en Python")

#Creamos una función para mostrar información adicional en una ventana emergente al pulsar la opcion "About"
def aboutInfo():
    messagebox.showinfo("About", "Version 1.0. \nDesarrollado por OpenAI.") #El primer argumento es el título de la ventana emergente y el segundo es el mensaje que queremos mostrar
    #Determinamos cuando queremos que aparezca la ventana emergente mediante el atributo commmand en la opción del menú

#Creamos una función para mostrar una ventana de advertencia al pulsar la opción "licencia"
def licenseInfo():
    messagebox.showwarning("License", "Producto bajo licencia GNU.") #Creamos una ventana de advertencia
    #Determinamos cuando queremos que aparezca la ventana emergente mediante el atributo commmand en la opción del menú
    
#Creamos una función para mostrar una ventana emergente que nos pregunte si queremos salir de la aplicación
def exitApp():
    value = messagebox.askquestion("Exit", "Do you want to exit the application?") #Creamos una ventana emergente con dos opciones: Yes y No
    #Determinamos cuando queremos que aparezca la ventana emergente mediante el atributo commmand en la opción del menú
    #Cuando el usuario pulsa "Yes" o "No", devuelve un valor diferente
    if value == "yes":
        root.destroy() 
    #Para cambiar los botones a "Ok" y "Cancel" se usa el metodo askokcancel, que devuelve "True" o "False"
        #value = messagebox.askokcancel("Exit", "Do you want to exit the application?")
        #if value == True:
            #root.destroy()

#Creamos una función para mostrara una ventana emergente que nos pregunte si queremos reintentar o cancelar
def closeDoc():
    value = messagebox.askretrycancel("Reintentar", "Documento bloqueado")
    if value == False:
        root.destroy()
        
#Creamos una variable para almacenar el menu
menuBar = Menu(root)
root.config(menu=menuBar, width=300, height=300)

#Establecemos el número de elementos del menu
fileMenu = Menu(menuBar) #"fileMenu" es el nombre interno de este elemento del menu
editMenu = Menu(menuBar)
toolsMenu = Menu(menuBar)
helpMenu = Menu(menuBar)

#Establecemos el texto de los elementos del menu
menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Edit", menu=editMenu)
menuBar.add_cascade(label="Tools", menu=toolsMenu)
menuBar.add_cascade(label="Help", menu=helpMenu)

#agregamos opciones al menu "File"
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save as...")
fileMenu.add_separator() #Agrega una linea separadora paara separar grupos de opciones
fileMenu.add_command(label="Close", command=closeDoc)
fileMenu.add_command(label="Exit", command=exitApp) #Cierra la ventana

#Agregamos opciones al menu "Edit"
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_separator()
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

#Agregamos opciones al menu "Tools"
toolsMenu.add_command(label="Options")

#Agregamos opciones al menu "Help"
helpMenu.add_command(label="Help")
helpMenu.add_command(label="License", command=licenseInfo) #Agregamos una función para mostrar una ventana de advertencia al pulsar esta opción
helpMenu.add_command(label="About", command=aboutInfo) #Al pulsar esta opción se ejecuta la función aboutInfo

#Quitamos la barra horizontal discontinua que aparece al inicio del submenu
fileMenu.config(tearoff=0) #Dentro del constructor de fileMenu agregamos tearoff=0
editMenu.config(tearoff=0)
toolsMenu.config(tearoff=0)
helpMenu.config(tearoff=0)

root.mainloop()
