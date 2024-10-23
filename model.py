import sqlite3

class Biblioteca:
    def __init__(self, db_file):
        self.db_file = db_file

    def conectar(self):
        return sqlite3.connect(self.db_file)

    def listar_livros(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        conn.close()
        return livros

    def adicionar_livro(self, titulo, autor):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO livros (titulo, autor, disponivel) VALUES (?, ?, 1)", (titulo, autor))
        conn.commit()
        conn.close()

    def devolver_livro(self, livro_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE livros SET disponivel = 1 WHERE id = ?", (livro_id,))
        conn.commit()
        conn.close()

    def emprestar_livro(self, livro_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE livros SET disponivel = 0 WHERE id = ?", (livro_id,))
        conn.commit()
        conn.close()
