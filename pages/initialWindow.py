from tkinter import *

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