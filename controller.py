from flask import Flask, render_template, request, redirect, url_for
from model import Biblioteca

app = Flask(__name__)
biblioteca = Biblioteca('biblioteca.db')

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
    return redirect(url_for('index'))

@app.route('/devolver/<int:livro_id>')
def devolver_livro(livro_id):
    biblioteca.devolver_livro(livro_id)
    return redirect(url_for('index'))

@app.route('/consultar', methods=['GET', 'POST'])
def consultar_livros():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        livros = biblioteca.consultar_livros(titulo, autor)
        return render_template('consultar.html', livros=livros)
    return render_template('consultar.html', livros=[])

if __name__ == '__main__':
    app.run(debug=True)
