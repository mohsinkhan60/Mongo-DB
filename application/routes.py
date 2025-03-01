from application import app
from flask import render_template, request, redirect, flash, url_for
from application import db
from application.forms import TodoForm
from datetime import datetime
from bson import ObjectId

@app.route('/')
def get_todos():
    todos = []
    for todo in db.todo_flask.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%Y-%m-%d %H:%M:%S")
        todos.append(todo)
    return render_template('view_todos.html', title='view_todos Page', todos=todos)    

@app.route('/add_todo', methods=['POST', 'GET'])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        db.todo_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.now()
        })
        flash('Todo added successfully', 'success')
        return redirect("/")
    else:
        form = TodoForm()
    return render_template('add_todo.html', form=form)

@app.route('/update_todo/<id>', methods=['POST', 'GET'])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        db.todo_flask.find_one_and_update({
            "_id": ObjectId(id)
        }, {
            "$set": {
                "name": todo_name,
                "description": todo_description,
                "completed": completed,
                "date_created": datetime.now()
            }
        })
        flash('Todo updated successfully', 'success')
        return redirect("/")
    else:
        form = TodoForm()
        todo = db.todo_flask.find_one({"_id": ObjectId(id)})
        if todo:
            form.name.data = todo.get("name", None)
            form.description.data = todo.get("description", None)
            form.completed.data = todo.get("completed", None)
        else:
            flash('Todo not found', 'danger')
            return redirect("/")
    return render_template('add_todo.html', form=form)

@app.route('/delete_todo/<id>')
def delete_todo(id):
    db.todo_flask.find_one_and_delete({"_id": ObjectId(id)})
    flash('Todo deleted successfully', 'success')
    return redirect("/")