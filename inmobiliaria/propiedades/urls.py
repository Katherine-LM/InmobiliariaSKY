from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista_propiedades, name='lista_propiedades'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('nuevo-inmueble/', views.nuevo_inmueble, name='nuevo_inmueble'),  # Ruta para agregar inmuebles
    path('editar-inmueble/<int:pk>/', views.editar_inmueble, name='editar_inmueble'),  # Ruta para editar inmuebles
    path('borrar-inmueble/<int:pk>/', views.borrar_inmueble, name='borrar_inmueble'),  # Ruta para borrar inmuebles
]
