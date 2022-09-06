from db import model
def getCPF(cpf):
    # Get the CPF from the database
    self.db_student = self.session.query(Student).where(Student.id == 3).first()
    for k, v in self.var_student.items():
        v.set(getattr(self.db_student, k))

def insertBalance(action, value):
    # Insert the balance into the database
    self.db_student = self.session.query(Student).where(Student.id == 3).first()
    for k, v in self.var_student.items():
        v.set(getattr(self.db_student, k))

def insertClient(name, sex, cpf, birthday):
    pass

def insertBankAccount(balance, cpf, accountType):
    pass

def insertMovimentation(value, account, movimentationType):
    pass


