import tkinter as tk
from pages.applyInterestWindow import *
from pages.costumerWindow import *
from pages.extractWindow import *
from pages.makeDepositWindow import *
from pages.makeWithdrawalWindow import *
from pages.makeDepositWindow import *
from pages.newAccountWindow import *

class initialWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the principal window
  self.title("Simplified Banking System")
  self.geometry('300x300')

  def initCostumerWindow(self):
   costumerWindow = createCostumerWindow()
   costumerWindow.mainloop()

  def initNewAccountWindow(self):
   newAccountWindow = createNewAccountWindow()
   newAccountWindow.mainloop()

  def initMakeDepositWindow(self):
    makeDepositWindow
    DepositWindow = makeDepositWindow()
    DepositWindow.mainloop()

  def initMakeWithdrawalWindow(self):
    WithdrawalWindow = makeWithdrawalWindow()
    WithdrawalWindow.mainloop()
  
  def initApplyInterestWindow(self):
    InterestWindow = applyInterestWindow()
    InterestWindow.mainloop()
  
  def initExtractWindow(self):
    extract = extractWindow()
    extract.mainloop()

  def destroy(self):
    self.destroy()

  # Create new costumer in the banking system
  self.button = tk.Button(self, text="Create new costumer", command=initCostumerWindow)
  self.button.pack()

  # Create new account for costumer
  self.button = tk.Button(self, text="Create new account for costumer", command=initNewAccountWindow)
  self.button.pack()

  # Make a deposit to an account
  self.button = tk.Button(self, text="Make deposit", command=initMakeDepositWindow)
  self.button.pack()

  # Withdraw an account
  self.button = tk.Button(self, text="Make withdrawal", command=initMakeWithdrawalWindow)
  self.button.pack()

  # Apply interest to an account
  self.button = tk.Button(self, text="Apply interest", command=initApplyInterestWindow)
  self.button.pack()

  # Extract account information
  self.button = tk.Button(self, text="Extract", command=initExtractWindow)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()

