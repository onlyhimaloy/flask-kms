#https://github.com/miguelgrinberg/oreilly-intro-to-flask-video
#
###########################################################

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ferozkhan:amiferoz69@localhost/server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


 
class kms(db.Model):
    __tablename__ = 'kms'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(500),unique=False)
    date = db.Column(db.DateTime)
     

@app.route("/", methods=['GET', 'POST'])
    
    
def index():
     #kms = kms.query.all()
     return render_template('index.html', kms=kms.query.all())


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
