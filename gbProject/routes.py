# Arquivo routes.py
from crypt import methods
import markdownify
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
    locations = Location.query.join(Vehicle).filter(Location.id_destination_city.is_not(None))

    total_value = []
    days = 0
    km_driven = 0
    value_km = 0
    value_day = 0


    for location in locations:
        value_day = location.days * location.vehicle.daily_value
        value_km =  location.km_driven * location.vehicle.km_value
        value = value_day + value_km
        total_value.append(round(value,2))

        days += location.days
        km_driven += location.km_driven
        value_km += location.vehicle.km_value
        value_km = round(value_km,2)
        value_day += location.vehicle.daily_value
        value_day = round(value_day,2)


    return render_template('resume.html', locations=locations, total_value=total_value, total_days=days, total_km=km_driven, total_value_by_km=value_km, total_daily_value=value_day)


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
            db.session.query(Vehicle).where(Vehicle.id == vehicle).update({Vehicle.available:False})
            db.session.commit()
        except Exception:
            db.session.rollback()
            return 'Error in the application, please try again later'

        return 'Location created successfully'

@app.route('/makeReturnLease', methods=['GET', 'POST'])
def makeReturnLease():

    if request.method == 'GET':

        client_name = int(request.args['client_name'])
        kmDriven = int(request.args['kmDriven'])
        #Get locations for client
        active_location = Location.query.filter(Location.id_client == client_name, Location.id_destination_city.is_(None)).first()
        if active_location is None:
            return 'Client dont have location available'

        #Get vehicles available in the city
        vehicles = Vehicle.query.filter(Vehicle.id == active_location.id_vehicle).first()

        value_day = active_location.days * vehicles.daily_value
        value_km =  kmDriven * vehicles.km_value

        value = value_day + value_km
        value_formated = round(value,2)

        return render_template('makeLocationReturn.html', vehicles=vehicles, value=value_formated, days=active_location.days)

    elif request.method == 'POST':
        #Get the vehicle id
        client_name = int(request.form['client_name'])
        kmDriven = int(request.form['kmDriven'])
        destination_city = request.form['destination_city']

        #get odometer
        # location = Location.query.filter(Location.id_client == client_name, Location.id_destination_city.is_(None)).first()
        location = Location.query.join(Vehicle).filter(Location.id_client == client_name, Location.id_destination_city.is_(None)).first()

        odometer = Vehicle.odometer + kmDriven
        


        try:
            #Update the location
            db.session.query(Location).where(Location.id_client == client_name, Location.id_destination_city.is_(None)).update({Location.id_destination_city:destination_city, Location.km_driven:kmDriven})
            db.session.query(Vehicle).where(Vehicle.id == location.id_vehicle).update({Vehicle.available:True, Vehicle.id_city:destination_city, Vehicle.odometer: odometer})
            db.session.commit()
        except Exception:
            db.session.rollback()
            return 'Error in the application, please try again later'
        
        return 'Location returned successfully'

@app.route('/consultLeasesByType', methods=['GET'])
def consultLease():
    parameter_type = request.args['parameter_type']
    parameter_value = request.args['parameter_value']

    #Validate the parameter
    if parameter_value == '':
        return 'Parameter is null, please enter a valid value'

    if parameter_type == 'Name':
        locations = Location.query.join(Client).filter(func.lower(Client.name) == func.lower(parameter_value)).all()
    elif parameter_type == 'Model':
        locations = Location.query.join(Vehicle).filter(func.lower(Vehicle.model) == func.lower(parameter_value)).all()

    if len(locations) == 0:
        return 'Nothing found'

    #Total Value
    total_value = []
    for location in locations:
        value_day = location.days * location.vehicle.daily_value
        value_km =  location.km_driven * location.vehicle.km_value
        value = value_day + value_km
        total_value.append(round(value,2))

    return render_template('table_location.html', locations=locations, total_value=total_value)