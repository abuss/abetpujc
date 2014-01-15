# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from addData2db import *

# create our little application :)
app = Flask(__name__)
app.config.update(dict(
    DATABASE='/tmp/abet.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('DB_Abet_SQLite.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
        
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_courses():
    add_data(g)
    cur = g.db.execute('select nomb_asig, id_asig, grupo_asig from asignaturas order by nomb_asig desc')
    entries = [dict(title=row[0], cod=row[1], grupo=row[2]) for row in cur.fetchall()]
    return render_template('main.html', entries=entries)

@app.route('/<codigo>/<grupo>', methods=['GET', 'POST'])
def asignatura(codigo,grupo):
    #print codigo
    return render_template(codigo)

@app.route('/<codigo>/notas', methods=['GET', 'POST'])
def notas(codigo):
    return render_template(codigo+'/notas.html')

@app.route('/<codigo>/evaluaciones', methods=['GET', 'POST'])
def evaluaciones(codigo):
    cur = g.db.execute('select nomb_asig, id_asig from asignaturas order by nomb_asig desc')
    entries = [dict(title=row[0], cod=row[1]) for row in cur.fetchall()]
    return render_template(codigo+'/evaluaciones.html', )

if __name__ == '__main__':
    init_db()
    app.run()
