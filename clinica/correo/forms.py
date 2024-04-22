from django import forms
from django.core.validators import validate_email, MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
#from clinica.wsgi import *
#from tienda.models import Categoria, Producto, Pedido, DetallePedido

class FormCorreo(forms.Form):
    
    nombre = forms.CharField(
        label = "Nombre Completo", 
        max_length=100,
        validators=[MinLengthValidator(3)],
        required=True,
        error_messages={
            'required': 'El nombre es un campo requerido. Agrega un nombre valido',
            'min_lenght': 'El nombre debe tener al menos 3 caracteres.'
        })
    
    email = forms.EmailField(
        label = "Correo alternativo",
        error_messages={
            'invalid': 'Ingrese una direccion de correo electronico valida'
        },
        required = False
        )
    mensaje = forms.CharField(
        label = "Mensaje",
        widget=forms.Textarea,
        error_messages={
            'required': 'El mensaje es un campo requerido'
        })
    
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    latitud = forms.DecimalField(max_digits=10, decimal_places=7, required=True)
    longitud = forms.DecimalField(max_digits=10, decimal_places=7, required=True)
    #categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    
    #METODO INIT
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['mensaje'].widget.attrs.update({'class': 'form-control'})
        self.fields['usuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitud'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitud'].widget.attrs.update({'class': 'form-control'})
        
        
        #self.fields['nombre'].label_suffix = ': *'
        for field_name, field in self.fields.items():
            print(field_name)
            if field.required:
                field.label_suffix = ': *'
                
    #METODO CLEANED  
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        mensaje = cleaned_data.get('mensaje')
        usuario = cleaned_data.get('usuario')
        
        if not nombre and not mensaje and not usuario:
            raise forms.ValidationError("Debe ingresar al menos uno de los campos!")
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if "example.com" in email:
            raise forms.ValidationError("No se permiten correos de example.com")
        return  email   

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        if "spam" in mensaje:
            raise forms.ValidationError("No se permite la palabra Spam en el mensaje")
        elif len(mensaje) < 10:
            raise forms.ValidationError("El emnsaje debe tener al menos 10 caracteres")
        elif len(mensaje) > 100:
            raise forms.ValidationError("El emnsaje no puede tener mas de 100 caracteres")
        return mensaje
    
    def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        if not usuario:
            raise forms.ValidationError("El usuario para envio de correo es necesario!", code='usuario_necesario')
        if not usuario.is_active:
            raise forms.ValidationError("El usuario seleccionado no esta activo.", code="usuario_inactivo")
       # if usuario.username.startwith('admin'):
        #    raise forms.ValidationError("No se permite enviar correo con nombre de usuario que comience con admin", code='usuario_admin')
        
        
        
        
    def clean_latitud(self):
        latitud = self.cleaned_data['latitud']
        if latitud is not None:
            if latitud < -90:
                raise forms.ValidationError("La latitud no puede ser menor a -90")
            if latitud > 90:
                raise forms.ValidationError("La latitud no puede ser mayor a 90")
            
        return latitud
    
    
    def cleen_longitud(self):
        longitud = self.cleaned_data['longitud']
        if longitud is not None:
            if longitud < -180:
                raise forms.ValidationError("La longitud no puede ser menor a -180")
            if longitud > 180:
                raise forms.ValidationError("La longitud no puede ser mayor a 180")
            
        return longitud
