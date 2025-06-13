import sqlite3
import os

# Caminho para o arquivo .db
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'financas.db')

def connect():
    """Abre conexão com o banco de dados."""
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acessar colunas por nome
    return conn


def create_tables():
    """Cria as tabelas do banco (caso não existam)."""
    
    conn = connect()
    cursor = conn.cursor()

    # Tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        usuario TEXT UNIQUE NOT NULL,
        avatar TEXT
    )
    """)

    # Tabela de categorias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT CHECK(tipo IN ('débito', 'crédito', 'ambos')) NOT NULL
    )
    """)

    # Tabela de transações
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        descricao TEXT,
        categoria_id INTEGER NOT NULL,
        tipo TEXT CHECK(tipo IN ('débito', 'crédito')) NOT NULL,
        compartilhado BOOLEAN DEFAULT 0,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )
    """)

    # Tabela de planejamentos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS planejamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        categoria_id INTEGER NOT NULL,
        mes TEXT NOT NULL,
        valor_planejado REAL NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )
    """)

    conn.commit()
    conn.close()
