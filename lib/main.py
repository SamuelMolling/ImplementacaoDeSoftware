
from datetime import *
from tkinter import messagebox
from lib.db_helper import *

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

def newAccountForCostumer(cpf, accountType, balance):
    if VerifyCPF(cpf):
        if not getBank(cpf):
            cpf_id = getIdCPF(cpf)
            accountTypeId = getAccountTypeId(accountType)
            insertBankAccount(cpf_id[0][0], accountTypeId[0][0], balance)
            showMessage('Account created', 'info')
        else:
            showMessage('Account already exists', 'error')
    else:
        showMessage('CPF not found', 'error')

def makeDeposit(cpf, value):
    if VerifyCPF(cpf):
        balance = getBalance(cpf)
        value += balance
        updateBalance(cpf, value)
    else:
        showMessage('CPF not found', 'error')