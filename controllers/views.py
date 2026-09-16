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


def apagarFilme(id):
    # Remove o filme com o id fornecido e redireciona para a lista
    for i, filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[i]
            break
    return redirect('/filmes')


def editar(id):
    # Exibe formulário pré-preenchido (GET) e processa atualização (POST)
    if request.method == 'GET':
        for filme in filmes:
            if filme.get('id') == id:
                return render_template('editar_filme.html', filme=filme)
        return redirect('/filmes')

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = request.form.get('ano')

        for filme in filmes:
            if filme.get('id') == id:
                if titulo:
                    filme['titulo'] = titulo
                if ano:
                    filme['ano'] = ano
                break
        return redirect('/filmes')


