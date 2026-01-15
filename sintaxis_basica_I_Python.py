Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print ("Hola mundo")
Hola mundo
>>> print("Hola mundo"); print("Adiós mundo cruel")
Hola mundo
Adiós mundo cruel
>>> #Se desaconseja introducir varias instrucciones en la misma linea
>>> #Disminuye la legibilidad
>>> mi_nombre="Carla"
>>> mi_nombre
'Carla'
>>> mi_nombre="mi nombre es\
... Carla"
>>> mi_nombre
'mi nombre esCarla'
>>> #salto de línea: escribimos en linea nueva pero se muestra en la misma
>>> a=0
>>> for i in range(5):
...     a+=1
...     print(a)
... 
...     
1
2
3
4
5
