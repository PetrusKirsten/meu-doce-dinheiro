"""
app.py

Autor: Petrus
Propósito: Arquivo principal com interface de terminal para o sistema 'Meu Doce Dinheiro'.
Permite listar usuários, categorias e transações, adicionar novas transações,
e gerenciar o banco de dados local de forma interativa.

Execução: python app.py
"""


from app.db           import criar_tabelas
from app.utils        import reset_db, popular_db, exibir_tabela
from app.users        import get_users
from app.categories   import get_categories
from app.transactions import listar_transacoes, add_transacao

def menu():
    while True:
        print("\n📊 MENU - Meu Doce Dinheiro")
        print("----------------------------")
        print("1. Listar usuários")
        print("2. Listar categorias")
        print("3. Listar transações")
        print("4. Adicionar transação")
        print("5. Resetar banco e popular dados")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            usuarios = get_users()
            exibir_tabela("Usuários", usuarios, ["id", "nome", "usuario"])
        
        elif escolha == "2":
            categorias = get_categories()
            exibir_tabela("Categorias", categorias, ["id", "nome", "metodo_pgto"])

        elif escolha == "3":
            transacoes = listar_transacoes()
            exibir_tabela("Transações", transacoes, [
                "id", "valor", "tipo", "forma_pagamento",
                "data", "descricao", "usuario", "categoria", "compartilhada"
            ])
        
        elif escolha == "4":
            try:
                valor         = float(input("Valor: R$ "))
                tipo          = input("Tipo (renda/despesa): ").strip().lower()
                forma         = input("Forma de pagamento: ").strip().lower()
                descricao     = input("Descrição: ")
                data          = input("Data (YYYY-MM-DD): ")
                usuario_id    = int(input("ID do usuário: "))
                categoria_id  = int(input("ID da categoria: "))
                compartilhada = input("Compartilhada? (s/n): ").strip().lower() == "s"

                add_transacao(
                    valor,
                    tipo, 
                    forma, 
                    descricao,
                    data,
                    usuario_id, 
                    categoria_id,
                    compartilhada
                )

            except Exception as e:
                print("❌ Erro ao adicionar transação:", e)

        elif escolha == "5":
            reset_db()
            criar_tabelas()
            popular_db()

        elif escolha == "0":
            print("👋 Até mais!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
