import os
import sys
import django
from django.core.management import execute_from_command_line

# Configuración esencial
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion.settings')
django.setup()

def crear_superusuario():
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Eliminar usuario existente si existe
        User.objects.filter(username='smarin').delete()
        
        # Crear superusuario con tus credenciales
        User.objects.create_superuser(
            username='smarin',
            email='smarin@ambientesled.com',
            password='Sebasmaria*1**'
        )
        print("✅ Superusuario CREADO CON ÉXITO")
        print("Usuario: smarin")
        print("Contraseña: Sebasmaria*1**")
        return True
    except Exception as e:
        print(f"❌ Error creando superusuario: {str(e)}")
        return False

if __name__ == '__main__':
    print("⚙️ Ejecutando migraciones...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    if crear_superusuario():
        sys.exit(0)
    else:
        sys.exit(1)
