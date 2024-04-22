from django.shortcuts import render



#HttpResponse es un objeto que contiene metadatos sobre una solicitud
#Django carga la vista y pasa por HttpResponse como primer argumento
#Cada vista es responsable de devolver un HttpResponse
from django.http import HttpResponse
import datetime
# Create your views here.


#creamos nuestra funcion
def mostrar(request):
    return HttpResponse('<h2>Bienvenidos! Esto es un Checked Code</h2>')

def mostrarDateTime(request):
    dt = datetime.datetime.now()
    dt= str(dt)
    c = "<h2>Fecha y Hora actual: </h2> " + "<b>"+ dt +"</br>"
    return HttpResponse(c)