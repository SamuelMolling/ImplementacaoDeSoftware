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

  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  def newCcostumer():
    for k, v in self.client.items():
      setattr(self.client, k, v.get())
      print(k, v.get())

    # name = self.name.get()
    # sex = self.sex.get()
    # cpf = self.cpf.get()
    # birthday = self.birthday.get()
    # newClient(name, sex, cpf, birthday)

  # Name
  self.label = tk.Label(self, text="Name")
  self.entry = tk.Entry(self, textvariable=self.client.get('name'))
  self.label.pack()
  self.entry.pack()

  # Sex
  self.label = tk.Label(self, text="Sex")
  self.entry = ttk.Combobox(self, textvariable=self.client.get('sex'))
  self.entry['values'] = ('M','F')
  self.label.pack()
  self.entry.pack()

  # CPF
  self.label = tk.Label(self, text="CPF")
  self.entry = tk.Entry(self, textvariable=self.client.get('cpf'))
  self.label.pack()
  self.entry.pack()

  # Birthday
  self.label = tk.Label(self, text="Birthday")
  self.entry = DateEntry(self,selectmode='day', textvariable=self.client.get('birthday'))
  self.label.pack()
  self.entry.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=newCcostumer)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()