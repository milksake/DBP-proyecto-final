from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, is_admin=False) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.is_admin =is_admin
    
    def set_password(self, password):
        self.password = password
    
    def check_password(self, password):
        return password == self.password
    
users = []

def get_user(username):
    for user in users:
        if user.username == username:
            return user
    return None