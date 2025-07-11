"""
app.py

Autor: Petrus
Propósito: Arquivo principal com interface de terminal para o sistema 'Meu Doce Dinheiro'.
Permite listar usuários, categorias e transações, adicionar novas transações,
e gerenciar o banco de dados local de forma interativa.

Execução: python app.py
"""

import time
import unicodedata

# Importa módulos internos do app
from backend.app.scripts.db           import criar_tabelas
from app.utils        import exibir_tabela, validar_data
from app.users        import get_users
from app.categories   import get_categories
from app.transactions import get_transactions, add_transacao

# Definições de tipos de transações
FORMAS_PGTO_VALIDAS = ["débito", "crédito", "pix", "dinheiro", "outro"]

# Inicializa o banco e garante que as tabelas existam
criar_tabelas()

# ==================
# Funções auxiliares
# ==================

# Função para mostrar boas-vindas e informações do aplicativo
def init_banner():
    from config import NOME_APP, VERSAO, DESCRICAO, AUTOR

    print("\n" + "-"*58)
    print(f"🧾  {NOME_APP.upper()} - v{VERSAO}")
    print(f"👤  Autor: {AUTOR}")
    print(f"📝  {DESCRICAO}")
    print("-"*58 + "\n")

    time.sleep(0.5)

# Função para normalizar texto (remover acentos e converter para minúsculo)
def normalizar(texto):
    """Remove acentos e converte pra minúsculo."""
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode().lower()

# Função para escolher uma opção de lista
def escolher_opcao(nome_campo, opcoes_validas):
    """
    Solicita ao usuário um valor, validando contra uma lista de opções válidas.
    Aceita variações sem acento ou maiúsculas.
    Retorna a string padronizada encontrada.
    """

    while True:
        entrada = input(f"🔸 {nome_campo}: ").strip().lower(); print("-"*40)
        entrada_normalizada = normalizar(entrada)

        for opcao in opcoes_validas:
            if normalizar(opcao) == entrada_normalizada:
                return opcao  # ✅ retorna a string original da lista

        print(f"\n❌ {nome_campo} inválido. Opções válidas:")
        for opcao in opcoes_validas:
            print(f"   • {opcao.capitalize()}")
        print()

# Função para escolher um item de uma lista de dicionários
def escolher_item(titulo, lista, campo_busca=["nome"], campo_retorno="id", mostrar_tabela=None):
    """
    Permite ao usuário escolher um item de uma lista de dicionários digitando um valor de busca.

    Parâmetros:
    - titulo: nome exibido ao usuário ("Usuário", "Categoria", etc.)
    - lista: lista de dicionários (ex: [{"id": 1, "nome": "Petrus", "usuario": "PP"}])
    - campo_busca: campos aceitos como entrada (ex: ["nome", "usuario"])
    - campo_retorno: valor retornado (normalmente o "id")
    - mostrar_tabela: função de exibição (ex: exibir_tabela), chamada em caso de erro
    """
    
    while True:
        entrada = input(f"🔸 {titulo}: ").strip().lower(); print("-"*40)
        entrada_normalizada = normalizar(entrada)


        for item in lista:
            for campo in campo_busca:
                if entrada_normalizada == normalizar(str(item[campo]).lower()):
                    return item[campo_retorno]

        print(f"\n❌ {titulo} não encontrado. Tente novamente.")
        if mostrar_tabela:
            mostrar_tabela(titulo, lista, list(lista[0].keys()))
        print()

# ====================================
# Função principal do menu interativo
# ====================================
def menu():
    while True:
        time.sleep(1)

        print("="*40)
        print("💰  MEU DOCE DINHEIRO - MENU PRINCIPAL")
        print("="*40)
        print("1️⃣  Listar usuários")
        print("2️⃣  Listar categorias")
        print("3️⃣  Listar transações")
        print("4️⃣  Adicionar transação")
        print("5️⃣  Resetar banco e popular dados")
        print("0️⃣  Sair")
        print("-"*40)

        escolha = input("🔸 Escolha uma opção: ").strip(); print("-"*40)

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

                valor         = float(input("💸 Valor (R$): ")); print("-"*40)
                tipo          = input("📌 Tipo (renda/despesa): ").strip().lower(); print("-"*40)
                forma_pgto    = escolher_opcao("Forma de pagamento", FORMAS_PGTO_VALIDAS)
                usuario_id    = escolher_item(
                    titulo         = "Usuário",
                    lista          = get_users(),
                    campo_busca    = ["nome", "usuario"],
                    campo_retorno  = "id",
                    mostrar_tabela = exibir_tabela)
                categoria_id  = escolher_item(
                    titulo         = "Categoria",
                    lista          = get_categories(),
                    campo_busca    = ["nome"],
                    campo_retorno  = "id",
                    mostrar_tabela = exibir_tabela)
                descricao     = input("📝 Descrição: "); print("-"*40)
                data          = validar_data(); print("-"*40)
                compartilhada = input("🤝 Compartilhada? (s/n): ").strip().lower() == "s"; print("-"*40)

                add_transacao(
                    valor,
                    tipo,
                    forma_pgto,
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
            print()

        elif escolha == "0":
            print("💚 Obrigado por usar o Meu Doce Dinheiro\n" \
                  "👋 Até mais!"); print("-"*40)
            time.sleep(1)
            print()
            break

        else:
            print("❌ Opção inválida. Tente novamente."); print("-"*40)


if __name__ == "__main__":
    init_banner()
    menu()
