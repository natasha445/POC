from flask import Flask, render_template, redirect, url_for, request, flash
import requests
from flask_mysqldb import MySQL


'''
python -m venv POC_env
POC_env\/Scripts\/activate.bat
python -m flask run
'''

'''
pip install Flask
pip install requests
pip install Flask-MySQLdb
'''

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'bank'

mysql = MySQL(app)

app.secret_key = "myKey"

@app.route("/")
def index():
    return "Nothing here"

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/userLogin/", methods=['POST'])
def userLogin():
    if request.method == "POST":
        name = request.form['userName']
        password = request.form['userPassword']
        
        myCursor = mysql.connection.cursor()
        myCursor.execute("SELECT UserValidationProcedure (%s, %s)", (name, password))
        functionResult = myCursor.fetchall()
        myCursor.close()

        for result in functionResult:
            validCredentials = result[0]

        if validCredentials == 0:
            flash('Credentials are invalid')
            return redirect(url_for('login'))

    return redirect(url_for('dashboard'))

@app.route("/dashboard/")
def dashboard():
    return "Here's the user bank account"