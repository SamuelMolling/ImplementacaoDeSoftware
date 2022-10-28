# Arquivo routes.py
from crypt import methods
from app import app
from datetime import datetime as dt
from flask import render_template, make_response, jsonify
from models import Client



@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/consult', methods=['GET'])
def consult():
    return render_template('consult_vehcicles.html')

@app.route('/makelease', methods=['GET'])
def getClient():
    client = []
    data = [(r.id, r.name) for r in client.query.all()]

    client.extend(f'<option value="{k}">{v}</option>' for k, v in data)
    return '\n'.join(client)
    # return render_template('make_lease.html')

# @app.route('/getopthtml')
# def get_opt_html():
#     opt = list()
#     data = [(r.id, r.option) for r in Option.query.all()]

#     for k, v in data:
#         opt.append(f'<option value="{k}">{v}</option>')

#     return '\n'.join(opt)


@app.route('/getoptjson')
def get_opt_json():
    opt = list()
    # data = [{r.id: r.option} for r in Option.query.all()]
    data = [(r.id, r.option) for r in Option.query.all()]

    return jsonify(data)

@app.route('/download')
def download():
    content = 'Arquivo com conteúdo gerado dinamicamente em ' + dt.now().strftime('%Y-%m-%d %H:%M:%S')
    response = make_response(content)
    response.headers.set('Content-Type', 'text')
    response.headers.set('Content-Disposition', 'attachment', filename='dynfile.txt')
    return response