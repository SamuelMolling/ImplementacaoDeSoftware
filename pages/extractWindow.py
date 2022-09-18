import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from lib.main import checkNumber, makeExtract, showMessage

class extractWindow(tk.Tk):
 def __init__(self):
  super().__init__()

  # Create the secondary window
  self.title("Extract")
  self.geometry('300x300')

  self.cpf = tk.StringVar(),
  self.initial_date = tk.StringVar(),
  self.finish_date = tk.StringVar()

  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  def extract():
    if checkNumber(self.cpf.get()) and len(self.cpf.get()) == 11:
      cpf = self.cpf.get()
      initial_date = self.initial_date.get()
      finish_date = self.finish_date.get()
      makeExtract(cpf, initial_date, finish_date)
    else:
      showMessage("Please, verify the information CPF.", 'error')

  # CPF
  self.label = tk.Label(self, text="Enter with your CPF")
  self.cpf = tk.Entry(self)
  self.label.pack()
  self.cpf.pack()

  # Inicial date
  self.label = tk.Label(self, text="Inicial date")
  self.initial_date = DateEntry(self,selectmode='day',years=(1935, 2020),date_pattern='d/m/Y')
  self.label.pack()
  self.initial_date.pack()

  # Finish date
  self.label = tk.Label(self, text="Finish date")
  self.finish_date = DateEntry(self,selectmode='day',years=(1935, 2020),date_pattern='d/m/Y')
  self.label.pack()
  self.finish_date.pack()

  # Button for search
  self.button = tk.Button(self, text="Search", command=extract)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()
