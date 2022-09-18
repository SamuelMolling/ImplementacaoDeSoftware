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
    window.geometry('600x600')

    ##### Cabeçalho #####
    Label(window, text="Costumer information").pack()
    costumerInformationColumn = ('Name', 'CPF', 'Sex', 'Birthday')
    tree = ttk.Treeview(window, columns=costumerInformationColumn, height=400, selectmode="extended", show='headings')
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('CPF', text="CPF", anchor=W)
    tree.heading('Sex', text="Sex", anchor=W)
    tree.heading('Birthday', text="Birthday", anchor=W)

    # Generate data of costumer
    for x in costumer:
        tree.insert('', 'end', values=x)
    tree.pack()

    Label(window, text="Bank information").pack()
    costumerInformationColumn = ('AccountType', 'Balance')
    tree = ttk.Treeview(window, columns=costumerInformationColumn, height=400, selectmode="extended", show='headings')
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('CPF', text="CPF", anchor=W)
    tree.heading('Sex', text="Sex", anchor=W)
    tree.heading('Birthday', text="Birthday", anchor=W)

    # Generate data of costumer
    for x in costumer:
        tree.insert('', 'end', values=x)
    tree.pack()
    ##### Finish Costumer information #####

    Button(window, text="Ler item", command=clicked).pack()

    # Sem scroll bars
    tree = ttk.Treeview(window, columns=("Col1", "Col2", "Col3"), height=400, selectmode="extended")


    tree.heading('Col1', text="Coluna 1", anchor=W)
    tree.heading('Col2', text="Coluna 2", anchor=W)
    tree.heading('Col3', text="Coluna 3", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    for i in range(30):
        tree.insert("", 'end', values=(i, i + 1, i + 2))

    window.mainloop()
