"""Blogly application."""

from flask import Flask, redirect, render_template,Request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def root():

    
    return redirect("/users")

@app.route("/users")
def users_index():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("index.html", users=users)

@app.route("/users/new", methods=["GET"])
def new_users():
    return redirect("new-user.html")

@app.route("/users/new", methods=["POST"])
def adding_new_user():
    new_user = User(
        first_name = Request.form["first_name"],
        last_name = Request.form["last_name"],
        image = Request.form["image"] or None)

   
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")