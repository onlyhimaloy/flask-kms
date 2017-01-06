#https://github.com/miguelgrinberg/oreilly-intro-to-flask-video
###########################################################

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
from wtforms.fields.html5 import DateField
import MySQLdb

app = Flask(__name__)

app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ferozkhan:amiferoz69@localhost/server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)




class KmsForm(Form):
    dt_start = DateField( format='%Y-%m-%d'  )
    dt_end = DateField( format='%Y-%m-%d'  )

    submit = SubmitField('Enter')


#class Kms(db.Model):
#
#    __tablename__ = 'kms'
#    id = db.Column(db.Integer, primary_key=True)
#    hostname = db.Column(db.String(500),unique=False)
#    date = db.Column(db.DateTime)
#
#    def __repr__(self):
#      return '<kms {0}>'.format(self.name)

@app.route("/", methods=['GET', 'POST'])

def index():
    form = KmsForm()
    kms = []   
    if form.validate_on_submit():
     
     #kms = Kms.query.filter(Kms.date.between ( form.dt_start.data ,form.dt_end.data))
     db = MySQLdb.connect("localhost","ferozkhan","amiferoz69","server")
     cur = db.cursor()
     cur.execute( "SELECT * from kms where date between '%s' and '%s' " %(form.dt_start.data  , form.dt_end.data ) )
     kms = cur.fetchall()

     print (form.dt_start.data) 
    return render_template('index.html' , form=form , kms=kms)




if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

