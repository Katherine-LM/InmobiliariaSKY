from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EditarPerfilForm
from .models import Propiedad

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
