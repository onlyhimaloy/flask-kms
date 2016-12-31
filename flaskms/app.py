#https://github.com/miguelgrinberg/oreilly-intro-to-flask-video
###########################################################

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms import DateField


app = Flask(__name__)


app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ferozkhan:amiferoz69@localhost/server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class KmsForm(Form):
    dt_start = DateField('Start Date', format='%Y-%m-%d' )
    dt_end = DateField('End Date', format='%Y-%m-%d' )
    submit = SubmitField('Submit')


class kms(db.Model):

    __tablename__ = 'kms'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(500),unique=False)
    date = db.Column(db.DateTime)

    def __repr__(self):
      return '<kms {0}>'.format(self.name)

@app.route("/", methods=['GET', 'POST'])

def index():
    form = KmsForm()
    if form.validate_on_submit():
     global kms	    
     kms = kms.query.filter(kms.date.between (dt_start , dt_end ))
     return render_template('index.html', form=form , kms=kms)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

