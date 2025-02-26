from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"    # This is a secret key that is used to protect your application against CSRF attacks.
app.config['MONGO_URI'] = "mongodb+srv://mohsinkhancontact0:Mohsin123khan@cluster0.tohv1.mongodb.net/todo_flask?retryWrites=true&w=majority&appName=Cluster0"

# setup the mongoDB connection
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes