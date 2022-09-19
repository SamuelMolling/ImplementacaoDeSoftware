
from datetime import *
from tkinter import messagebox
from lib.db_helper import *
from pages.extract import ExtractWindow

operations = {
    1: "Deposit",
    2: "Withdraw",
    3: "Apply Interest"
}

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

def convertStringInDatetime(date):
    try:
       return datetime.strptime(date,'%d/%m/%Y %H:%M:%S')
    except Exception as e:
        return e


# Create new costumer
def newClient(name, sex, cpf, birthday):
    if VerifyCPF(cpf):
        showMessage('CPF already exists', 'warning')
    else:
        birthday = convertStringInDate(birthday)
        error = insertClient(name, sex, cpf, birthday)
        if error != None:
            showMessage(error, 'error')
        else:
            showMessage('Client created', 'info')

def newAccountForCostumer(cpf, accountType, balance):
    if VerifyCPF(cpf):
        if not getBank(cpf):
            cpf_id = getIdCPF(cpf)
            accountTypeId = getAccountTypeId(accountType)
            error = insertBankAccount(cpf_id[0][0], accountTypeId[0][0], balance)
            if error != None:
                showMessage(error, 'error')
            else:
                showMessage('Account created', 'info')
        else:
            showMessage('Account already exists', 'warning')
    else:
        showMessage('CPF not found', 'error')

def Operation(action, cpf, value):
    match action:
        case 1: #Deposit
            if VerifyCPF(cpf):
                if getBank(cpf):
                    cpf_id = getIdCPF(cpf)
                    balance = getBalance(cpf_id[0][0])
                    balance = balance[0][0] + float(value)
                    error = updateBalance(cpf_id[0][0], balance)
                    if error != None:
                        showMessage(error, 'error')
                        return
                else:
                    showMessage('Account does not exists', 'error')
                    return
            else:
                showMessage('CPF not found', 'error')
                return
        case 2: #Withdraw
            if VerifyCPF(cpf):
                if getBank(cpf):
                    cpf_id = getIdCPF(cpf)
                    balance = getBalance(cpf_id[0][0])
                    balance = balance[0][0] - float(value)
                    if balance >= 0:
                        if (getAccountType(cpf_id[0][0])[0][0] == 1 or getAccountType(cpf_id[0][0])[0][0] == 2):
                            error = updateBalance(cpf_id[0][0], balance)
                            if error != None:
                                showMessage(error, 'error')
                                return
                        else:
                            showMessage('Account type does not allow withdraw', 'error')
                            return
                    else:
                        showMessage('Insufficient balance', 'error')
                        return
                else:
                    showMessage('Account does not exists', 'error')
                    return
            else:
                showMessage('CPF not found', 'error')
                return
        case 3:  #Apply juros
            if VerifyCPF(cpf):
                if getBank(cpf):
                    cpf_id = getIdCPF(cpf)
                    balance = getBalance(cpf_id[0][0])
                    balance = balance[0][0] + (balance[0][0] * (float(value)/100))
                    if (getAccountType(cpf_id[0][0])[0][0] == 2 or getAccountType(cpf_id[0][0])[0][0] == 3):
                        error = updateBalance(cpf_id[0][0], balance)
                        if error != None:
                            showMessage(error, 'error')
                            return
                    else:
                        showMessage('Account type not provide this operation', 'error')
                        return
                else:
                    showMessage('Account does not exists', 'error')
                    return
            else:
                showMessage('CPF not found', 'error')
                return
    id_bank = getIdBank(cpf)
    error = insertMovimentation(action, id_bank[0][0], datetime.now(), value)
    if error != None:
        showMessage(error, 'error')
    else:
        balance = getBalance(cpf_id[0][0])
        showMessage('Operation '+ operations[action] +' is done. \nYour new balance is: '+ str(round(balance[0][0],2)) + 'R$', 'info')

def makeExtract(cpf, initial_date, finish_date):
    if VerifyCPF(cpf):
        if getBank(cpf):
            cpf_id = getIdCPF(cpf)
            costumer = getCostumer(cpf)
            id_bank = getIdBank(cpf)
            initial_date = convertStringInDatetime(f"{initial_date} 00:00:00")
            finish_date = convertStringInDatetime(f"{finish_date} 23:59:59")
            extract = getExtract(id_bank[0][0], initial_date, finish_date)
            bankInfo = getAccountInfo(cpf_id[0][0])
            if extract is None:
                showMessage('No extract found', 'info')
            else: 
                ExtractWindow(costumer, bankInfo, extract, initial_date, finish_date)
        else:
            showMessage('Account does not exists', 'error')
    else:
        showMessage('CPF not found', 'error')