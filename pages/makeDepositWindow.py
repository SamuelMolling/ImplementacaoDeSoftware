from tkinter import *

class makeDepositWindow:
 def __init__(self):
  # Create the secondary window
  self.createCostumerWindow = Tk()
  self.createCostumerWindow.title("Make a deposit")
  self.createCostumerWindow.geometry('300x300')
  
  # CPF
  self.button = Label(self.createCostumerWindow, text="Enter with your CPF").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Balance
  self.button = Label(self.createCostumerWindow, text="Insert a value for the deposit").pack(side = LEFT)
  self.label = Entry(self.createCostumerWindow) 
  self.button.pack()

  # Button for save
  self.button = Button(self.createCostumerWindow, text="Save", command=self.VerifyCPF)
  self.button.pack()

  # Running
  mainloop()

gui = makeDepositWindow()