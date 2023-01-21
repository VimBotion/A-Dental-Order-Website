from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Set up the data base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '\xb5\xe2\xe0\xad\xec\xb9\xd3\xef\x11\x0f\xae\x98\xf0\x9e\x9d\x05\xf1'

with app.app_context():
    db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False)
    hash = db.Column(db.String(30), nullable=False)

    def __init__(self, username, email, hash):
        self.name = username
        self.email = email
        self.hash = hash

@app.route('/')
@login_required
def index():
    user = session["user"]
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("name")
        session["user"] = user
        return redirect('/')
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/login')

@app.route('/register')
def register():
    return render_template("register.html")
    



if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
