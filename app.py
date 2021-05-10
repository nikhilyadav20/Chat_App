from flask import Flask,render_template
from wtforms_layout import *
from models import *

app = Flask(__name__)
app.secret_key = 'replace later'

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://pjecfjuvufvcbi:cb13122faf62bb6a3598546606e943b7ce830939944c8dee2fc96f9e6fbdc75d@ec2-52-0-114-209.compute-1.amazonaws.com:5432/db8l39u420h9p6'
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
        return "Inserted into DB"

    return render_template('index.html',form=reg_form)

if __name__=="__main__":
    app.run(debug=True)
