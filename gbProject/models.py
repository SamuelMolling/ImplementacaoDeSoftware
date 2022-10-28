from app import db, app
import csv

class Client(db.Model):
    __tablename__ = 'client'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)

class City(db.Model):
    __tablename__ = 'city'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    id_city = db.Column(db.Integer, db.ForeignKey('city.id'))
    model = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(15), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    odometer = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    daily_value = db.Column(db.Float, nullable=False)
    km_value = db.Column(db.Float, nullable=False)

class Location(db.Model):
    __tablename__ = 'location'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    id_vehicle = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    id_client = db.Column(db.Integer, db.ForeignKey('client.id'))
    id_origin_city = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    id_destination_city = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)
    km_driven = db.Column(db.Integer, nullable=True)
    days = db.Column(db.Integer, nullable=False)

Vehicle.city = db.relationship('City', back_populates='vehicle')
City.vehicle = db.relationship('Vehicle', back_populates='city')
Location.vehicle = db.relationship('Vehicle', back_populates='location')
Vehicle.location = db.relationship('Location', back_populates='vehicle')
Location.client = db.relationship('Client', back_populates='location')
Client.location = db.relationship('Location', back_populates='client')
Location.origin_city = db.relationship('City', back_populates='location_origin', foreign_keys=[Location.id_origin_city])
City.location_origin = db.relationship('Location', back_populates='origin_city', foreign_keys=[Location.id_origin_city])
Location.destination_city = db.relationship('City', back_populates='location_destination', foreign_keys=[Location.id_destination_city])
City.location_destination = db.relationship('Location', back_populates='destination_city', foreign_keys=[Location.id_destination_city])

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

        with open('database/cliente.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                db.session.add(Client(nome=row[1]))
        db.session.commit()

        with open('database/cidade.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                db.session.add(City(nome=row[1]))
        db.session.commit()

        with open('database/veiculo.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(row[6])
                db.session.add(Vehicle(id_city=row[5], model=row[1], color=row[2], year=row[3], odometer=row[4], available=eval(row[6]), daily_value=row[7], km_value=row[8]))
        db.session.commit()

        with open('database/locacao.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                db.session.add(Location(id_vehicle=row[1], id_client=row[2], id_origin_city=row[3], id_destination_city=row[4], km_driven=row[5], days=row[6]))
        db.session.commit()

