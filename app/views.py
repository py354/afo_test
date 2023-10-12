from flask import render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from .forms import RegistrationForm, LoginForm, BankDetailsForm, DeleteDetailsForm, SetActiveDetailsForm
from .models import User, BankDetail, UserActiveBank


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
    bank_details = None
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        active_id = None
        if user is None:
            return 'Пользователя с таким email не существует'

        if user.active_detail_row:
            active_id = user.active_detail_row.bank_details_id

        bank_details = user.bank_details
        for i in range(len(bank_details)):
            set_active_form = SetActiveDetailsForm()
            set_active_form.bank_details_id.data = bank_details[i].id
            delete_form = DeleteDetailsForm()
            delete_form.bank_details_id.data = bank_details[i].id
            setattr(bank_details[i], 'set_active_form', set_active_form)
            setattr(bank_details[i], 'delete_form', delete_form)
            setattr(bank_details[i], 'is_active', bank_details[i].id == active_id)

    return render_template('bank_details.html', email=session.get('email'), bank_details=bank_details)


@app.route('/add_bank_details', methods=('GET', 'POST'))
def add_bank_details():
    if 'email' not in session:
        return redirect(url_for('bank_details'))

    form = BankDetailsForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=session['email']).first()
        if user is None:
            return 'Пользователя с таким email не существует'

        details = BankDetail(
            bik=form.bik.data,
            bank_name=form.bank_name.data,
            checking_account=form.checking_account.data,
            correspondent_account=form.correspondent_account.data,
            swift=form.swift.data,
            iban=form.iban.data,
            user_id=user.id,
        )
        db.session.add(details)
        db.session.commit()
        return redirect(url_for('bank_details'))

    return render_template('add_bank_details.html', form=form, email=session.get('email'))


@app.route('/delete_bank_details', methods=('POST', ))
def delete_bank_details():
    if 'email' not in session:
        return redirect(url_for('bank_details'))

    user = User.query.filter_by(email=session['email']).first()
    if user is None:
        return 'Пользователя с таким email не существует'

    form = DeleteDetailsForm()
    if form.validate_on_submit():
        BankDetail.query.filter_by(id=form.bank_details_id.data, user_id=user.id).delete()
        db.session.commit()
    return redirect(url_for('bank_details'))


@app.route('/set_active_bank_details', methods=('POST', ))
def set_active_bank_details():
    if 'email' not in session:
        return redirect(url_for('bank_details'))

    user = User.query.filter_by(email=session['email']).first()
    if user is None:
        return 'Пользователя с таким email не существует'
    #
    form = SetActiveDetailsForm()
    if form.validate_on_submit():
        if user.active_detail_row:
            UserActiveBank.query.filter_by(user_id=user.id).update({UserActiveBank.bank_details_id: form.bank_details_id.data})
        else:
            UserActiveBank(user_id=user.id, bank_details_id=form.bank_details_id.data)
        db.session.commit()
    return redirect(url_for('bank_details'))
