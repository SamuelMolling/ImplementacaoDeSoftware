from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry


class createCostumerWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Create New Costumer")
  self.createCostumerWindow.geometry('300x300')
  
  # Name
  self.button = Label(self.createCostumerWindow, text="Name").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Sex
  self.button = Label(self.createCostumerWindow, text="Sex").pack(side = LEFT)
  self.label = ttk.ComboBox(self.createCostumerWindow)
  self.label['values'] = ('M','F')
  self.button.pack()

  # CPF
  self.button = Label(self.createCostumerWindow, text="CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Birthday
  self.button = Label(self.createCostumerWindow, text="Birthday").pack(side = LEFT)
  self.label = DateEntry(self.createCostumerWindow,selectmode='day')
  self.button.pack()

  # Running
  mainloop()

gui = createCostumerWindow()