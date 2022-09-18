import tkinter as tk
from tkinter import messagebox
from lib.main import Operation, checkNumber, showMessage

class applyInterestWindow(tk.Tk):
 def __init__(self):
  super().__init__()

  # Create the secondary window
  self.title("Apply Interest")
  self.geometry('300x300')

  self.cpf = tk.StringVar(),
  self.value = tk.DoubleVar()
  
  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  # Make a deposit for a costumer
  def applyInterest():
    if checkNumber(self.cpf.get()) and len(self.cpf.get()) == 11 and float(self.value.get()) > 0:
      cpf = self.cpf.get()
      value = self.value.get()
      Operation(3, cpf, value)
    else:
      showMessage("Please, verify the information value or CPF.", 'error')

  # CPF
  self.label = tk.Label(self, text="Enter with your CPF")
  self.cpf = tk.Entry(self) 
  self.label.pack()
  self.cpf.pack()

  # Balance
  self.label = tk.Label(self, text="Insert a value for the interest")
  self.value = tk.Entry(self) 
  self.label.pack()
  self.value.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=applyInterest)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()