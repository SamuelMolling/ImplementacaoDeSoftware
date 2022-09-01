from model import *

Session = orm.sessionmaker(bind=engine)
session = Session()

# Insert
try:

    default = [
        MovimentationType(
            type='deposito'),
        MovimentationType(
            type='saque'),
        MovimentationType(
            type='juros')
    ]

    session.add_all(default)
    session.commit()
except Exception as e:
    session.rollback()
    print(e)

# Close connection with database
session.close()
conn.close()
engine.dispose()