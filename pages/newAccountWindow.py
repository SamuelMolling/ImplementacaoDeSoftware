from tkinter import *
import tkinter.ttk as ttk


class createNewAccountWindow(Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Create New Account for a Costumer")
  self.geometry('300x300')
  
  # CPF
  self.button = Label(self, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Account type
  self.button = Label(self, text="Select account type").pack(side = LEFT)
  self.label = ttk.ComboBox(self)
  self.label['values'] = ('1 - Corrente','2 - Poupança','3 - Investimento')
  self.button.pack()

  # CPF
  self.button = Label(self, text="Enter with your balance").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Button for save
  self.button = Button(self, text="Save", command=validateToSave)
  self.button.pack()

  # Quit
  self.button = Button(self, text="Quit", command=self.destroy())
  self.button.pack()