from app.users import add_user, get_users
from app.db import create_tables

if __name__ == "__main__":
    create_tables()

    # Mostrar usuários
    print("\n📋 Usuários cadastrados:")
    get_users()
