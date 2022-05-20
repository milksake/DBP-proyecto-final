from user import users #lista de productos
products = []

class Product():
    def __init__(self, id, name, stars, price, image, description, user=None) -> None:
        self.id = id
        self.name = name.capitalize()
        self.stars = stars
        self.price = price
        self.image = image
        self.description = description
        self.user = user

#Búsqueda de producto por ID
def get_product(id):
    for x in products:
        if x.id == id:
            #Retorna toooodos los datos del producto
            return x
    return None

def add_product(name, stars, price, image, description, user):
    products.append(Product(len(products), name, stars, price, image, description, user))

def get_product_list(user):
    products_list = []
    for i in products:
        if i.user == user:
            products_list.append(i)
    return products_list

# Placeholder products

add_product("Cubo de Rubik Lanlan Dodecaedro Rómbico", 5, 80, "imagenes/cubo1.jpeg", "cubo", users[0])
add_product("Cubo Dayan Tangram", 5, 60, "imagenes/cubo2.jpeg", "cubo", users[0])
add_product("Cubo DaYan Bagua", 5, 90, "imagenes/cubo3.jpeg", "cubo", users[0])
add_product("Cubo de Rubik Icosaedro", 5, 100, "imagenes/cubo4.jpeg", "cubo", users[0])
add_product("Cubo de Rubik Pyramorphix ", 5, 100, "imagenes/cubo5.jpeg", "cubo", users[0])
add_product("Timur Gear Skewb", 5, 100, "imagenes/cubo6.jpeg", "cubo", users[0])
add_product("Cubo de Rubik Dayan Wheels of Wisdom", 5, 120, "imagenes/cubo7.jpeg", "cubo", users[0])
add_product("Cubo de Rubik 3x3", 5, 70, "imagenes/cubo8.jpeg", "cubo", users[0])
add_product("YJ Floppy Ghost Cuboide 3x3x1", 5, 90, "imagenes/cubo9.jpeg", "cubo raro", users[0])
add_product( "Qiyi Cubo Mágico Mirror 2×2", 5, 90, "imagenes/cubo10.jpeg", "cubo", users[0])
add_product( "Cubo Mirror Moyu Meilong", 5, 70, "imagenes/cubo12.jpeg", "cubito", users[0])
add_product( "Serpiente Twist Sheng Shou", 5, 70, "imagenes/cubo11.jpeg", "cubito", users[0])
add_product( "Cubo de Rubik 3x3", 5, 150, "imagenes/cubo13.jpeg", "cubo lindo", users[0])
