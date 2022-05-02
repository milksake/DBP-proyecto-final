
class Product():
    def __init__(self, id, name, stars, price, image, description) -> None:
        self.id = id
        self.name = name
        self.stars = stars
        self.price = price
        self.image = image
        self.description = description

ejemplo1 = Product(1, "Audifonos", 5, 100, "../static/audifonos.jpg", "audifonos bonitos")
ejemplo2 = Product(2, "Polo", 5, 100, "../static/polo.jpg", "audifonos bonitos")
ejemplo3 = Product(3, "tazas", 5, 100, "../static/tazas.jpg", "audifonos bonitos")
ejemplo4 = Product(4, "bolsa", 5, 100, "../static/bolso.jpg", "audifonos bonitos")
#lista de productos
products = [ejemplo1, ejemplo2, ejemplo3, ejemplo4 ]

#Búsqueda de producto por ID
def get_product(id):
    for x in products:
        if x.id == id:
            #Retorna toooodos los datos del producto
            return x
    return None  
