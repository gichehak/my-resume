from flask_script import Manager
from myresume import app, db, Professor

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    thomas_Trinter = Professor(name='Thomas Trinter', department='Finance')
    clinton_White = Professor(name='Clinton White', department='Management Information Systems')
    mark_Serva = Professor(name='Mark Serva', department='Management Information Systems')
    edward_Hortono = Professor(name='Edward Hortono', department='Management Information Systems')
    db.session.add(clinton_White)
    db.session.add(thomas_Trinter)
    db.session.add(mark_Serva)
    db.session.add(edward_Hortono)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
