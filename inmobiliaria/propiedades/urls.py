from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista_propiedades, name='lista_propiedades'),
]