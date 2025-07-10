"""
Autor: Petrus
Propósito: Funções auxiliares de utilidade geral, como resetar o banco de dados.
"""

# Função para recriar o banco de dados
def recriar_db():
    """
    Deleta o banco, recria as tabelas e popula com dados iniciais.
    """
    import os
    from app.db         import criar_tabelas
    from app.users      import add_user
    from app.categories import add_categoria

    caminho_db = "data/financas.db"
    if os.path.exists(caminho_db):
        os.remove(caminho_db)
        print("🗑️ Banco de dados removido com sucesso!")
    else:
        print("⚠️ Banco de dados não encontrado para resetar.")

    # Agora sim: cria estrutura nova
    criar_tabelas()

    print("🚀 Inserindo dados iniciais...")

    # Usuários
    add_user("Petrus", "PP",     "🧔")
    add_user("Mel",    "_memel", "👩")
    add_user("Casal",  "nos2",   "💑")

    # Categorias
    categorias = [
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
    for nome, metodo in categorias:
        add_categoria(nome, metodo)

    print("✅ Banco recriado e dados inseridos com sucesso!")

# Função para exibir uma tabela formatada no console
def exibir_tabela(titulo, dados, colunas):
    """
    Exibe uma tabela formatada no console com cabeçalhos alinhados.
    """
    
    if not dados:
        print(f"\n⚠️ Nenhum dado encontrado para '{titulo}'.\n")
        return

    # Calcular larguras para cada coluna
    larguras = {}
    for col in colunas:
        maior_conteudo = max(len(str(linha[col])) for linha in dados)
        larguras[col] = max(len(col), maior_conteudo) + 2
    cabecalho = "  ".join(col.upper().ljust(larguras[col]) for col in colunas)

    # Título
    print(f"\n{titulo.upper().center(len(cabecalho))}")

    # Cabeçalho
    print("-" * len(cabecalho))
    print(cabecalho)
    print("-" * len(cabecalho))

    # Conteúdo
    for linha in dados:
        linha_formatada = []

        for col in colunas:
            valor = linha[col]
        
            if col == "compartilhada":
                valor = "Sim" if valor else "Não"

            elif isinstance(valor, str) and col not in ['nome', 'usuario']:
                valor = valor.capitalize()
            
            elif isinstance(valor, float):
                valor = f"{valor:.2f}".replace('.', ',')  # se quiser decimal bonito
            
            valor_formatado = str(valor).ljust(larguras[col])
            linha_formatada.append(valor_formatado)
            
        print("  ".join(linha_formatada))
    print("-" * len(cabecalho))

    print()

# Função para popular o banco com dados iniciais
def popular_db():
    from app.users      import add_user
    from app.categories import add_categoria
    
    print("🚀 Inserindo dados iniciais...")

    # Usuários fictícios
    add_user("Petrus", "PP",     "🧔")
    add_user("Mel",    "_memel", "👩")
    add_user("Casal",  "nos2",   "💑")

    # Categorias padrão
    categorias = [
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

    for nome, metodo in categorias:
        add_categoria(nome, metodo)

    print("✅ Dados inseridos com sucesso!")

# Função para validar e formatar uma data
def validar_data(texto=None):
    """
    Solicita uma data do usuário e valida.
    Retorna no formato 'YYYY-MM-DD'.
    Se 'texto' for passado, valida direto.
    """
    from datetime import datetime

    formatos_validos = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%Y.%m.%d", "%d-%m-%Y"]

    while True:
        if not texto:
            texto = input("📅 Data (YYYY-MM-DD ou DD/MM/AAAA): ").strip()

        for fmt in formatos_validos:
            try:
                dt = datetime.strptime(texto, fmt)
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                continue

        print("❌ Data inválida. Tente novamente.\n")
        texto = None  # força novo input

