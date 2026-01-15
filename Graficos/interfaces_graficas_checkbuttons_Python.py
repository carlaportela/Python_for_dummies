from tkinter import *

root=Tk()
root.title("Checkbuttons")

#Agregamos una imagen

picture=PhotoImage(file="D:\Ciclo Desarrollo Web\Curso_Python\Graficos\\avion.png")
picture_label=Label(root, image=picture)
picture_label.pack()

#Creamos una variable para cada checkbutton
beach=IntVar()
mountain=IntVar()
countryside=IntVar()

#Creamos una función para mostrar las opciones seleccionadas
def show_choices():
    choice="" #Donde se van a almacenar las opciones seleccionadas
    if beach.get()==1:
        choice+=" playa"
        if mountain.get()==1:
            if countryside.get()==1:
                choice+=", montaña"
                choice+=" y campo."
            else:
                choice+=" y montaña."
        else:
            if countryside.get()==1:
                choice+=" y campo."
    else:
        if mountain.get()==1:
            choice+="montaña"
            if countryside.get()==1:
                choice+=" y campo."
            else:
                choice+="."
        else:
            if countryside.get()==1:
                choice+="campo."
            else:
                choice=""
    selected_choices_label.config(text="Has seleccionado: " +choice)

#Creamos un frame para agrupar los elementos

frame=Frame(root)
frame.pack()

#creamos una etiqueta que indique al usuario lo que debe hacer

Label(frame, text="Elige tu destino:", width=50).pack()

#Creamos un grupo de checkbuttons

Checkbutton(frame, text="Playa", variable=beach, onvalue=1, offvalue=0, command=show_choices).pack()
Checkbutton(frame, text="Montaña", variable=mountain, onvalue=1, offvalue=0, command=show_choices).pack()
Checkbutton(frame, text="Campo", variable=countryside, onvalue=1, offvalue=0, command=show_choices).pack()

selected_choices_label=Label(frame)
selected_choices_label.pack()

root.mainloop()
