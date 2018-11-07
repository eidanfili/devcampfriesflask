from flask import Flask, render_template

app = Flask(__name__)
from flask_heroku import Heroku

@app.route('/')
def homes():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.debug = True
    app.run()