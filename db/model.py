import sqlalchemy as db
import sqlalchemy.orm as orm

engine = db.create_engine('sqlite:///bank.db', echo=True)
conn = engine.connect()
Base = orm.declarative_base()

# Client table
class Client(Base):
  __tablename__ = 'client'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  sex = db.Column(db.String(1), nullable=False)
  cpf = db.Column(db.String(11), nullable=False)
  birthday = db.Column(db.Date, nullable=False)

# Bank Account table 
class BankAccount(Base):
  __tablename__ = 'bank_account'
  id = db.Column(db.Integer, primary_key=True)
  client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
  account_type = db.Column(db.Integer, db.ForeignKey('account_type.id'))
  balance = db.Column(db.Float, nullable=False)

# Account Type table 
class AccountType(Base):
  __tablename__ = 'account_type'
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(10), nullable=False)

# Movimentation table 
class Movimentation(Base):
  __tablename__ = 'movimentation'
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.Integer, db.ForeignKey('movimentation_type.id'))
  account = db.Column(db.Integer, db.ForeignKey('bank_account.id'))
  date = db.Column(db.DateTime, nullable=False)
  value = db.Column(db.Float, nullable=False)

# Movimentation type table 
class MovimentationType(Base):
  __tablename__ = 'movimentation_type'
  id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(50), nullable=False)

# Relationships between tables
## Client 1/1 BankAccount
Client.bank_accounts = orm.relationship('BankAccount', back_populates='client')
BankAccount.client = orm.relationship('Client', back_populates='bank_accounts')
## BankAccount n/1 AccountType
BankAccount.account_types = orm.relationship('AccountType', back_populates='bank_accounts')
AccountType.bank_accounts = orm.relationship('BankAccount', back_populates='account_types')
## BankAccount 1/n Movimentation
BankAccount.movimentations = orm.relationship('AccountType', back_populates='movimentations', overlaps="account_types,bank_accounts")
AccountType.movimentations = orm.relationship('BankAccount', back_populates='movimentations', overlaps="account_types,bank_accounts")
## Movimentation n/1 MovimentationType
Movimentation.types = orm.relationship('MovimentationType', back_populates='movimentations')
MovimentationType.movimentations = orm.relationship('Movimentation', back_populates='types')

Base.metadata.create_all(engine)