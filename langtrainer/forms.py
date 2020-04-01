from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from langtrainer.models import User

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=100, message="This name is too long")])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=100, message="This name is too long")])
    email = StringField("Email", validators=[Email(), Length(max=100, message="This email address is too long")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=50, message="Password must be between 5 and 50 characters long.")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords must match")])
    submit = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one.")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email(), Length(max=100, message="Try again")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=50, message="Try again")])
    login = SubmitField("Login")
    remember_me = BooleanField("Remember Me")

class AddWordsForm(FlaskForm):
    native_word = StringField("Native Word", validators=[Length(max=100, message="This word is too long")])
    foreign_word = StringField("Foreign Word", validators=[Length(max=100, message="This word is too long")])
    add = SubmitField("Add")
