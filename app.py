from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.environ["DATABASE_URI"]}"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Comment(db.Model):
    id: Mapped  
    user = db.Column()

@app.route("/get-blogs")
def get_blogs():
    return "Not implemented yet", 400

@app.route("/post-blogs", methods=["POST"])
def post_blogs():
    return "Not implemented yet", 400