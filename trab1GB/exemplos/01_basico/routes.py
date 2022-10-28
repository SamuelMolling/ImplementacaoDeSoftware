# Arquivo routes.py
from app import app

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello Flask!</h1>'