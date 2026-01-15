from tkinter import *

root = Tk()
root.title("Menus en Python")
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
fileMenu.add_command(label="Close")
fileMenu.add_command(label="Exit", command=root.quit) #Cierra la ventana

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
helpMenu.add_command(label="About")

#Quitamos la barra horizontal discontinua que aparece al inicio del submenu
fileMenu.config(tearoff=0) #Dentro del constructor de fileMenu agregamos tearoff=0
editMenu.config(tearoff=0)
toolsMenu.config(tearoff=0)
helpMenu.config(tearoff=0)

root.mainloop()
