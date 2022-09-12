import tkinter as tk
import tkinter.ttk as ttk


class createNewAccountWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Create New Account for a Costumer")
  self.geometry('300x300')

  def destroy(self):
    self.destroy()

  # CPF
  self.button = tk.Label(self, text="Enter with your CPF").pack(side = tk.LEFT)
  self.label = tk.Entry(self) 
  self.button.pack()

  # Account type
  self.button = tk.Label(self, text="Select account type").pack(side = tk.LEFT)
  self.label = ttk.ComboBox(self)
  self.label['values'] = ('1 - Corrente','2 - Poupança','3 - Investimento')
  self.button.pack()

  # CPF
  self.button = tk.Label(self, text="Enter with your balance").pack(side = tk.LEFT)
  self.label = tk.Entry(self) 
  self.button.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=validateToSave)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()