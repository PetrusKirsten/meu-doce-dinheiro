"""
Autor: Petrus Kirsten
Propósito: Funções para registrar, listar e filtrar transações financeiras (despesas e receitas).
"""

from backend.app.scripts.db import get_cursor


def add_transacao(valor, 
                  tipo,
                  forma_pagamento, 
                  descricao, 
                  data, 
                  usuario_id, 
                  categoria_id, 
                  compartilhada=False):
    """Adiciona uma nova transação financeira."""

    # Validações básicas
    if tipo not in ("renda", "despesa"):
        print("❌ Tipo inválido. Use 'renda' ou 'despesa'.")
        return

    formas_validas = ("débito", "crédito", "pix", "dinheiro", "outro")
    if forma_pagamento not in formas_validas:
        print(f"❌ Forma de pagamento inválida. Use: {', '.join(formas_validas)}.")
        return

    try:
        conn, cursor = get_cursor()
        cursor.execute("""
            INSERT INTO transacoes (
                valor, tipo, forma_pagamento,
                descricao, data, compartilhada,
                usuario_id, categoria_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            valor,
            tipo,
            forma_pagamento,
            descricao,
            data,
            int(compartilhada),
            usuario_id,
            categoria_id
        ))
        conn.commit()
        conn.close()
        print("✅ Transação adicionada com sucesso!")

    except Exception as e:
        print("❌ Erro ao adicionar transação:", e)


def get_transactions(usuario_id=None, tipo=None, mes=None, forma_pagamento=None, compartilhada=None):
    """
    Lista transações com filtros opcionais.
    """

    conn, cursor = get_cursor()

    # Monta a query base
    query = """
        SELECT
            t.id,
            t.valor,
            t.tipo,
            t.forma_pagamento,
            t.data,
            t.descricao,
            t.compartilhada,
            u.nome AS usuario,
            c.nome AS categoria
        FROM transacoes t
        JOIN usuarios u ON t.usuario_id = u.id
        JOIN categorias c ON t.categoria_id = c.id
        WHERE 1 = 1
    """
    parametros = []

    # Filtros opcionais
    if usuario_id:
        query += " AND t.usuario_id = ?"
        parametros.append(usuario_id)

    if tipo:
        query += " AND t.tipo = ?"
        parametros.append(tipo)

    if forma_pagamento:
        query += " AND t.forma_pagamento = ?"
        parametros.append(forma_pagamento)

    if compartilhada is not None:
        query += " AND t.compartilhada = ?"
        parametros.append(int(compartilhada))

    if mes:
        query += " AND strftime('%Y-%m', t.data) = ?"
        parametros.append(mes)

    query += " ORDER BY t.data DESC"

    cursor.execute(query, parametros)
    
    colunas = [col[0] for col in cursor.description]
    dados   = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    
    conn.close()
    
    return dados

