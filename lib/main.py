 
class client:
    def __init__(self, name, sex, cpf, birthday):
        self.name = name
        self.sex = sex
        self.cpf = cpf
        self.birthday = birthday

class bankAccount:
    def __init__(self, accountType, balance):
        self.cpf = client.cpf
        self.accountType = accountType
        self.balance = balance

class accountType:
    def __init__(self, type):
        self.type = type

class movimentationType:
    def __init__(self, type):
        self.type = type

class movimentation:
    def __init__(self, cpf, value):
        self.cpf = cpf
        self.type = movimentationType.type
        self.account = bankAccount.cpf
        self.value = value

def getCPF(cpf):
    pass

def updateBalance(action, value):
    pass

def closeWindow(window):
    window.destroy()