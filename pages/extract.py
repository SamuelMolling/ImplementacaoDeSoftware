from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

def ExtractWindow(costumer, account, movimentations):
    def clicked():
        if curItem := tree.focus():
            messagebox.showinfo('Item', tree.item(curItem))
        else:
            messagebox.showinfo('Item', 'Item not selected')

    window = Tk()
    window.title("Extract Window")
    window.geometry('800x800')

    ##### Cabeçalho #####
    Label(window, text="Costumer information").pack()
    costumerInformationColumn = ('Name', 'CPF', 'Sex', 'Birthday')
    tree = ttk.Treeview(window, columns=costumerInformationColumn, height=50, selectmode="extended", show='headings')
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('CPF', text="CPF", anchor=W)
    tree.heading('Sex', text="Sex", anchor=W)
    tree.heading('Birthday', text="Birthday", anchor=W)

    for x in costumer:
        tree.insert('', 'end', values=(x[0], x[1], x[2], x[3]))
    tree.pack()

    Label(window, text="Bank information").pack()
    costumerInformationColumn = ('AccountType', 'Balance')
    tree = ttk.Treeview(window, columns=costumerInformationColumn, height=200, selectmode="extended", show='headings')
    tree.heading('AccountType', text="AccountType", anchor=W)
    tree.heading('Balance', text="Balance", anchor=W)

    for x in account:
        tree.insert('', 'end', vvalues=(x[0], x[1]))
    tree.pack()

    ##### Movimentações #####
    Label(window, text="Movimentations").pack()
    ##### Movimentações #####

    ##### Rodapé #####
    ##### Rodapé #####
    Button(window, text="Ler item", command=clicked).pack()

    window.mainloop()
