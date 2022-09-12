import tkinter as tk
from tkcalendar import DateEntry

class extractWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Extract")
  self.geometry('300x300')
  
  def destroy(self):
    self.destroy()

  # CPF
  self.button = tk.Label(self, text="Enter with your CPF").pack(side = tk.LEFT)
  self.label = tk.Entry(self) 
  self.button.pack()

  # Inicial date
  self.button = tk.Label(self, text="Inicial date").pack(side = tk.LEFT)
  self.label = DateEntry(self,selectmode='day')
  self.button.pack()

  # Finish date
  self.button = tk.Label(self, text="Finish date").pack(side = tk.RIGHT)
  self.label = DateEntry(self,selectmode='day')
  self.button.pack()

  # Button for search
  self.button = tk.Button(self, text="Search", command=self.VerifyCPF)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()
