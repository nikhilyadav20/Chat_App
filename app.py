from flask import Flask, render_template, request, redirect, url_for,flash
from flask_login import LoginManager,login_user, current_user,login_required, logout_user
from wtform_fields import *
from models import *

app = Flask(__name__)

app.secret_key='replace later'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pwkmyavayzntvz:0120a8661135920ea51a7b77aa8ed0494a28fbd828b42b4c40c05f3bde462486@ec2-52-1-115-6.compute-1.amazonaws.com:5432/d6fcun29rs1lp0"
db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        hashed_pswd = pbkdf2_sha256.hash(password)
        
        user = User(username=username,password=hashed_pswd)
        db.session.add(user)
        db.session.commit()
        
        flash('Registered successfully','success')
        return redirect(url_for('login'))

    return render_template("index.html",form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))


    return render_template("login.html", form = login_form)

@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    flash('Logged out successfully','success')
    return redirect(url_for('login'))

@app.route("/chat", methods=['GET', 'POST'])
def chat():

    if not current_user.is_authenticated:
        flash('Please login','danger')
        return redirect(url_for('login'))


    return "Chat"

if __name__ == "__main__":
    app.run(debug=True)
