from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin):
    def __init__(self, id, username, email, password, is_admin=False) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.cart = []

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


users = [User("0", "admin", "example@mail.com", "grupo8plataformas", True)]


def get_user(username):
    for user in users:
        if user.username == username:
            return user
    return None


def get_user_from_id(id):
    for user in users:
        if user.id == id:
            return user
    return None


def get_user_from_email(email):
    for user in users:
        if user.email == email:
            return user
    return None
