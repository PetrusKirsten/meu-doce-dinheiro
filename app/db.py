"""
Autor: Petrus Kirsten
Propósito: Gerencia a conexão com o banco de dados e a criação das tabelas.
"""

import sqlite3
import os

# Caminho para o arquivo .db
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'financas.db')

def connect():
    """Abre conexão com o banco de dados."""
    
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row  # permite acessar colunas por nome

    return connection


def get_cursor():
    """Abre conexão com o banco de dados e retorna seu cursor."""
    
    connection = connect()
    cursor = connection.cursor()

    return connection, cursor


def criar_tabelas():
    """Cria as tabelas do banco (caso não existam)."""
    
    conn, cursor = get_cursor()

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
        metodo_pgto TEXT CHECK(metodo_pgto IN ('débito', 'crédito', 'ambos')) NOT NULL
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

    # Tabela de transações
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            tipo TEXT CHECK(tipo IN ('renda', 'despesa')) NOT NULL,
            forma_pagamento TEXT CHECK(forma_pagamento IN ('débito', 'crédito', 'pix', 'dinheiro', 'outro')) NOT NULL,
            descricao TEXT,
            data TEXT NOT NULL,
            compartilhada BOOLEAN DEFAULT 0,
            usuario_id INTEGER NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    """)

    conn.commit()
    conn.close()
