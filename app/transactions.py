"""
Autor: Petrus Kirsten
Propósito: Funções para registrar, listar e filtrar transações financeiras (despesas e receitas).
"""

from app.db     import get_cursor
from app.utils  import exibir_tabela


def get_transacoes():
    conn, cursor = get_cursor()

    cursor.execute("""
        SELECT
            t.id,
            t.valor,
            t.tipo,
            t.tipo,
            t.data,
            t.descricao,
            t.compartilhada,
            u.nome AS usuario,
            c.nome AS categoria
        FROM transacoes t
        JOIN usuarios u ON t.usuario_id = u.id
        JOIN categorias c ON t.categoria_id = c.id
        ORDER BY t.data DESC
    """)

    transacoes = cursor.fetchall()
    conn.close()

    exibir_tabela("Transações", transacoes, [
        "id", "valor", "tipo", "tipo",
        "data", "descricao", "usuario", "categoria", "compartilhada"
    ])
    
    return transacoes
