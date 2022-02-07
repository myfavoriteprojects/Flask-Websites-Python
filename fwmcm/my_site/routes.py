from flask import render_template, url_for
from my_site import app


@app.route('/')
def home():
    return render_template('home.html',title='Home')