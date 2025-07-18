"""
Autor: Petrus Kirsten
Propósito: Funções relacionadas ao cadastro e atualização de usuários.
"""

from backend.app.scripts.db     import get_cursor
from app.utils  import exibir_tabela


def add_user(nome, usuario, avatar):
    """Insere um novo usuário no banco de dados."""
    
    conn, cursor = get_cursor()

    try:
        cursor.execute(
            """
            INSERT INTO usuarios (nome, usuario, avatar)
            VALUES (?, ?, ?)
            """, 
            (nome, usuario, avatar)
        )
        conn.commit()
        print(f"✅ Usuário '{nome}' inserido com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao inserir usuário: {e}")

    finally:
        conn.close()


def atualizar_user(usuario_atual, novo_nome=None, novo_usuario=None, novo_avatar=None):
    """
    Atualiza dados de um usuário existente.
    É possível alterar: nome, nome de usuário, avatar.
    """
    
    conn, cursor = get_cursor()

    if novo_nome:
        cursor.execute(
            """
            UPDATE usuarios
            SET nome = ?
            WHERE usuario = ?
            """,
            (novo_nome, usuario_atual)
        )

    if novo_usuario:
        cursor.execute(
            """
            UPDATE usuarios
            SET usuario = ?
            WHERE usuario = ?
            """,
            (novo_usuario, usuario_atual)
        )

    if novo_avatar:
        cursor.execute(
            """
            UPDATE usuarios
            SET avatar = ?
            WHERE usuario = ?
            """,
            (novo_avatar, usuario_atual)
        )

    conn.commit()
    conn.close()
    
    print(f"🛠 Usuário '{usuario_atual}' atualizado com sucesso!")


def get_users():
    """Mostra todos os usuários cadastrados."""
    
    conn, cursor = get_cursor()

    cursor.execute("SELECT * FROM usuarios")

    colunas = [col[0] for col in cursor.description]
    dados   = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

    conn.close()
    
    return dados
