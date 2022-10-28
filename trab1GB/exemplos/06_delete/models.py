from app import db

class Task(db.Model):
    __tablename__ = 'task'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'

if __name__ == '__main__':
    from datetime import datetime
    db.create_all()
    for i in range(3):
        task = Task(title=f'Tarefa {i + 1}', date=datetime.now())
        db.session.add(task)
        print(task)
    db.session.commit()