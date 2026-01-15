#1) Crear archivo setup.py en la carpeta del paquete para distribuirlo
    #Va a contener la descripción del paquete y sus dependencias
    #Con el siguiente contenido:
from setuptools import setup #Instalar setuptools si no lo tienes instalado, mediante pip install setuptools en la consola

setup(
    
    name='Mi_primer_paquete_distribuible', #nombre del paquete
    version='0.1', #versión del paquete
    description='Un paquete de ejemplo para aprender a crear y distribuir paquetes en Python', #descripción del paquete
    author='Maldita Carlita', #tu nombre  
    author_email='carlaportelaubeira@gmail.com', #tu email
    url='https://www.linkedin.com/carla-portela-ubeira-developer', #URL del proyecto
    packages=['Mi_primer_paquete', 'Mi_primer_paquete.Subpaquete_modulos'], #lista de paquetes a incluir (rutas relativas desde la carpeta raíz)
    install_requires=[], #dependencias del paquete, si las hay
    
)

#2) Crear el paquete distribuible
    #En la consola en modo adminusitrador, nos movemos a la carpeta raíz del paquete
    #mediante cmd -> cd ruta/a/tu/paquete 
    #y escribimos: python setup.py sdist
    #creandose en el directorio raíz dos carpetas: dist y .info
    #En la dist se encuentra el archivo comprimido .tar.gz con el nombre del paquete y la versión 
    #Este archivo es el que se puede distribuir, subir o enviar a otros usuarios y que tendrán que instalar para usar el paquete.
    
#3) Instalar el paquete distribuible
    #Nos movemos desde la consolo como administrador a la carpeta donde se encuentra el archivo comprimido .tar.gz
    #y escribimos: pip3 install nombre_del_paquete.tar.gz
    #Una vez instalado el módulo, se puede importar dichas funciones desde cualquier ubicación del sistema (no tiene porque encontrarse en la misma carpeta que el script que lo importa)
    #mediante la instrucción import nombre_del_paquete o import nombre_del_paquete.Subpaquete_modulos.nombre_del_modulo
    
#4) Desinstalar el paquete distribuible
    #Para desinstalar el paquete distribuible, se puede hacer desde la consola con el comando:
    #pip3 uninstall nombre_del_paquete (del atributo name del setup.py)
    