from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:111988@localhost:5432/todoapp'

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    def __repr__(self):
        return f"<todo {self.id} - {self.description}>"


db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
    