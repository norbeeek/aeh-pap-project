from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, User_loginprv
from werkzeug.security import check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User_loginprv.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                try:
                    login_user(user, remember=True)
                    flash('Login successful', category='success')
                except:
                    flash("Cannot login to that account", category='error')
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password', category='error')
        else:
            flash('User does not exist',category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Account for that email already exist',category='error')
        elif len(email) < 4:
            flash('Email is too short', category='error')
        elif not "." in email:
            flash('Email does not have dot', category='error')
        elif len(name) < 3:
            flash('Name is too short', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password is too short', category='error')
        elif not any(x.isupper() for x in password1):
            flash('Password requires at least one upper case character', category='error')
        elif not any(x.islower() for x in password1):
            flash('Password requires at least one lower case character', category='error')
        elif not any(x.isdigit() for x in password1):
            flash('Password requires at least one number', category='error')
        elif password1.isalnum():
            flash('Password requires at least one special character', category='error')
        elif len(email) > 40:
            flash('Email is too long', category='error')
        elif len(name) > 40:
            flash('Name is too long', category='error')
        elif len(password1) > 40:
            flash('Password is too long', category='error')
        else:
            new_user = User(email=email, name=name, password=password1, isAdmin=False)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Account created', category='success')
            except:
                db.session.rollback()
            try:
                login_user(new_user, remember=True)
            except:
                flash('Cannot login to that account', category='error')

            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)