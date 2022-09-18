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

    for i in costumer:
        Label(window, text=costumer[0][i]).pack()
    # Label(window, text=f"Name:{costumer[0][0]}").pack()
    # Label(window, text="Costumer information").pack()
    # costumerInformationColumn = ('Name', 'CPF', 'Sex', 'Birthday')
    # costumer_view = ttk.Treeview(window, columns=costumerInformationColumn, height=50, selectmode="extended", show='headings')
    # costumer_view.heading('Name', text="Name")
    # costumer_view.heading('CPF', text="CPF")
    # costumer_view.heading('Sex', text="Sex")
    # costumer_view.heading('Birthday', text="Birthday")

    # for x in costumer:
    #     costumer_view.insert('', 'end', values=(x[0], x[1], x[2], x[3]))
    # costumer_view.pack()

    # Label(window, text="Bank information").pack()
    # bankingInformationColumn = ('AccountType', 'Balance')
    # banking_view = ttk.Treeview(window, columns=bankingInformationColumn, height=200, selectmode="extended", show='headings')
    # banking_view.heading('AccountType', text="AccountType", anchor=W)
    # banking_view.heading('Balance', text="Balance", anchor=W)

    # for x in account:
    #     banking_view.insert('', 'end', values=(x[0], x[1]))
    # banking_view.pack()

    # ##### Movimentações #####
    # Label(window, text="Movimentations").pack()
    # ##### Movimentações #####
    # movimentationsColumn = ('Date', 'Description', 'Value')
    # tree = ttk.Treeview(window, columns=movimentationsColumn, height=200, selectmode="extended", show='headings')
    # tree.heading('Date', text="Date", anchor=W)
    # tree.heading('Description', text="Description", anchor=W)
    # tree.heading('Value', text="Value", anchor=W)

    # for x in movimentations:
    #     tree.insert('', 'end', values=(x[0], x[1], x[2]))
    # tree.pack()

    ##### Rodapé #####
    ##### Rodapé #####
    Button(window, text="Ler item", command=clicked).pack()

    window.mainloop()
