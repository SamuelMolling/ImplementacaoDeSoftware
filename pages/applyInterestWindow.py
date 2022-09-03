from tkinter import *

class applyInterestWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Apply Interest")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Balance
  self.button = Label(self.createCostumerWindow, text="Insert a value for the interest").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Running
  mainloop()

gui = applyInterestWindow()