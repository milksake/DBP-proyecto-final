from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from user import users, get_user, User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'GRUPO8DEDESARROLLOBASADOENPLATAFORMAS'

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return "Ya estas loggeado"
    if request.method == 'POST':
        user = get_user(request.form['username'])
        if user and user.check_password(request.form['password']):
            login_user(user, remember=True)
            return "Te acabas de loggear"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return "Ya estas loggeado"
    if request.method == 'POST':
        newUser = User(str(len(users)), request.form['username'], request.form['password'])
        users.append(newUser)
        login_user(newUser, remember=True)
        return "Te acabas de loggear"
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return "Te desloggeaste(?)"
    
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)