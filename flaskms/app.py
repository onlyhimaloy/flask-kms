#Flask simple form application
#Fetch hostnames and date/time stamp of KMS activation form Even log which has gathered to this DB 

from flask import Flask, make_response  
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, Length
from wtforms.fields.html5 import DateField
import time
import requests 

from flask.ext import excel
from flask_paginate import Pagination
from flask.ext.sqlalchemy import Pagination
app = Flask(__name__)

app.config['SECRET_KEY'] = 'top secret!123#098'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ferozkhan:amiferoz69@localhost/server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)




class KmsForm(Form):
    dt_start = DateField( format='%Y-%m-%d'  )
    dt_end = DateField( format='%Y-%m-%d'  )
    idc = SelectField('IDC', choices = [('1', 'JAPAN'), ('2', 'ALL')]) 
    submit = SubmitField('Enter')



class DBC(db.Model):
    __tablename__ = 'kms'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(500),unique=False)
    date = db.Column(db.DateTime)


@app.route("/", defaults={'page': 1},methods=['GET', 'POST'])
@app.route("/page/<int:page>/", methods=["GET", "POST"])

def index(page):

    form = KmsForm()
    global kms
    pagination = [] 
    if form.validate_on_submit(): 
        if form.idc.data == '1':
          kms = DBC.query.filter(DBC.hostname.op('regexp')(r'[1][0-9][0-9][0-9]$')|DBC.hostname.like('%%jp2v') , DBC.date.between (form.dt_start.data , form.dt_end.data ))
          pagination = kms.paginate(page, 20)
	       
        else:
          kms = DBC.query.filter(DBC.date.between ( form.dt_start.data , form.dt_end.data  ))
          pagination = kms.paginate(page, 20)

    return render_template('index.html' , form=form , pagination=pagination)




##Download the Excel formated file from the data inputed in Form method 
##By usning global variable KMS

@app.route('/download')
def download():

    timestr = time.strftime("%Y%m%d-%H%M%S")
    global kms
    data =  kms.all()
    column_names =['id' , 'hostname' , 'date']
    output = excel.make_response_from_query_sets(data, column_names, 'csv')
    output.headers["Content-Disposition"] = "attachment; filename=kms"+timestr+".csv"
    output.headers["Content-type"] = "text/csv"
    return output



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)


