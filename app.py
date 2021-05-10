from flask import Flask,render_template
from wtforms_layout import *
from models import *
from create import *

app = Flask(__name__)
app.secret_key = 'replace later'

db = SQLAlchemy(app)

@app.route('/',methods = ['Get','POST'])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted"

    return render_template('index.html',form=reg_form)

if __name__=="__main__":
    app.run(debug=True)
