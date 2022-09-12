from tkinter import *


class makeDepositWindow(Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Make a deposit")
  self.geometry('300x300')
  
  # CPF
  self.button = Label(self, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Balance
  self.button = Label(self, text="Insert a value for the deposit").pack(side = LEFT)
  self.label = Entry(self) 
  self.button.pack()

  # Button for save
  self.button = Button(self, text="Save", command=self.VerifyCPF)
  self.button.pack()
    
  # Quit
  self.button = Button(self, text="Quit", command=self.destroy())
  self.button.pack()