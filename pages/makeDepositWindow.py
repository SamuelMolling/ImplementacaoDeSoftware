import tkinter as tk


class makeDepositWindow(tk.Tk):
 def __init__(self):
  super().__init__()
  # Create the secondary window
  self.title("Make a deposit")
  self.geometry('300x300')
  
  def destroy(self):
    self.destroy()

  # CPF
  self.button = tk.Label(self, text="Enter with your CPF").pack(side = tk.LEFT)
  self.label = tk.Entry(self) 
  self.button.pack()

  # Balance
  self.button = tk.Label(self, text="Insert a value for the deposit").pack(side = tk.LEFT)
  self.label = tk.Entry(self) 
  self.button.pack()

  # Button for save
  self.button = tk.Button(self, text="Save", command=self.VerifyCPF)
  self.button.pack()
    
  # Quit
  self.button = tk.Button(self, text="Quit", command=destroy)
  self.button.pack()