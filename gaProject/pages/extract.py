from tkinter import *
import tkinter.ttk as ttk

def ExtractWindow(costumer, account, movimentations, initialDate, finalDate):

    window = Tk()
    window.title("Extract Window")
    window.geometry('800x800')

    ##### Cabeçalho #####
    Label(window, text="Costumer information", font=('Times', 24)).pack()
    Label(window, text=f"Name:{costumer[0].name}").pack()
    Label(window, text=f"CPF:{costumer[0].cpf}").pack()
    Label(window, text=f"Sex:{costumer[0].sex}").pack()
    Label(window, text=f"Birthday:{costumer[0].birthday}").pack()
    Label(window, text="").pack()
    Label(window, text="Bank information", font=('Times', 24)).pack()
    Label(window, text=f"Balance: {account[0].balance} R$").pack()
    Label(window, text=f"Account Type: {account[0].type}").pack()
    Label(window, text="").pack()
    Label(window, text="Search date", font=('Times', 24)).pack()
    Label(window, text=f"Initial Date: {initialDate}").pack()
    Label(window, text=f"Final Date: {finalDate}").pack()
    Label(window, text="").pack()

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

    ##### Rodapé #####
    Label(window, text="").pack()
    Label(window, text="Movimentations", font=('Times', 24)).pack()
    Label(window, text=f"Deposit: {qnt_deposit} times, total value: {round(value_deposit,2)} R$").pack()
    Label(window, text=f"Withdraw: {qnt_withdraw} times, total value: {round(value_withdraw,2)} R$").pack()
    Label(window, text=f"Interest: {qnt_interest} times, total value: {value_interest} %").pack()

    window.mainloop()
