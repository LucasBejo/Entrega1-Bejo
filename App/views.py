from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *
# Create your views here.

def inicio(request):
    
    return render(request,"App/inicio.html")


def personas(request):
    if request.method == 'POST':

        miFormulario = PersonaFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
          informacion = miFormulario.cleaned_data

          persona = Persona (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'],
          fecha_nacimiento=informacion['fecha_nacimiento'])
        
          persona.save()
        
          return render(request,"App/inicio.html")
    else:
        miFormulario=PersonaFormulario()
    
    return render(request,"App/personas.html", {"miFormulario":miFormulario})




def trabajos(request):
    if request.method == 'POST':

        miFormulario = TrabajoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
          informacion = miFormulario.cleaned_data

          trabajo = Trabajo (trabajo=informacion['trabajo'])
        
          trabajo.save()
        
          return render(request,"App/inicio.html")
    else:
        miFormulario=TrabajoFormulario()
    
    
    return render(request,"App/trabajos.html", {"miFormulario":miFormulario}) 




def hobbies(request):
    if request.method == 'POST':

        miFormulario = HobbyFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
          informacion = miFormulario.cleaned_data

          hobby = Hobby (hobby=informacion['hobby'])
        
          hobby.save()
        
          return render(request,"App/inicio.html")
    else:
        miFormulario=HobbyFormulario()
    
    return render(request,"App/hobbies.html", {"miFormulario":miFormulario})


   