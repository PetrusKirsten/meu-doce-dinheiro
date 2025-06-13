from app.db import conectar

def inserir_usuario(nome, usuario, avatar):
    """Insere um novo usuário no banco de dados."""
    
    conn = conectar()
    cursor = conn.cursor()

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


def atualizar_usuario(usuario, novo_nome=None, novo_avatar=None):
    """Atualiza nome e/ou avatar de um usuário, baseado no nome de usuário."""
    
    conn = conectar()
    cursor = conn.cursor()

    if novo_nome:
        cursor.execute(
            """
            UPDATE usuarios
            SET nome = ?
            WHERE usuario = ?
            """, 
            (novo_nome, usuario)
        )

    if novo_avatar:
        cursor.execute(
            """
            UPDATE usuarios
            SET avatar = ?
            WHERE usuario = ?
            """, 
            (novo_avatar, usuario)
        )

    conn.commit()
    conn.close()

    print(f"🛠 Usuário '{usuario}' atualizado com sucesso!")


def listar_usuarios():
    """Mostra todos os usuários cadastrados."""
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(f"{u['id']} - {u['nome']} ({u['usuario']})")
    conn.close()

