from flask import Flask, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from langtrainer import app, db
from langtrainer.forms import RegistrationForm, LoginForm, AddWordsForm
from langtrainer.models import User, WordsDict
from datetime import datetime
from flask_login import current_user, login_user, logout_user
import random



@app.route("/account")
def account():
    if current_user.is_authenticated is False:
        return redirect(url_for("login"))
    return render_template("account.html")


@app.route("/delete_word/<int:word_id>", methods=["POST"])
def delete_word(word_id):
    if current_user.is_authenticated is False:
        return redirect(url_for("login"))
    word = WordsDict.query.get(word_id)
    db.session.delete(word)
    db.session.commit()
    return redirect("/vocabulary")


@app.route("/add_word")
def add_word():
    return redirect(url_for('vocabulary'))


@app.route("/vocabulary", methods=['GET', 'POST'])
def vocabulary():
    if current_user.is_authenticated is False:
        return redirect(url_for('login'))
    vocabulary = WordsDict.query.with_entities(WordsDict.id, WordsDict.native_word, WordsDict.foreign_word).filter_by(words_owner_id=current_user.id)
    form = AddWordsForm()
    if form.validate_on_submit():
        word = WordsDict(native_word=form.native_word.data, foreign_word=form.foreign_word.data, words_owner_id=current_user.id)
        db.session.add(word)
        db.session.commit()
        return redirect("/add_word")
    return render_template("vocabulary.html", form=form, vocabulary=vocabulary)


@app.route("/practice", methods=["POST", "GET"])
@app.route("/")
def practice():
    if current_user.is_authenticated is False:
        return redirect(url_for("login"))
    vocabulary = WordsDict.query.with_entities(WordsDict.id, WordsDict.native_word, WordsDict.foreign_word).filter_by(words_owner_id=current_user.id)
    vocabulary_list = []
    for word in vocabulary:
        vocabulary_list.append(word)
    if vocabulary_list == []:
        return redirect(url_for("vocabulary"))
    word = random.choice(vocabulary_list)
    return render_template("practice.html", title="Practice", word=word)

@app.route("/show_word/<int:word_id>", methods=["POST", "GET"])
def show_word(word_id):
    if current_user.is_authenticated is False:
        return redirect(url_for("login"))
    word = WordsDict.query.with_entities(WordsDict.id, WordsDict.native_word, WordsDict.foreign_word).filter_by(id=word_id)[0]
    return render_template("show_word.html", word=word)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated is True:
        return redirect(url_for('practice'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password_hash=generate_password_hash(form.password.data), date_registered=datetime.now())
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.email.data}! You can now log in", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('practice'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("practice"))
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))