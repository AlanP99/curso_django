from django.shortcuts import render
#importacion de la categoria.
from tienda.models import Categoria, Juguetes
# Create your views here.


#request, se pasa como parametro a nuestra función
def categorias(request):
    #Accedemos a la categoria, con todas sus propiedades
    categorias = Categoria.objects.all()
    #Creamos nuestro diccionario, pasando a la clave, los parametros de la categoria
    cat_dic = {'cat_dic': categorias}
    #retornamos nuestra petición, indicando la URL a la ubicacion de nuestro fichero
    #en este caso el HTML
    return render(request, 'tienda/categorias.html', cat_dic)

#Funcion que define los valores de un diccionario, busca y encuentra.
def juguetes(request):
    
    tipoJuguetes = Juguetes.objects.all()
    juguetes_dic = {'juguetes_dic': tipoJuguetes}
    dict_productos = {
        "juguete1" : "Pelota",
        "juguete2" : "Balon",
        "juguete3" : "Flauta"}
    return render(request, "tienda/juguetes.html", dict_productos)



""" def zapatos(request):
    dict_productos = {
        "zapato1" : "zapato1",
        "zapato2" : "zapato2",
        "zapato3" : "zapato3"}
    return render(request, "tienda/zapatos.html", dict_productos)


def jardineria(request):
    dict_productos = {"usuario ": "Alan"}
    return render(request, "tienda/eco.html", dict_productos)
 """
def categoria(request):
    dict_productos = {"usuario ": "Alan"}
    return render(request, "tienda/categorias.html", dict_productos)