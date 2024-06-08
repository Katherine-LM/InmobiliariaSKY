from django.contrib import admin
from django.urls import include, path
from propiedades import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('propiedades.urls')),
    path('get-comunas/<int:region_id>/', views.get_comunas, name='get_comunas'),

    ]

