from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

def ExtractWindow(costumer, account, movimentations):
    def clicked():
        if curItem := tree.focus():
            messagebox.showinfo('Item', tree.item(curItem))
        else:
            messagebox.showinfo('Item', 'Nenhum item selecionado')

    window = Tk()
    window.title("Extract Window")
    window.geometry('600x600')

    ##### Cabeçalho #####
    Label(window, text="Costumer information").pack()
    tree = ttk.Treeview(window, columns=(costumer), height=400, selectmode="extended")
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
