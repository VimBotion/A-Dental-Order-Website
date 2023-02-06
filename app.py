from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date


app = Flask(__name__)

# Forces the user to be log in to see some contents of the page
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Set up the data base
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '\xb5\xe2\xe0\xad\xec\xb9\xd3\xef\x11\x0f\xae\x98\xf0\x9e\x9d\x05\xf1'

with app.app_context():
    db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    hash = db.Column(db.String(30), nullable=False)
    patient = db.relationship('Order', backref='doctor', uselist=False)

    def __init__(self, username, email, hash):
        self.username = username
        self.email = email
        self.hash = hash

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(120), nullable=False)
    patient_age = db.Column(db.Integer, nullable=False)
    color_chart = db.Column(db.String(30), nullable=False)
    dates = db.Column(db.Date)
    patient_sex = db.Column(db.String(10), nullable=False)
    indications = db.Column(db.String(120), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, patient_name, patient_age, color_chart, dates, patient_sex, indications, doctor_id):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.color_chart = color_chart
        self.dates = dates
        self.patient_sex = patient_sex
        self.indications = indications
        self.doctor_id = doctor_id


@app.route('/')
@login_required
def index():
    """Show homepage""" 

    user_id = session["id"]
    order_info = db.session.execute(db.select(Order).filter_by(doctor_id=user_id).order_by(Order.dates.desc())).scalars().all()

    return render_template("index.html", order=order_info)

@app.route('/login', methods=["POST", "GET"])
def login():
    """Log user in"""                       

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        username = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Ensure username, email and password were submitted
        if not username or not email or not password:
            return render_template("login.html")

        # Query database for username
        rows = db.session.execute(db.select(User).filter_by(username=username)).scalars().all()

        # Ensure username exists and password and email are correct
        if len(rows) == 0 or not check_password_hash(rows[0].hash, password) or rows[0].email != email:
            return render_template("login.html")
                                                                                                                   
        # Remember which user has logged in
        session["id"] = rows[0].id

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    """Log user out"""

    session.pop("user", None)
    return redirect('/login')

@app.route('/register', methods=["POST", "GET"])
def register():
    """Register user"""

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        # Ensure username, email and password were submitted
        if not name or not email or not password:
            return render_template("register.html")

        # Ensure password and confirm password are equal
        if password != confirm_password:
            return render_template("register.html")

        # Encript the password
        hash = generate_password_hash(password)

        # Add the new user to the database only if the new name doesn't exist
        try: 
            new_user = User(username=name, email=email, hash=hash)
            db.session.add(new_user)
            db.session.commit()
            session["id"] = "new_user.get_id"
            return redirect("/")
        except: 
            return redirect("/register")

    else:
        return render_template("register.html")
    
@app.route('/location')
@login_required
def location():
    return render_template("location.html")

@app.route('/order', methods=["POST", "GET"])
@login_required
def order():
    """Show the form to do an order""" 
    if request.method == "POST":
        patient_name = request.form.get("patient-name")
        patient_age = request.form.get("patient-age")
        patient_color_chart = request.form.get("tooth-color-chart")
        indications = request.form.get("indications")
        patient_sex = request.form.get("gender")
        dates = date.today()

        user_id = session["id"]

        # Ensure all the data were entered correctly
        if not patient_name or not patient_age or not patient_color_chart or not indications:
            return render_template("order.html")
        if int(patient_age) < 5:
            return render_template("order.html")

        if patient_sex:
            # Insert into the database a patient who is a men
            new_patient = Order(patient_name=patient_name, patient_age=patient_age, color_chart=patient_color_chart, dates=dates, patient_sex=patient_sex, indications=indications, doctor_id=user_id)
            db.session.add(new_patient)
            db.session.commit()
        

        return redirect("/")
    else:
        return render_template("order.html")
    

if __name__ == "__main__":
    from app import app, db
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
