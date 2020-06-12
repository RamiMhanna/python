from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys 

app = Flask(__name__)
#db = SQLAlchemy(app, session_options={"expire_on_commit": False})
db = SQLAlchemy(app)

migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:111988@localhost:5432/todoapp'

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)
    
    def __repr__(self):
        return f"<todo {self.id} - {self.description}>"


class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)





@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    error = False
    try:
        print('Deleted')
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({ 'success': True })


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description, completed=False)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['completed'] = todo.completed
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    else:
        abort (400)
    
@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    error = False
    try:
        #print('completed', completed)
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    return redirect(url_for('index'))



@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html', data=Todo.query.filter_by(list_id=list_id).order_by('id').all())


@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))