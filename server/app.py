
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Author, Post
from model import Author, Post


from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Change the URI as needed
db = SQLAlchemy(app)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Validations lab'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    