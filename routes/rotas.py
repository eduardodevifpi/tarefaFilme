from controllers.views import home, listarTodos, cadastrar, encontrarPorId, editar, apagarFilme

def iniciar_rotas(app):
    app.add_url_rule('/', view_func=home, methods=['GET'])
    app.add_url_rule('/filmes', view_func=listarTodos, methods=['GET'])
    app.add_url_rule('/filmes/cadastrar', view_func=cadastrar, methods=['GET', 'POST'])
    app.add_url_rule('/buscar', view_func=encontrarPorId, methods=['GET'])
    app.add_url_rule('/filmes/editar/<int:id>', view_func=editar, methods=['GET', 'POST'])
    app.add_url_rule('/filmes/apagar/<int:id>', view_func=apagarFilme, methods=['POST'])
    
