from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista_propiedades, name='lista_propiedades'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
]
