from curses.ascii import isdigit
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from lib.main import checkNumber, checkString, newClient, showMessage

class createCostumerWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  
  # Create the secondary window
  self.title("Create New Costumer")
  self.geometry('300x300')

  self.id = tk.IntVar(),
  self.name = tk.StringVar(),
  self.sex = tk.StringVar(),
  self.cpf = tk.StringVar(),
  self.birthday = tk.StringVar()

  # Destroy this page
  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  # Create new costumer
  def newCostumer():
    if checkNumber(self.cpf.get()) and len(self.cpf.get()) == 11 and checkString(self.name.get()) is False:
      name = self.name.get()
      sex = self.sex.get()
      cpf = self.cpf.get()
      birthday = self.birthday.get()
      newClient(name, sex, cpf, birthday)
    else:
      showMessage("Please, verify the information name or CPF.", 'error')

  # Name
  self.label = tk.Label(self, text="Name")
  self.name = tk.Entry(self)
  self.label.pack()
  self.name.pack()

  # Sex
  self.label = tk.Label(self, text="Sex")
  self.sex = ttk.Combobox(self, state='readonly')
  self.sex['values'] = ('M','F')
  self.label.pack()
  self.sex.pack()

  # CPF
  self.label = tk.Label(self, text="CPF")
  self.cpf = tk.Entry(self)
  self.label.pack()
  self.cpf.pack()

  # Birthday
  self.label = tk.Label(self, text="Birthday")
  self.birthday = DateEntry(self,selectmode='day',years=(1935, 2020),date_pattern='d/m/Y')
  self.label.pack()
  self.birthday.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=newCostumer)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()