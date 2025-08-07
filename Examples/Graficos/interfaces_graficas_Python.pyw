#GUI - Graphic User Interface. Intermediario entre usuario y programa.
#Se emplean bibliotecas como Tkinter, WxPython, PyQT, PyGTK

#Estructura de ventana con Tkinter: Raíz(Tk o ventana) -> Frame (Organizador de elementos) -> Widgets (Elementos, el frame también es un widget) ---------------------------------------------------------------------------------------------------------------------------------
    #Importamos la librería Tkinter al completo
from tkinter import *

    #Creamos la raiz
raiz = Tk()

    #Modificamos las características de la ventana por defecto
raiz.title("ventana de pruebas") #Modificamos el título de la ventana
#raiz.resizable(0,0) #Permitimos o no redimensionar la ventana. este método admite dos datos de tipo boolean (width o ancho y heigth o alto). En este caso, bloqueamos que se pueda redimensionar (False, False).
#raiz.geometry("650x350") #Modificamos las dimensiones por defecto de la ventana. Arugmento entre comillas de ancho x alto
raiz.iconbitmap("D:\Ciclo Desarrollo Web\Curso_Python\Graficos\desktop.ico") #Modificamos el icono de la ventana. archivo .ico en directorio del programa que estamos creando. EL argumento es la ruta del archivo .ico
raiz.config(bg="black") #Cambiamos el color de fondo

#Creamos un frame. Un frame es un organizador de elementos que nos permite agrupar widgets ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
miFrame = Frame(raiz) 

    #Es necesario empaquetarlo dentro de la raíz   
miFrame.pack() 

    #€xisten muchas opciones para empaquetar un frame dentro de la raíz.
miFrame.pack(side="left", anchor="n", fill="y", expand="yes") 
        #side: lado donde se coloca el frame (left, right, top, bottom)
        #anchor: ancla del frame (n, s, e, w)
        #fill: cómo se rellena el frame (x, y, both)
        #expand: si se expande o no (yes, no). 
        
    #Cambiamos el color de fondo del frame para poder verlo mejor
miFrame.config(bg="white") 
        #Admitimos cualquier color en formato hexadecimal o por nombre.
        
    #Para poder ver el frame, debemos darle un tamaño. 
        #Para ello, debemos comentar la línea de código que modifica el tamaño de la raíz y modificar el tamaño del frame,
        #Ya que la raíz se adapta al tamaño del frame.
miFrame.config(width="650", height="800") 
        #El frame tiene tamaño fijo; por defecto no se adapta al tamaño de la raíz.
    
    #Modificamos el borde del frame pero antes modificamos el tamaño del borde, que por defecto es 0.
miFrame.config(bd=5)
miFrame.config(relief="groove") 
        #Admite varios tipos de borde: flat, raised, sunken, ridge, solid, groove, inset
    
    #Modificamos el icono del cursor del frame
miFrame.config(cursor="hand2") 
        #Admite varios tipos de iconos de cursor: arrow, circle, clock, cross, dot, hand2, 
    
    #Todos estos cambios del frame podemos aplicarlos también a la raíz, ya que la raíz es un frame.  
        #raiz.relief = "sunken" 
        #raiz.config(bd=7)
        #raiz.config(cursor="circle")
  
#Creación de labels (Widgets de texto estático) ---------------------------------------------------------------------------------------------------------------------------------
miLabel = Label(miFrame, text="Formulario", bg="white", fg="black", font=("Arial", 20), cursor="circle")
    
    #Empaquetamos el label dentro del frame
miLabel.pack(side="top", anchor="n", fill="x", expand="yes")
        #side: lado donde se coloca el label (left, right, top, bottom)
        #anchor: ancla del label (n, s, e, w)
        
    #El método place() se usa para colocar el label en una posición concreta dentro del frame.
miLabel.place(x=50, y=50)
        #x: posición horizontal del label en píxeles
        #y: posición vertical del label en píxeles
    
    #Se puede prescindir de la variable miLabel y crear el label directamente dentro del frame.
        #Label(miFrame, text="Hola, soy un label", bg="white", fg="black", font=("Arial", 20), cursor="circle").pack(side="top", anchor="n", fill="x", expand="yes").place(x=50, y=50)

    #Labels con imágenes (Tkinter admite formatos .gif y .png)
miImagen = PhotoImage(file="D:\Ciclo Desarrollo Web\Curso_Python\Graficos\laptop.png") 
miLabelImagen = Label(miFrame, image=miImagen)
        
        #Empaquetamos el label con la imagen dentro del frame
miLabelImagen.pack(side="top", anchor="n", fill="x", expand="yes")
        
        #Lo posicionamos dentro del frame
miLabelImagen.place(x=50, y=250)

#Creación de cuadro de entrada (Wdiget Entry) ---------------------------------------------------------------------------------------------------------------------------------
miEntry = Entry(miFrame, bg="white", fg="black", font=("Arial", 20), cursor="xterm")
    
    #Empaquetamos el entry dentro del frame
miEntry.pack(side="top", anchor="n", fill="x", expand="yes")
    
    #Lo posicionamos dentro del frame
miEntry.place(x=175, y=170)
    
    #Creamos un texto antes del entry
nombreLabel = Label(miFrame, text="Nombre:", bg="white", fg="blue", font=("Arial", 20), cursor="circle")
    
    #Empaquetamos el label dentro del frame
nombreLabel.pack(side="top", anchor="n", fill="x", expand="yes")
    
    #Lo posicionamos dentro del frame
nombreLabel.place(x=50, y=170)
#Creación de otros labels y entries para un formulario
apellidoLabel = Label(miFrame, text="Apellidos:", bg="white", fg="blue", font=("Arial", 20), cursor="circle")
apellidoLabel.pack(side="top", anchor="n", fill="x", expand="yes")
apellidoLabel.place(x=50, y=220)
apellidoEntry = Entry(miFrame, bg="white", fg="black", font=("Arial", 20), cursor="xterm")
apellidoEntry.pack(side="top", anchor="n", fill="x", expand="yes")
apellidoEntry.place(x=175, y=220)

direccionLabel = Label(miFrame, text="Dirección:", bg="white", fg="blue", font=("Arial", 20), cursor="circle")
direccionLabel.pack(side="top", anchor="n", fill="x", expand="yes")
direccionLabel.place(x=50, y=270)
direccionEntry = Entry(miFrame, bg="white", fg="black", font=("Arial", 20), cursor="xterm")
direccionEntry.pack(side="top", anchor="n", fill="x", expand="yes")
direccionEntry.place(x=175, y=270)

telefonoLabel = Label(miFrame, text="Teléfono:", bg="white", fg="blue", font=("Arial", 20), cursor="circle")
telefonoLabel.pack(side="top", anchor="n", fill="x", expand="yes")
telefonoLabel.place(x=50, y=320)
telefonoEntry = Entry(miFrame, bg="white", fg="black", font=("Arial", 20), cursor="xterm")
telefonoEntry.pack(side="top", anchor="n", fill="x", expand="yes")
telefonoEntry.place(x=175, y=320)

contraseñaLabel = Label(miFrame, text="Contraseña:", bg="white", fg="blue", font=("Arial", 20), cursor="circle")
contraseñaLabel.pack(side="top", anchor="n", fill="x", expand="yes")
contraseñaLabel.place(x=50, y=370)
contraseñaEntry = Entry(miFrame, bg="white", fg="black", font=("Arial", 20), cursor="xterm", show="*")

#Creación de botón (Widget Button) ---------------------------------------------------------------------------------------------------------------------------------
miBoton = Button(miFrame, text="Enviar", bg="white", fg="black", font=("Arial", 20), cursor="hand2", bd=5, relief="raised", command=lambda: print("Botón pulsado"))
    #Empaquetamos el botón dentro del frame
miBoton.pack(side="top", anchor="n", fill="x", expand="yes")
    #Lo posicionamos dentro del frame
miBoton.place(x=500, y=170)

    #Existe un método nuevo, grid(), que nos permite organizar los widgets en una cuadrícula.
        #Para ello, sustituimos el método pack() por grid() y especificamos la fila y columna donde queremos colocar el widget.
        #Es muy útil para formularios.
miLabel.grid(row=0, column=0, sticky="w") #sticky="w" alinea el texto a la izquierda
nombreLabel.grid(row=1, column=0, sticky="e")
miEntry.grid(row=1, column=1, pady=10, sticky="e") #padx y pady añaden espacio alrededor del widget
apellidoLabel.grid(row=2, column=0, sticky="e")
apellidoEntry.grid(row=2, column=1, pady=10, sticky="e")
direccionLabel.grid(row=3, column=0, sticky="e")
direccionEntry.grid(row=3, column=1, pady=10, sticky="e")
telefonoLabel.grid(row=4, column=0, sticky="e")
telefonoEntry.grid(row=4, column=1, pady=10, sticky="e")
contraseñaLabel.grid(row=5, column=0, sticky="e")
contraseñaEntry.grid(row=5, column=1, pady=10, sticky="e")
contraseñaEntry.config(show="*") #Oculta el texto introducido en el entry de contraseña 
miBoton.grid(row=6, column=1, pady=10, sticky="e") #sticky="e" alinea el botón a la derecha
miLabelImagen.grid(row=7, column=0, columnspan=3)

#Ejecutamos la ventana. Para que una ventana esté en ejecución debe de estar en un bucle infinito y debe estar a la escucha de las acciones del usuario (eventos) ----------------------------------------------
    #Este método debe estar siempre en ÜLTIMO lugar.
raiz.mainloop() 

#Si modificamos la extensión de la aplicación.py por pyw, al hacer click sobre ella va a abrir directamente la ventana en lugar de la consola
    

