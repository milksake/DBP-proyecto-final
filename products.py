#lista de productos
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

products.append(Product(1, "Cubo ", 5, 80, "imagenes/cubo1.jpeg", "cubo"))
products.append(Product(2, "cubo", 5, 60, "imagenes/cubo2.jpeg", "cubo"))
products.append(Product(3, "cubo", 5, 90, "imagenes/cubo3.jpeg", "cubo"))
products.append(Product(4, "cubo", 5, 100, "imagenes/cubo4.jpeg", "cubo"))
products.append(Product(5, "Cubo ", 5, 100, "imagenes/cubo5.jpeg", "cubo"))
products.append(Product(6, "cubo", 5, 100, "imagenes/cubo6.jpeg", "cubo"))
products.append(Product(7, "cubo", 5, 120, "imagenes/cubo7.jpeg", "cubo"))
products.append(Product(8, "cubo", 5, 70, "imagenes/cubo8.jpeg", "cubo"))
products.append(Product(9, "Cubo ", 5, 90, "imagenes/cubo9.jpeg", "cubo raro"))
products.append(Product(10, "cubo", 5, 90, "imagenes/cubo10.jpeg", "cubo"))
products.append(Product(11, "cubo", 5, 70, "imagenes/cubo11.jpeg", "cubito"))
products.append(Product(12, "cubo", 5, 70, "imagenes/cubo12.jpeg", "cubito"))
products.append(Product(13, "cubo", 5, 150, "imagenes/cubo13.jpeg", "cubo lindo"))

#Búsqueda de producto por ID
def get_product(id):
    for x in products:
        if x.id == id:
            #Retorna toooodos los datos del producto
            return x
    return None  
