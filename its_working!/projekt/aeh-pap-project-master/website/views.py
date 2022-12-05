from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db, app
from .models import Books_userprv, Favourites_userprv



views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        books = Books_userprv.query.all()
        user_has_books = Favourites_userprv.query.filter_by(User_id=int(current_user.id)).all()
        userbooks = []
        for book in user_has_books:
            favbook = book.Books_id
            userbooks.append(int(favbook))
        return render_template("home.html", user=current_user, books=books, userbooks=userbooks)
    if request.method == 'POST':
        imie = request.form.get('imie')
        nazwisko = request.form.get('nazwisko')
        tytul = request.form.get('tytul')

        books = Books_userprv.query.filter(Books_userprv.AuthorsFirstName.like(f'%{imie}%')).filter(Books_userprv.AuthorsSurname.like(f'%{nazwisko}%')).filter(Books_userprv.BookName.like(f'%{tytul}%')).all()
        user_has_books = Favourites_userprv.query.filter_by(User_id=int(current_user.id)).all()
        userbooks = []
        for book in user_has_books:
            favbook = book.Books_id
            userbooks.append(int(favbook))
        return render_template("home.html", user=current_user, books=books, userbooks=userbooks)


@views.route('/favourites', methods=['GET', 'POST'])
@login_required
def favourites():
    if request.method == 'GET':
        user_has_books = Favourites_userprv.query.filter_by(User_id=int(current_user.id)).all()
        userbooks = []
        for books in user_has_books:
            book = Books_userprv.query.filter_by(id=int(books.Books_id)).first()
            userbooks.append(book)

        return render_template("favourites.html", user=current_user, books=userbooks)

    if request.method == 'POST':
        imie = request.form.get('imie')
        nazwisko = request.form.get('nazwisko')
        tytul = request.form.get('tytul')

        booksq = Books_userprv.query.filter(Books_userprv.AuthorsFirstName.like(f'%{imie}%')).filter(
            Books_userprv.AuthorsSurname.like(f'%{nazwisko}%')).filter(Books_userprv.BookName.like(f'%{tytul}%')).all()

        user_has_books = Favourites_userprv.query.filter_by(User_id=int(current_user.id)).all()
        userbooks = []
        for books in user_has_books:
            book = Books_userprv.query.filter_by(id=int(books.Books_id)).first()
            userbooks.append(book)

        final_books = set(booksq).intersection(set(userbooks))

        return render_template("favourites.html", user=current_user, books=final_books)



@views.route('/manage_favourites', methods=['POST'])
@login_required
def manage_favourites():
    if request.method == 'POST':
        if request.form.get('add'):

            fav_id=request.form.get('add')
            user=current_user.id
            favourite = Favourites_userprv.query.filter_by(User_id=int(user),Books_id=int(fav_id)).first()

            if favourite:
                flash('Book is already in favourites', category='error')
            else:
                new_fav = Favourites_userprv(User_id=int(user), Books_id=int(fav_id))
                try:
                    db.session.add(new_fav)
                    db.session.commit()
                    flash('Book added to favourites', category='success')
                except:
                    db.session.rollback()
                    flash('Book cannot be added to favourites', category='error')

            return redirect(url_for('views.home'))

        elif request.form.get('remove'):

            fav_id = request.form.get('remove')
            user = current_user.id
            favourite = Favourites_userprv.query.filter_by(User_id=int(user), Books_id=int(fav_id)).first()

            if favourite:
                try:
                    db.session.delete(favourite)
                    db.session.commit()
                    flash('Book removed from favourites', category='success')
                except:
                    db.session.rollback()
                    flash('Book cannot be removed from favourites', category='error')
            else:
                flash('Book is not in favourites', category='error')

            return redirect(url_for('views.favourites'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')