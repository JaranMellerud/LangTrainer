from langtrainer import db
from flask_login import UserMixin
from langtrainer import login
from werkzeug.security import check_password_hash


# database table with all the users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    date_registered = db.Column(db.DateTime)
    words = db.relationship("WordsDict", backref="words_owner")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# database table with all the words for all the users
class WordsDict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    native_word = db.Column(db.String(255))
    foreign_word = db.Column(db.String(255))
    knowledge_level = db.Column(db.Integer(), default=1)
    words_owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

