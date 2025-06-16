from app.db import get_cursor


def add_categoria(name, metodo_pgto):
    """Adiciona uma nova categoria ao banco de dados."""

    conn, cursor = get_cursor()

    try:
        cursor.execute(
            """
            INSERT INTO categorias (nome, metodo_pgto)
            VALUES (?, ?)
            """,
            (name, metodo_pgto)
        )
        conn.commit()
        print(f"✅ Categoria '{name}' adicionada!")

    except Exception as e:
        print(f"❌ Erro ao adicionar categoria: {e}")

    finally:
        conn.close()


def get_categories():
    """Lista todas as categorias cadastradas."""

    conn, cursor = get_cursor()

    cursor.execute("SELECT * FROM categorias")
    categories = cursor.fetchall()

    print("\n📋 Categorias:")
    for cat in categories:
        print(f"{cat['id']} - {cat['nome']} ({cat['metodo_pgto']})")
    
    conn.close()


def update_category(nome_atual, nome_novo=None, novo_metodo_pgto=None):
    """Atualiza nome e/ou tipo de pagamento de uma categoria."""
    
    conn, cursor = get_cursor()

    if nome_novo:
        cursor.execute(
            """
            UPDATE categorias
            SET nome = ?
            WHERE nome = ?
            """,
            (nome_novo, nome_atual)
        )

    if novo_metodo_pgto:
        cursor.execute(
            """
            UPDATE categorias
            SET payment_type = ?
            WHERE nome = ?
            """,
            (novo_metodo_pgto, nome_atual)
        )

    conn.commit()
    conn.close()

    print(f"🛠 Categoria '{nome_atual}' atualizada!")
