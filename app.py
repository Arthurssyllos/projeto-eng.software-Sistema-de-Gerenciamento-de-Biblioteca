from flask import Flask, render_template, request, redirect, url_for
from model import Biblioteca

app = Flask(__name__)
DATABASE = 'biblioteca.db'
biblioteca = Biblioteca(DATABASE)

@app.route('/')
def index():
    livros = biblioteca.listar_livros()
    return render_template('index.html', livros=livros)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        biblioteca.adicionar_livro(titulo, autor)
        return redirect(url_for('index'))
    return render_template('cadastrar.html')

@app.route('/emprestar/<int:livro_id>')
def emprestar_livro(livro_id):
    biblioteca.emprestar_livro(livro_id)
    return render_template('emprestar.html')

@app.route('/devolver/<int:livro_id>')
def devolver_livro(livro_id):
    biblioteca.devolver_livro(livro_id)
    return render_template('devolver.html')

@app.route('/consultar')
def consultar_livros():
    livros = biblioteca.listar_livros()
    return render_template('consultar.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)
