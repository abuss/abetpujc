# all the imports
from __future__ import division
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
            add_data(db)
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
    cur = g.db.execute('select nomb_asig, id_asig, grupo_asig from asignaturas order by nomb_asig desc')
    entries = [dict(title=row[0], cod=row[1], grupo=row[2]) for row in cur.fetchall()]
    return render_template('main.html', entries=entries)

@app.route('/<codigo>/<grupo>', methods=['GET', 'POST'])
def asignatura(codigo,grupo):
    cur = g.db.execute("select nomb_asig, id_asig, grupo_asig from asignaturas where id_asig=?",[codigo])
    entries = [dict(title=row[0], cod=row[1], grupo=row[2]) for row in cur.fetchall()]
    return render_template('course.html', entries=entries[0])

@app.route('/<codigo>/<grupo>', methods=['GET', 'POST'])
def notas(codigo):
    return render_template(codigo+'/notas.html')

@app.route('/<codigo>/<grupo>/defcourse', methods=['GET', 'POST'])
def evaluaciones(codigo,grupo):
    cur1 = g.db.execute("select nomb_asig from asignaturas where id_asig=?",[codigo])
    cur2 = g.db.execute('select id_resprog, peso from relevresulprog where id_asig=?',[codigo])
    formula = cur2.fetchall()
    suma = 0
    for i in formula:
        suma = suma + i[1]
    for i in range(len(formula)):
        temp = list(formula[i])
        temp.append(int(formula[i][1]*1000/suma))
        formula[i] = tuple(temp)
    print formula
    entries = {'nombre':cur1.fetchone()[0],'resprog':formula, 'suma':suma}
    return render_template('defcourse.html', entries=entries)

if __name__ == '__main__':
    init_db()
    app.run()
