from django.db import models
#Libreria para acceder al modelo de usuario para autentificación
#asi como roles, creacion de usarios y administracion de usuarios, etc
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    #verbose_name es un atributo de metadatos para declarar el nombr de etiqueta, sustituyendo 
    #el nombre de la variable por el verbose_name 
    nombre = models.CharField(max_length=100, verbose_name='Nombre',unique=True)
    #blank define si un campo de la DB puede estar vacion o no
    descripcion = models.CharField(max_length=400,null = True, blank = True, verbose_name='Descripción')
    #On_delete es un parametro que se utiliza al definir relacion de modelos
    #se comparta como objetos relacionados que al ser eleminado el objeto del cual viene relacionado
    #este eliminara todos los objetos relacionados al modelo
    # significa que cuando el objeto relacionado es eliminado, todos los objetos que dependen de ese objeto también serán eliminados.
    #User, podrá realizar cualquier tipo de modificación a la categoria
    autor_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #auto_now_add parametro que sirve para indicar a un campo la fecha y hora actual en la que se crear el registro
    creacion = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de Creación")    
    actualizacion = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de Edición") 

    #Metodo tipo string, objeto de una clase, define como se mostrara el objeto
    #cuando este sea mostrado en la interfaz
    def __str__(self) -> str:
        return self.nombre 
    

class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre',unique=True)
    #decimal_places = 2, sirve para especificar la cantidad de decimales de un numero que se deben
    #de tomar en cuenta
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Precio")
    #upload_to, se utiliza para archivos y imagenes, al usarlo permite controlar la estructura
    #del directorio y ubicacion donde se guardan los archivos
    #productos/%Y/$m/%d, indica en que carpeta se guardara el archivo y con que fecha se guardara
    imagen = models.ImageField(upload_to='productos/%Y/$m/%d', null=True, blank=True, verbose_name="Imagen")
    #on_delete, es utilizado para eliminar objetos relacionados con otros objetos
    categoria_id = models.ForeignKey(Categoria, on_delete = models.CASCADE, verbose_name = "Categoria")
    autor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Productos")
    
    def __str__(self) -> str:
        return self.nombre
    
class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add = True)
    #ManyToManyField, define una relación muchos a muchos entre dos modelos.
    productos = models.ManyToManyField(Producto)
    
    
    def __str__(self) -> str:
        return f'Pedido {self.id} de {self.cliente}'
    
    
class DetallePedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #se utiliza para almacenar enteros positivos en la base de datos. 
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.pedido_id} - {self.producto_id}[{self.cantidad}]'
    
class Juguetes:
    def __str__(self) -> str:
        return self