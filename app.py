from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.db'
with app.app_context():
    db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '\xb5\xe2\xe0\xad\xec\xb9\xd3\xef\x11\x0f\xae\x98\xf0\x9e\x9d\x05\xf1'



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    hash = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def infex():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)