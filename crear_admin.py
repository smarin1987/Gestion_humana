import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion.settings')

def reset_superuser():
    try:
        import django
        django.setup()
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Eliminar usuario existente si hay alguno
        User.objects.filter(username='smarin').delete()
        
        # Crear superusuario con TUS credenciales
        User.objects.create_superuser(
            username='smarin',
            email='smarin@ambientesled.com',
            password='Sebasmaria*1**'
        )
        print("✅ Superusuario CREADO: Usuario: smarin | Contraseña: Sebasmaria*1**")
    except Exception as e:
        print(f"❌ Error creando usuario: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    print("⚙️ Ejecutando migraciones...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("⚙️ Creando superusuario...")
    reset_superuser()
