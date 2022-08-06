from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.debug = True

# Code to connect to the database. dialect->username->password->host&port->dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:*@localhost:5432/db_udacity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name


db.create_all()


@app.route('/')
def index():
    person = Person.query.first()
    return f'Hello, {person.name}!'


if __name__ == '__main__':
    app.run(debug=True)
