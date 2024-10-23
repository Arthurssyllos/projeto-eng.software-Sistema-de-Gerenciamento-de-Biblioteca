import sqlite3

DATABASE = 'biblioteca.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Criação da tabela livros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            disponivel INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Tabela 'livros' criada com sucesso!")

if __name__ == '__main__':
    init_db()
