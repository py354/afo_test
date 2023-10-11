from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
@app.route('/bank-details')
def index():
    return render_template('bank_details.html')


@app.route('/logout')
def logout():
    return 'logout'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/bank-details')
def bank_details():
    return render_template('bank_details.html')

