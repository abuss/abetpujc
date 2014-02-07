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
    cur = db.execute('select nombre, codigo, grupo, periodo from asignatura where periodo=? order by nombre asc',['2014-1'])
    entries = [dict(title=row[0], cod=row[1], grupo=row[2], periodo=row[3]) for row in cur.fetchall()]
    return render_template('main.html', entries=entries)

@app.route('/<codigo>/<grupo>', methods=['GET', 'POST'])
def asignatura(codigo,grupo):
    db = get_db()
    cur = db.execute("select nombre, codigo, grupo, periodo from asignatura where codigo=?",[codigo])
    entries = [dict(title=row[0], cod=row[1], grupo=row[2], periodo=row[3]) for row in cur.fetchall()]
    return render_template('course.html', entries=entries[0])

@app.route('/<codigo>/<grupo>/defcourse', methods=['GET', 'POST'])
def instrumentos(codigo,grupo):
    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute("select nombre, codigo, grupo, periodo, id from asignatura where codigo=?",[codigo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) y procesa los datos de resultados de programa
    cur2 = db.execute('select resultado_de_programa, peso from formula where asignatura=?',[detalles[4]])
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

    # Recupera (de la base de datos) y procesa los datos de nombre de evaluaciones, y porcentaje de evaluaciones y resultados de programa
    cur3 = db.execute('select d.evaluacion, d.porcentaje, e.competencia, e.porcentaje, d.id_evaluacion from porcentaje_instrumento as d, porcentaje_abet as e where d.asignatura = e.asignatura and d.id_evaluacion = e.evaluacion and e.nivel = 1 and d.asignatura=?',[detalles[4]])
    evaluaciones = []
    for row in cur3.fetchall():
        evaluaciones.append(row)

    # Recupera (de la base de datos) el numero de evaluaciones
    cur4 = db.execute("select count(*) from porcentaje_instrumento where asignatura=?",[detalles[4]])
    numevals = cur4.fetchall()

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles':detalles, 'resprog':formula, 'suma':suma, 'numevals':numevals[0][0], 'evaluaciones':evaluaciones, 'conteo':conteo}
    return render_template('defcourse.html', entries=entries)

@app.route('/<codigo>/<grupo>/guardarPesosEvaluaciones', methods=['POST'])
def guardarPesosInstrumentos(codigo,grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute("select nombre, codigo, grupo, periodo, id from asignatura where codigo=?",[codigo])
    detalles = cur1.fetchall()[0]

    # Recupera de la base de datos los resultados de programa del curso
    cur2 = db.execute('select resultado_de_programa from formula where asignatura=?',[detalles[4]])
    resultados = cur2.fetchall()

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

    # Validacion antes de insertar: si el instrumento ya existe no se puede ingresar
    # Si no hay datos repetidos que no pueden ser guardados
    if request.form['hayRepetidos'] == '0':
        # Elimina de la base de datos los registros viejos
        db.execute('delete from porcentaje_abet where asignatura=?',[detalles[4]])
        db.execute('delete from porcentaje_instrumento where asignatura=?',[detalles[4]])
        db.commit()

        # Inserta la nueva informacion en la base de datos
        for i in range(1,int(numero)-3):
            db.execute('insert into porcentaje_instrumento (asignatura, evaluacion, porcentaje) values (?,?,?)', [detalles[4], datos1[i-1][0], datos1[i-1][1]])
            db.commit()
            cur = db.execute('select id_evaluacion from porcentaje_instrumento where evaluacion=? and asignatura=?',[datos1[i-1][0], detalles[4]])
            numeroEval = cur.fetchall()
            for j in range(len(resultados)):
                db.execute('insert into porcentaje_abet values (?,?,?,?,?,?)', [detalles[4], numeroEval[0][0], resultados[j][0], datos2[i-1][j],1,''])
                db.commit()

        flash("Datos guardados")

    # Recarga la pagina de instrumentos
    return redirect(url_for('instrumentos', codigo=codigo, grupo=grupo))

@app.route('/<codigo>/<grupo>/assessments', methods=['GET', 'POST'])
def indicadores(codigo,grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute("select nombre, codigo, grupo, periodo, id from asignatura where codigo=?",[codigo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur2 = db.execute("select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje, f.descripcion from porcentaje_instrumento as d, porcentaje_abet as e, resultado_de_programa as f where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? order by d.id_evaluacion",[detalles[4]])
    resprog = cur2.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur3 = db.execute("select d.evaluacion, e.competencia, e.porcentaje, e.superior from porcentaje_instrumento as d, porcentaje_abet as e, indicador_de_desempeno as f where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3")
    porcindicadores = cur3.fetchall()

    # Procesa los datos de los instrumentos de evaluacion, incluyendo la informacion previamente guardada
    inst = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])
        if i >= len(resprog)-1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i])
            if i >= len(resprog)-1:
                break
            i = i + 1

        for j in range(len(temp1)):
            temp2 = list(temp1[j])
            temp3 = []
            k = 0
            while k < len(porcindicadores):
                if porcindicadores[k][0] == temp1[j][0] and porcindicadores[k][3] == temp1[j][2]:
                    temp3.append([porcindicadores[k][1],porcindicadores[k][2]])
                    del porcindicadores[k]
                else:
                    k = k + 1
            temp3.insert(0,len(temp3))
            temp2.append(temp3)
            temp1[j] = tuple(temp2)

        inst.append(temp1)

    # Recupera (de la base de datos) los indicadores de desempeno
    cur4 = db.execute("select * from indicador_de_desempeno")

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles':detalles, 'resprog':inst, 'indicdesemp':cur4.fetchall()}
    return render_template('assessments.html', entries=entries)

@app.route('/<codigo>/<grupo>/guardarPesosIndicadores', methods=['POST'])
def guardarPesosIndicadores(codigo,grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute("select nombre, codigo, grupo, periodo, id from asignatura where codigo=?",[codigo])
    detalles = cur1.fetchall()[0]

    # Recupera de la base de datos los resultados de programa del curso
    cur2 = db.execute('select d.id_evaluacion, d.evaluacion, e.competencia from porcentaje_instrumento as d, porcentaje_abet as e where d.id_evaluacion = e.evaluacion and e.porcentaje > 0 and e.nivel = 1 and d.asignatura=?',[detalles[4]])
    instrumentos = cur2.fetchall()

    # Procesa los datos guardados en la base de datos, necesarios para hacer la insercion
    temp = []
    i = 0
    while i < range(len(instrumentos)):
        temp1 = []
        resprog = instrumentos[i][0]
        temp1.append(instrumentos[i])
        if i >= len(instrumentos)-1:
            break
        i = i + 1
        while resprog == instrumentos[i][0]:
            temp1.append(instrumentos[i])
            if i >= len(instrumentos)-1:
                break
            i = i + 1
        temp.append(temp1)

    # Recupera (de la base de datos) el numero de resultados de programa
    cur3 = db.execute('select count(*) from formula where asignatura=?',[detalles[4]])
    numero = cur3.fetchall()

    # Recupera de la pagina los datos de las entradas y los procesa
    datos = []
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            numero = int(request.form['numeroDeFilas'+str(temp[i][j][0])+str(temp[i][j][2])])
            for k in range(numero-2):
                datos.append([temp[i][j][0], temp[i][j][2], request.form["indicador"+str(temp[i][j][0])+str(temp[i][j][2])+str(k)][:5], request.form["pesoind"+str(temp[i][j][0])+str(temp[i][j][2])+str(k)]])

    # Elimina de la base de datos los registros viejos
    db.execute('delete from porcentaje_abet where asignatura=? and nivel=?',[detalles[4],3])
    db.commit()

    # Inserta la nueva informacion en la base de datos
    for d in datos:
        if d[2] != '---':
            db.execute('insert into porcentaje_abet values (?,?,?,?,?,?)', [detalles[4], d[0], d[2], int(d[3]), 3, d[1]])
    db.commit()

    # Recarga la pagina de los indicadores
    return redirect(url_for('indicadores', codigo=codigo, grupo=grupo))

@app.route('/<codigo>/<grupo>/grades', methods=['GET', 'POST'])
def notas(codigo,grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute("select nombre, codigo, grupo, periodo, id from asignatura where codigo=?",[codigo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los estudiantes
    cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc",[detalles[4]])
    estudiantes = cur2.fetchall()

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute("select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje from porcentaje_instrumento as d, porcentaje_abet as e, resultado_de_programa as f where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? order by d.id_evaluacion",[detalles[4]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur4 = db.execute("select d.evaluacion, e.competencia, e.porcentaje, e.superior, f.descripcion from porcentaje_instrumento as d, porcentaje_abet as e, indicador_de_desempeno as f where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3")
    porcindicadores = cur4.fetchall()

    # Procesa los datos de los instrumentos de evaluacion, incluyendo la informacion previamente guardada
    inst = []
    indicadores = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])
        if i >= len(resprog)-1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i])
            if i >= len(resprog)-1:
                break
            i = i + 1

        temp5 = 0
        temp6 = []
        for j in range(len(temp1)):
            temp2 = list(temp1[j])
            temp3 = []
            temp4 = []
            k = 0
            while k < len(porcindicadores):
                if porcindicadores[k][0] == temp1[j][0] and porcindicadores[k][3] == temp1[j][2]:
                    temp3.append([porcindicadores[k][1],porcindicadores[k][2],porcindicadores[k][4]])
                    temp4.append(porcindicadores[k][1])
                    del porcindicadores[k]
                else:
                    k = k + 1
            temp5 = temp5 + len(temp3)
            temp6.append(temp4)
            temp3.insert(0,len(temp3))
            temp2.append(temp3)
            temp1[j] = tuple(temp2)

        print [temp5,reduce(lambda x,y: x+y,temp6)]
        indicadores.append([temp5,reduce(lambda x,y: x+y,temp6)])
        inst.append(temp1)

    #print inst

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles':detalles, 'estudiantes':estudiantes, 'resprog':inst, 'numinstrumentos':len(inst), 'numestudiantes':len(estudiantes), 'indicadores':indicadores}
    return render_template('grades.html', entries=entries)

@app.route('/<codigo>/<grupo>/guardarNotas', methods=['POST'])
def guardarNotas(codigo,grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute("select nombre, codigo, grupo, periodo, id from asignatura where codigo=?",[codigo])
    detalles = cur1.fetchall()[0]

    # Recupera de la base de datos los resultados de programa del curso
    cur2 = db.execute('select d.id_evaluacion, d.evaluacion, e.competencia from porcentaje_instrumento as d, porcentaje_abet as e where d.id_evaluacion = e.evaluacion and e.porcentaje > 0 and e.nivel = 1 and d.asignatura=?',[detalles[4]])
    instrumentos = cur2.fetchall()

    # Procesa los datos guardados en la base de datos, necesarios para hacer la insercion
    temp = []
    i = 0
    while i < range(len(instrumentos)):
        temp1 = []
        resprog = instrumentos[i][0]
        temp1.append(instrumentos[i])
        if i >= len(instrumentos)-1:
            break
        i = i + 1
        while resprog == instrumentos[i][0]:
            temp1.append(instrumentos[i])
            if i >= len(instrumentos)-1:
                break
            i = i + 1
        temp.append(temp1)

    # Recupera (de la base de datos) el numero de resultados de programa
    cur3 = db.execute('select count(*) from formula where asignatura=?',[detalles[4]])
    numero = cur3.fetchall()

    # # Recupera de la pagina los datos de las entradas y los procesa
    # datos = []
    # for i in range(len(temp)):
    #     for j in range(len(temp[i])):
    #         numero = int(request.form['numeroDeFilas'+str(temp[i][j][0])+str(temp[i][j][2])])
    #         for k in range(numero-2):
    #             datos.append([temp[i][j][0], temp[i][j][2], request.form["indicador"+str(temp[i][j][0])+str(temp[i][j][2])+str(k)][:5], request.form["pesoind"+str(temp[i][j][0])+str(temp[i][j][2])+str(k)]])

    # # Elimina de la base de datos los registros viejos
    # db.execute('delete from porcentaje_abet where asignatura=? and nivel=?',[detalles[4],3])
    # db.commit()

    # # Inserta la nueva informacion en la base de datos
    # for d in datos:
    #     if d[2] != '---':
    #         db.execute('insert into porcentaje_abet values (?,?,?,?,?,?)', [detalles[4], d[0], d[2], int(d[3]), 3, d[1]])
    # db.commit()

    # Recarga la pagina de los indicadores
    return redirect(url_for('notas', codigo=codigo, grupo=grupo))

if __name__ == '__main__':
    init_db()
    app.run()
