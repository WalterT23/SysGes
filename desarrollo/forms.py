from django import forms

class FormularioCrearProyecto(forms.Form):
    titulo= forms.CharField(label='Nombre',max_length=50, required=True)
    descripcion= forms.CharField(label='Descripción ',widget=forms.Textarea)
    fecha_inicio=forms.DateTimeField(required=True)
    fecha_fin=forms.DateTimeField()