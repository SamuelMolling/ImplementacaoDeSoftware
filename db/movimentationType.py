from model import *

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.echo=True

# Validate if the Movimentation Type is already registered
rows = session.query(MovimentationType).all()
if rows > 3:
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