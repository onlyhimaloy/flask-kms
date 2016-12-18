# flask-kms
A dashboard to show event log of Windows server 

#install flask with virtual environment

python3.5 -m venv flaskms
[root@web1 flask-kms]# source flaskms/bin/activate

#install required package including flask for the application

pip install --upgrade pip
pip install flask flask-bootstrap flask-wtf Flask-MySQLdb pymysql uwsgi
