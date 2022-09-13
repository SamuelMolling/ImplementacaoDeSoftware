#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from db.model import *
from db.movimentationType import *
from db.AccountType import *
from pages.initialWindow import *

if __name__ == "__main__":
    app = initialWindow()
    app.mainloop()
    ##Pesquisar init.py para criar o banco de dados