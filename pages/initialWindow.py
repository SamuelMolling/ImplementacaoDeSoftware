from tkinter import *
from lib.main import app

class initialWindow(app):
 def __init__(self):
  super().__init__()
  # Create the principal window
  self.title("Simplified Banking System")
  self.geometry('300x300')

  # Create new costumer in the banking system
  self.button = Button(self, text="Create new costumer", command=lambda: createCostumerWindow)
  self.button.pack()

  # Create new account for costumer
  self.button = Button(self, text="Create new account for costumer", command=createNewAccount)
  self.button.pack()

  # Make a deposit to an account
  self.button = Button(self, text="Make deposit", command=makeDepositWindow)
  self.button.pack()

  # Withdraw an account
  self.button = Button(self, text="Make withdrawal", command=makeWithdrawal)
  self.button.pack()

  # Apply interest to an account
  self.button = Button(self, text="Apply interest", command=applyInterest)
  self.button.pack()

  # Extract account information
  self.button = Button(self, text="Extract", command=getExtract)
  self.button.pack()

  # Quit
  self.button = Button(self, text="Quit", command=self.destroy())
  self.button.pack()