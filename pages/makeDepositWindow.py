import tkinter as tk
from tkinter import messagebox
from lib.main import checkNumber, showMessage


class makeDepositWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Make a deposit")
  self.geometry('300x300')

  self.cpf = tk.StringVar(),
  self.value = tk.DoubleVar()
  
  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  def makeDeposit():
    if checkNumber(self.cpf.get()) and len(self.cpf.get()) == 11:
      cpf = self.cpf.get()
      value = self.value.get()
      makeDeposit(cpf, value)
    else:
      showMessage("Please, verify the information name or CPF.", 'error')

  # CPF
  self.label = tk.Label(self, text="Enter with your CPF")
  self.cpf = tk.Entry(self) 
  self.label.pack()
  self.cpf.pack()

  # Balance
  self.label = tk.Label(self, text="Insert a value for the deposit")
  self.value = tk.Entry(self)
  self.label.pack() 
  self.value.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=makeDeposit)
  self.button.pack()
    
  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()