from flask_login import UserMixin, current_user
from . import db
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, BaseView, expose
from flask import redirect, url_for, flash
from gettext import gettext


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    BookName = db.Column(db.String(50), nullable=False)
    AuthorsFirstName = db.Column(db.String(50), nullable=False)
    AuthorsSurname = db.Column(db.String(50), nullable=False)
    users = db.relationship('Favourites', backref='Book')

    def __repr__(self):
        return '<Books %r>' % (self.BookName)

class Books_userprv(Books):
    __bind_key__ = 'user'

class BooksView(ModelView):
    form_columns = ['BookName', 'AuthorsFirstName', 'AuthorsSurname']

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.isAdmin
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('views.home'))

    def delete_model(self, model):
        """
            Delete model.
            :param model:
                Model to delete
        """
        try:
            favs = Favourites.query.filter_by(Books_id=model.id)
            favs.delete(synchronize_session=False)
            self.on_model_delete(model)
            self.session.flush()
            self.session.delete(model)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to delete record. %(error)s', error=str(ex)), 'error')

            self.session.rollback()

            return False
        else:
            self.after_model_delete(model)

        return True

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    isAdmin = db.Column(db.Boolean(), nullable=False)
    books = db.relationship('Favourites', backref='User')

    def __repr__(self):
        return '<User %r>' % (self.email)

class User_loginprv(User):
    __bind_key__ = 'login'


class UserView(ModelView):
    form_columns = ['email', 'name', 'password', 'isAdmin']

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.isAdmin
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('views.home'))

    def delete_model(self, model):
        """
            Delete model.
            :param model:
                Model to delete
        """
        try:
            favs = Favourites.query.filter_by(User_id=model.id)
            favs.delete(synchronize_session=False)
            self.on_model_delete(model)
            self.session.flush()
            self.session.delete(model)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to delete record. %(error)s', error=str(ex)), 'error')

            self.session.rollback()

            return False
        else:
            self.after_model_delete(model)

        return True

class Favourites(db.Model):
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    Books_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)

class Favourites_userprv(Favourites):
    __bind_key__ = 'user'

class FavouritesView(ModelView):
    pass

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.isAdmin
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('views.home'))

class MyAdminIndexView(AdminIndexView):
    pass

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.isAdmin
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('views.home'))

class MainPageView(BaseView):
    pass

    @expose('/')
    def index(self):
        return redirect(url_for('views.home'))

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.isAdmin
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('views.home'))