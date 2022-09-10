from tkinter import *
from lib.main import app

class applyInterestWindow(app):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Apply Interest")
  self.geometry('300x300')
  
  # CPF
  self.button = Label(self, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Balance
  self.button = Label(self, text="Insert a value for the interest").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Button for save
  self.button = Button(self, text="Save", command=VerifyCPF)
  self.button.pack()

  # Quit
  self.button = Button(self, text="Quit", command=self.destroy())
  self.button.pack()