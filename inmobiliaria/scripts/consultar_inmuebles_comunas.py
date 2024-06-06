import os
import sys
import django

# Añadir la ruta del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("sys.path:", sys.path)  # Línea de depuración para verificar las rutas

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria.settings')
print("Configurando Django...")
django.setup()
print("Django configurado correctamente.")

# Importa los modelos necesarios
try:
    from propiedades.models import Inmueble, Comuna
    print("Modelos importados correctamente.")
except Exception as e:
    print(f"Error al importar modelos: {e}")

# Abre un archivo de texto para escribir la información
try:
    with open('inmuebles_por_comunas.txt', 'w', encoding='utf-8') as file:
        print("Archivo abierto correctamente.")
        for comuna in Comuna.objects.all():
            print(f"Procesando comuna: {comuna.nombre}")
            file.write(f'Comuna: {comuna.nombre}\n')
            inmuebles = Inmueble.objects.filter(comuna=comuna, disponible=True).values('nombre', 'descripcion')
            for inmueble in inmuebles:
                file.write(f"  Nombre: {inmueble['nombre']}\n")
                file.write(f"  Descripción: {inmueble['descripcion']}\n")
                print(f"  Escribiendo inmueble: {inmueble['nombre']}")
            file.write('\n')
    print("Archivo inmuebles_por_comunas.txt creado correctamente.")
except Exception as e:
    print(f"Error al escribir en el archivo: {e}")
