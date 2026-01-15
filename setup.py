from setuptools import setup
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