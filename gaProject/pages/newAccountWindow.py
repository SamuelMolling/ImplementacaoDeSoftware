import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from lib.main import checkNumber, showMessage, newAccountForCostumer

class createNewAccountWindow(tk.Tk):
 def __init__(self):
  super().__init__()

  # Create the secondary window
  self.title("Create New Account for a Costumer")
  self.geometry('300x300')

  self.cpf = tk.StringVar(),
  self.accountType = tk.StringVar(),
  self.balance = tk.DoubleVar()

  # Create new costumer
  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  # Create new account for a costumer
  def newAccount():
    if checkNumber(self.cpf.get()) and len(self.cpf.get()) == 11:
      cpf = self.cpf.get()
      accountType = self.accountType.get()
      balance = self.balance.get()
      newAccountForCostumer(cpf, accountType, balance)
    else:

      showMessage("Please, verify the information balance or CPF.", 'error')

  # CPF
  self.label = tk.Label(self, text="Enter with your CPF")
  self.cpf = tk.Entry(self)
  self.label.pack()
  self.cpf.pack()

  # Account type
  self.label = tk.Label(self, text="Select account type")
  self.accountType = ttk.Combobox(self)
  self.accountType['values'] = ('corrente','poupanca','investimento')
  self.label.pack()
  self.accountType.pack()

  # Balance
  self.label = tk.Label(self, text="Enter with your balance")
  self.balance = tk.Entry(self) 
  self.label.pack()
  self.balance.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=newAccount)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()