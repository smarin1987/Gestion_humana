import os
import sys
from django.core.management import execute_from_command_line

# Configuración básica de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion.settings')

def create_superuser():
    try:
        import django
        django.setup()
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Eliminar usuario existente si hay alguno (evita duplicados)
        User.objects.filter(username='smarin').delete()
        
        # Crear superusuario con TUS credenciales exactas
        User.objects.create_superuser(
            username='smarin',
            email='smarin@ambientesled.com',
            password='Sebasmaria*1**'
        )
        print("✅ Superusuario creado EXITOSAMENTE con estas credenciales:")
        print("Usuario: smarin")
        print("Contraseña: Sebasmaria*1**")
        print("\n⚠️ IMPORTANTE: Después de acceder, cambia la contraseña en el panel admin")
    except Exception as e:
        print(f"❌ Error creando superusuario: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    # Ejecutar migraciones primero (IMPORTANTE)
    print("⚙️ Ejecutando migraciones...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Luego crear el superusuario
    print("⚙️ Creando superusuario...")
    create_superuser()
