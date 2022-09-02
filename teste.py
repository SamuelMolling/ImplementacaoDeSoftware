from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox

 
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

class initialWindow:
 def __init__(self):
  # Create the principal window
  self.principalWindow = Tk()
  self.principalWindow.title("Simplified Banking System")
  self.principalWindow.geometry('300x300')

  # Create new costumer in the banking system
  self.button = Button(self.principalWindow, text="Create new costumer", command=createNewCostumer)
  self.button.pack()

  # Create new account for costumer
  self.button = Button(self.principalWindow, text="Create new account for costumer", command=createNewAccount)
  self.button.pack()

  # Make a deposit to an account
  self.button = Button(self.principalWindow, text="Make deposit", command=makeDeposit)
  self.button.pack()

  # Withdraw an account
  self.button = Button(self.principalWindow, text="Make withdrawal", command=makeWithdrawal)
  self.button.pack()

  # Apply interest to an account
  self.button = Button(self.principalWindow, text="Apply interest", command=applyInterest)
  self.button.pack()

  # Extract account information
  self.button = Button(self.principalWindow, text="Extract", command=getExtract)
  self.button.pack()

  # Quit
  self.button = Button(self.principalWindow, text="Quit", command=closeWindow(self.principalWindow))
  self.button.pack()
  
  # Running
  mainloop()

gui = initialWindow()
###############################################################################
class createCostumerWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Create New Costumer")
  self.createCostumerWindow.geometry('300x300')
  
  # Name
  self.button = Label(self.createCostumerWindow, text="Name").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Sex
  self.button = Label(self.createCostumerWindow, text="Sex").pack(side = LEFT)
  self.label = ttk.ComboBox(self.createCostumerWindow)
  self.label['values'] = ('M','F')
  self.button.pack()

  # CPF
  self.button = Label(self.createCostumerWindow, text="CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Birthday
  self.button = Label(self.createCostumerWindow, text="Birthday").pack(side = LEFT)
  self.label = DateEntry(self.createCostumerWindow,selectmode='day')
  self.button.pack()

  # Running
  mainloop()

gui = createCostumerWindow()
###############################################################################
###############################################################################
class createNewAccountWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Create New Account for a Costumer")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Account type
  self.button = Label(self.createCostumerWindow, text="Select account type").pack(side = LEFT)
  self.label = ttk.ComboBox(self.createCostumerWindow)
  self.label['values'] = ('1 - Corrente','2 - Poupança','3 - Investimento')
  self.button.pack()

  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your balance").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()
  
gui = createCostumerWindow()
###############################################################################
###############################################################################
class createNewAccountWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Create New Account for a Costumer")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Account type
  self.button = Label(self.createCostumerWindow, text="Select account type").pack(side = LEFT)
  self.label = ttk.ComboBox(self.createCostumerWindow)
  self.label['values'] = ('1 - Corrente','2 - Poupança','3 - Investimento')
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()

  def insertNewCostumer(self):
    messagebox.showinfo('INSERIR NOVO CLIENTE AQUI')

gui = createCostumerWindow()
###############################################################################
###############################################################################
class makeDepositWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Make a deposit")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Balance
  self.button = Label(self.createCostumerWindow, text="Insert a value for the deposit").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()

gui = createCostumerWindow()
###############################################################################
###############################################################################
class makeWithdrawalWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Make a withdrawal")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Balance
  self.button = Label(self.createCostumerWindow, text="Insert a value for the deposit").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()

gui = createCostumerWindow()
###############################################################################
###############################################################################
class applyInterestWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Apply Interest")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Balance
  self.button = Label(self.createCostumerWindow, text="Insert a value for the interest").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()

gui = applyInterestWindow()
###############################################################################
###############################################################################
class Extract:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Extract")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Inicial date
  self.button = Label(self.createCostumerWindow, text="Inicial date").pack(side = LEFT)
  self.label = DateEntry(self.createCostumerWindow,selectmode='day')
  self.button.pack()

  # Finish date
  self.button = Label(self.createCostumerWindow, text="Finish date").pack(side = RIGHT)
  self.label = DateEntry(self.createCostumerWindow,selectmode='day')
  self.button.pack()

  # Button for search
  self.button = Button(self.createCostumerWindow, text="Search", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()

gui = applyInterestWindow()
###############################################################################
###############################################################################