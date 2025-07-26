import os
import shutil
import django
import sys

confirm = input("⚠️ Tem certeza que deseja apagar o banco e as migrations? Digite 'apagar' para confirmar: ")

if confirm.lower() != "apagar":
    print("❌ Operação cancelada.")
    sys.exit()

# Remove o banco de dados
try:
    os.remove("db.sqlite3")
    print("🗑️ Banco de dados removido.")
except FileNotFoundError:
    print("⚠️ Banco de dados não encontrado.")
except PermissionError:
    print("🚫 Não foi possível remover o banco. Feche o servidor e tente novamente.")
    sys.exit()

# Remove arquivos de migrations (exceto __init__.py)
for root, dirs, files in os.walk(".", topdown=False):
    if "migrations" in dirs:
        mig_path = os.path.join(root, "migrations")
        for f in os.listdir(mig_path):
            if f != "__init__.py" and f.endswith(".py"):
                os.remove(os.path.join(mig_path, f))
        for f in os.listdir(mig_path):
            if f.endswith(".pyc"):
                os.remove(os.path.join(mig_path, f))
        print(f"📂 Migrations limpas em: {mig_path}")

# Recria as migrations e aplica
print("🔄 Rodando makemigrations e migrate...")
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

# Setup do Django para criar superusuário direto no script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="james").exists():
    User.objects.create_superuser("james", "james@james.com", "1234")
    print("✅ Superusuário criado: james / 1234")
else:
    print("ℹ️ Usuário 'james' já existe.")

print("🚀 Tudo pronto. Rode o servidor com: python manage.py runserver")
