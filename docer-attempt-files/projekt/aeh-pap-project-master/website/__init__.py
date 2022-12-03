from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin


db = SQLAlchemy()
app = Flask(__name__)

def create_app():
    app.config['SECRET_KEY'] = 'aeh projekt'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://admin2:adminpass2@localhost/library3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'user': "mysql://user2:user2@localhost/library3",
        'login': "mysql://login2:loginpass2@localhost/library3"
    }

    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Books, Favourites, UserView, BooksView, MyAdminIndexView, FavouritesView, MainPageView

    admin = Admin(app, index_view=MyAdminIndexView())

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .functions import hash_user_password

    admin.add_view(UserView(User, db.session))
    admin.add_view(BooksView(Books, db.session))
    admin.add_view(FavouritesView(Favourites, db.session))
    admin.add_view(MainPageView(name="Return to main page"))

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app