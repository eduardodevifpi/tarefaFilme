from controllers.views import home, listarTodos, cadastrar

def iniciar_rotas(app):
    app.add_url_rule('/', view_func=home, methods=['GET'])
    app.add_url_rule('/filmes', view_func=listarTodos, methods=['GET'])
    app.add_url_rule('/filmes/cadastrar', view_func=cadastrar, methods=['GET', 'POST'])
    
