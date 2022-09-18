from datetime import date
from logging import exception
from db.model import *

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True    

def getCPF(cpf):
    return bool(cpf := session.query(Client).where(Client.cpf == cpf).all())

def getIdCPF(cpf):
    return session.query(Client.id).where(Client.cpf == cpf).all()

def getBank(cpf): #AJUSTAR O JOIN
    return bool(cpf := session.query(BankAccount).join(Client).where(Client.cpf == cpf).all())

def getAccountTypeId(accountType):
    return session.query(AccountType.id).where(AccountType.type == accountType).all()

def getBalance(cpf, value): #AJUSTAR O JOIN
    balance = session.query(BankAccount).where(BankAccount.cpf == cpf).all()

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
        return e

def insertBankAccount(cpf, accountType, balance):
    try:
        default = [
            BankAccount(
                client_id=cpf,
                account_type=accountType,
                balance=balance
                )
        ]

        session.add_all(default)
        session.commit()
    except Exception as e:
        session.rollback()
        return e

def updateBalance(client_id, balance):
    try:
        update = (
            update(BankAccount).
            where(BankAccount.client_id == client_id).
            values(balance=balance)
        )
        session.execute(update)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)

def insertMovimentation(value, account, movimentationType):
    pass

def getExtrato(cpf):
    pass

session.close()
conn.close()
engine.dispose()