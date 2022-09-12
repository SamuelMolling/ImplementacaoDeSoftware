import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry


class createCostumerWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Create New Costumer")
  self.geometry('300x300')
  
  def destroy(self):
    self.destroy()
    
  # Name
  self.button = tk.Label(self, text="Name").pack(side = tk.LEFT)
  self.label = tk.Entry(self) 
  self.button.pack()

  # Sex
  self.button = tk.Label(self, text="Sex").pack(side = tk.LEFT)
  self.label = ttk.ComboBox(self)
  self.label['values'] = ('M','F')
  self.button.pack()

  # CPF
  self.button = tk.Label(self, text="CPF").pack(side = tk.LEFT)
  self.label = tk.Entry(self) 
  self.button.pack()

  # Birthday
  self.button = tk.Label(self, text="Birthday").pack(side = tk.LEFT)
  self.label = DateEntry(self,selectmode='day')
  self.button.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=app.saveInformations("costumer"))
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()