from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()


class TrabajoFormulario(forms.Form):
    trabajo = forms.CharField(max_length=40)


class HobbyFormulario(forms.Form):
    hobby= forms.CharField(max_length=40)    

