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
    Label(window, text=f"Name:{costumer[0][0]}").pack()
    Label(window, text=f"CPF:{costumer[0][1]}").pack()
    Label(window, text=f"Sex:{costumer[0][2]}").pack()
    Label(window, text=f"Birthday:{costumer[0][3]}").pack()
    Label(window, text="").pack()
    Label(window, text="Bank information").pack()
    Label(window, text=f"Balance: {account[0][0]} R$").pack()
    Label(window, text=f"Account Type: {account[0][1]}").pack()

    ##### Movimentations #####
    movimentacao = ttk.Treeview(window, columns=('Date', 'Type', 'Value'), show='headings')
    movimentacao.heading('Date', text='Date')
    movimentacao.heading('Type', text='Type')
    movimentacao.heading('Value', text='Value')
    movimentacao.pack()

    qnt_deposit = 0
    qnt_withdraw = 0
    qnt_interest = 0
    value_deposit = 0
    value_withdraw = 0
    value_interest = 0

    for movimentation in movimentations:
        movimentacao.insert('', 'end', values=(movimentation[0], movimentation[1], movimentation[2]))
        if movimentation[1] == 'deposito':
            qnt_deposit += 1
            value_deposit += movimentation[2]
        elif movimentation[1] == 'saque':
            qnt_withdraw += 1
            value_withdraw += movimentation[2]
        elif movimentation[1] == 'juros':
            qnt_interest += 1
            value_interest += movimentation[2]
    
    Label(window, text="").pack()
    Label(window, text="Movimentations").pack()
    Label(window, text=f"Deposit: {qnt_deposit} times, total value: {value_deposit} R$").pack()
    Label(window, text=f"Withdraw: {qnt_withdraw} times, total value: {value_withdraw} R$").pack()
    Label(window, text=f"Interest: {qnt_interest} times, total value: {value_interest} %").pack()
    ##### Rodapé #####
    ##### Rodapé #####

    window.mainloop()
