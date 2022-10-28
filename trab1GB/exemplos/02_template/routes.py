# Arquivo routes.py
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        conteudo='Página principal da aplicação')

@app.route('/about')
def about():
    return render_template(
        'about.html',
        conteudo='Sobre a aplicação')