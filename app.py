from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
from wtforms import Form, StringField, SubmitField, validators

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.environ["DATABASE_URI"]}"

class Base(DeclarativeBase):
    pass

class BlogForm(Form):
    user = StringField("User", [validators.DataRequired()])
    text = StringField("Text", [validators.DataRequired()])
    submit = SubmitField("Send")

db = SQLAlchemy(model_class=Base)

@app.route("/")
def default():
    return redirect(url_for('page')), 302

@app.route("/get-blogs")
def get_blogs():
    return "Not implemented yet", 400

@app.route("/post-blogs", methods=["POST"])
def post_blogs():
    return "Not implemented yet", 400

@app.route("/page", methods=["GET", "POST"])
def page():
    return render_template("page.html"), 200