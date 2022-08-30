from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox

#Utilizando classe
class initialWindow:
 def __init__(self):
  # Criamos a janela principal
  self.principalWindow = Tk()
  
  # Criando o botão
  self.botao = Button(self.principalWindow, text='Clique aqui', command=self.hello_world)
  
  # Empacotando o botão na janela principal
  self.botao.pack()
  
  # Rodando
  mainloop()

  
 def hello_world(self):
  messagebox.showinfo('Adoro a Apostila Python Progressivo!')
gui = initialWindow()

###############################################################################
def createNewCostumer():
    newWindow = tk.Toplevel(app)

    #Name
    lbl_name = Label(newWindow, text='Name: ').grid( \
    row=1, column=0)
    entry_name = Entry(newWindow, width=30)
    entry_name.grid(row=1, column=1)
    lbl_name.pack()
    button.pack()
   
    #Sex
    lbl_sex = Label(newWindow, text='Sex: ').grid(row=2, column=0)
    sex = ttk.Combobox(newWindow, width=28)
    sex['values']= ('M', 'F')
    sex.current(0)
    sex.grid(row=2, column=1)
    lbl_sex.pack()
    button.pack()
   

    #CPF
    lbl_cpf = Label(newWindow, text='CPF: ').grid( \
    row=3, column=0)
    entry_cpf = Entry(newWindow, width=30)
    entry_cpf.grid(row=3, column=1)
    lbl_cpf.pack()
    button.pack()

    #Birthday
    lbl_birthday = Label(newWindow, text='Birthday: ').grid( \
    row=4, column=0)
    window=DateEntry(newWindow,selectmode='day')
    window.grid(row=4,column=1,padx=15)
    lbl_birthday.pack()
    button.pack()


   
###############################################################################
def createNewAccount():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "Create new account")
    button = tk.Button(newWindow, text = "Create new account2")
    label.pack()
    button.pack()

def makeDeposit():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "makeDeposit")
    button = tk.Button(newWindow, text = "makeDeposit")
    label.pack()
    button.pack()

def makeWithdrawal():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "makeDeposit")
    button = tk.Button(newWindow, text = "makeDeposit")

    label.pack()
    button.pack()    

def applyInterest():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "makeDeposit")
    button = tk.Button(newWindow, text = "makeDeposit")

    label.pack()
    button.pack() 

def getExtract():
    newWindow = tk.Toplevel(app)
    label = tk.Label(newWindow, text = "makeDeposit")
    button = tk.Button(newWindow, text = "makeDeposit")

    label.pack()
    button.pack() 

def quit():
    app.destroy()

app = tk.Tk()
app.title("Simplified Banking System")
app.geometry('300x300')

#Create new costumer in the banking system
button = tk.Button(app, 
              text="Create new costumer",
              command=createNewCostumer)
button.pack()

# Create new account for costumer
button = tk.Button(app, 
              text="Create new account for costumer",
              command=createNewAccount)
button.pack()

# Make a deposit to an account
button = tk.Button(app, 
              text="Make deposit",
              command=makeDeposit)
button.pack()

# Withdraw an account
button = tk.Button(app, 
              text="Make withdrawal",
              command=makeWithdrawal)
button.pack()

# Apply interest to an account
button = tk.Button(app, 
              text="Apply interest",
              command=applyInterest)
button.pack()

# Extract account information
button = tk.Button(app, 
              text="Extract",
              command=getExtract)
button.pack()

# Quit
button = tk.Button(app, 
              text="Quit",
              command=quit)
button.pack()

# Start the mainloop
app.mainloop()