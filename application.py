from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from user import users, get_user, User, get_user_from_email, get_user_from_id
from products import (
    add_product,
    products,
    get_product,
    get_product_list,
    get_product_list_from_tag,
    search_products,
)
from werkzeug.utils import secure_filename
import os
import API

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SECRET_KEY"] = "GRUPO8DEDESARROLLOBASADOENPLATAFORMAS"
app.config["DATABASE"] = "data.db"

UPLOAD_FOLDER = "static/imagenes/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    filename_in_ext = filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return "." in filename and filename_in_ext


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None


@app.route("/")
def index():
    #return render_template("index.html", product_list=products)
    return "Para obtener todos los usuarios: '/get-all-users' y para obtener todos los productos: '/get-all-products'"


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if request.method == "POST":
        user = get_user(request.form["username"])
        if user and user.check_password(request.form["password"]):
            login_user(user, remember=True)
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if request.method == "POST":
        succesful = True
        if get_user(request.form["username"]):
            flash("Username already taken")
            succesful = False
        if get_user_from_email(request.form["email"]):
            flash("Email is already used by other account")
            succesful = False
        if request.form["password"] != request.form["password-repeat"]:
            flash("Both passwords must be the same")
            succesful = False
        if succesful:
            newUser = User(
                str(len(users)),
                request.form["username"],
                request.form["email"],
                request.form["password"],
            )
            users.append(newUser)
            login_user(newUser, remember=True)
            return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/cart")
def cart():
    if current_user.is_authenticated:
        p = 0
        for i in current_user.cart:
            p += i.price
        return render_template("cart.html", p_list=current_user.cart, price=p)
    flash("Login to add products to your cart")
    return redirect(url_for("login"))


@app.route("/add-product", methods=["GET", "POST"])
def new_product():
    if not current_user.is_authenticated:
        flash("Login to add products to the shop")
        return redirect(url_for("login"))
    if request.method == "POST":

        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No image selected for uploading")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # print('upload_image filename: ' + filename)
            flash("Image successfully uploaded and displayed below")
        image_dir = "/imagenes/" + filename
        add_product(
            request.form["product_name"],
            0,
            int(request.form["price"]),
            image_dir,
            request.form["description"],
            [request.form["category"]],
            current_user,
        )
    return render_template("new_product.html")


@app.route("/remove-from-cart/<int:id>")
def remove_from_cart(id):
    if current_user.is_authenticated:
        current_user.cart.remove(get_product(id))
        return redirect(url_for("cart", id=id))
    flash("Login to add products to your cart")
    return redirect(url_for("login"))


@app.route("/product/<int:id>")
def display_product(id):
    return render_template("product.html", product=get_product(id))


@app.route("/add-to-cart/<int:id>")
def add_to_cart(id):
    if current_user.is_authenticated:
        current_user.cart.append(get_product(id))
        flash("Product added to cart")
        return redirect(url_for("display_product", id=id))
    flash("Login to add products to your cart")
    return redirect(url_for("login"))


@app.route("/user/<id>")
def display_user(id):
    candy = get_user_from_id(id)
    tetris = get_product_list(candy)
    return render_template("user.html", user=candy, product_list=tetris)


@app.route("/tag/<tag>")
def display_tagged_products(tag):
    tetris = get_product_list_from_tag(tag)
    flash(f"Showing products tagged {tag}")
    return render_template("index.html", product_list=tetris)


@app.route("/search/<text>")
def display_searched_products(text):
    product_list = search_products(text)
    if product_list:
        flash("Products that contain " + text)
    else:
        flash("There are no products that contain " + text)
    return render_template("index.html", product_list=product_list)

# API functions

@app.route('/get-all-users')
def get_all_users():
    with app.app_context():
        u = API.get_users()
    return u

@app.route('/get-all-products')
def get_all_products():
    with app.app_context():
        p = API.get_products()
    return p


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
    with app.app_context():
        API.close_db()
