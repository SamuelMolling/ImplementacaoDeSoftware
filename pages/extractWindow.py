from tkinter import *
from tkcalendar import DateEntry

class extractWindow(Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Extract")
  self.geometry('300x300')
  
  # CPF
  self.button = Label(self, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Inicial date
  self.button = Label(self, text="Inicial date").pack(side = LEFT)
  self.label = DateEntry(self,selectmode='day')
  self.button.pack()

  # Finish date
  self.button = Label(self, text="Finish date").pack(side = RIGHT)
  self.label = DateEntry(self,selectmode='day')
  self.button.pack()

  # Button for search
  self.button = Button(self, text="Search", command=self.VerifyCPF)
  self.button.pack()

  # Quit
  self.button = Button(self, text="Quit", command=self.destroy())
  self.button.pack()
