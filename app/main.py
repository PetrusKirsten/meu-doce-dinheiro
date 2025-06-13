from app.db import conectar, criar_tabelas

def listar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()
    for t in tabelas:
        print(t["name"])
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Tabelas existentes no banco:")
    listar_tabelas()
