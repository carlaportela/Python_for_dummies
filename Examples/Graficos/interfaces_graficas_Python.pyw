#GUI - Graphic User Interface. Intermediario entre usuario y programa.
#Se emplean bibliotecas como Tkinter, WxPython, PyQT, PyGTK

#Estructura de ventana con Tkinter: Raíz(Tk o ventana) -> Frame (Organizador de elementos) -> Widgets (Elementos, el frame también es un widget)
    #Importamos la librería Tkinter al completo
from tkinter import *

    #Creamos la raiz
raiz = Tk()

    #Modificamos las características de la ventana por defecto
raiz.title("ventana de pruebas") #Modificamos el título de la ventana
raiz.resizable(0,0) #Permitimos o no redimensionar la ventana. este método admite dos datos de tipo boolean (width o ancho y heigth o alto). En este caso, bloqueamos que se pueda redimensionar (False, False).
raiz.geometry("650x350") #Modificamos las dimensiones por defecto de la ventana. Arugmento entre comillas de ancho x alto
raiz.iconbitmap("D:\Ciclo Desarrollo Web\Curso_Python\Graficos\desktop.ico") #Modificamos el icono de la ventana. archivo .ico en directorio del programa que estamos creando. EL argumento es la ruta del archivo .ico
raiz.config(bg="black") #Cambiamos el color de fondo

    
    #Ejecutamos la ventana. Para que una ventana esté en ejecución debe de estar en un bucle infinito y debe estar a la escucha de las acciones del usuario (eventos)
    #Este método debe estar siempre en ÜLTIMO lugar.
raiz.mainloop() 

    #Si modificamos la extensión de la aplicación.py por pyw, al hacer click sobre ella va a abrir directamente la ventana en lugar de la consola
    

