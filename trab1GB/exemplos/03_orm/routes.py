# Arquivo routes.py
from app import app
from models import Task
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/about')
def about():
    return render_template(
        'about.html',
        conteudo='Sobre a aplicação')