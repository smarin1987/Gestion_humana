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
        
        # Verificamos si el usuario ya existe para no duplicar
        if not User.objects.filter(username='admin').exists():
            # Usamos variables de entorno para mayor seguridad
            admin_email = os.getenv('ADMIN_EMAIL', 'admin@midominio.com')
            admin_password = os.getenv('ADMIN_PASSWORD', 'TempPassword123')
            
            User.objects.create_superuser(
                username='admin',
                email=admin_email,
                password=admin_password
            )
            print("✅ Superusuario creado exitosamente")
        else:
            print("ℹ️ El superusuario ya existe")
    except Exception as e:
        print(f"❌ Error creando superusuario: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    # Primero ejecutamos las migraciones (importante)
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Luego creamos el superusuario
    create_superuser()
