from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import DateEntry


def btn_nome_click():
  lbl_status.configure(text='Nome = ' + \
    entry_nome.get())
def btn_sexo_click():
  lbl_status.configure(text='Sexo = ' + \
    combo_sexo.get())
window = Tk()
window.title("Simplified Banking System")
window.geometry('600x300')
lbl_nome = Label(window, text='Name: ').grid( \
  row=1, column=0)
entry_nome = Entry(window, width=30)
entry_nome.grid(row=1, column=1)

#Sex
Label(window, text='Sex: ').grid(row=2, column=0)
combo_sexo = ttk.Combobox(window, width=28)
combo_sexo['values']= ('M', 'F')
combo_sexo.current(0)
combo_sexo.grid(row=2, column=1)

#CPF
lbl_nome = Label(window, text='CPF: ').grid( \
  row=3, column=0)
entry_nome = Entry(window, width=30)
entry_nome.grid(row=3, column=1)

#Birhday
lbl_nome = Label(window, text='Birthday: ').grid( \
  row=4, column=0)
window=DateEntry(window,selectmode='day')
window.grid(row=4,column=1,padx=15)


window.mainloop()