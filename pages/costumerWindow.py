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
  self.label = tk.Label(self, text="Name")
  self.entry = tk.Entry(self) 
  self.label.pack()
  self.entry.pack()

  # Sex
  self.label = tk.Label(self, text="Sex")
  self.entry = ttk.Combobox(self)
  self.entry['values'] = ('M','F')
  self.label.pack()
  self.entry.pack()

  # CPF
  self.label = tk.Label(self, text="CPF")
  self.entry = tk.Entry(self) 
  self.label.pack()
  self.entry.pack()

  # Birthday
  self.label = tk.Label(self, text="Birthday")
  self.entry = DateEntry(self,selectmode='day')
  self.label.pack()
  self.entry.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=destroy)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()