#Flask simple form application


from flask import Flask, make_response  
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, Length
from wtforms.fields.html5 import DateField
import MySQLdb

from flask.ext import excel

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
    global kms
    kms = []

    if form.validate_on_submit(): #and form.idc.choices == 1:
        db = MySQLdb.connect("localhost","ferozkhan","amiferoz69","server")
        cur = db.cursor()
        #cur.execute( "SELECT * from kms where date between '%s' and '%s' " %(form.dt_start.data  , form.dt_end.data ) )
        cur.execute ("SELECT  * from kms  where hostname regexp '[1][0-9][0-9][0-9]$' OR hostname LIKE '%%jp2v'  and date between '%s' and '%s' " %(form.dt_start.data , form.dt_end.data)  )
        
        kms = list(cur.fetchall())
      
    return render_template('index.html' , form=form , kms=kms)

@app.route('/download')
def download():

    global kms
    output = excel.make_response_from_array(kms, 'csv')
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)





if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
