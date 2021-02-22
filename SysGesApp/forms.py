from django import forms
#crear una clase cuya instancia sera el nombre del formulario que queremos

class FormularioDesarrollo(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()
    