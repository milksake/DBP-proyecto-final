from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from user import users, get_user, User, get_user_from_email, get_user_from_id
from products import Product, products, get_product, get_product_list
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'GRUPO8DEDESARROLLOBASADOENPLATAFORMAS'

UPLOAD_FOLDER = 'static/imagenes/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None

@app.route('/')
def index():
    return render_template('index.html', product_list=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = get_user(request.form['username'])
        if user and user.check_password(request.form['password']):
            login_user(user, remember=True)
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        succesful = True
        if get_user(request.form['username']):
            flash("Username already taken")
            succesful = False
        if get_user_from_email(request.form['email']):
            flash("Email is already used by other account")
            succesful = False
        if request.form['password'] != request.form['password-repeat']:
            flash("Both passwords must be the same")
            succesful = False
        if succesful:
            newUser = User(str(len(users)), request.form['username'], request.form['email'], request.form['password'])
            users.append(newUser)
            login_user(newUser, remember=True)
            return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/cart')
def cart():
    if current_user.is_authenticated:
        price = 0
        for i in current_user.cart:
            price += i.price
        return render_template('cart.html', product_list=current_user.cart, price=price)
    flash("Login to add products to your cart")
    return redirect(url_for('login'))

@app.route('/add-product', methods=['GET', 'POST'])
def new_product():
    if current_user.is_authenticated == False:
        flash("Login to add products to the shop")
        return redirect(url_for('login'))
    if request.method == 'POST':
        
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
        image_dir='/imagenes/'+filename
        newProduct = Product(len(products), request.form['product_name'], 0, request.form['price'], image_dir, request.form['description'], current_user)
        products.append(newProduct)
    return render_template('new_product.html')

@app.route('/product/<int:id>')
def display_product(id):
    return render_template('product.html', product=get_product(id))

@app.route('/add-to-cart/<int:id>')
def add_to_cart(id):
    if current_user.is_authenticated:
        current_user.cart.append(get_product(id))
        flash("Product added to cart")
        return redirect(url_for("display_product", id=id))
    flash("Login to add products to your cart")
    return redirect(url_for('login'))

@app.route('/user/<id>')
def display_user(id):
    candy = get_user_from_id(id)
    tetris = get_product_list(candy)
    return render_template('user.html', user=candy, product_list=tetris)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
