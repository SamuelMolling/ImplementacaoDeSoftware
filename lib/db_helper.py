from logging import exception
from db.model import *

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True    

def getCPF(cpf):
    return bool(cpf := session.query(Client).where(Client.cpf == cpf).all())

def getBank(cpf): #AJUSTAR O JOIN
    return bool(cpf := session.query(BankAccount).where(BankAccount.cpf == cpf).all())

def getBalance(cpf, value): #AJUSTAR O JOIN
    balance = session.query(BankAccount).where(BankAccount.cpf == cpf).all()

def createBalance(cpf, value):
    pass

def insertBalance(cpf, value):
    pass

def decreaseBalance(cpf, value):
    pass

def updateBalance(cpf, value):
    pass

def insertClient(name, sex, cpf, birthday):
    try:
        default = [
            Client(
                name=name, 
                sex=sex,
                cpf=cpf,
                birthday=birthday
                )
        ]

        session.add_all(default)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)

def insertBankAccount(balance, cpf, accountType):
    try:
        default = [
            Client(
                balance=balance,
                cpf=cpf,
                accountType=accountType
                )
        ]

        session.add_all(default)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)

def ValidateAction(action, cpf, value):
    if getCPF(cpf):
        if action == 1: # deposito
                insertBalance()
                insertMovimentation(action, value, cpf)
        elif action == 2: # Saque
            balance = getBalance(cpf, value)
            if balance > value:
                decreaseBalance(cpf, value)
                insertMovimentation(action, value, cpf)
        elif action == 3:   # Juros
            updateBalance(cpf, value)
            insertMovimentation(action, value, cpf)
    else:
        exception('Cliente não cadastrado')

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