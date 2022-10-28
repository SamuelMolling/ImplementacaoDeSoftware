# Arquivo routes.py
from app import app, db
from models import Task
from forms import AddTaskForm
from flask import render_template, redirect, url_for
from datetime import datetime as dt

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

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddTaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, date=dt.now())
        db.session.add(task)
        db.session.commit()
        print('Adicionado:', task.title)
        return redirect(url_for('index'))
    return render_template('add.html', form=form, operacao='Adicionar tarefa')