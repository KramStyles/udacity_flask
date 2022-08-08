import sys

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.debug = True

# Code to connect to the database. dialect->username->password->host&port->dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:*@localhost:5432/db_udacity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
    data = Todo.query.order_by('id').all()
    return render_template('index.html', data=data)


# Function calls
@app.route('/todos/create', methods=['POST'])
def todo_create():
    error = False
    msg = ''

    try:
        item = request.form.get('todo_item', '').strip()
        # item = request.json.get('todo_item', '').strip()
        if not item:
            return "Empty values are not allowed"

        item = Todo(description=item)
        db.session.add(item)
        db.session.commit()
    except Exception as err:
        msg = str(err)
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()

    if not error:
        return redirect(url_for('index'))
    return msg


@app.route('/todos/update/<data_id>', methods=['POST'])
def todo_update(data_id):
    state = request.form.get('current_state')
    msg = ''

    try:
        todo = Todo.query.get(data_id)
        todo.completed = True if state == 'true' else False
        db.session.commit()

        msg = 'ok'
    except Exception as err:
        db.session.rollback()
        msg = str(err)
    finally:
        db.session.close()

    return msg


if __name__ == '__main__':
    app.run(debug=True)
