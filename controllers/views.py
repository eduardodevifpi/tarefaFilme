from flask import render_template, request, redirect


filmes = []

def home():
    return render_template('index.html')


def listarTodos():
    return render_template('listar_filmes.html', lista_filmes=filmes)

def cadastrar():
    if request.method == 'GET':
        return render_template('cadastrar_filme.html')
        
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = request.form.get('ano')
        id_filme = len(filmes) + 1
        
        filme = {
            'id': id_filme,
            'titulo': titulo,
            'ano': ano
        }
        filmes.append(filme)
        return redirect('/filmes')


def encontrarPorId():
    id_buscado = request.args.get('id_busca')

    if id_buscado:

        id_int = int(id_buscado)
        for filme in filmes:
            if filme['id'] == id_int:
                return render_template('detalhes_filme.html', filme=filme)


