from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry
from lib.main import app


class createCostumerWindow(app):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Create New Costumer")
  self.geometry('300x300')
  
  # Name
  self.button = Label(self, text="Name").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Sex
  self.button = Label(self, text="Sex").pack(side = LEFT)
  self.label = ttk.ComboBox(self)
  self.label['values'] = ('M','F')
  self.button.pack()

  # CPF
  self.button = Label(self, text="CPF").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Birthday
  self.button = Label(self, text="Birthday").pack(side = LEFT)
  self.label = DateEntry(self,selectmode='day')
  self.button.pack()

  # Quit
  self.button = Button(self, text="Quit", command=self.destroy())
  self.button.pack()