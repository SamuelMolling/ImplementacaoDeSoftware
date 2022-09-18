
from datetime import *
from tkinter import messagebox
from lib.db_helper import *

# bankAccount = {
#     'id': tk.IntVar(),
#     'balance': tk.IntVar(),
#     'cpf': tk.StringVar(),
#     'accountType': tk.StringVar()
# }

# accountType = {
#     'id': tk.IntVar(),
#     'type': tk.StringVar()
# }

# movimentationType = {
#     'id': tk.IntVar(),
#     'type': tk.StringVar()
# }

# movimentation = {
#     'id': tk.IntVar(),
#     'value': tk.IntVar(),
#     'account': tk.IntVar(),
#     'movimentationType': tk.IntVar()
# }
# Show message
def showMessage(text, type):
    types = {
        'error': messagebox.showerror,
        'info': messagebox.showinfo,
        'warning': messagebox.showwarning
    }
    types[type](type,text)

# Check if cpf is only numbers
def checkNumber(cpf):
    return bool(cpf.isdigit())

# Check if string is only letters
def checkString(name):
    return bool(name.isdigit())

# Check if the account exists
def VerifyCPF(cpf):
    if getCPF(cpf):
        return True

# def convertStringInDate(birthday):
#     try:
#         datetime.datetime.strptime(birthday, '%d/%m/%Y')
#         # (birthday, '%Y/%mm/%dd')
#     except Exception as e:
#         return e

def convertStringInDate(birthday):
    try:
       return datetime.strptime(birthday,'%d/%m/%Y')
    except Exception as e:
        return e

# Create new costumer
def newClient(name, sex, cpf, birthday):
    if VerifyCPF(cpf):
        showMessage('CPF already exists', 'error')
    else:
        birthday = convertStringInDate(birthday)
        insertClient(name, sex, cpf, birthday)
        showMessage('Client created', 'info')

def saveInformations(action):    
    match action:
        case 2:
            insertBankAccount(bankAccount['balance'].get, bankAccount['cpf'].get, bankAccount['accountType'].get)
        case 3:
            insertMovimentation(movimentation['value'].get, movimentation['account'].get, movimentation['movimentationType'].get)
        case 4:
            ValidateAction(movimentation['movimentationType'].get, movimentation['account'].get, movimentation['value'].get)
        case 5:
            getExtrato(movimentation['account'].get)
        case 6:
            validateToSave(movimentation['account'].get)
