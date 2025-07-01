"""
Autor: Petrus Kirsten
Propósito: Arquivo principal para executar e testar as funcionalidades do sistema.
"""

from app.db           import criar_tabelas
from app.utils        import reset_db, popular_db
from app.users        import get_users
from app.categories   import get_categories
from app.transactions import get_transacoes


if __name__ == "__main__":
    # reset_db()
    # popular_db()
    criar_tabelas()

    get_users()    
    get_categories()
    get_transacoes()
