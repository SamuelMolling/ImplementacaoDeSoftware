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

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)

    if task:
        form = AddTaskForm()
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = dt.now()
            db.session.commit()
            print('Atualizado:', task.title)
            return redirect(url_for('index'))
        
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id, operacao='Editar tarefa')
    else:
        print('Tarefa não localizada!')

    return redirect(url_for('index'))