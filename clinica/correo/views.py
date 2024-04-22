from django.shortcuts import render
from .forms import FormCorreo
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.mail import send_mail
# Create your views here.

@csrf_protect
def mensaje_correo(request):
    if request.method == 'POST':
        form = FormCorreo(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            #usuario = form.cleaned_date['usuario']
            #Procesar datos del formulario
            #print(nombre, mensaje)
            send_mail(
                'Cheked Code | Curso Django 4.2',
                f'Nombre: {nombre}\n Email: {email}\n Mensaje: {mensaje}',
                'kinktotfm@gmail.com',
                [form.cleaned_data['usuario'].email],
                fail_silently=False,
            )
            return JsonResponse({'mensaje': "Mensaje Enviado!"})
        if not form.is_valid():
            usuario_errors = form.errors.as_data().get('usuario')
            print("usuario_errors", usuario_errors)
            if usuario_errors:
                print("Codigo", usuario_errors[0].code)
        
    else:
        #EN caso cuya solicitud no sea POST
        form = FormCorreo()
    return render(request, 'correo.html', {'form': form})

