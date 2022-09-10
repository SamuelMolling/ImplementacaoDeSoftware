import tkinter as tk

class app(tk):
    def __init__(self):
        super().__init__()

    Cliente = {
        'id': tk.IntVar(),
        'name': tk.StringVar(),
        'sex': tk.StringVar(),
        'cpf': tk.StringVar(),
        'birthday': tk.StringVar()
    }

    bankAccount = {
        'id': tk.IntVar(),
        'balance': tk.IntVar(),
        'cpf': tk.StringVar(),
        'accountType': tk.StringVar()
    }

    accountType = {
        'id': tk.IntVar(),
        'type': tk.StringVar()
    }

    movimentationType = {
        'id': tk.IntVar(),
        'type': tk.StringVar()
    }

    movimentation = {
        'id': tk.IntVar(),
        'value': tk.IntVar(),
        'account': tk.IntVar(),
        'movimentationType': tk.IntVar()
    }

    

    def closeWindow(self):
        self.destroy()

    def VerifyCPF(self):
        pass