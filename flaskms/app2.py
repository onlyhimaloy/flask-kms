###########################################################

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import DateField
#from flask.ext.sqlalchemy import SQLAlchemy
app2 = Flask(__name__)


app2.config['SECRET_KEY'] = 'top secret!'
app2.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ferozkhan:amiferoz69@localhost/server'
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app2)
db = SQLAlchemy(app2)


 
class kms(db.Model):
     __tablename__ = 'kms'
     id = db.Column(db.Integer, primary_key=True)
     hostname = db.Column(db.String(500),unique=False)
     date = db.Column(db.DateTime)
		      

@app2.route("/", methods=['GET', 'POST'])

			      
def index2():
       #kms = kms.query.al
      global kms     
      kms = kms.query.filter(kms.date.between ('2016-12-17 00:00:00' , '2016-12-18 23:59:00' ))
      #kms = kms.query.all() 
      return render_template('index2.html', kms=kms)


if __name__ == "__main__":
    app2.run(host='0.0.0.0',debug=True)
