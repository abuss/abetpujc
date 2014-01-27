# all the imports
from __future__ import division
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

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

def add_data(db):
	with app.open_resource('addData2db.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

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
        
# @app.before_request
# def before_request():
#     g.db = connect_db()

# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()

@app.route('/')
def show_courses():
    db = get_db()
    cur = db.execute('select nomb_asig, id_asig, grupo_asig, periodo from asignaturas where periodo=? order by nomb_asig asc',['2014-1'])
    entries = [dict(title=row[0], cod=row[1], grupo=row[2], periodo=row[3]) for row in cur.fetchall()]
    return render_template('main.html', entries=entries)

@app.route('/<codigo>/<grupo>', methods=['GET', 'POST'])
def asignatura(codigo,grupo):
    db = get_db()
    cur = db.execute("select nomb_asig, id_asig, grupo_asig, periodo from asignaturas where id_asig=?",[codigo])
    entries = [dict(title=row[0], cod=row[1], grupo=row[2], periodo=row[3]) for row in cur.fetchall()]
    return render_template('course.html', entries=entries[0])

@app.route('/<codigo>/<grupo>', methods=['GET', 'POST'])
def notas(codigo):
    return render_template(codigo+'/notas.html')

@app.route('/<codigo>/<grupo>/defcourse', methods=['GET', 'POST'])
def instrumentos(codigo,grupo):
    # Recupera los datos de la base de datos
    db = get_db()
    cur1 = db.execute("select nomb_asig, id_asig, grupo_asig, periodo from asignaturas where id_asig=?",[codigo])
    cur2 = db.execute('select id_resprog, peso from relevresulprog where id_asig=?',[codigo])
    cur3 = db.execute('select desc_eval, porceval, id_resprog, porc_abet, n.id_eval from defcalificacion as d, defnotaabet as n where d.id_asig = n.id_asig and d.id_eval = n.id_eval and d.id_asig=?',[codigo])
    cur4 = db.execute("select count(*) from defcalificacion where id_asig=?",[codigo])

    # Procesa los datos de resultados de programa
    formula = cur2.fetchall()
    suma = 0
    for i in formula:
        suma = suma + i[1]
    for i in range(len(formula)):
        temp1 = list(formula[i])
        temp1.append(int(formula[i][1]*1000/suma))
        formula[i] = tuple(temp1)
 
    # Variable para saber el numero de resultados de programa
    conteo = len(formula)

    # Procesa los datos de nombre de evaluaciones, y porcentaje de evaluaciones y resultados de programa
    evaluaciones = []
    for row in cur3.fetchall():
    	print "Row:",row
        evaluaciones.append(row)

    # Variable para saber el numero de evaluaciones
    numevals = cur4.fetchall()

    # print " "
    # print conteo
    # print numevals
    # print evaluaciones
    # print " "

    # # Agrupa los datos procesados en una sola lista y la retorna
    entries = {'detalles':cur1.fetchall()[0], 'resprog':formula, 'suma':suma, 'numevals':numevals[0][0], 'evaluaciones':evaluaciones, 'conteo':conteo}
    return render_template('defcourse.html', entries=entries)

@app.route('/<codigo>/<grupo>/guardarPesosEvaluaciones', methods=['POST'])
def guardarPesosInstrumentos(codigo,grupo):
    # Recupera de la base de datos los resultados de programa del curso
    db = get_db()
    cur = db.execute('select id_resprog from relevresulprog where id_asig=?',[codigo])
    resultados = cur.fetchall()

    # Recupera de la pagina el numero de instrumentos actual
    numero = int(request.form['numeroDeFilas'])

    # Recupera y procesa todos los datos (porcentajes) actuales de la pagina
    datos1 = []
    datos2 = []
    for i in range(1,int(numero)-3):
        datos1.append([request.form['evaluacion'+str(i)], request.form['porcentaje'+str(i)]])
        tmp = []
        for j in range(len(resultados)):
            tmp.append(request.form[resultados[j][0]+str(i)])
        datos2.append(tmp)

    print " "
    print datos1
    print datos2
    print " "

    # Elimina de la base de datos los registros viejos
    db.execute('delete from defnotaabet where id_asig=?',[codigo])
    db.execute('delete from defcalificacion where id_asig=?',[codigo])
    db.commit()

    # Inserta la nueva informacion en la base de datos
    for i in range(1,int(numero)-3):
        db.execute('insert into defcalificacion (id_asig, grupo_asig, desc_eval, porceval) values (?,?,?,?)', [codigo, grupo, datos1[i-1][0], datos1[i-1][1]])
        cur = db.execute('select id_eval from defcalificacion where desc_eval=?',[datos1[i-1][0]])
        numeroEval = cur.fetchall()
        for j in range(len(resultados)):
            db.execute('insert into defnotaabet values (?,?,?,?,?)', [codigo, grupo, numeroEval[0][0], resultados[j][0], datos2[i-1][j]])
    db.commit()

    flash("Datos guardados")

    # Recarga la pagina de instrumentos
    return redirect(url_for('instrumentos', codigo=codigo, grupo=grupo))

@app.route('/<codigo>/<grupo>/assessments', methods=['GET', 'POST'])
def indicadores(codigo,grupo):
    # Recupera los datos de la base de datos
    db = get_db()
    cur1 = db.execute("select nomb_asig, id_asig, grupo_asig, periodo from asignaturas where id_asig=?",[codigo])
    cur2 = db.execute("select d.desc_eval, d.id_eval, n.id_resprog, porc_abet, m.descr_resprog from defcalificacion as d, defnotaabet as n, resulprograma as m where porc_abet > 0 and d.id_eval = n.id_eval and n.id_resprog = m.id_resprog and n.id_asig=? order by d.id_eval",[codigo])
    cur3 = db.execute("select * from indicdesemp")
 
    # Procesa los datos de los instrumentos de evaluacion
    resprog = cur2.fetchall()
    temp = []
    i = 0
    while i<len(resprog):
        temp2 = []
        numero = resprog[i][1]
        temp2.append(resprog[i])
        if i>=len(resprog)-1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp2.append(resprog[i])
            if i>=len(resprog)-1:
                break
            i = i + 1
        temp.append(temp2)

    # Agrupa los datos procesados en una sola lista y la retorna
    entries = {'detalles':cur1.fetchall()[0], 'resprog':temp, 'indicdesemp':cur3.fetchall()}
    return render_template('assessments.html', entries=entries)

@app.route('/<codigo>/<grupo>/guardarPesosEvaluaciones', methods=['GET', 'POST'])
def guardarPesosIndicadores(codigo,grupo):
    db = get_db()
    cur = db.execute('select id_resprog from relevresulprog where id_asig=?',[codigo])
    resultados = cur.fetchall()

    # numero = int(request.form['numeroFilas'])
    # #numero = 0

    # datos1 = []
    # datos2 = []
    # for i in range(1,int(numero)+1):
    #     datos1.append([request.form['evaluacion'+str(i)], request.form['porcentaje'+str(i)]])
    #     tmp = []
    #     for j in range(len(resultados)):
    #         tmp.append(request.form[resultados[j][0]+str(i)])
    #     datos2.append(tmp)

    # print " "
    # print numero
    # print datos1
    # print datos2
    # print " "

    # g.db.execute('delete from defcalificacion where id_asig=?',[codigo])
    # g.db.execute('delete from defnotaabet where id_asig=?',[codigo])
    # g.db.commit()

    # for i in range(1,int(numero)+1):
    #     g.db.execute('insert into defcalificacion (id_asig, grupo_asig, desc_eval, porceval) values (?,?,?,?)', [codigo, grupo, datos1[i-1][0], datos1[i-1][1]])
    #     for j in range(len(resultados)):
    #         g.db.execute('insert into defnotaabet values (?,?,?,?,?)', [codigo, grupo, i, resultados[j][0], datos2[i-1][j]])
    # g.db.commit()

    return redirect(url_for('indicadores', codigo=codigo, grupo=grupo))

if __name__ == '__main__':
    init_db()
    app.run()
