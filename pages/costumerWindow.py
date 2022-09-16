from curses.ascii import isdigit
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from lib.main import checkNumber, convertStringInDate, newClient, showMessage

class createCostumerWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Create New Costumer")
  self.geometry('300x300')

  # self.var_client = {
  #   'id': tk.IntVar(),
  #   'name': tk.StringVar(),
  #   'sex': tk.StringVar(),
  #   'cpf': tk.StringVar(),
  #   'birthday': tk.StringVar()
  # }
  self.id = tk.IntVar(),
  self.name = tk.StringVar(),
  self.sex = tk.StringVar(),
  self.cpf = tk.StringVar(),
  self.birthday = tk.StringVar()

  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  def newCostumer():
    if checkNumber(self.cpf.get()):
      name = self.name.get()
      sex = self.sex.get()
      cpf = self.cpf.get()
      birthday = self.birthday.get()
      convertStringInDate(birthday)
      newClient(name, sex, cpf, birthday)
    else:
      showMessage("Please, use numbers in CPF.", 'error')


  # # Id
  # self.label = tk.Label(self, text="Id", state=tk.DISABLED)
  # self.entry = tk.Entry(self, state=tk.DISABLED)
  # self.label.pack()
  # self.entry.pack()

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
  self.birthday = DateEntry(self,selectmode='day',years=(1935, 2020))
  self.label.pack()
  self.birthday.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=newCostumer)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()