from logging import exception
from db.model import *

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True    

def getCPF(cpf):
    return bool(cpf := session.query(Client).where(Client.cpf == cpf).all())

def getIdCPF(cpf):
    return session.query(Client.id).where(Client.cpf == cpf).all()

def getCostumer(cpf):
    return session.query(Client.name, Client.cpf, Client.sex, Client.birthday).where(Client.cpf == cpf).all()

def getBank(cpf):
    return bool(cpf := session.query(BankAccount).join(Client).where(Client.cpf == cpf).all())

def getIdBank(cpf):
    return session.query(BankAccount.id).join(Client).where(Client.cpf == cpf).all()

def getBankAccount(cpf):
    return session.query(BankAccount).join(Client).where(Client.cpf == cpf).all()

def getAccountTypeId(accountType):
    return session.query(AccountType.id).where(AccountType.type == accountType).all()

def getBalance(cpf):
    return session.query(BankAccount.balance).where(BankAccount.client_id == cpf).all()

def getAccountType(cpf):
    return session.query(BankAccount.account_type).where(BankAccount.client_id == cpf).all()

def getAccountInfo(cpf_id):
    return session.query(BankAccount.balance, AccountType.type).join(AccountType).where(BankAccount.client_id == cpf_id).all()

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
        session.query(BankAccount).where(BankAccount.client_id == client_id).update({BankAccount.balance:balance})
        session.commit()
    except Exception as e:
        session.rollback()
        return e

def insertMovimentation(action, account_id, date, value):
    try:
        default = [
            Movimentation(
                type=action,
                account=account_id,
                date=date,
                value=value
                )
        ]

        session.add_all(default)
        session.commit()
    except Exception as e:
        session.rollback()
        return e

def getExtract(id_bank, initial_date, finish_date):
    return session.query(Movimentation).join(BankAccount).where(BankAccount.id == id_bank and (Movimentation.date.between(initial_date, finish_date))).all()

session.close()
conn.close()
engine.dispose()