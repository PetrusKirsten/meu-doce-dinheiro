"""
Autor: Petrus Kirsten
Propósito: Arquivo principal para executar e testar as funcionalidades do sistema.
"""

from app.db         import criar_tabelas
from app.categories import get_categories
from app.users      import get_users


if __name__ == "__main__":
    criar_tabelas()

    get_users()    
    get_categories()
