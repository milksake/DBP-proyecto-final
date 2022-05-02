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

products.append(Product(1, "audifonos", 5, 100, "../static/imagenes/audifonos.jpg", "audifonos bonitos"))
products.append(Product(2, "polo", 5, 100, "../static/imagenes/audifonos.jpg", "audifonos bonitos"))
products.append(Product(3, "tazas", 5, 100, "../static/imagenes/audifonos.jpg", "audifonos bonitos"))
products.append(Product(4, "bolsa", 5, 100, "../static/imagenes/audifonos.jpg", "audifonos bonitos"))

#Búsqueda de producto por ID
def get_product(id):
    for x in products:
        if x.id == id:
            #Retorna toooodos los datos del producto
            return x
    return None  
