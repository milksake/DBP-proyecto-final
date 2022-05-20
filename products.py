from user import users #lista de productos
products = []

class Product():
    def __init__(self, id, name, stars, price, image, description, tags, user=None) -> None:
        self.id = id
        self.name = name.capitalize()
        self.stars = stars
        self.price = price
        self.image = image
        self.description = description
        self.tags = tags
        self.user = user

#Búsqueda de producto por ID
def get_product(id):
    for x in products:
        if x.id == id:
            #Retorna toooodos los datos del producto
            return x
    return None

def add_product(name, stars, price, image, description, tags, user):
    products.append(Product(len(products), name, stars, price, image, description, tags, user))

def get_product_list(user):
    products_list = []
    for i in products:
        if i.user == user:
            products_list.append(i)
    return products_list

def get_product_list_from_tag(tag):
    product_list = []
    for x in products:
        for y in x.tags:
            if y == tag:
                product_list.append(x)
    return product_list

# Placeholder products

add_product("Cubo de Rubik Lanlan Dodecaedro Rómbico", 5, 80, "imagenes/cubo1.jpeg", "Es una modificacion del Cubo de Rubik 4x4, a pesar de tener 12 caras tiene exactamente el mismo número de piezas que el cubo 4x4.", ['4x4'], users[0])
add_product("Cubo Dayan Tangram", 5, 60, "imagenes/cubo2.jpeg", "Es una modificación del Cubo de Rubik. Marca: Dayan. Versión: Tangram", [], users[0])
add_product("Cubo DaYan Bagua", 5, 90, "imagenes/cubo3.jpeg", "Es una modificacion compleja del Cubo de Rubik 3x3. La oieza central de cada cara dividida en 5 piezas a ordenar. Marca: Dayan. Versión: Bagua", ['3x3'], users[0])
add_product("Cubo de Rubik Icosaedro", 5, 100, "imagenes/cubo4.jpeg", "Sy giro es en torno a las caras por lo que cuenta con 20 ejes de giro, se puede mezcalr con jumbling para que se deforme o sin jumbling. Modelo: Lanlanicosromb", ['5x5 +'], users[0])
add_product("Cubo de Rubik Pyramorphix ", 5, 100, "imagenes/cubo5.jpeg", "Es una modificación del 2x2. Esta es la versión piramidal con lineas rectas.", ['2x2','Pyramix'], users[0])
add_product("Timur Gear Skewb", 5, 100, "imagenes/cubo6.jpeg", "El Timur Gear Skewb es un Skewb con engranajes, diseñado por Timur Evbatyrov y producido por Calvins.", ['2x2', 'Gear cubes'], users[0])
add_product("Cubo de Rubik Dayan Wheels of Wisdom", 5, 120, "imagenes/cubo7.jpeg", "Dayan Wheels of Wisdom es un Cubo de 3x3 completamente modificado.", ['3x3'], users[0])
add_product("Cubo de Rubik 3x3", 5, 70, "imagenes/cubo8.jpeg", "Tradicional cubo de 3x3.", ['3x3'], users[0])
add_product("YJ Floppy Ghost Cuboide 3x3x1", 5, 90, "imagenes/cubo9.jpeg", "YJ Floppy Ghost Cuboide 3x3x1 es una versión adaptada de los cortes de un Cubo Chost 3x3, haciendo que tenga un aforma particulas.", ['Mirror cubes'], users[0])
add_product( "Qiyi Cubo Mágico Mirror 2×2", 5, 90, "imagenes/cubo10.jpeg", "Es la variacion del clásico cubo Rubik 2x2, base negra con stickers color plata.", ['2x2','Mirror cubes'], users[0])
add_product( "Cubo Mirror Moyu Meilong", 5, 70, "imagenes/cubo12.jpeg", "Moyu Meilong 3x3x3 Plateado. Modelo 1761", ['3x3', 'Mirror cubes'], users[0])
add_product( "Serpiente Twist Sheng Shou", 5, 70, "imagenes/cubo11.jpeg", "Serpiente de ShengShou Twist Snake blanca. Muchas soluciones y ninguna incorrecta.", [], users[0])
add_product( "Cubo de Rubik 3x3", 5, 150, "imagenes/cubo13.jpeg", "El clasico cubo de Rubik 3x3 en un color particular.", ['3x3'], users[0])
