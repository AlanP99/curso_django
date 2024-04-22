#Acceso a variables del sistema 
#Manipulación de excepciones
#Control del intérprete de Python
#Sys puede acceder a varias utilidades del sistema, dando acceso a modulos especificos    
import sys
#Agregar al path, donde se esta alojando la ubicación del fichero, para tener acceso a nuestros datos
sys.path.append('C:\\Users\\Alan Garcia P\\Documents\\Repos\\curso_django\\clinica')
from clinica.wsgi import *
from tienda.models import Categoria, Producto, Pedido, DetallePedido
#permite acceder a varias funcionalidades y objetos útiles que se utilizan comúnmente al realizar consultas y operaciones en la base de datos a través del ORM 
#Q Es una clase que te permite construir consultas complejas y combinar condiciones lógicas (AND, OR, NOT) de manera dinámica. 
#Avg: Es una función de agregación que calcula el promedio de los valores de un campo numérico en un conjunto de datos.
from django.db.models import Q, Avg, Min, Max, Sum, Count
from django.contrib.auth.models import User
from datetime import date
from faker import Faker
#from django.test import TestCase

# Create your tests here.

""" admin = User.objects.get(username= "admin")
categoria=Categoria.objects.create(nombre="Libros", descripcion="Libros de varios generos y autores", autor_id=admin)
print(categoria) """



""" #Crear producto

#1 Seleccionar la categoria en la cual se va crear el producto
categoria = Categoria.objects.get(nombre = "Libros")

#usamos el admin para cualquier moviemiento de la base, en este caso aplica
admin = User.objects.get(username= "admin")

#Le pasamos al objeto los datos que vamos a ingresar y sus parametros
producto = Producto.objects.create(nombre="Batman", precio=50.00, imagen = " batman.jpg",categoria_id = categoria, autor_id = admin)
print(producto) """

""" admin = User.objects.get(username= "admin")
#de esta forma podemos crear una variable tipo lista, donde creamos diferentes categorias en una solo consulta
#asi podemos hacer mas rapido el proceso para generar consultas a la BD
productos = [
    Producto(nombre = "Balón", precio = 5.00, categoria_id =Categoria.objects.get(nombre="Juguetes"), autor_id = admin),
    Producto(nombre = "Historia del mundo", precio = 50.00, categoria_id =Categoria.objects.get(nombre="Libros"), autor_id = admin),
    Producto(nombre="Historia de México", precio= 30.00, categoria_id =Categoria.objects.get(nombre="Libros"), autor_id = admin)
    
]
#el metodo bulk_crerate nos permite ejecutar varias consultas a la vez
Producto.objects.bulk_create(productos)
print(productos)

 """
#CREAR CATEGORIAS ALEATORIAS
""" admin = User.objects.get(username= "admin")

def crear_categorias_aleatorias(n):
    for i in range(n):
        fake = Faker("es_ES")
        categoria = fake.word()
        nombre = categoria
        #print(nombre)
        try:
            categoria = Categoria.objects.create(nombre=nombre, autor_id=admin)
            print(f'Se ha creado la categoria {nombre}')
        except Exception as e:
            print("La categoria", e, "ya ha sido agregada")
            
            
crear_categorias_aleatorias(5)"""
#Metodo Update
""" qs = Producto.objects.filter(nombre = "Reloj Inteligente").update(precio=10.00)
print(qs)
 """
#Metodo Delete
#Tambien podemos generar una tupla, donde demos el numero de eliminados
# y el diccionario que es el numero de producto
""" (num, dic) = Producto.objects.filter(categoria_id__nombre = "Juguetes").delete()
print(num)
print(dic)
 """

    

 
 