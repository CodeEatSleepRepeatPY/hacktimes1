from flask import Flask, render_template, request
import database
import utils

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        provided_username = request.form['username']
        provided_password = request.form['password']

        if database.validate(provided_username, provided_password):
            return 'Logged in as admin'
        else:
            return 'Incorrect username or password'

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('Register.html')
    else:
        provided_username = request.form['username']
        provided_password = request.form['password']
        database.add(provided_username, provided_password)

        return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("Blog.html")

@app.route("/contact")
def contact():
    return render_template("Contact.html")

@app.route("/about")
def about():
    return render_template("About.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)
