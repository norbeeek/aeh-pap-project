from flask_sqlalchemy import event
from werkzeug.security import generate_password_hash
from .models import User


@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return generate_password_hash(value,method='sha256')
    return value
