"""
app.py

Autor: Petrus
Propósito: Arquivo principal com interface de terminal para o sistema 'Meu Doce Dinheiro'.
Permite listar usuários, categorias e transações, adicionar novas transações,
e gerenciar o banco de dados local de forma interativa.

Execução: python app.py
"""


from app.db           import criar_tabelas
from app.utils        import popular_db, exibir_tabela
from app.users        import get_users
from app.categories   import get_categories
from app.transactions import get_transactions, add_transacao

# Inicializa o banco e garante que as tabelas existam
criar_tabelas()


def menu():
    while True:
        print("\n" + "="*40)
        print("💰  MEU DOCE DINHEIRO - MENU PRINCIPAL")
        print("="*40)
        print("1️⃣  Listar usuários")
        print("2️⃣  Listar categorias")
        print("3️⃣  Listar transações")
        print("4️⃣  Adicionar transação")
        print("5️⃣  Resetar banco e popular dados")
        print("0️⃣  Sair")
        print("-"*40)

        escolha = input("🔸 Escolha uma opção: ").strip()

        if escolha == "1":
            usuarios = get_users()
            exibir_tabela("Usuários", usuarios, ["id", "nome", "usuario"])
        
        elif escolha == "2":
            categorias = get_categories()
            exibir_tabela("Categorias", categorias, ["id", "nome", "metodo_pgto"])

        elif escolha == "3":
            print("\n🔎 Filtros para listar transações (pressione Enter para ignorar)")
            
            try:
                usuario_id = input("🙋 ID do usuário: ").strip()
                usuario_id = int(usuario_id) if usuario_id else None

                mes = input("📅 Mês (formato YYYY-MM): ").strip()
                mes = mes if mes else None

                tipo = input("📌 Tipo (renda/despesa): ").strip().lower()
                tipo = tipo if tipo else None

                forma_pgto = input("💳 Forma de pagamento: ").strip().lower()
                forma_pgto = forma_pgto if forma_pgto else None

                compartilhada = input("🤝 Compartilhada? (s/n): ").strip().lower()
                if compartilhada == "s":
                    compartilhada = True

                elif compartilhada == "n":
                    compartilhada = False

                else:
                    compartilhada = None

                transacoes = get_transactions(
                    usuario_id      = usuario_id,
                    tipo            = tipo,
                    mes             = mes,
                    forma_pagamento = forma_pgto,
                    compartilhada   = compartilhada
                )

                exibir_tabela("Transações Filtradas", transacoes, [
                    "id", "valor", "tipo", "forma_pagamento",
                    "data", "descricao", "usuario", "categoria", "compartilhada"
                ])

            except Exception as e:
                print("❌ Erro ao aplicar filtros:", e)

        elif escolha == "4":
            try:
                print("\n📥 Adicionar nova transação")
                print("-"*40)

                valor         = float(input("💸 Valor (R$): "))
                tipo          = input("📌 Tipo (renda/despesa): ").strip().lower()
                forma         = input("💳 Forma de pagamento: ").strip().lower()
                descricao     = input("📝 Descrição: ")
                data          = input("📅 Data (YYYY-MM-DD): ")

                usuarios   = get_users()
                usuario_id = None
                while usuario_id is None:
                    usuario_input = input("🙋 Digite o nome ou usuário: ").strip().lower()
                    usuario_id    = next(
                        (u["id"] for u in usuarios 
                         if usuario_input in [u["nome"].lower(), u["usuario"].lower()]),
                        None)
                    if usuario_id is None:
                        print("❌ Usuário não encontrado. Veja a lista disponível:\n")
                        exibir_tabela("Usuários", usuarios, ["id", "nome", "usuario"])
                
                categorias   = get_categories()
                categoria_id = None
                while categoria_id is None:
                    categoria_input = input("🏷️  Digite o nome da categoria: ").strip().lower()
                    categoria_id    = next(
                        (c["id"] for c in categorias 
                            if categoria_input == c["nome"].lower()),
                        None)
                    if categoria_id is None:
                        print("❌ Categoria não encontrada. Veja a lista disponível:\n")
                        exibir_tabela("Categorias", categorias, ["id", "nome", "metodo_pgto"])

                compartilhada = input("🤝 Compartilhada? (s/n): ").strip().lower() == "s"

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
            from app.utils import recriar_db
            print("\n⚠️  Resetando banco de dados...")
            recriar_db()

        elif escolha == "0":
            print("\n👋 Até mais! Obrigado por usar o Meu Doce Dinheiro.")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
