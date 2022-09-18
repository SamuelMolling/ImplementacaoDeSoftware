import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from lib.main import Operation, checkNumber, getExtract, showMessage

class extractWindow(tk.Tk):
 def __init__(self):
  super().__init__()

  # Create the secondary window
  self.title("Extract")
  self.geometry('600x600')

  self.cpf = tk.StringVar(),
  self.initial_date = tk.StringVar(),
  self.finish_date = tk.StringVar()
  self.initial_hour = tk.IntVar(),
  self.finish_hour = tk.IntVar(),
  self.initial_minute = tk.IntVar(),
  self.finish_minute = tk.IntVar(),
  self.initial_second = tk.IntVar(),
  self.finish_second = tk.IntVar()


  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  def transformDateInDatetime(date, hour, minute, second):
   return f'{date} {hour}:{minute}:{second}'

  def extract():
    if checkNumber(self.cpf.get()) and len(self.cpf.get()) == 11:
      cpf = self.cpf.get()
      initial_date = transformDateInDatetime(self.initial_date.get(), self.initial_hour.get(), self.initial_minute.get(), self.initial_second.get())
      finish_date = transformDateInDatetime(self.finish_date.get(), self.finish_hour.get(), self.finish_minute.get(), self.finish_second.get())
      getExtract(cpf, initial_date, finish_date)
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

  i_hr=tk.Label(self,text='Hour').pack()
  hr = tk.Scale(self, from_=0, to=23,
      orient='horizontal',length=150)
  hr.pack()

  i_mn=tk.Label(self,text='Mintue').pack()
  mn = tk.Scale(self, from_=0, to=59,
      orient='horizontal',length=150)
  mn.pack()

  i_sc=tk.Label(self,text='Second').pack()
  sc = tk.Scale(self, from_=0, to=59,
      orient='horizontal',length=150)
  sc.pack()

  # Finish date
  self.label = tk.Label(self, text="Finish date")
  self.finish_date = DateEntry(self,selectmode='day',years=(1935, 2020),date_pattern='d/m/Y')
  self.label.pack()
  self.finish_date.pack()

  f_hr=tk.Label(self,text='Hour').pack()
  hr = tk.Scale(self, from_=0, to=23,
      orient='horizontal',length=150)
  hr.pack()

  f_mn=tk.Label(self,text='Mintue').pack()
  mn = tk.Scale(self, from_=0, to=59,
      orient='horizontal',length=150)
  mn.pack()
  f_sc=tk.Label(self,text='Second').pack()
  sc = tk.Scale(self, from_=0, to=59,
      orient='horizontal',length=150)
  sc.pack()

  # Button for search
  self.button = tk.Button(self, text="Search", command=extract)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()
