#Flask simple form application

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, Length
from wtforms.fields.html5 import DateField
import MySQLdb

app = Flask(__name__)

app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)




class KmsForm(Form):
    dt_start = DateField( format='%Y-%m-%d'  )
    dt_end = DateField( format='%Y-%m-%d'  )
    idc = SelectField('IDC', choices = [('1', 'JAPAN'), ('2', 'ALL')]) 
    submit = SubmitField('Enter')



@app.route("/", methods=['GET', 'POST'])

def index():
    form = KmsForm()
    kms = []   
    if form.validate_on_submit():
      db = MySQLdb.connect("localhost","ferozkhan","amiferoz69","server")
      cur = db.cursor()
      cur.execute( "SELECT * from kms where date between '%s' and '%s' " %(form.dt_start.data  , form.dt_end.data ) )
      kms = cur.fetchall()
    
    return render_template('index.html' , form=form , kms=kms)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
