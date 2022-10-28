# Arquivo app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
# db = SQLAlchemy(app, engine_options={'echo': True})

from routes import *

if __name__ == '__main__':
    app.run(debug=True)