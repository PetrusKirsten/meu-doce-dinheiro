"""
Autor: Petrus
Propósito: Funções auxiliares de utilidade geral, como resetar o banco de dados.
"""

def reset_db():
    from app.db         import get_cursor
    from app.users      import add_user
    from app.categories import add_categoria

    conn, cursor = get_cursor()

    # Limpa todas as tabelas
    tabelas = ['transacoes', 'planejamentos', 'usuarios', 'categorias']
    for tabela in tabelas:
        cursor.execute(f"DELETE FROM {tabela}")
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{tabela}'")  # reseta AUTOINCREMENT
    conn.commit()
    print("\n🧹 Tabelas limpas e IDs resetados.\n")

    # Recria usuários iniciais
    add_user("PP",    "petrus279", None)
    add_user("Memel", "_memel", None)

    # Recria categorias
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
    for nome, metodo in categorias_padrao:
        add_categoria(nome, metodo)
    print("\n📦 Dados padrão recriados com sucesso!")
    
    conn.close()


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
        
            if isinstance(valor, str) and col not in ['nome', 'usuario']:
                valor = valor.capitalize()
            
            elif isinstance(valor, float):
                valor = f"{valor:.2f}".replace('.', ',')  # se quiser decimal bonito
            
            valor_formatado = str(valor).ljust(larguras[col])
            linha_formatada.append(valor_formatado)
            
        print("  ".join(linha_formatada))
    print("-" * len(cabecalho))

    print()
