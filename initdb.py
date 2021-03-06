# all the imports
import sqlite3
from contextlib import closing

# Base de datos oficial
#DATABASE = '/home/abetpujc/abetpujc/abet.db'
# Para hacer pruebas
#DATABASE = '/Users/gsarria/Dropbox/Work/ABETForm/github/abetpujc/abet.db'
DATABASE = 'C:/Users/Usuario/Documents/Javeriana/3 Semestre/ABET/abet.db'

#DATA_DATABASE = 'scripts/addData2db.sql'
DATA_DATABASE = 'C:/Users/Usuario/Desktop/Abet/abetpujc-master/scripts/addData2db.sql'

#ABET_DATABASE = 'scripts/DB_Abet_SQLite.sql'
ABET_DATABASE = 'C:/Users/Usuario/Desktop/Abet/abetpujc-master/scripts/DB_Abet_SQLite.sql'


def connect_db():
    return sqlite3.connect(DATABASE)


def add_data(db):
    with open(DATA_DATABASE, encoding='utf8', mode='r') as f:
        print("Filling DB")
        db.executescript(f.read())
    db.commit()


def init_db():
    with closing(connect_db()) as db:
        with open(ABET_DATABASE, encoding='utf8', mode='r') as f:
            print("Creating DB")
            db.executescript(f.read())
            add_data(db)
        db.commit()


if __name__ == "__main__":
    init_db()
