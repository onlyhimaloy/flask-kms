#Flask simple form application


from flask import Flask, make_response
import MySQLdb
from flask.ext import excel

dl = Flask(__name__)

dl.config['SECRET_KEY'] = 'top secret!'


@dl.route("/", methods=['GET', 'POST'])

def hello():

    return '''
            <html><body>
                    Hello. <a href="/download">Download</a>
                            </body></html>
                                    '''

@dl.route('/download')
def download():

    db = MySQLdb.connect("localhost","ferozkhan","amiferoz69","server")
    cur = db.cursor()
    cur.execute ( "SELECT * from kms where date between '2016-12-17 00:00:00' and '2016-12-18 23:59:00' " )

    kms = list(cur.fetchall())
    output = excel.make_response_from_array(kms, 'csv')
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output



if __name__ == "__main__":
    dl.run(host='0.0.0.0',debug=True)
(flaskms)
