from flask import render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from .forms import RegistrationForm, LoginForm
from .models import User


@app.route('/logout')
def logout():
    session.pop('email')
    return redirect(url_for('bank_details'))


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return 'Пользователя с таким email не существует'

        if not check_password_hash(user.password_hash, form.password.data):
            return 'Неверный логин или пароль'

        session['email'] = user.email
        return redirect(url_for('bank_details'))

    return render_template('login.html', form=form, email=session.get('email'))


@app.route('/registration', methods=('GET', 'POST'))
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            return 'Пользователь с таким email уже существует'

        user = User(email=form.email.data, password_hash=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        session['email'] = user.email
        return redirect(url_for('bank_details'))

    return render_template('registration.html', form=form, email=session.get('email'))


@app.route('/')
@app.route('/index')
@app.route('/bank-details')
def bank_details():
    return render_template('bank_details.html', email=session.get('email'))

