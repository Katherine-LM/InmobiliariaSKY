from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EditarPerfilForm, PropiedadForm
from .models import Propiedad
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'lista_propiedades.html', {'propiedades': propiedades})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

def nuevo_inmueble(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmueble agregado con éxito.')
            return redirect('lista_propiedades')
    else:
        form = PropiedadForm()
    return render(request, 'nuevo_inmueble.html', {'form': form})

@login_required
def editar_inmueble(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inmueble actualizado con éxito.')
            return redirect('lista_propiedades')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'editar_inmueble.html', {'form': form})

@login_required
def borrar_inmueble(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        propiedad.delete()
        messages.success(request, 'Inmueble borrado con éxito.')
        return redirect('lista_propiedades')
    return render(request, 'borrar_inmueble.html', {'propiedad': propiedad})
