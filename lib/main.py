import tkinter as tk
from tkinter import messagebox
from lib.db_helper import *
from dateutil import parser

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

def showMessage(text, type):
    types = {
        'error': messagebox.showerror,
        'info': messagebox.showinfo,
        'warning': messagebox.showwarning
    }
    types[type](type,text)

def checkNumber(cpf):
    return bool(cpf.isdigit())

def VerifyCPF(cpf):
    if getCPF(cpf):
        return True

def convertStringInDate(birthday):
    try:
        t = parser.parse(birthday, parser.parserinfo(dayfirst=True))
        return t.strftime('%d-%m-%Y')
    except Exception:
        return None

def newClient(name, sex, cpf, birthday):
    if VerifyCPF(cpf):
        showMessage('CPF already exists', 'error')
    else:
        print(birthday)
        print(type(birthday))
        insertClient(name, sex, cpf, str(birthday))
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
