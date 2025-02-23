from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"    # This is a secret key that is used to protect your application against CSRF attacks.
app.config['MONGO_URI'] = "mongodb+srv://mohsinkhancontact0:<db_password>@cluster0.tohv1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# setup the mongoDB connection
mongo_client = PyMongo(app)
db = mongo_client.db

from application import routes