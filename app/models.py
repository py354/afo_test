from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.Text(), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)

    bank_details = db.relationship('BankDetail')
    active_detail_row = db.relationship('UserActiveBank', uselist=False)

    def __repr__(self):
        return "<user {}:{}>".format(self.id, self.email)


class BankDetail(db.Model):
    __tablename__ = 'bank_details'
    id = db.Column(db.Integer(), primary_key=True)
    bik = db.Column(db.String(9), nullable=False)
    bank_name = db.Column(db.String(30), nullable=False)
    checking_account = db.Column(db.String(20), nullable=False)
    correspondent_account = db.Column(db.String(20), nullable=False)
    swift = db.Column(db.String(11), nullable=False)
    iban = db.Column(db.String(34), nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')

    def __repr__(self):
        return "bank_details <{}:{}>".format(self.id, self.user_id)


class UserActiveBank(db.Model):
    __tablename__ = 'user_active_models'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False, unique=True)
    bank_details_id = db.Column(db.Integer(), db.ForeignKey('bank_details.id'), nullable=False)
