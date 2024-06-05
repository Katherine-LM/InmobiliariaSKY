from django.shortcuts import render
from .models import Propiedad

def index(request):
    return render(request, 'index.html')

def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedades/lista_propiedades.html', {'propiedades': propiedades})
