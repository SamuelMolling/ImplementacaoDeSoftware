import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox

class extractWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Extract")
  self.geometry('300x300')
  
  def destroy():
    op = messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        self.destroy()

  # CPF
  self.label = tk.Label(self, text="Enter with your CPF")
  self.entry = tk.Entry(self) 
  self.label.pack()
  self.entry.pack()

  # Inicial date
  self.label = tk.Label(self, text="Inicial date")
  self.entry = DateEntry(self,selectmode='day')
  self.label.pack()
  self.entry.pack()

  # Finish date
  self.label = tk.Label(self, text="Finish date")
  self.entry = DateEntry(self,selectmode='day')
  self.label.pack()
  self.entry.pack()

  # Button for search
  self.button = tk.Button(self, text="Search", command=destroy)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()
