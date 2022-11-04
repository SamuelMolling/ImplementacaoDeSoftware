# Arquivo routes.py
from crypt import methods
import string
from app import app
from datetime import datetime as dt
from flask import render_template, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import *
from sqlalchemy import func

db = SQLAlchemy(app, engine_options={'echo': True})

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/consultVehcicle', methods=['GET'])
def consultVehcicle():
    return render_template('consult_vehcicles.html')

@app.route('/makeLease', methods=['GET'])
def makeLease():
    return render_template('make_lease.html')

@app.route('/makeReturn', methods=['GET'])
def makeReturn():
    return render_template('make_return.html')

@app.route('/consultLeases', methods=['GET'])
def makeLeases():
    return render_template('consult_leases.html')

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')

#Routes for consults
@app.route('/getVehicles', methods=['GET'])
def getVehicles():
    parameter_type = request.args['parameter_type']
    parameter_value = request.args['parameter_value']

    if parameter_value == '':
        return 'Parameter is null, please enter a valid value'

    #Validate the parameter type
    if parameter_type == 'City':
        vehicles = Vehicle.query.join(City).filter(func.lower(City.name) == func.lower(parameter_value)).all()
    elif parameter_type == 'Color':
        vehicles = Vehicle.query.filter(func.lower(Vehicle.color) == func.lower(parameter_value)).all()
    elif parameter_type == 'Model':
        vehicles = Vehicle.query.filter(func.lower(Vehicle.model) == func.lower(parameter_value)).all()
    
    if len(vehicles) == 0:
        return 'No vehicles found in this city'
    
    return render_template('table_vehicle.html', vehicles=vehicles)


@app.route('/getName', methods=['GET'])
def getName():

    data = [(r.id, r.name) for r in Client.query.all()]
    name = []

    name.extend(f'<option value="{k}">{v}</option>' for k, v in data)
    return '\n'.join(name)

@app.route('/getOriginCity', methods=['GET'])
def getOriginCity():

    # data = [(r.id_origin_city, r.name) for r in City.query.distinct(City.name).with_entities(Location.id_origin_city,City.name).join(Location, Location.id_origin_city==City.id).all()]
    data = [(r.id, r.name) for r in City.query.all()]
    origin_city = []

    origin_city.extend(f'<option value="{k}">{v}</option>' for k, v in data)
    return '\n'.join(origin_city)

@app.route('/makeLocation', methods=['GET', 'POST'])
def makeLocation():

    if request.method == 'GET':
        client_name = int(request.args['client_name'])
        origin_city = int(request.args['origin_city'])
        #Get locations for client
        active_location = Location.query.filter(Location.id_client == client_name, Location.id_destination_city.is_(None)).first()
        if active_location is not None:
            return 'This client already has an active location'

        #Get vehicles available in the city
        vehicles = Vehicle.query.join(City).filter(City.id==origin_city, Vehicle.available==True).all()

        return 'No vehicles available in this city' if len(vehicles) == 0 else render_template('makeLocation.html', vehicles=vehicles)

    elif request.method == 'POST':
        #Get the vehicle id
        client_name = int(request.form['client_name'])
        origin_city = int(request.form['origin_city'])
        vehicle = int(request.form['vehicles'])
        days = int(request.form['days'])

        #New location
        try:
            new_location = Location(id_client=client_name, id_origin_city=origin_city, id_destination_city=None, km_driven=None,days=days, id_vehicle=vehicle)
            db.session.add(new_location)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return 'Error in the application, please try again later'
        
        try: 
            #Update the vehicle status
            db.session.query(Vehicle).where(Vehicle.id == vehicle).update({Vehicle.available:False})
            db.session.commit()
        except Exception:
            db.session.rollback()
            return 'Error in the application, please try again later'

        return 'Location created successfully'

# @app.route('/makeLease', methods=['GET'])
# def getClient():
#     client = []
#     data = [(r.id, r.name) for r in client.query.all()]

#     client.extend(f'<option value="{k}">{v}</option>' for k, v in data)
#     return '\n'.join(client)
    # return render_template('make_lease.html')

# @app.route('/getopthtml')
# def get_opt_html():
#     opt = list()
#     data = [(r.id, r.option) for r in Option.query.all()]

#     for k, v in data:
#         opt.append(f'<option value="{k}">{v}</option>')

#     return '\n'.join(opt)


# @app.route('/getoptjson')
# def get_opt_json():
#     opt = list()
#     # data = [{r.id: r.option} for r in Option.query.all()]
#     data = [(r.id, r.option) for r in Option.query.all()]

#     return jsonify(data)

# @app.route('/download')
# def download():
#     content = 'Arquivo com conteúdo gerado dinamicamente em ' + dt.now().strftime('%Y-%m-%d %H:%M:%S')
#     response = make_response(content)
#     response.headers.set('Content-Type', 'text')
#     response.headers.set('Content-Disposition', 'attachment', filename='dynfile.txt')
#     return response