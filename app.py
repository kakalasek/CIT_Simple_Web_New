from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import Text, String
from dotenv import load_dotenv
import os
from wtforms import Form, StringField, SubmitField, validators

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv("DATABASE_URI")}"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class BlogForm(Form):
    user = StringField("User", [validators.DataRequired()])
    text = StringField("Text", [validators.DataRequired()])
    submit = SubmitField("Send")

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column(String(50))
    text: Mapped[str] = mapped_column(Text())


db.init_app(app)

with app.app_context():
    db.create_all()

comments = []

def fetch_comments():
    global comments

    comments_fetched = db.session.execute(db.select(Comment).order_by(Comment.id)).scalars()

    for comment_fetched in comments_fetched:
        comment_fetched_json = {"id": comment_fetched.id, "user": comment_fetched.user, "text": comment_fetched.text}

        if comment_fetched_json not in comments:
            comments.append(comment_fetched_json)

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
    blogform = BlogForm(request.form)

    fetch_comments()

    if request.method == 'POST' and blogform.validate():
        comment = Comment(user=blogform.user.data, text=blogform.text.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('page')), 302

    return render_template("page.html", blogform=blogform, comments=comments), 200