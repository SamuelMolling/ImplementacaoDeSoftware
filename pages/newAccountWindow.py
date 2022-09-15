import tkinter as tk
import tkinter.ttk as ttk


class createNewAccountWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Create New Account for a Costumer")
  self.geometry('300x300')

  def destroy():
    self.destroy()

  # CPF

  self.label = tk.Label(self, text="Enter with your CPF")
  self.entry = tk.Entry(self)
  self.label.pack()
  self.entry.pack()

  # Account type
  self.label = tk.Label(self, text="Select account type")
  self.entry = ttk.Combobox(self)
  self.entry['values'] = ('1 - Corrente','2 - Poupança','3 - Investimento')
  self.label.pack()
  self.entry.pack()

  # CPF
  self.label = tk.Label(self, text="Enter with your balance")
  self.entry = tk.Entry(self) 
  self.label.pack()
  self.entry.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=destroy)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()