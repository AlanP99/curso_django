from django.contrib import admin
from tienda.models import Categoria, Producto, Pedido, DetallePedido

# Register your models here.

#La creación de la clase es para traer los elementos del modelo al Admin
class CategoriaAdmin(admin.ModelAdmin):
    
    #Decide como va listar los elementos que quieres mostrar
    list_display = ['id', 'nombre', 'descripcion']
    
#Realizamos el registro donde pasamos la categoria(modelo), y nuestro listado deseado
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)





