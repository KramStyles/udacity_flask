from flask import Flask, render_template
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


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)


@app.route('/')
def index():
    data = ['Wash clothes', 'Eat food', 'Play games', 'Finish project']
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
