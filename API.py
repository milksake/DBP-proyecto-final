import sqlite3
from flask import g, current_app, jsonify

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get_users():
    db = get_db()
    cursor = db.cursor()

    statement = "SELECT * FROM users"
    rows = cursor.execute(statement,).fetchall()

    db.commit()

    return jsonify( [dict(user) for user in rows] )


def get_products():
    db = get_db()
    cursor = db.cursor()

    statement = "SELECT * FROM products"
    rows = cursor.execute(statement,).fetchall()

    db.commit()

    return jsonify( [dict(product) for product in rows] )
