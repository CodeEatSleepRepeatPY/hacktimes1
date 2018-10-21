import random
from flask import Flask, render_template, redirect, url_for, request
import pymysql
from flask_bcrypt import Bcrypt
import hashlib

app = Flask(__name__)

registered = False

uname = " "
pwd = " "

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('MainPage.html')
    else:
        db = pymysql.connect('127.0.0.1', 'root', 'seangorelik123', 'username and passwords', port=3306)

        cursor = db.cursor()

        select = """SELECT * FROM `username and passwords`.`userpwd` LIMIT 1000;"""

        cursor.execute(select)

        db.close()

        l = cursor.fetchmany(100)
        for i in l:
            global uname
            global pwd
            uname = i[0]
            pwd = i[1]

        if request.form['username'] == uname and hashlib.sha512(str(request.form['password']).encode()).hexdigest() == pwd:
            registered = True
            return 'Logged in as admin'
        else:
            return 'Incorrect username or password'

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('Register.html')
    else:
        username = request.form['username']
        password = hashlib.sha512(str(request.form['password']).encode()).hexdigest()

        db = pymysql.connect('127.0.0.1', 'root', 'seangorelik123', 'username and passwords', port=3306)
        cursor = db.cursor()
        insert = """INSERT INTO `username and passwords`.`userpwd` (`USERNAME`, `PASSWORD`)
                            VALUES (%s,%s);""" % ('\'' + username + '\'', '\'' + str(password) + '\'')
        cursor.execute(insert)
        db.commit()
        db.close()
        return redirect(url_for('index'))

@app.route('/blog',methods=['GET', 'POST'])
def Blog():
    if request.method == 'GET':
            return render_template('Blog.html')
    else:
            return 'You need to register'

@app.route('/contact',methods=['GET', 'POST'])
def Contact():
    if request.method == 'GET':
            return render_template('Contact.html')
    else:
            return ''

@app.route('/about',methods=['GET', 'POST'])
def About():
    if request.method == 'GET':
            return render_template('About.html')
    else:
            return ''

if __name__ == '__main__':
    app.config['SECRET_KEY'] = "Your_secret_string"
    app.run(debug=True)
