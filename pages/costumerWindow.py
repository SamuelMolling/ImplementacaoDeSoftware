import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from lib.main import newClient

class createCostumerWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Create New Costumer")
  self.geometry('300x300')

  self.client = {
    'name': tk.StringVar(),
    'sex': tk.StringVar(),
    'cpf': tk.StringVar(),
    'birthday': tk.StringVar()
  }
  self.name = tk.StringVar(),
  self.sex = tk.StringVar(),
  self.cpf = tk.StringVar(),
  self.birthday = tk.StringVar()

  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  def newCostumer():
    name = self.name
    sex = self.sex
    cpf = self.cpf
    birthday = self.birthday
    newClient(name, sex, cpf, birthday)

  # # Id
  # self.label = tk.Label(self, text="Id", state=tk.DISABLED)
  # self.entry = tk.Entry(self, state=tk.DISABLED)
  # self.label.pack()
  # self.entry.pack()

  # Name
  self.label = tk.Label(self, text="Name")
  self.entry = tk.Entry(self, textvariable=self.name)
  self.label.pack()
  self.entry.pack()

  # Sex
  self.label = tk.Label(self, text="Sex")
  self.entry = ttk.Combobox(self, state='readonly',textvariable=self.sex)
  self.entry['values'] = ('M','F')
  self.label.pack()
  self.entry.pack()

  # CPF
  self.label = tk.Label(self, text="CPF")
  self.entry = tk.Entry(self, textvariable=self.cpf)
  self.label.pack()
  self.entry.pack()

  # Birthday
  self.label = tk.Label(self, text="Birthday")
  self.entry = DateEntry(self,selectmode='day', textvariable=self.birthday)
  self.label.pack()
  self.entry.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=newCostumer)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()