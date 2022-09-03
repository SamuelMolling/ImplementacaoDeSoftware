from tkinter import *
import tkinter.ttk as ttk

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
  
gui = createNewAccountWindow()