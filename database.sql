DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS users(
user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
cart_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
stars INTEGER,
price INTEGER NOT NULL,
img TEXT,
description TEXT,
tags TEXT,
user INTEGER
);

INSERT INTO users (username, email, password, cart_id)
VALUES
("admin", "example@mail.com", "grupo8plataformas", 1);

INSERT INTO products (name, stars, price, img, description, tags, user)
VALUES
(
    "Cubo de Rubik Lanlan Dodecaedro Rómbico",
    5,
    80,
    "imagenes/cubo1.jpeg",
    "Es una modificacion del Cubo de Rubik 4x4, a pesar " +
    "de tener 12 caras tiene exactamente " +
    "el mismo número de piezas que el cubo 4x4. ",
    "4x4",
    1
),
(
    "Cubo Dayan Tangram",
    5,
    60,
    "imagenes/cubo2.jpeg",
    "Es una modificación del Cubo de Rubik. Marca: Dayan. Versión: Tangram",
    "[]",
    1
),
(
    "Cubo DaYan Bagua",
    5,
    90,
    "imagenes/cubo3.jpeg",
    "Es una modificacion compleja del Cubo de Rubik 3x3. " +
    "La pieza central de cada cara dividida en 5 " +
    "piezas a ordenar. Marca: Dayan. Versión: Bagua ",
    "3x3",
    1
),
(
    "Cubo de Rubik Icosaedro",
    5,
    100,
    "imagenes/cubo4.jpeg",
    "Su giro es en torno a las caras por lo que cuenta " +
    "con 20 ejes de giro, se puede mezclar" +
    "con jumbling para que se deforme o sin jumbling. Modelo: Lanlanicosromb",
    "5x5 +",
    1
),
(
    "Cubo de Rubik Pyramorphix ",
    5,
    100,
    "imagenes/cubo5.jpeg",
    "Es una modificación del 2x2. " +
    "Esta es la versión piramidal con lineas rectas.",
    "2x2 Pyramix",
    1
)
;