from tkinter import * #Importamos la librería Tkinter
import re #Importamos la librería re para usar expresiones regulares

raiz = Tk() #Creamos la ventana principal
raiz.title('Calculadora') #Asignamos un título a la ventana
raiz.geometry('400x450') #Definimos el tamaño de la ventana, 400 píxeles de ancho y 400 píxeles de alto
#raiz.resizable(0, 0) #Deshabilitamos el cambio de tamaño de la ventana, tanto en ancho como en alto

frame = Frame(raiz) #Creamos un frame para contener los widgets
frame.pack() #Empaquetamos el frame para que se muestre y se le de el tamaño por defecto

#------------------------------------Creamos un wodget Entry para la entrada de número, operaciones y resultados---------------------------------------------

#(1) Creamos una variable para almacenar el número introducido
numeroPantalla = StringVar()
numeroPantalla.set("") #Inicializamos la variable numeroPantalla como una cadena vacía

entrada = Entry(frame, width=28, font=('Arial', 16), textvariable=numeroPantalla) #Ancho de 30 caracteres y fuente Arial de tamaño 16
#Con el atributo textvariable vinculamos el Entry a la variable numeroPantalla
#Esto permite que el Entry muestre el valor de numeroPantalla y se actualice automáticamente cuando cambie
entrada.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #Colocamos el Entry en la primera fila y ocupa 4 columnas
#Columnspan permite que el Entry ocupe varias columnas, en este caso 4
#padx y pady añaden un margen de 10 píxeles alrededor del Entry
entrada.focus() #Focalizamos el Entry para que esté listo para recibir entrada de texto
#Esto hace que el cursor aparezca en el Entry cuando se abre la ventana
#y permite al usuario empezar a escribir inmediatamente
entrada.config(background='black', fg='white', justify='right') #Configuramos el color de fondo, de texto y lo alineamos a la derecha


#(2)#Creamos un widget Label para mostrar la operación actual
#Este widget se usará para mostrar la operación que se está realizando
#y se actualizará cada vez que se pulse un botón de número o de operación

operacionPantalla = StringVar() #Creamos una variable StringVar para almacenar la operación actual
operacionPantalla.set("") #Inicializamos la variable operacionPantalla como una cadena vacía

operacion = Label(frame,  height=3, font=('Arial', 12), textvariable=operacionPantalla) #Creamos un widget Text para mostrar la operación
#Con el atributo textvariable vinculamos el Label a la variable operacionPantalla
#Lo que permite que el Label muestre el valor de operacionPantalla y se actualice automáticamente cuando cambie
operacion.grid(row=0, column=1, columnspan=4, sticky='e') #Colocamos el Text en la primera fila y ocupa 4 columnas
#padx y pady añaden un margen de 10 píxeles alrededor del Text
operacion.config(fg='grey') #Configuramos el color de fondo, de texto y lo alineamos a la derecha

global resultado #Declaramos la variable resultado como global para poder usarla en las funciones
resultado = StringVar() #Creamos una variable StringVar para almacenar el resultado de la operación
resultado.set("") #Inicializamos la variable resultado como una cadena vacía


#------------------------------------------Funciones de los botones--------------------------------------------------------------------------------------

#Función para visualizar números en el Entry al pulsar los botones:
#   - Definimos la variable 'numeroPantalla' que recibe el valor del botón pulsado.
#   - La asociamos a la pantalla de la calculadora (1).

def visualizarNumero(numero): #Cuando pulsemos botones numéricos
    if re.search(r"^\.", numeroPantalla.get()): #SI comienza con punto decimal lo eliminamos
        numeroPantalla.set(numeroPantalla.get().lstrip(".") + numero) 
    elif re.search(r"^0{2,}", numeroPantalla.get()): #Si hay más de un cero al principio del número los eliminamos
        numeroPantalla.set(numeroPantalla.get().lstrip("0") + numero)
    elif re.search(r"\.\.+", numeroPantalla.get()): #Si hay dos puntos decimales seguidos en el número lo sustituimos por uno
        numeroPantalla.set(numeroPantalla.get().strip(".") + "." + numero)
    elif re.search(r"\.\d+\.", numeroPantalla.get()): #Si hay más de un punto decimal, lo eliminamos
        numeroPantalla.set(numeroPantalla.get().strip(".") + numero) 
    else:
        numeroPantalla.set(numeroPantalla.get() + numero) #Actualizamos el valor de la pantalla con el número que ya teníamos y el nuevo número pulsado, al final
        
#Función para visualizar la operación en el Label al pulsar los botones:
#   - Definimos la variable 'operacionPantalla' que recibe el valor del botón pulsado.
#   - La asociamos a la pantalla de la calculadora (2).

def visualizarOperacion(operacion): #Cuando pulsamos los botones de operaciones
    if resultado.get() != "": #Si ya se ha pulsado el botón de igual y hay un resultado
        if operacionPantalla.get() == "" and re.search(r"\.[1-9]+0+$", numeroPantalla.get()):  #Si la pantalla de operación está vacía y hay ceros a la derecha del punto decimal y se pulsa el botón 0, no se añade
            numeroPantalla.set(numeroPantalla.get().rstrip("0")) #Eliminamos los ceros a la derecha del punto decimal
            operacionPantalla.set(numeroPantalla.get() + " " + operacion) #Actualizamos el valor de la pantalla de operación con la operación que ya teníamos y la nueva operación pulsada, al final
            numeroPantalla.set("")
        elif operacionPantalla.get() == "" and re.search(r"\.0+$", numeroPantalla.get()): #Si hay ceros a la derecha del punto decimal y se pulsa el botón de operación, los eliminamos
            numeroPantalla.set(numeroPantalla.get().rstrip("0").strip(".")) #Eliminamos los ceros a la derecha del punto decimal y el punto decimal si no hay decimales
            operacionPantalla.set(numeroPantalla.get() + " " + operacion) #Actualizamos el valor de la pantalla de operación con la operación que ya teníamos y la nueva operación pulsada, al final
            numeroPantalla.set("")
        elif operacionPantalla.get() == "": #Si la pantalla de operación está vacía
            operacionPantalla.set(operacionPantalla.get() + numeroPantalla.get() + " " + operacion)
            numeroPantalla.set("") #Limpiamos la pantalla de número para que el usuario pueda introducir el siguiente número
        else: #Si la pantalla de operación no está vacía
            operacionPantalla.set(operacionPantalla.get() + " " + operacion) #Actualizamos el valor de la pantalla de operación con la operación que ya teníamos y la nueva operación pulsada, al final
            numeroPantalla.set("") #Limpiamos la pantalla de número para que el usuario pueda introducir el siguiente númeronumeroPantalla.set("") #Limpiamos la pantalla de número para que el usuario pueda introducir el siguiente número
    else: #Si no se ha pulsado el botón de igual acumulamos las operaciones
        operacionPantalla.set(operacionPantalla.get() + numeroPantalla.get() + " " + operacion) #Actualizamos el valor de la pantalla de operación con la operación que ya teníamos y la nueva operación pulsada, al final
        numeroPantalla.set("") #Limpiamos la pantalla de número para que el usuario pueda introducir el siguiente número

#Funcion para calcular el resultado de la operación al pulsar el botón de igual: 

def calcularResultado(): #Cuando pulsamos el botón de igual
    if re.search(r"\.[1-9]+0+$", numeroPantalla.get()):  #Si hay ceros a la derecha del punto decimal y se pulsa el botón igual, los eliminamos
        numeroPantalla.set(numeroPantalla.get().rstrip("0")) #Eliminamos los ceros a la derecha del punto decimal
    elif re.search(r"\.0+$", numeroPantalla.get()): #Si hay ceros a la derecha del punto decimal y se pulsa el botón de operación, los eliminamos
        numeroPantalla.set(numeroPantalla.get().rstrip("0").strip(".")) #Eliminamos los ceros a la derecha del punto decimal y el punto decimal si no hay decimales
    try:
        operacionTotal = operacionPantalla.get() + (numeroPantalla.get()) #Concatenamos la operación actual con el número actual previo a pulsar el botón igual
        resultado = str(eval(operacionTotal)) #Evaluamos la operación
        operacionPantalla.set(operacionTotal) #Actualizamos la pantalla de operación con la operación completa y el signo igual
        if re.search(r"\.\d+0+$", resultado): #Si el resultado tiene ceros a la derecha del punto decimal, los eliminamos
            resultado = resultado.rstrip("0") #Eliminamos los ceros a la derecha del punto decimal
        elif re.search(r"\.0+$", resultado): #Si termina en .0, lo eliminamos
            resultado = resultado.rstrip(".0")
        numeroPantalla.set(resultado) #Actualizamos la pantalla de número con el resultado de la operación
    except Exception as e:
        numeroPantalla.set("Error") #Si hay un error en la operación, mostramos "Error" en la pantalla de número
        operacionPantalla.set("") #Limpiamos la pantalla de operación para que no se muestre la operación errónea
        
#Función para borrar la pantalla de número y operación al pulsar el botón de borrar:
def borrarTodo():
    numeroPantalla.set("") #Limpiamos la pantalla de número
    operacionPantalla.set("") #Limpiamos la pantalla de operación

#------------------------------------Creamos los botones de la calculadora-----------------------------------------------------------------------------------

#Primera fila de botones
boton7 = Button(frame, text='7', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("7")) #Botón para el número 7
#Si en command=visualizacionarNumero("7") no se pone el lambda, se ejecutaría la función inmediatamente al crear el botón
#Por eso las funciones lambda para que se ejecute solo cuando se pulse el botón
boton7.grid(row=2, column=1) #Colocamos el botón en la segunda fila y primera columna
boton8 = Button(frame, text='8', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("8")) #Botón para el número 8
boton8.grid(row=2, column=2)
boton9 = Button(frame, text='9', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("9")) #Botón para el número 9
boton9.grid(row=2, column=3)
botonMultiplicar = Button(frame, text='*', width=5, height=2, font=('Arial', 16), command=lambda:visualizarOperacion(" * ")) #Botón para la multiplicación
botonMultiplicar.grid(row=2, column=4)

#Segunda fila de botones
boton4 = Button(frame, text='4', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("4")) #Botón para el número 4
boton4.grid(row=3, column=1)
boton5 = Button(frame, text='5', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("5")) #Botón para el número 5
boton5.grid(row=3, column=2)
boton6 = Button(frame, text='6', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("6")) #Botón para el número 6
boton6.grid(row=3, column=3)
botonDividir = Button(frame, text='/', width=5, height=2, font=('Arial', 16), command=lambda:visualizarOperacion(" / ")) #Botón para la división
botonDividir.grid(row=3, column=4)

#Tercera fila de botones
boton1 = Button(frame, text='1', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("1")) #Botón para el número 1
boton1.grid(row=4, column=1)
boton2 = Button(frame, text='2', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("2"))  #Botón para el número 2
boton2.grid(row=4, column=2)
boton3 = Button(frame, text='3', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("3")) #Botón para el número 3
boton3.grid(row=4, column=3)
botonRestar = Button(frame, text='-', width=5, height=2, font=('Arial', 16), command=lambda:visualizarOperacion(" - ")) #Botón para la resta
botonRestar.grid(row=4, column=4)

#Cuarta fila de botones
botonPunto = Button(frame, text='.', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero(".")) #Botón para el igual
botonPunto.grid(row=5, column=1)
boton0 = Button(frame, text='0', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero("0")) #Botón para el número 0
boton0.grid(row=5, column=2)
botonComa = Button(frame, text=',', width=5, height=2, font=('Arial', 16), command=lambda:visualizarNumero(".")) #Botón para la coma decimal
botonComa.grid(row=5, column=3) #Botón para la coma decimal
botonSumar = Button(frame, text='+', width=5, height=2, font=('Arial', 16), command=lambda:visualizarOperacion(" + ")) #Botón para la suma
botonSumar.grid(row=5, column=4)

#Quinta fila de botones
botonBorrarPantalla = Button(frame, text='CE', fg='blue', width=5, height=2, font=('Arial', 16), command=lambda:numeroPantalla.set("")) #Botón para borrar la pantalla de número
botonBorrarPantalla.grid(row=6, column=2) #Colocamos el botón en la sexta fila y primera columna
botonBorrarTodo = Button(frame, text='C', fg='red' ,width=5, height=2, font=('Arial', 16), command=borrarTodo) #Botón para borrar la entrada
botonBorrarTodo.grid(row=6, column=3) #Colocamos el botón en la sexta fila y segunda columna
botonIgual = Button(frame, text='=', fg='blue', width=5, height=2, font=('Arial', 16), command=calcularResultado) #Botón para calcular el resultado
botonIgual.grid(row=6, column=4) #Colocamos el botón en la sexta fila y tercera columna


#------------------------------------------Iniciamos el bucle principal de la ventana----------------------------------------------------------------

raiz.mainloop() 
#Esto mantiene la ventana abierta hasta que el usuario decida cerrarla
#Se coloca al final del código para que todo lo anterior se ejecute antes de iniciar el bucle
#Si no se coloca, la ventana se cerrará inmediatamente después de crearla

