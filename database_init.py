import sqlite3

if __name__ == "__main__":
    db = sqlite3.connect("data.db")
    with open('database.sql') as f:
        db.executescript(f.read())