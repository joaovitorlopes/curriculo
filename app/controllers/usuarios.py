from app import app
from flask import render_template

@app.route('/usuarios')
def listar_usuarios():
    return "<h1>Listando Usuários</h1>"
