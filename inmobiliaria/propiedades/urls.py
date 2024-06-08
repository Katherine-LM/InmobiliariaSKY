from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista_propiedades, name='lista_propiedades'),
    path('nuevo-inmueble/', views.nuevo_inmueble, name='nuevo_inmueble'),
    path('get-comunas/<int:region_id>/', views.get_comunas, name='get_comunas'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('borrar-inmueble/<int:pk>/', views.borrar_inmueble, name='borrar_inmueble'),
    path('editar-inmueble/<int:pk>/', views.editar_inmueble, name='editar_inmueble'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)