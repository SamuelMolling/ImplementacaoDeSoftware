from logging import exception
from turtle import update
from model import *

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True    

def getCPF(cpf): #AJUSTAR O JOIN
    return bool(cpf := session.query(Client).where(Client.cpf == cpf).all())

def getBank(cpf): #AJUSTAR O JOIN
    return bool(cpf := session.query(BankAccount).where(BankAccount.cpf == cpf).all())

def getBalance(cpf, value): #AJUSTAR O JOIN
    balance = session.query(BankAccount).where(BankAccount.cpf == cpf).all()

def insertBalance(cpf, value):
    pass

def decreaseBalance(cpf, value):
    pass

def updateBalance(cpf, value):
    pass

def ValidateAction(action, cpf, value):
    if action == 1: # deposito
        if getCPF(cpf):
            insertBalance()
            insertMovimentation(action, value, cpf)
        else:
            exception('Cliente não cadastrado')
    elif action == 2: # Saque
        balance = getBalance(cpf, value)
        if balance > value:
            decreaseBalance(cpf, value)
            insertMovimentation(action, value, cpf)
    elif action == 3:   # Juros
        balance = getBalance(cpf, value)
        if balance > value:
            updateBalance(cpf, value)
            insertMovimentation(action, value, cpf)
            #PRINT ERROR

def insertClient(name, sex, cpf, birthday):
    pass

def insertBankAccount(balance, cpf, accountType):
    pass

def insertMovimentation(value, account, movimentationType):
    pass

def validateToSave(cpf):
    if getCPF(cpf):
        pass

def getExtrato(cpf):
    pass

session.close()
conn.close()
engine.dispose()