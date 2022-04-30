
class Product():
    def __init__(self, id, name, stars, price, image, description) -> None:
        self.id = id
        self.name = name
        self.stars = stars
        self.price = price
        self.image = image
        self.description = description

ejemplo = Product(1, "sample", 5, 100, "link", "sample_text")
#lista de productos
products = [ejemplo]

#Búsqueda de producto por ID
def get_product(id):
    for x in products:
        if x.id == id:
            #Retorna toooodos los datos del producto
            return x.id, x.name, x.stars ,x.price, x.image, x.description
    return None
