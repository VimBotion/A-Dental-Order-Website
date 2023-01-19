from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["user"] is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Set up the data base
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///usuario.db'
with app.app_context():
    db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '\xb5\xe2\xe0\xad\xec\xb9\xd3\xef\x11\x0f\xae\x98\xf0\x9e\x9d\x05\xf1'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    hash = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
@login_required
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        session["user"] = user
        return redirect('/')
    else:
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect("/login")

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/login')

    



if __name__ == "__main__":
    app.run(debug=True)
