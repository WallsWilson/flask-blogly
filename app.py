"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def user():

    users = User.query.all()
    return render_template('base.html', users=users)

@app.route("/users")
def users():
    users = db.session.execute(db.select(User).order_by(user.fist_name)).scalars()
    return render_template("base.html", users=users)

@app.route("/users/new")
def new_users():
    return redirect("new-user.html")

@app.route("/users/new", methods="POST")
def adding_new_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image = request.form["image"]

    new_user = User(first_name=first_name, last_name
    =last_name, image=image)
    db.session.add(new_user)
    db.session.commit()

    return redirect("base.html")