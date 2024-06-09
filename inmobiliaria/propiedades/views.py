from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import RegistroForm, EditarPerfilForm, PropiedadForm
from .models import Propiedad, Region, Comuna
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def lista_propiedades(request):
    region_id = request.GET.get('region', '0')
    comuna_id = request.GET.get('comuna', '0')
    
    propiedades = Propiedad.objects.all()
    
    if region_id != '0':
        propiedades = propiedades.filter(comuna__region_id=region_id)
        comunas = Comuna.objects.filter(region_id=region_id)
    else:
        comunas = Comuna.objects.all()
    
    if comuna_id != '0':
        propiedades = propiedades.filter(comuna_id=comuna_id)

    regiones = Region.objects.all()
    
    return render(request, 'lista_propiedades.html', {
        'propiedades': propiedades,
        'regiones': regiones,
        'comunas': comunas,
        'selected_region': int(region_id) if region_id != '0' else None,
        'selected_comuna': int(comuna_id) if comuna_id != '0' else None,
    })

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
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

@login_required
def nuevo_inmueble(request):
    if request.method == "POST":
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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

def get_comunas(request, region_id):
    comunas = list(Comuna.objects.filter(region_id=region_id).values('id', 'nombre'))
    return JsonResponse({'comunas': comunas})
