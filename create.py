from flask import Flask
from models import *
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("postgres://pjecfjuvufvcbi:cb13122faf62bb6a3598546606e943b7ce830939944c8dee2fc96f9e6fbdc75d@ec2-52-0-114-209.compute-1.amazonaws.com:5432/db8l39u420h9p6")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()