# Sistema de evaluacion ABET
# Librerias
from __future__ import division
import sqlite3
from contextlib import closing

from flask import Flask, request, g, redirect, url_for, \
    render_template, flash

from operator import itemgetter
import sys

# Inicializacion de variables
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
    with app.open_resource('scripts/addData2db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('scripts/DB_Abet_SQLite.sql', mode='r') as f:
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
    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los cursos
    cur1 = db.execute(
        "select nombre_carrera, id_carrera from acreditacion_abet where periodo=? order by nombre_carrera asc",
        ['2014-1'])
    carreras = cur1.fetchall()

    # Recupera (de la base de datos) los cursos
    cur2 = db.execute(
        "select nombre, codigo, grupo, periodo, id_carrera from asignatura where periodo=? order by nombre asc",
        ['2014-1'])
    cursos = [dict(title=row[0], cod=row[1], grupo=row[2], periodo=row[3], carrera=row[4]) for row in cur2.fetchall()]

    # Agrupa los datos recuperados en una sola lista y la retorna a la pagina web
    entries = {'carreras': carreras, 'cursos': cursos}

    return render_template('main.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>', methods=['GET', 'POST'])
def asignatura(periodo, codigo, grupo):
    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select d.nombre, d.codigo, d.grupo, d.periodo, d.id, d.id_carrera, e.nombre_carrera \
        from asignatura as d, acreditacion_abet as e \
        where d.codigo=? and d.grupo=? and d.periodo=? and d.id_carrera = e.id_carrera",
        [codigo, grupo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los estudiantes
    cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [detalles[4]])
    estudiantes = cur2.fetchall()

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje, f.descripcion \
        from porcentaje_instrumento as d, porcentaje_abet as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
            and f.carrera=? \
        order by d.id_evaluacion",
        [detalles[4], detalles[5]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur4 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, f.descripcion \
        from porcentaje_instrumento as d, porcentaje_abet as e, resultado_de_programa as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 1")
    porcresultados = cur4.fetchall()

    # Recupera (de la base de datos) la informacion de las notas de los indicadores ya contenida en la base de datos
    cur5 = db.execute(
        "select evaluacion, competencia, codigo_estudiante, nota from nota_abet where asignatura=? and nivel=1",
        [detalles[4]])
    notasInd = cur5.fetchall()

    # Recupera (de la base de datos) y procesa los datos de resultados de programa
    cur6 = db.execute(
        "select d.resultado_de_programa, d.peso, e.descripcion from formula as d, resultado_de_programa as e \
        where asignatura=? and e.id = d.resultado_de_programa and e.carrera=?",
        [detalles[4], detalles[5]])
    formula = cur6.fetchall()
    numResultados = len(formula)
    resultados = []
    for a,b,c in formula:
        resultados.append(a)
    suma = 0
    for i in formula:
        suma = suma + i[1]
    for i in range(len(formula)):
        temp1 = list(formula[i])
        temp1.append(int(formula[i][1] * 1000 / suma))
        formula[i] = tuple(temp1)

    # Variable para saber el numero de resultados de programa
    conteo = len(formula)

    # Recupera (de la base de datos) la informacion de las notas de los instrumentos ya contenida en la base de datos
    cur7 = db.execute(
        "select evaluacion, codigo_estudiante, nota from nota_instrumento where asignatura=?",
        [detalles[4]])
    notasIns = cur7.fetchall()

    # Recupera (de la base de datos) la informacion de las notas de los instrumentos ya contenida en la base de datos
    cur8 = db.execute(
        "select codigo_estudiante, nota from nota_definitiva where asignatura=?",
        [detalles[4]])
    notasDef = cur8.fetchall()

    # Procesa los datos de los resultados de programa de las evaluaciones
    inst = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])
        if i >= len(resprog) - 1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i])
            if i >= len(resprog) - 1:
                break
            i = i + 1

        inst.append(temp1)
    for i in range(len(inst)):
        inst[i].insert(0,len(inst[i]))

    # Procesa los datos de las notas de los resultados de programa de cada instrumento guardadas previamente
    notasIndicadores = {}
    for i in range(1,len(inst)+1):
        notasIndicadores[i]=dict([(e[1],{}) for e in estudiantes])
    for (x,y,z,w) in notasInd:
        notasIndicadores[x][z][y] = round(w,1)

    # Procesa los datos de las notas de los instrumentos guardadas previamente
    notasInstrumentos = {}
    for i in range(1,len(inst)+1):
        notasInstrumentos[i]=dict([(e[1],{}) for e in estudiantes])
    for (x,y,z) in notasIns:
        notasInstrumentos[x][y] = round(z,1)

    # Procesa los datos de las notas de los resultados de programa totales
    cur9 = db.execute(
        "select d.evaluacion, d.competencia, d.codigo_estudiante, d.nota, e.porcentaje \
        from nota_abet as d, porcentaje_abet as e \
        where d.asignatura=? and d.nivel=1 and d.evaluacion = e.evaluacion and d.competencia = e.competencia \
        order by d.competencia",
        [detalles[4]])
    temp1 = cur9.fetchall()
    sumaResultados = dict(zip(resultados,[0]*len(resultados)))
    for i in resultados:
        cur10 = db.execute(
            "select evaluacion, competencia, porcentaje \
            from porcentaje_abet \
            where asignatura=? and competencia=? \
            order by competencia",
            [detalles[4],i])
        temp2 = cur10.fetchall()
        suma = 0
        for j,k,l in temp2:
            suma += l
        sumaResultados[i] = suma
    resultadosTotales = {}
    for e in estudiantes:
        resultadosTotales[e[1]] = dict(zip(resultados,[0]*len(resultados)))
    for (a,b,c,d,e) in temp1:
        resultadosTotales[c][b] = round(resultadosTotales[c][b]+((d*e)/sumaResultados[b]),1)

    # Procesa los datos de las notas definitivas guardadas previamente
    notasDefinitivas = dict([(e[1],0) for e in estudiantes])
    for (x,y) in notasDef:
        notasDefinitivas[x] = round(y,1)

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'estudiantes': estudiantes, 'resprog': inst, 'numinstrumentos': len(inst),
               'numestudiantes': len(estudiantes), 'notasIndicadores': notasIndicadores, 'conteo': conteo,
               'formula': formula, 'notasInstrumentos': notasInstrumentos, 'notasDefinitivas': notasDefinitivas,
               'resultadosTotales': resultadosTotales}
    return render_template('course.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/defcourse', methods=['GET', 'POST'])
def instrumentos(periodo, codigo, grupo):
    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select d.nombre, d.codigo, d.grupo, d.periodo, d.id, d.id_carrera, e.nombre_carrera \
        from asignatura as d, acreditacion_abet as e \
        where d.codigo=? and d.grupo=? and d.periodo=? and d.id_carrera = e.id_carrera",
        [codigo, grupo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) y procesa los datos de resultados de programa
    cur2 = db.execute(
        "select d.resultado_de_programa, d.peso, e.descripcion \
        from formula as d, resultado_de_programa as e \
        where asignatura=? and d.resultado_de_programa = e.id and e.carrera=?",
        [detalles[4], detalles[5]])
    formula = cur2.fetchall()
    suma = 0
    for i in formula:
        suma = suma + i[1]
    for i in range(len(formula)):
        temp1 = list(formula[i])
        temp1.append(int(formula[i][1] * 1000 / suma))
        formula[i] = tuple(temp1)

    # Variable para saber el numero de resultados de programa
    conteo = len(formula)

    # Recupera (de la base de datos) y procesa los datos de nombre de evaluaciones,
    # y porcentaje de evaluaciones y resultados de programa
    cur3 = db.execute(
        'select d.evaluacion, d.porcentaje, e.competencia, e.porcentaje, d.id_evaluacion \
        from porcentaje_instrumento as d, porcentaje_abet as e \
        where d.asignatura = e.asignatura and d.id_evaluacion = e.evaluacion and e.nivel = 1 and d.asignatura=?',
        [detalles[4]])
    evaluaciones = []
    for row in cur3.fetchall():
        evaluaciones.append(row)

    # Recupera (de la base de datos) el numero de evaluaciones
    cur4 = db.execute("select count(*) from porcentaje_instrumento where asignatura=?", [detalles[4]])
    numevals = cur4.fetchall()

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'resprog': formula, 'suma': suma, 'numevals': numevals[0][0],
               'evaluaciones': evaluaciones, 'conteo': conteo}
    return render_template('defcourse.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarPesosEvaluaciones', methods=['POST'])
def guardarPesosInstrumentos(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select nombre, codigo, grupo, periodo, id from asignatura where codigo=? and grupo=? and periodo=?",
        [codigo,grupo,periodo])
    detalles = cur1.fetchall()[0]

    # Recupera de la base de datos los resultados de programa del curso
    cur2 = db.execute('select resultado_de_programa from formula where asignatura=?', [detalles[4]])
    resultados = cur2.fetchall()

    # Recupera de la pagina el numero de instrumentos actual
    numero = int(request.form['numeroDeFilas'])

    # Recupera y procesa todos los datos (porcentajes) actuales de la pagina
    datos1 = []
    datos2 = []
    for i in range(1, int(numero) - 3):
        datos1.append([request.form['evaluacion' + str(i)], request.form['porcentaje' + str(i)]])
        tmp = []
        for j in range(len(resultados)):
            tmp.append(request.form[resultados[j][0] + str(i)])
        datos2.append(tmp)

    # Validacion antes de insertar: si el instrumento ya existe no se puede ingresar
    # Si no hay datos repetidos que no pueden ser guardados
    if request.form['hayRepetidos'] == '0':
        # Elimina de la base de datos los registros viejos
        db.execute('delete from porcentaje_abet where asignatura=?', [detalles[4]])
        db.execute('delete from porcentaje_instrumento where asignatura=?', [detalles[4]])
        db.commit()

        # Inserta la nueva informacion en la base de datos
        for i in range(1, int(numero) - 3):
            db.execute('insert into porcentaje_instrumento (asignatura, evaluacion, porcentaje) values (?,?,?)',
                       [detalles[4], datos1[i - 1][0], datos1[i - 1][1]])
            db.commit()
            cur = db.execute('select id_evaluacion from porcentaje_instrumento where evaluacion=? and asignatura=?',
                             [datos1[i - 1][0], detalles[4]])
            numeroEval = cur.fetchall()
            for j in range(len(resultados)):
                db.execute('insert into porcentaje_abet values (?,?,?,?,?,?)',
                           [detalles[4], numeroEval[0][0], resultados[j][0], datos2[i - 1][j], 1, ''])
                db.commit()

        flash("Datos guardados")

    # Recarga la pagina de instrumentos
    return redirect(url_for('instrumentos', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/<periodo>/<codigo>/<grupo>/assessments', methods=['GET', 'POST'])
def indicadores(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select d.nombre, d.codigo, d.grupo, d.periodo, d.id, d.id_carrera, e.nombre_carrera \
        from asignatura as d, acreditacion_abet as e \
        where d.codigo=? and d.grupo=? and d.periodo=? and d.id_carrera = e.id_carrera",
        [codigo, grupo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur2 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje, f.descripcion \
        from porcentaje_instrumento as d, porcentaje_abet as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
            and f.carrera=? \
        order by d.id_evaluacion",
        [detalles[4], detalles[5]])
    resprog = cur2.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur3 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior \
        from porcentaje_instrumento as d, porcentaje_abet as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3")
    porcindicadores = cur3.fetchall()

    # Procesa los datos de los instrumentos de evaluacion, incluyendo la informacion previamente guardada
    inst = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])
        if i >= len(resprog) - 1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i])
            if i >= len(resprog) - 1:
                break
            i = i + 1

        for j in range(len(temp1)):
            temp2 = list(temp1[j])
            temp3 = []
            k = 0
            while k < len(porcindicadores):
                if porcindicadores[k][0] == temp1[j][0] and porcindicadores[k][3] == temp1[j][2]:
                    temp3.append([porcindicadores[k][1], porcindicadores[k][2]])
                    del porcindicadores[k]
                else:
                    k = k + 1
            temp3.insert(0, len(temp3))
            temp2.append(temp3)
            temp1[j] = tuple(temp2)

        inst.append(temp1)

    # Recupera (de la base de datos) los indicadores de desempeno
    cur4 = db.execute(
        "select id, descripcion, resultado_de_programa from indicador_de_desempeno where carrera=?",
        [detalles[5]])

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'resprog': inst, 'indicdesemp': cur4.fetchall()}
    return render_template('assessments.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarPesosIndicadores', methods=['POST'])
def guardarPesosIndicadores(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select nombre, codigo, grupo, periodo, id from asignatura where codigo=? and grupo=? and periodo=?",
        [codigo,grupo,periodo])
    detalles = cur1.fetchall()[0]

    # Recupera de la base de datos los resultados de programa del curso
    cur2 = db.execute(
        'select d.id_evaluacion, d.evaluacion, e.competencia \
        from porcentaje_instrumento as d, porcentaje_abet as e \
        where d.id_evaluacion = e.evaluacion and e.porcentaje > 0 and e.nivel = 1 and d.asignatura=?',
        [detalles[4]])
    instrumentos = cur2.fetchall()

    # Procesa los datos guardados en la base de datos, necesarios para hacer la insercion
    temp = []
    i = 0
    while i < range(len(instrumentos)):
        temp1 = []
        resprog = instrumentos[i][0]
        temp1.append(instrumentos[i])
        if i >= len(instrumentos) - 1:
            break
        i += 1
        while resprog == instrumentos[i][0]:
            temp1.append(instrumentos[i])
            if i >= len(instrumentos) - 1:
                break
            i = i + 1
        temp.append(temp1)

    # Recupera (de la base de datos) el numero de resultados de programa
    cur3 = db.execute('select count(*) from formula where asignatura=?', [detalles[4]])
    numero = cur3.fetchall()

    # Recupera de la pagina los datos de las entradas y los procesa
    datos = []
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            numero = int(request.form['numeroDeFilas' + str(temp[i][j][0]) + str(temp[i][j][2])])
            for k in range(numero - 2):
                datos.append([temp[i][j][0], temp[i][j][2],
                              request.form["indicador" + str(temp[i][j][0]) + str(temp[i][j][2]) + str(k)][:5],
                              request.form["pesoind" + str(temp[i][j][0]) + str(temp[i][j][2]) + str(k)]])

    # Elimina de la base de datos los registros viejos
    db.execute('delete from porcentaje_abet where asignatura=? and nivel=?', [detalles[4], 3])
    db.commit()

    # Inserta la nueva informacion en la base de datos
    for d in datos:
        if d[2] != '---':
            db.execute('insert into porcentaje_abet values (?,?,?,?,?,?)',
                       [detalles[4], d[0], d[2], int(d[3]), 3, d[1]])
    db.commit()

    # Recarga la pagina de los indicadores
    return redirect(url_for('indicadores', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/<periodo>/<codigo>/<grupo>/grades', methods=['GET', 'POST'])
def notas(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select d.nombre, d.codigo, d.grupo, d.periodo, d.id, d.id_carrera, e.nombre_carrera \
        from asignatura as d, acreditacion_abet as e \
        where d.codigo=? and d.grupo=? and d.periodo=? and d.id_carrera = e.id_carrera",
        [codigo, grupo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los estudiantes
    cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [detalles[4]])
    estudiantes = cur2.fetchall()

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje \
        from porcentaje_instrumento as d, porcentaje_abet as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
        order by d.id_evaluacion",
        [detalles[4]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur4 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior, f.descripcion \
        from porcentaje_instrumento as d, porcentaje_abet as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3")
    porcindicadores = cur4.fetchall()

    # Recupera (de la base de datos) la informacion de las notas de los indicadores ya contenida en la base de datos
    cur5 = db.execute(
        "select evaluacion, competencia, codigo_estudiante, nota from nota_abet where asignatura=? and nivel=3",
        [detalles[4]])
    notasInd = cur5.fetchall()

    # Procesa los datos de los instrumentos de evaluacion, incluyendo la informacion previamente guardada
    inst = []
    indicadores = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])
        if i >= len(resprog) - 1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i])
            if i >= len(resprog) - 1:
                break
            i = i + 1

        temp5 = 0
        temp6 = []
        temp8 = []
        temp9 = []
        for j in range(len(temp1)):
            temp2 = list(temp1[j])
            temp3 = []
            temp4 = []
            temp7 = []

            k = 0
            while k < len(porcindicadores):
                if porcindicadores[k][0] == temp1[j][0] and porcindicadores[k][3] == temp1[j][2]:
                    temp3.append([porcindicadores[k][1], porcindicadores[k][2]])
                    temp4.append(porcindicadores[k][1])
                    temp7.append(porcindicadores[k][4])
                    del porcindicadores[k]
                else:
                    k = k + 1
            temp5 = temp5 + len(temp3)
            temp6.append(temp4)
            temp8.append(temp7)
            for l in range(len(temp3)):
                temp9.append(temp3[l][1]*temp2[3]/10000)
            temp1[j] = tuple(temp2)

        indicadores.append([temp5, reduce(lambda x, y: x + y, temp6), reduce(lambda x, y: x + y, temp8), temp9])
        inst.append(temp1)

    # Procesa los datos de las notas guardadas previamente
    notas = {}
    for i in range(1,len(inst)+1):
        notas[i]=dict([(e[1],{}) for e in estudiantes])
    for (x,y,z,w) in notasInd:
        notas[x][z][y] = w

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'estudiantes': estudiantes, 'resprog': inst, 'numinstrumentos': len(inst),
               'numestudiantes': len(estudiantes), 'indicadores': indicadores, 'notas': notas}
    return render_template('grades.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarNotas', methods=['POST'])
def guardarNotas(periodo, codigo, grupo):
    # Accede la base de datos
    global porcentajes_instrumentos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select nombre, codigo, grupo, periodo, id from asignatura where codigo=? and grupo=? and periodo=?",
        [codigo,grupo,periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los estudiantes
    cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre desc", [detalles[4]])
    estudiantes = cur2.fetchall()

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje \
        from porcentaje_instrumento as d, porcentaje_abet as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id \
            and e.asignatura=? order by d.id_evaluacion",
        [detalles[4]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur4 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior, f.descripcion, d.id_evaluacion \
        from porcentaje_instrumento as d, porcentaje_abet as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3")
    porcentaje_indicadores = cur4.fetchall()
    copia_porcentaje_indicadores = porcentaje_indicadores[:]

    # Recupera (de la base de datos) y procesa los datos de nombre de evaluaciones,
    # y porcentaje de evaluaciones y resultados de programa
    cur5 = db.execute(
        'select d.evaluacion, d.porcentaje, e.competencia, e.porcentaje, d.id_evaluacion \
        from porcentaje_instrumento as d, porcentaje_abet as e \
        where d.asignatura = e.asignatura and d.id_evaluacion = e.evaluacion and e.nivel = 1 and d.asignatura=?',
        [detalles[4]])
    instrumentos = []
    for row in cur5.fetchall():
        instrumentos.append(row)

    # Recupera (de la base de datos) el numero de evaluaciones
    cur6 = db.execute("select count(*) from porcentaje_instrumento where asignatura=?", [detalles[4]])
    numevals = cur6.fetchall()

    # Procesa los datos de los indicadores de evaluacion, incluyendo la informacion previamente guardada
    indicadores = []
    pesos = []
    evaluacion = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])
        if i >= len(resprog) - 1:
            break
        i += 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i])
            if i >= len(resprog) - 1:
                break
            i += 1

        temp4 = []
        temp5 = []
        for j in range(len(temp1)):
            temp2 = []
            temp3 = []

            k = 0
            while k < len(copia_porcentaje_indicadores):
                if copia_porcentaje_indicadores[k][0] == temp1[j][0] and copia_porcentaje_indicadores[k][3] == temp1[j][2]:
                    temp2.append([copia_porcentaje_indicadores[k][1], copia_porcentaje_indicadores[k][2]])
                    temp3.append(copia_porcentaje_indicadores[k][1])
                    del copia_porcentaje_indicadores[k]
                else:
                    k = k + 1
            for l in range(len(temp2)):
                temp5.append(temp2[l][1]*temp1[j][3]/10000)
            temp4.append(temp3)

        indicadores.append(reduce(lambda x, y: x + y, temp4))
        pesos.append(temp5)
        evaluacion.append(numero)

    # Recupera de la pagina los datos de las entradas y los procesa
    datos = []
    for i in range(1,len(indicadores)+1):
        temp1 = []
        for j in range(1,len(estudiantes)+1):
            temp2 = []
            if indicadores[j-1][0] != 0:
                for k in range(len(indicadores[i-1])):
                    temp2.append(request.form["ind" + str(i) + str(estudiantes[j-1][1]) + str(k)])
            temp1.append(temp2)
        datos.append(temp1)

    # Elimina de la base de datos los registros viejos
    db.execute('delete from nota_abet where asignatura=?',[detalles[4]])
    db.execute('delete from nota_instrumento where asignatura=?',[detalles[4]])
    db.execute('delete from nota_definitiva where asignatura=?',[detalles[4]])
    db.commit()

    # Procesa e inserta la nueva informacion de indicadores, resultados de programa e instrumentos en la base de datos
    definitiva_asignatura = []
    m = n = 0
    # Ciclo para los instrumentos (tabs)
    for d in range(len(datos)):
        n = m
        if m < len(porcentaje_indicadores):
            temp1 = porcentaje_indicadores[m][0]
        # Ciclo para los estudiantes (filas)
        for e in range(len(datos[d])):
            if datos[d][e] == []:
                continue
            else:
                definitiva_instrumento = 0

                # Procesa e inserta los valores de los indicadores
                for i in range(len(datos[d][e])):
                    if datos[d][e][i] != u'':
                        db.execute(
                            "insert into nota_abet values (?,?,?,?,?,?)",
                            [detalles[4], evaluacion[d], indicadores[d][i], 3, estudiantes[e][1], int(datos[d][e][i])])

                        definitiva_instrumento += (5.0*int(datos[d][e][i])*pesos[d][i]/100)
                    else:
                        db.execute(
                            "insert into nota_abet (asignatura, evaluacion, competencia, nivel, codigo_estudiante) \
                            values (?,?,?,?,?)",
                            [detalles[4], evaluacion[d], indicadores[d][i], 3, estudiantes[e][1]])

                # Procesa e inserta los valores de los resultados de programa
                m = n
                resultado = 0.0
                o = 0
                if m < len(porcentaje_indicadores):
                    temp2 = porcentaje_indicadores[m][3]
                    while temp1 == porcentaje_indicadores[m][0]:
                        if temp2 == porcentaje_indicadores[m][3]:
                            if datos[d][e][o] != '':
                                resultado += 5*int(datos[d][e][o])*porcentaje_indicadores[m][2]/10000
                            m += 1
                            o += 1
                        else:
                            db.execute(
                                "insert into nota_abet values (?,?,?,?,?,?)",
                                [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1], round(resultado,1)])
                            resultado = 0.0
                            temp2 = porcentaje_indicadores[m][3]
                        if m >= len(porcentaje_indicadores):
                            break

                    db.execute(
                        "insert into nota_abet values (?,?,?,?,?,?)",
                        [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1], round(resultado,1)])

                # Inserta el valor de la nota definitiva de las evaluaciones
                db.execute(
                    "insert into nota_instrumento values (?,?,?,?)",
                    [detalles[4], evaluacion[d], estudiantes[e][1], round(definitiva_instrumento,1)])

                definitiva_asignatura.append([definitiva_instrumento, evaluacion[d], estudiantes[e][1]])
        db.commit()

    # Procesa e inserta la nueva informacion de nota definitiva de una asignatura en la base de datos
    porcentajes_instrumentos = []
    for i in range(0, len(instrumentos), int(len(instrumentos)/numevals[0][0])):
        porcentajes_instrumentos.append(instrumentos[i])
    definitiva_asignatura = sorted(definitiva_asignatura, key=itemgetter(2))
    j = 0
    for i in range(len(estudiantes)):
        nota_def = 0.0
        est = estudiantes[i][1]
        if j >= len(definitiva_asignatura) - 1:
                break
        while est == definitiva_asignatura[j][2]:
            for k in porcentajes_instrumentos:
                if k[4] == definitiva_asignatura[j][1]:
                    nota_def += definitiva_asignatura[j][0] * k[1] / 100
            j += 1
            if j >= len(definitiva_asignatura) - 1:
                break
        db.execute("insert into nota_definitiva values (?,?,?)", [detalles[4], estudiantes[i][1], round(nota_def,1)])
        db.commit()

    # Recarga la pagina de los indicadores
    return redirect(url_for('notas', periodo=periodo, codigo=codigo, grupo=grupo))


if __name__ == '__main__':
    if len(sys.argv)>2 and sys.argv[1]=='initdb':
        init_db()
    app.run()
