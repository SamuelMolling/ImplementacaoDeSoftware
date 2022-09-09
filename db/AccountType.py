from model import *

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True

# Validate if the Account Type is already registered
rows = session.query(AccountType).all()
if rows > 3:
# Insert
    try:

        default = [
            AccountType(
                type='corrente'),
            AccountType(
                type='poupanca'),
            AccountType(
                type='investimento')
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