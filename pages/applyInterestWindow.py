import tkinter as tk

class applyInterestWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Apply Interest")
  self.geometry('300x300')
  
  def destroy():
    self.destroy()

  # CPF
  self.label = tk.Label(self, text="Enter with your CPF")
  self.entry = tk.Entry(self) 
  self.label.pack()
  self.entry.pack()

  # Balance
  self.label = tk.Label(self, text="Insert a value for the interest")
  self.entry = tk.Entry(self) 
  self.label.pack()
  self.entry.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=destroy)
  self.button.pack()

  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()