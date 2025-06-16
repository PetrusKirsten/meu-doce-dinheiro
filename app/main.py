from app.db         import connect, criar_tabelas
from app.categories import add_categoria, get_categories
from app.users      import listar_users


if __name__ == "__main__":
    criar_tabelas()

    # Mostrar usuários
    print("\n📋 Usuários cadastrados:")
    listar_users()
    
    # Adicionar categorias
    categorias_padrao = [
        ("Alimentação",     "ambos"),
        ("Investimentos",   "débito"),
        ("Moradia",         "ambos"),
        ("Pessoal",         "ambos"),
        ("Presentes",       "ambos"),
        ("Saúde",           "ambos"),
        ("Taxas",           "ambos"),
        ("Transporte",      "ambos"),
        ("Viagens",         "ambos"),
        ("Casamento",       "ambos"),
        ("Pgto. de fatura", "débito"),
        ("Pagamento",       "ambos"),
        ("Juros",           "ambos"),
        ("Outros",          "ambos")
    ]
    for name, tipo_pagamento in categorias_padrao:
        add_categoria(name, tipo_pagamento)

    # Mostrar categorias
    get_categories()
