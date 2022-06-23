from django.urls import path
from App import views
urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('personas/',views.personas,name="Personas"),
    path('trabajos/',views.trabajos,name="Trabajos"),
    path('hobbies/',views.hobbies,name="Hobbies"),
    #path('personasFormulario/',views.personasFormulario,name="PersonasFormulario"),

]