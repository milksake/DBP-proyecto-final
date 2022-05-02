#lista de productos
products = []

class Product():
    def __init__(self, id, name, stars, price, image, description) -> None:
        self.id = id
        self.name = name.capitalize()
        self.stars = stars
        self.price = price
        self.image = image
        self.description = description

products.append(Product(1, "Cubo ", 5, 80, "../static/imagenes/cubo1.jpg", "cubo"))
products.append(Product(2, "cubo", 5, 60, "../static/imagenes/cubo2.jpg", "cubo"))
products.append(Product(3, "cubo", 5, 90, "../static/imagenes/cubo3.jpg", "cubo"))
products.append(Product(4, "cubo", 5, 100, "../static/imagenes/cubo4.jpg", "cubo"))
products.append(Product(5, "Cubo ", 5, 100, "../static/imagenes/cubo5.jpg", "cubo"))
products.append(Product(6, "cubo", 5, 100, "../static/imagenes/cubo6.jpg", "cubo"))
products.append(Product(7, "cubo", 5, 120, "../static/imagenes/cubo7.jpg", "cubo"))
products.append(Product(8, "cubo", 5, 70, "../static/imagenes/cubo8.jpg", "cubo"))
products.append(Product(9, "Cubo ", 5, 90, "../static/imagenes/cubo9.jpg", "cubo raro"))
products.append(Product(10, "cubo", 5, 90, "../static/imagenes/cubo10.jpg", "cubo"))
products.append(Product(11, "cubo", 5, 70, "../static/imagenes/cubo11.jpg", "cubito"))
products.append(Product(12, "cubo", 5, 70, "../static/imagenes/cubo12.jpg", "cubito"))
products.append(Product(13, "cubo", 5, 150, "../static/imagenes/cubo13.jpg", "cubo lindo"))

#Búsqueda de producto por ID
def get_product(id):
    for x in products:
        if x.id == id:
            #Retorna toooodos los datos del producto
            return x
    return None  
