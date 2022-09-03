from tkinter import *
from tkcalendar import DateEntry

class Extract:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Extract")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Inicial date
  self.button = Label(self.createCostumerWindow, text="Inicial date").pack(side = LEFT)
  self.label = DateEntry(self.createCostumerWindow,selectmode='day')
  self.button.pack()

  # Finish date
  self.button = Label(self.createCostumerWindow, text="Finish date").pack(side = RIGHT)
  self.label = DateEntry(self.createCostumerWindow,selectmode='day')
  self.button.pack()

  # Button for search
  self.button = Button(self.createCostumerWindow, text="Search", command=self.VerifyCPF)
  self.button.pack()

  # Running
  mainloop()

gui = Extract()