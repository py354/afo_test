from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Optional, Email, Length, EqualTo, Regexp

password_length_validator = Length(min=4, max=20, message='Пароль должен содержать от 4 до 20 символов')


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email('Некорректный email')])
    password = PasswordField("Пароль: ", validators=[DataRequired(), password_length_validator])
    submit = SubmitField("Войти")


class RegistrationForm(FlaskForm):
    email = StringField("Email: ", validators=[Email('Некорректный email')])
    password = PasswordField("Пароль: ", validators=[DataRequired(), password_length_validator])
    password_repeat = PasswordField("Повторите пароль: ", validators=[
        DataRequired(), password_length_validator, EqualTo('password', 'Пароли не совпадают')
    ])
    submit = SubmitField("Регистрация")


class BankDetailsForm(FlaskForm):
    bik = StringField('БИК', validators=[
        DataRequired(), Regexp('^\\d{9}$', message='БИК должен состоять из 9 цифр')
    ])
    bank_name = StringField('Наименование банка', validators=[
        DataRequired(), Length(max=30, message='Название не должно превышать 30 символов')
    ])
    checking_account = StringField('Расчётный счет', validators=[
        DataRequired(), Regexp('^\\d{20}$', message='Расчётный счет должен состоять из 20 цифр')
    ])
    correspondent_account = StringField('Корреспондентский счет', validators=[
        DataRequired(), Regexp('^\\d{20}$', message='Корреспондентский счет должен состоять из 20 цифр')
    ])
    swift = StringField('SWIFT', validators=[
        DataRequired(), Length(min=8, max=11, message='SWIFT должен состоять из 8-11 символов')
    ])
    iban = StringField('IBAN (необязательное поле)', validators=[
        Optional(), Length(max=34, message='IBAN должен содержать до 34 символов')
    ])
    submit = SubmitField("Сохранить")
