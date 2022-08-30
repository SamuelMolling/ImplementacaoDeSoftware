from db import *

Session = db.sessionmaker(bind=engine)
session = Session()

# Insert
try:

    s4 = [
        Student(
            name='Bianca', lastname='Santos', sex='F', age=18,
            addresses=[Address(address='Rua das Camélias', email='bianca@gmail.com')]),

        Student(
            name='Renato', lastname='Assis', sex='M', age=22,
            addresses=[Address(address='Rua das Papoulas', email='renato@gmail.com')])
    ]

    session.add_all(s4)
    session.commit()
except Exception as e:
    session.rollback()
    print(e)

# Encerra a conexão com o banco de dados
session.close()
conn.close()
engine.dispose()