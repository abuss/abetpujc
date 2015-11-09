# all the imports
import sqlite3
from contextlib import closing

DATABASE = '/home/abetpujc/abetpujc/abet.db'


def connect_db():
    return sqlite3.connect(DATABASE)


def add_data(db):
    with open('scripts/addData2db.sql', mode='r') as f:
        print("Filling DB")
        db.executescript(f.read())
    db.commit()


def init_db():
    with closing(connect_db()) as db:
        with open('scripts/DB_Abet_SQLite.sql', mode='r') as f:
            print("Creating DB")
            db.executescript(f.read())
            add_data(db)
        db.commit()


if __name__ == "__main__":
    init_db()
