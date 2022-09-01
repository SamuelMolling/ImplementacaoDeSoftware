from msilib.schema import ComboBox
from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox

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
  self.button = Button(self.principalWindow, text="Quit", command=quit)
  self.button.pack()
  
  # Running
  mainloop()
  gui = initialWindow()

#  def hello_world(self):
#   messagebox.showinfo('Adoro a Apostila Python Progressivo!')
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
  self.label = ComboBox(self.createCostumerWindow)
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

  # Rodando
  mainloop()

 def VerifyCPF(self):
  messagebox.showinfo('VALIDAR CPF AQUI')

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
  self.label = ComboBox(self.createCostumerWindow)
  self.label['values'] = ('1 - Corrente','2 - Poupança','3 - Investimento')
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()

 def VerifyCPF(self):
  messagebox.showinfo('VALIDAR CPF AQUI')
  
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
  self.label = ComboBox(self.createCostumerWindow)
  self.label['values'] = ('1 - Corrente','2 - Poupança','3 - Investimento')
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Rodando
  mainloop()

 def VerifyCPF(self):
  messagebox.showinfo('VALIDAR CPF AQUI')

  def insertNewCostumer(self):
    messagebox.showinfo('INSERIR NOVO CLIENTE AQUI')

  def insertInitialBalance(self):
    messagebox.showinfo('INSERIR SALDO INICIAL AQUI')
  
  def quit(self):
    self.principalWindow.destroy()

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

 def VerifyCPF(self):
  messagebox.showinfo('VALIDAR CPF AQUI')

  def insertBalance(self):
    messagebox.showinfo('INSERIR SALDO INICIAL AQUI')
  
  def quit(self):
    self.principalWindow.destroy()

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

 def VerifyCPF(self):
  messagebox.showinfo('VALIDAR CPF AQUI')

  def insertBalance(self):
    messagebox.showinfo('INSERIR SALDO INICIAL AQUI')
  
  def quit(self):
    self.principalWindow.destroy()

gui = createCostumerWindow()
###############################################################################

def makeWithdrawal():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "makeDeposit")
    button = tk.Button(newWindow, text = "makeDeposit")

    label.pack()
    button.pack()    

def applyInterest():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "makeDeposit")
    button = tk.Button(newWindow, text = "makeDeposit")

    label.pack()
    button.pack() 

def getExtract():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "makeDeposit")
    button = tk.Button(newWindow, text = "makeDeposit")

    label.pack()
    button.pack() 

def quit():
    app.destroy()

app = tk.Tk()
app.title("Simplified Banking System")
app.geometry('300x300')



# Start the mainloop
app.mainloop()