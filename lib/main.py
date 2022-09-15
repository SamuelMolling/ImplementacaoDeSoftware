import tkinter as tk
from tkinter import messagebox
from lib.db_helper import *

Cliente = {
    'id': tk.IntVar(),
    'name': tk.StringVar(),
    'sex': tk.StringVar(),
    'cpf': tk.StringVar(),
    'birthday': tk.StringVar()
}

bankAccount = {
    'id': tk.IntVar(),
    'balance': tk.IntVar(),
    'cpf': tk.StringVar(),
    'accountType': tk.StringVar()
}

accountType = {
    'id': tk.IntVar(),
    'type': tk.StringVar()
}

movimentationType = {
    'id': tk.IntVar(),
    'type': tk.StringVar()
}

movimentation = {
    'id': tk.IntVar(),
    'value': tk.IntVar(),
    'account': tk.IntVar(),
    'movimentationType': tk.IntVar()
}

def showMessage(text, type):
    types = {
        'error': messagebox.showerror,
        'info': messagebox.showinfo,
        'warning': messagebox.showwarning
    }
    types[type](text)

def VerifyCPF(cpf):
    if getCPF(Cliente[cpf].get()):
        return True

def newClient(name, sex, cpf, birthday):
    if VerifyCPF(cpf):
        showMessage('CPF already exists', 'error')
    else:
        insertClient(name, sex, cpf, birthday)
        showMessage('Client created', 'info')

def saveInformations(action):    
    match action:
        case 1:
            insertClient(Cliente['name'].get) ##PEGAR INFO DO FORM
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
