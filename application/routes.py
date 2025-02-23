from application import app
from flask import render_template
from application.forms import TodoForm

@app.route('/')
def index():
    return render_template('view_todos.html', title='view_todos Page')    

    
@app.route('/add_todo')
def add_todo():
    form = TodoForm()
    return render_template('add_todo.html', form=form)    