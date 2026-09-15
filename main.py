from flask import Flask
from routes.rotas import iniciar_rotas

app = Flask(__name__)

iniciar_rotas(app)