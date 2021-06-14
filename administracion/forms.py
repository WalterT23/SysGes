from administracion.models import Rol
from django import forms
from django.forms import fields, widgets
#from django.contrib.auth import forms
from django.contrib import *
class RolForm(forms.Form):
    
    class Meta:
        #aqui SE LE INDICA DE QUE MODELO VA SER EL FORMULARIO
        model= Rol

        #aqui ponemos los campos que vamos a utilizar
        """
            Si van a utilizar todos los campos del modelo basta con hacer : fields = '__all__'  y listo.
        """
        fields=[
            '__all__'
            
        ]

        #aqui ponemos las etiquetas (titulos) que van a tener los campos
        labels = {
            'id' : 'Id',
            'tipo' : 'Acción'
        }

        #aqui pondremos los que se van a pintar como etiquetas de HTML
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'})
            #cuando va ser un select se pone asi : forms.Select(attrs={'class':'form-control'})
            #cuando es un campo many yo many se pone asi: forms.CheckboxSelectMultiple() 
        }

