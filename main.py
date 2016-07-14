#!/usr/bin/python
# -*- coding: latin1 -*-

# Sistema de evaluacion ABET

# Librerias
from __future__ import division
import sqlite3
from contextlib import closing
import math, statistics

from flask import Flask, request, g, redirect, url_for, \
    render_template, flash, session, send_from_directory, make_response
import flask
import requests
from functools import wraps, reduce
from operator import itemgetter
import sys
from flask import json
from os import path
import xlsxwriter
import pdfkit

# Inicializacion de variables /home/abetpujc/abetpujc/abet.db
# /home/amezqui/work/abetpujc

app = Flask(__name__)
app.config.update(dict(
    # Base de datos oficial
    # DATABASE = '/home/abetpujc/abetpujc/abet.db',
    # Para hacer pruebas
    DATABASE='/Users/gsarria/Dropbox/Work/ABETForm/github/abetpujc/abet.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    EXCEL='excel',
    PDF='pdf'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# class flask.ext.login.LoginManager(app=app, add_context_processor=True)


# login_manager = LoginManager()

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
    """
    Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def get_students(src, args):
    # periodo="", grupo="", codigo="", urlget=""
    if src == "ws":
        estudiantes = []
        p_periodo = args[0]
        group = args[1]
        proof = {'pCurso': args[2], 'pGrupo': group, 'pPeriodo': p_periodo}
        # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
        r = requests.get(args[3], params=proof)

        proofjson = r.json()
        for x in proofjson:
            estudiante = [x['nombre'].capitalize(), int(x['emplid'])]
            estudiantes.append(estudiante)

        for e in estudiantes:
            nombre = e[0].rsplit(' ')
            if len(nombre) > 3:
                temp1 = nombre[0].capitalize()
                temp2 = nombre[1].capitalize()
                nombre[0] = nombre[2].capitalize()
                nombre[1] = nombre[3].capitalize()
                nombre[2] = temp1
                nombre[3] = temp2
            elif len(nombre) == 3:
                temp1 = nombre[0].capitalize()
                nombre[0] = nombre[1].capitalize()
                nombre[1] = nombre[2].capitalize()
                nombre[2] = temp1
            else:
                temp1 = nombre[0].capitalize()
                nombre[0] = nombre[1].capitalize()
                nombre[1] = temp1
            e[0] = reduce(lambda x, y: x + ' ' + y, nombre)
        estudiantes.sort()
        return estudiantes
    elif src == "bd":
        db = get_db()
        cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [args[4]])
        estudiantes = cur2.fetchall()
        return estudiantes
    else:
        print("No hay procedimiento para la fuente: ", src)


def NotasExcel(periodo, codigo, grupo, data):
    nombre = 'excel/' + str(periodo) + str(codigo) + str(grupo) + '.xlsx'
    workbook = xlsxwriter.Workbook(nombre)
    worksheet = workbook.add_worksheet()
    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'silver'})
    merge_format2 = workbook.add_format({'border': 1})
    merge_format3 = workbook.add_format({'border': 1, 'fg_color': '#FFD1A3', 'align': 'right'})
    formatb = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'})
    format = workbook.add_format({'border': 1})
    formatp = workbook.add_format({'border': 1})
    formatp.set_num_format('0.0%')
    formatn = workbook.add_format({'border': 1})
    formatn.set_num_format('0.00')
    format2 = workbook.add_format({'border': 1, 'fg_color': '#FFD1A3'})
    formatp2 = workbook.add_format({'border': 1, 'fg_color': '#FFD1A3'})
    formatp2.set_num_format('0.0%')
    formatn2 = workbook.add_format({'border': 1, 'fg_color': '#FFD1A3'})
    formatn2.set_num_format('0.00')
    worksheet.write('A2', 'Curso:', merge_format2)
    worksheet.write('A3', 'Periodo:', merge_format2)
    worksheet.write('A4', 'Profesor:', merge_format2)
    worksheet.merge_range('A1:M1', 'Resumen de las calificaciones de los estudiantes', merge_format)
    worksheet.merge_range('B2:M2', data['detalles'][0], merge_format2)
    worksheet.merge_range('B3:M3', data['detalles'][3], merge_format2)
    worksheet.merge_range('B4:M4', data['detalles'][7], merge_format2)
    worksheet.merge_range('A6:M6', 'Fórmula del Curso', merge_format)
    worksheet.add_table('B7:L7', {'header_row': False})
    i = 6
    j = 1
    worksheet.write(i, 0, '', formatb)
    for c in data['ordcompt']:
        worksheet.write(i, j, c, formatb)
        j += 1
    worksheet.write(i, j, 'Total', formatb)
    i = 7
    j = 0
    sumtot = 0
    worksheet.write(i, j, 'Pesos', format)
    for f in data['ordcompt']:
        sumtot += data['formm'][f]
        if data['formm'][f] == 0:
            worksheet.write(i, j + 1, ' ', formatn)
        else:
            worksheet.write(i, j + 1, data['formm'][f], formatn)
        j += 1
    worksheet.write_formula(i, j + 1, '=SUM(B8:L8)', formatn2)
    i = 8
    j = 0
    tot2 = 0
    worksheet.write(i, j, 'Porcentajes', format)
    for f in data['ordcompt']:
        if data['formm'][f] == 0:
            worksheet.write(i, j + 1, 0, formatp)
        else:
            worksheet.write(i, j + 1, round((data['formm'][f] / sumtot), 1), formatp)
            tot2 += (data['formm'][f] / sumtot)
        j += 1
    worksheet.write(i, j + 1, tot2, formatp2)
    worksheet.merge_range('A12:M12', 'Resultados', merge_format)
    i = 12
    j = 0
    worksheet.write(i, j, 'Estudiante', format)
    for c in data['ordcompt']:
        worksheet.write(i, j + 1, c, formatb)
        j += 1
    worksheet.write(i, j + 1, 'Nota Final', formatb)
    i = 13
    for estud in data['sestud']:
        j = 0
        worksheet.write(i, j, estud[0], format)
        for c in data['ordcompt']:
            if c in data['comres'][estud[1]]:
                worksheet.write(i, j + 1, data['comres'][estud[1]][c], formatn)
            else:
                worksheet.write(i, j + 1, ' ', format)
            j += 1
        worksheet.write(i, j + 1, data['notdef'][estud[1]], formatn)
        i += 1

    if data['estud'] <= 26:
        num = 27 - data['estud']
        for x in range(num):
            j = 0
            worksheet.write(i, j, '', formatn)
            for c in data['ordcompt']:
                worksheet.write(i, j + 1, ' ', formatn)
                j += 1
            worksheet.write(i, j + 1, '', formatn)
            i += 1
        worksheet.merge_range('A41:M41', 'Población Total', merge_format)
        i += 1
        j = 0
        worksheet.write(i, j, 'Promedio', format)
        for c in data['ordcompt']:
            if data['promgeneralind'][c] > 0:
                worksheet.write(i, j + 1, data['promgeneralind'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=SI.ERROR(PROMEDIO(M14:M40),0)', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'Desv. Estándar', format)
        for c in data['ordcompt']:
            if data['desviacion'][c] > 0:
                worksheet.write(i, j + 1, data['desviacion'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=SI.ERROR(PROMEDIO(M14:M40),0)', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'DE/Promedio', format)
        for c in data['ordcompt']:
            if data['devmed'][c] > 0:
                worksheet.write(i, j + 1, data['devmed'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=SI.ERROR(M43/M42,0)', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'Mínimo', format)
        for c in data['ordcompt']:
            if data['minimo'][c] > 0:
                worksheet.write(i, j + 1, data['minimo'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=MIN(M14:M40)', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'Maximo', format)
        for c in data['ordcompt']:
            if data['maximo'][c] > 0:
                worksheet.write(i, j + 1, data['maximo'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=MAX(M14:M40)', format2)
        i += 2
        j = 0
        worksheet.write(i - 1, j, 'No Estudiantes', format)
        worksheet.merge_range('B47:M47', data['estud'], merge_format3)
        worksheet.write(i, j, '%Aprueban', format)
        for c in data['ordcompt']:
            if data['promgeneralindaprob'][c] > 0:
                worksheet.write(i, j + 1, data['promgeneralindaprob'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=CONTAR.SI(M14:M40,">=2.95")/$B$47', format2)
        worksheet.merge_range('A50:M50', 'Estudiantes que aprobaron', merge_format)
        i += 3
        j = 0
        worksheet.write(i, j, 'Promedio', format)
        for c in data['ordcompt']:
            if data['promgeneralindaprob'][c] > 0:
                worksheet.write(i, j + 1, data['promgeneralindaprob'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=SI.ERROR(PROMEDIO.SI($M14:$M40,">=2.95",M14:M40),0)', format2)

    else:
        worksheet.merge_range(i, 0, i, 12, 'Población Total', merge_format)
        itot = i
        i += 1
        j = 0
        worksheet.write(i, j, 'Promedio', format)
        for c in data['ordcompt']:
            if data['promgeneralind'][c] > 0:
                worksheet.write(i, j + 1, data['promgeneralind'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1

        worksheet.write_formula(i, j + 1, '=SI.ERROR(PROMEDIO(M14:M' + str(itot) + '),0)', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'Desv. Estándar', format)
        for c in data['ordcompt']:
            if data['desviacion'][c] > 0:
                worksheet.write(i, j + 1, data['desviacion'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=SI.ERROR(PROMEDIO(M14:M' + str(itot) + '),0)', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'DE/Promedio', format)
        for c in data['ordcompt']:
            if data['devmed'][c] > 0:
                worksheet.write(i, j + 1, data['devmed'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=SI.ERROR(M' + str(itot + 2) + '/M' + str(itot + 3) + ',0)', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'Mínimo', format)
        for c in data['ordcompt']:
            if data['minimo'][c] > 0:
                worksheet.write(i, j + 1, data['minimo'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=MIN(M14:M' + str(itot) + ')', format2)
        i += 1
        j = 0
        worksheet.write(i, j, 'Maximo', format)
        for c in data['ordcompt']:
            if data['maximo'][c] > 0:
                worksheet.write(i, j + 1, data['maximo'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=MAX(M14:M' + str(itot) + ')', format2)
        i += 2
        j = 0
        worksheet.write(i - 1, j, 'No Estudiantes', format)
        worksheet.merge_range(i - 1, 1, i - 1, 12, data['estud'], merge_format3)
        worksheet.write(i, j, '%\Aprueban', format)
        for c in data['ordcompt']:
            if data['promgeneralindaprob'][c] > 0:
                worksheet.write(i, j + 1, data['promgeneralindaprob'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1, '=CONTAR.SI(M14:M' + str(itot) + ',">=2.95")/$B$' + str(itot + 7) + '',
                                format2)
        i += 2
        worksheet.merge_range(i, 0, i, 12, 'Estudiantes que aprobaron', merge_format)
        i += 1
        j = 0
        worksheet.write(i, j, 'Promedio', format)
        for c in data['ordcompt']:
            if data['promgeneralindaprob'][c] > 0:
                worksheet.write(i, j + 1, data['promgeneralindaprob'][c], formatn2)
            else:
                worksheet.write(i, j + 1, 0.00, formatn2)
            j += 1
        worksheet.write_formula(i, j + 1,
                                '=SI.ERROR(PROMEDIO.SI($M14:$M' + str(itot) + ',">=2.95",M14:M' + str(itot) + '),0)',
                                format2)

    workbook.close()
    return 0


def reportepdf(periodo, codigo, grupo, datos):
    nombre = 'pdf/' + str(periodo) + str(codigo) + str(grupo) + '.pdf'
    rendered_template = render_template('reportPDF.html', entries=datos)
    pdf = pdfkit.from_string(rendered_template, nombre, css='static/style.css', options={'encoding': 'utf-8'})
    # return 0


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


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
@login_required
def show_periods():
    """
    Funcion asociada a la pagina que muestra los periodos academicos
    """

    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los periodos
    cur1 = db.execute("select distinct periodo from acreditacion_abet order by periodo asc")
    periodos = cur1.fetchall()

    # Organiza los usuarios
    per = 1
    if len(periodos) == 0:
        per = 0
    usuario = session['id_prof'][1] if 'id_prof' in session else session['user']
    power = session['lvl']

    # Agrupa los datos recuperados en una sola lista y la retorna a la pagina web
    entries = {'periodos': periodos, 'hayperiodos': per, 'usuario': usuario, 'permisos': power}

    return render_template('periods.html', entries=entries)


@app.route('/<periodo>', methods=['GET', 'POST'])
@login_required
def show_courses(periodo):
    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los cursos
    cur1 = db.execute(
        "select nombre_carrera, id_carrera from acreditacion_abet where periodo=? order by nombre_carrera asc",
        [periodo])
    carreras = cur1.fetchall()

    # Recupera (de la base de datos) los cursos
    if session['lvl'] == 4:
        cur2 = db.execute(
            "select nombre, codigo, grupo, periodo, id_carrera from asignatura where periodo=? and id_profesor=? order by nombre asc",
            [periodo, session['id_prof'][0]])
    else:
        cur2 = db.execute(
            "select nombre, codigo, grupo, periodo, id_carrera from asignatura where periodo=? order by nombre asc",
            [periodo])
    cursos = [dict(title=row[0], cod=row[1], grupo=row[2], periodo=row[3], carrera=row[4]) for row in cur2.fetchall()]
    cursosAux = [x['carrera'] for x in cursos]

    for x in carreras:
        if x[1] not in cursosAux:
            carreras.remove(x)

    vacio = 0
    usuario = session['id_prof'][1] if 'id_prof' in session else session['user']
    power = session['lvl']

    # Agrupa los datos recuperados en una sola lista y la retorna a la pagina web
    entries = {'carreras': carreras, 'cursos': cursos, 'vacio': vacio, 'usuario': usuario, 'permisos': power}

    return render_template('main.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>', methods=['GET', 'POST'])
@login_required
def asignatura(periodo, codigo, grupo):
    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select d.nombre, d.codigo, d.grupo, d.periodo, d.id, d.id_carrera, e.nombre_carrera, e.codigo_periodo \
        from asignatura as d, acreditacion_abet as e \
        where d.codigo=? and d.grupo=? and d.periodo=? and d.id_carrera = e.id_carrera and e.periodo=?",
        [codigo, grupo, periodo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera los estudiantes
    # cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [detalles[4]])
    # estudiantes = cur2.fetchall()
    # Periodos:
    # 2014-1: 0930
    # 2014-2: 0940
    # 2015-1: 0945
    # 2015-2: 0950
    # 2016-1: 0955
    # 2016-2: 0960
    p_periodo = detalles[7]
    # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
    urlget = "http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante"
    # periodo="", grupo="",codigo="",urlget=""
    argmnts = [p_periodo, grupo, codigo, urlget]
    estudiantes = get_students("ws", argmnts)
    # estudiantes = get_students("bd",detalles)

    # Elimina estudiantes repetidos que vienen del web service
    i = 0
    while i < len(estudiantes):
        if(i<len(estudiantes)-1):
            if(estudiantes[i][1] == estudiantes[i+1][1]):
                del estudiantes[i]
            else:
                i = i + 1
        else:
            break

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje, f.descripcion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
            and f.carrera=? \
        order by d.id_evaluacion",
        [detalles[4], detalles[5]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur4 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, f.descripcion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 1")
    porcresultados = cur4.fetchall()

    # Recupera (de la base de datos) la informacion de las notas de los indicadores ya contenida en la base de datos
    cur5 = db.execute(
        "select evaluacion, codigo_estudiante, competencia, nota from nota_abet where asignatura=? and nivel=1",
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
    for a, b, c in formula:
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
        inst[i].insert(0, len(inst[i]))

    # Procesa los datos de las notas de los resultados de programa de cada instrumento guardadas previamente
    supinst = []
    for com in resprog:
        if com[1] not in supinst:
            supinst.append(com[1])
    compt = dict([(ind, {}) for ind in supinst])
    tempcompt = []
    if (resprog != []):
        idtemp = resprog[0][1]
        for com in resprog:
            if idtemp == com[1]:
                tempcompt.append(com[2])
            else:
                compt[idtemp] = tempcompt
                idtemp = com[1]
                tempcompt = [com[2]]

        compt[supinst[len(supinst) - 1]] = tempcompt

    notasIndicadores = dict([(ind, {}) for ind in supinst])

    for nota in notasIndicadores:
        notasIndicadores[nota] = dict([(e[1], {}) for e in estudiantes])

    for nota in notasIndicadores:
        for estudiante in notasIndicadores[nota]:
            notasIndicadores[nota][estudiante] = dict([(comp, {}) for comp in compt[nota]])
            # notasIndicadores = {}

    for i in range(1, len(inst) + 1):
        notasIndicadores[i] = dict([(e[1], {}) for e in estudiantes])

    for (x, y, z, w) in notasInd:
        notasIndicadores[x][y][z] = float(round(w, 2))

    # Procesa los datos de las notas de los instrumentos guardadas previamente
    notasInstrumentos = dict([(ind, {}) for ind in supinst])

    for nota in notasInstrumentos:
        notasInstrumentos[nota] = dict([(e[1], {}) for e in estudiantes])

        # notasInstrumentos = {}
        # for i in range(1,len(inst)+1):
        # notasInstrumentos[i]=dict([(e[1],{}) for e in estudiantes])

    for (x, y, z) in notasIns:
        notasInstrumentos[x][y] = float(round(z, 2))

    # Procesa los datos de las notas de los resultados de programa totales
    cur9 = db.execute(
        "select d.evaluacion, d.competencia, d.codigo_estudiante, d.nota, e.porcentaje \
        from nota_abet as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e\
        where d.asignatura=? and d.nivel=1 and d.evaluacion = e.evaluacion and d.competencia = e.competencia \
        order by d.competencia",
        [detalles[4]])
    temp1 = cur9.fetchall()
    sumaResultados = dict(zip(resultados, [0] * len(resultados)))
    for i in resultados:
        cur10 = db.execute(
            "select e.evaluacion, dsak.competencia, e.porcentaje \
            from porcentaje_abet as e inner join Descripcion_A_K as dsak on e.Id_COMPETENCIA = dsak.competencia \
            where asignatura=? and dsak.competencia=? \
            order by competencia",
            [detalles[4], i])
        temp2 = cur10.fetchall()
        suma = 0
        for j, k, l in temp2:
            if (l != ''):
                suma += l
        sumaResultados[i] = suma
    resultadosTotales = dict([(e[1], {}) for e in estudiantes])
    for e in estudiantes:
        resultadosTotales[e[1]] = dict(zip(resultados, [0] * len(resultados)))
    for (a, b, c, d, e) in temp1:
        if (d == "" or e == ""):
            resultadosTotales[c][b] = float(round(resultadosTotales[c][b], 2))
        else:
            resultadosTotales[c][b] = float(round(resultadosTotales[c][b] + (d * e / sumaResultados[b]), 2))

    for est in resultadosTotales:
        for compt in resultadosTotales[est]:
            resultadosTotales[est][compt] = float(round(resultadosTotales[est][compt], 2))

    # Procesa los datos de las notas definitivas guardadas previamente
    notasDefinitivas = dict([(e[1], 0) for e in estudiantes])
    for (x, y) in notasDef:
        notasDefinitivas[x] = float(round(y, 2))

    comptorg = list(resultadosTotales[estudiantes[0][1]].keys())
    comptorg.sort()
    # for k in estudiantes:
    #    for j in notasIndicadores[supinst[0]].keys():
    #        if j == k[1]:
    #            print(k[0],j)
    #    for j in comptorg:
    #        print(resultadosTotales[k[1]][j],j,k[1])
    # print(notasDefinitivas[k[1]])
    usuario = session['id_prof'][1] if 'id_prof' in session else session['user']
    power = session['lvl']

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'estudiantes': estudiantes, 'resprog': inst, 'numinstrumentos': len(inst),
               'numestudiantes': len(estudiantes), 'notasIndicadores': notasIndicadores, 'conteo': conteo,
               'formula': formula, 'notasInstrumentos': notasInstrumentos, 'notasDefinitivas': notasDefinitivas,
               'resultadosTotales': resultadosTotales, 'periodo': periodo, 'idinst': supinst, 'idcompt': comptorg,
               'usuario': usuario, 'permisos': power}
    if not notasDef:
        entries['habrep'] = 0
    else:
        entries['habrep'] = 1

    return render_template('course.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/defcourse', methods=['GET', 'POST'])
@login_required
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
        from instrumento as d, \
        (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e \
        where e.asignatura = d.asignatura and d.id_evaluacion = e.evaluacion and e.nivel = 1 and d.asignatura=?',
        [detalles[4]]
    )
    evaluaciones = []
    for row in cur3.fetchall():
        evaluaciones.append(row)

    # Recupera (de la base de datos) el numero de evaluaciones
    cur4 = db.execute("select count(*) from instrumento where asignatura=?", [detalles[4]])
    numevals = cur4.fetchall()

    usuario = session['id_prof'][1] if 'id_prof' in session else session['user']
    power = session['lvl']
    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'resprog': formula, 'suma': suma, 'numevals': numevals[0][0],
               'evaluaciones': evaluaciones, 'conteo': conteo, 'usuario': usuario, "permisos": power}
    return render_template('defcourse.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarPesosEvaluaciones', methods=['POST'])
@login_required
def guardarPesosInstrumentos(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select nombre, codigo, grupo, periodo, id from asignatura where codigo=? and grupo=? and periodo=?",
        [codigo, grupo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera de la base de datos los resultados de programa del curso
    cur2 = db.execute('select resultado_de_programa from formula where asignatura=?', [detalles[4]])
    resultados = cur2.fetchall()

    # Recupera de la pagina el numero de instrumentos actual
    x = request.form['numeroDeFilas']
    if (x != ''):
        numero = int(request.form['numeroDeFilas'])
    else:
        numero = 5

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
        # Inserta la nueva informacion en la base de datos
        for i in range(1, int(numero) - 3):
            if not db.execute("select asignatura from instrumento where asignatura = ? and evaluacion = ? ",
                              [detalles[4], datos1[i - 1][0]]).fetchall():
                db.execute('insert or IGNORE into instrumento (asignatura, evaluacion, porcentaje) values (?,?,?)',
                           [detalles[4], datos1[i - 1][0], datos1[i - 1][1]])
                db.commit()
                cur = db.execute('select id_evaluacion from instrumento where evaluacion=? and asignatura=?',
                                 [datos1[i - 1][0], detalles[4]])
                numeroEval = cur.fetchall()
                for j in range(len(resultados)):
                    # NEED FIX HERE!(ASK)
                    idnxt = db.execute('select max(Id) from porcentaje_abet')
                    nxtid = idnxt.fetchall();
                    # insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
                    db.execute(
                        'insert or IGNORE into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (?,?,?,?,?)',
                        [detalles[4], numeroEval[0][0], resultados[j][0], datos2[i - 1][j], int(nxtid[0][0]) + 1])
                    db.commit()
            else:
                db.execute('UPDATE or IGNORE instrumento set porcentaje = ? where asignatura =? and evaluacion = ?',
                           [datos1[i - 1][1], detalles[4], datos1[i - 1][0]])
                db.commit()
                cur = db.execute('select id_evaluacion from instrumento where evaluacion=? and asignatura=?',
                                 [datos1[i - 1][0], detalles[4]])
                numeroEval = cur.fetchall()
                for j in range(len(resultados)):
                    # NEED FIX HERE!(ASK)
                    if not db.execute(
                            "select asignatura from porcentaje_abet where asignatura = ? and evaluacion = ? and Id_COMPETENCIA = ?",
                            [detalles[4], numeroEval[0][0], resultados[j][0]]).fetchall():
                        idnxt = db.execute('select max(Id) from porcentaje_abet')
                        nxtid = idnxt.fetchall();
                        # insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
                        db.execute(
                            'INSERT or IGNORE into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (?,?,?,?,?)',
                            [detalles[4], numeroEval[0][0], resultados[j][0], datos2[i - 1][j], int(nxtid[0][0]) + 1])
                        db.commit()
                    else:
                        db.execute(
                            'UPDATE or IGNORE porcentaje_abet set porcentaje = ? where asignatura =? and evaluacion = ? and Id_COMPETENCIA = ?',
                            [datos2[i - 1][j], detalles[4], numeroEval[0][0], resultados[j][0]])
                        db.commit()
        # Elimina los que ya no estan
        curMat = db.execute('select EVALUACION from instrumento where asignatura=?', [detalles[4]])
        dbInst = [x[0] for x in curMat.fetchall()]
        datos3 = [x[0] for x in datos1]
        for Inst in dbInst:
            if Inst not in datos3:
                # print("Borrar")
                db.execute('DELETE from INSTRUMENTO where evaluacion = ?  and asignatura = ?', [Inst, detalles[4]])
        db.commit()
        flash("Datos guardados")

    # Recarga la pagina de instrumentos
    return redirect(url_for('instrumentos', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/<periodo>/<codigo>/<grupo>/assessments', methods=['GET', 'POST'])
@login_required
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
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
            and f.carrera=? \
        order by d.id_evaluacion",
        [detalles[4], detalles[5]])
    resprog = cur2.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur3 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",
        [detalles[4]])
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
    usuario = session['id_prof'][1] if 'id_prof' in session else session['user']
    power = session['lvl']

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'resprog': inst, 'indicdesemp': cur4.fetchall(), 'usuario': usuario,
               'permisos': power}

    return render_template('assessments.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarPesosIndicadores', methods=['POST'])
@login_required
def guardarPesosIndicadores(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select nombre, codigo, grupo, periodo, id from asignatura where codigo=? and grupo=? and periodo=?",
        [codigo, grupo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera de la base de datos los resultados de programa del curso
    cur2 = db.execute(
        'select d.id_evaluacion, d.evaluacion, e.competencia \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e \
        where d.id_evaluacion = e.evaluacion and e.porcentaje > 0 and e.nivel = 1 and d.asignatura=?',
        [detalles[4]])
    instrumentos = cur2.fetchall()

    # Procesa los datos guardados en la base de datos, necesarios para hacer la insercion
    temp = []
    i = 0
    while i < len(instrumentos):
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
            numero2 = int(request.form['numeroDeFilas' + str(temp[i][j][0]) + str(temp[i][j][2])])
            for k in range(numero2 - 2):
                datos.append((temp[i][j][0], temp[i][j][2],
                              request.form["indicador" + str(temp[i][j][0]) + str(temp[i][j][2]) + str(k)][:3],
                              request.form["pesoind" + str(temp[i][j][0]) + str(temp[i][j][2]) + str(k)]))

    # Inserta la nueva informacion en la base de datos
    for d in datos:
        if d[2] != '---':
            # insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
            # insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values() insert into porcentaje_abet values
            idnxt = db.execute('select max(Id) from porcentaje_abet')
            nxtid = idnxt.fetchall()
            db.execute('INSERT OR IGNORE  into Descripcion_A_K values (?,?,?)', [d[2], d[1], 3])
            db.execute(
                'INSERT or IGNORE into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (?,?,?,?,?)',
                [detalles[4], d[0], d[2], int(d[3]), nxtid[0][0]])
            db.execute(
                'UPDATE or IGNORE porcentaje_abet SET PORCENTAJE = ? where ASIGNATURA = ? and EVALUACION = ? and Id_COMPETENCIA = ? and Id = ?',
                [int(d[3]), detalles[4], d[0], d[2], nxtid[0][0]])
    curmagico = db.execute(
        'select e.evaluacion, e.superior ,e.Id_COMPETENCIA , cast(e.PORCENTAJE as text)   from (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e  where e.nivel = 3 and e.asignatura=?',
        [detalles[4]])
    registrados = curmagico.fetchall()
    for r in registrados:
        if r not in datos:
            db.execute('DELETE from porcentaje_abet where evaluacion = ? and Id_COMPETENCIA = ? and asignatura = ?',
                       [r[0], r[2], detalles[4]])
    db.commit()
    flash("Datos guardados")

    # Recarga la pagina de los indicadores
    return redirect(url_for('indicadores', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/<periodo>/<codigo>/<grupo>/grades', methods=['GET', 'POST'])
@login_required
def notas(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select d.nombre, d.codigo, d.grupo, d.periodo, d.id, d.id_carrera, e.nombre_carrera, e.codigo_periodo \
        from asignatura as d, acreditacion_abet as e \
        where d.codigo=? and d.grupo=? and d.periodo=? and d.id_carrera = e.id_carrera and e.periodo=?",
        [codigo, grupo, periodo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los estudiantes
    # cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [detalles[4]])
    estudiantes = []
    p_periodo = detalles[7]
    # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
    urlget = "http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante"
    # periodo="", grupo="",codigo="",urlget=""
    argmnts = [p_periodo, grupo, codigo, urlget]
    estudiantes = get_students("ws", argmnts)
    # estudiantes = get_students("bd",detalles)

    # Elimina estudiantes repetidos que vienen del web service
    i = 0
    while i < len(estudiantes):
        if (i < len(estudiantes) - 1):
            if (estudiantes[i][1] == estudiantes[i + 1][1]):
                del estudiantes[i]
            else:
                i = i + 1
        else:
            break

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select  distinct d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
        order by d.id_evaluacion",
        [detalles[4]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur4 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior, f.descripcion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",
        [detalles[4]])
    porcindicadores = cur4.fetchall()

    # Recupera (de la base de datos) la informacion de las notas de los indicadores ya contenida en la base de datos
    cur5 = db.execute(
        "select evaluacion, competencia, codigo_estudiante, nota from nota_abet where asignatura=? and nivel=3",
        [detalles[4]])
    notasInd = cur5.fetchall()
    cur6 = db.execute(
        "select  distinct d.id_evaluacion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
        order by d.id_evaluacion",
        [detalles[4]])
    supinst = cur6.fetchall()
    supinst = reduce(lambda x, y: x + y, supinst)

    # Procesa los datos de los instrumentos de evaluacion, incluyendo la informacion previamente guardada
    inst = []
    indicadores = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]  # Id evaluacion
        temp1.append(resprog[i])  # Evaluacion
        if i >= len(resprog) - 1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i])  # Las competencias que faltan en la evaluacion que se esta revisando
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
                if (temp2[3] != ''):
                    temp9.append(temp3[l][1] * temp2[3] / 10000)
                else:
                    temp9.append(0)
            temp1[j] = tuple(temp2)

        indicadores.append([temp5, reduce(lambda x, y: x + y, temp6), reduce(lambda x, y: x + y, temp8), temp9])
        inst.append(temp1)

    # Procesa los datos de las notas guardadas previamente
    supinst = list(supinst)
    subcompt = dict([(ind, {}) for ind in supinst])
    for Subind, idinst in zip(indicadores, supinst):
        subcompt[idinst] = Subind[1]
    notas = dict([(ind, {}) for ind in supinst])

    for nota in notas:
        notas[nota] = dict([(e[1], {}) for e in estudiantes])

    for nota in notas:
        for estudiante in notas[nota]:
            notas[nota][estudiante] = dict([(scomp, {}) for scomp in subcompt[nota]])
            # tempnota = nota[0][0]
            # nots = 1
            # for nota in notasInd:
            #   while tempnota =:
            #      pass

            # notas = {}
            #   for i in range(1,len(inst)+1):
            #  notas[i]=dict([(e[1],{}) for e in estudiantes])

    for (x, y, z, w) in notasInd:
        notas[x][z][y] = w  # x es el instrumento, z es el codigo del estudiante, y es la subcompetencia, w es la nota
        # continue
    usuario = session['id_prof'][1] if 'id_prof' in session else session['user']
    power = session['lvl']

    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'estudiantes': estudiantes, 'resprog': inst, 'numinstrumentos': len(inst),
               'numestudiantes': len(estudiantes), 'indicadores': indicadores, 'notas': notas, 'idinst': supinst,
               'usuario': usuario, "permisos": power}
    return render_template('grades.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarNotas', methods=['POST'])
@login_required
def guardarNotas(periodo, codigo, grupo):
    # Accede la base de datos
    global porcentajes_instrumentos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select d.nombre, d.codigo, d.grupo, d.periodo, d.id, e.codigo_periodo from asignatura as d, acreditacion_abet as e \
        where d.codigo=? and d.grupo=? and d.periodo=? and d.id_carrera = e.id_carrera and e.periodo=?",
        [codigo, grupo, periodo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los estudiantes
    # cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre desc", [detalles[4]])
    # estudiantes = cur2.fetchall()
    p_periodo = detalles[5]
    # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
    urlget = "http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante"
    # periodo="", grupo="",codigo="",urlget=""
    argmnts = [p_periodo, grupo, codigo, urlget]
    estudiantes = get_students("ws", argmnts)
    # estudiantes = get_students("bd",detalles)

    # Elimina estudiantes repetidos que vienen del web service
    i = 0
    while i < len(estudiantes):
        if (i < len(estudiantes) - 1):
            if (estudiantes[i][1] == estudiantes[i + 1][1]):
                del estudiantes[i]
            else:
                i = i + 1
        else:
            break

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id \
            and e.asignatura=? order by d.id_evaluacion",
        [detalles[4]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur3 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",
        [detalles[4]])
    porcindicadores = cur3.fetchall()

    cur4 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior, f.descripcion, d.id_evaluacion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",
        [detalles[4]])
    porcentaje_indicadores = cur4.fetchall()
    copia_porcentaje_indicadores = porcentaje_indicadores[:]

    # Recupera (de la base de datos) y procesa los datos de nombre de evaluaciones,
    # y porcentaje de evaluaciones y resultados de programa
    cur5 = db.execute(
        'select d.evaluacion, d.porcentaje, e.competencia, e.porcentaje, d.id_evaluacion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e \
        where d.asignatura = e.asignatura and d.id_evaluacion = e.evaluacion and e.nivel = 1 and d.asignatura=?',
        [detalles[4]])
    instrumentos = []
    for row in cur5.fetchall():
        instrumentos.append(row)

    # Recupera (de la base de datos) el numero de evaluaciones
    cur6 = db.execute("select count(*) from instrumento where asignatura=?", [detalles[4]])
    numevals = cur6.fetchall()

    # Procesa los datos de los indicadores de evaluacion, incluyendo la informacion previamente guardada
    indicadores = []
    pesos = []
    evaluacion = []
    i = 0

    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])  # Temp1 ej: [('Talleres', 31, 'A', 30), ('Talleres', 31, 'J', 70)]

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
            # REVISAR ESTO
            while k < len(copia_porcentaje_indicadores):
                if copia_porcentaje_indicadores[k][0] == temp1[j][0] and copia_porcentaje_indicadores[k][3] == temp1[j][
                    2]:
                    temp2.append([copia_porcentaje_indicadores[k][1], copia_porcentaje_indicadores[k][2]])
                    temp3.append(copia_porcentaje_indicadores[k][1])
                    del copia_porcentaje_indicadores[k]
                else:
                    k = k + 1

            for l in range(len(temp2)):
                if (temp2[l][1] == "" or temp1[j][3] == ""):
                    temp5.append(0)
                else:
                    temp5.append(temp2[l][1] * temp1[j][3] / 10000)
            temp4.append(temp3)

        indicadores.append(reduce(lambda x, y: x + y, temp4))
        pesos.append(temp5)
        evaluacion.append(numero)

    # Recupera de la pagina los datos de las entradas y los procesa
    datos = []
    for i in range(len(indicadores)):
        temp1 = []
        for j in range(len(estudiantes)):
            temp2 = []
            for k in range(len(indicadores[i])):
                if request.form["ind" + str(i + 1) + estudiantes[j][0] + str(k)] == "":
                    temp2.append("0")
                else:
                    temp2.append(request.form["ind" + str(i + 1) + estudiantes[j][0] + str(k)])
            temp1.append(temp2)
        datos.append(temp1)

    # Elimina de la base de datos los registros viejos
    # db.execute('delete from nota_abet where asignatura=?',[detalles[4]])
    # db.execute('delete from nota_instrumento where asignatura=?',[detalles[4]])
    # db.execute('delete from nota_definitiva where asignatura=?',[detalles[4]])
    # db.commit()

    # Procesa e inserta la nueva informacion de indicadores, resultados de programa e instrumentos en la base de datos
    j = 0
    revisados = []
    for el in porcentaje_indicadores:
        i = 0
        for modf in porcentaje_indicadores:
            if el[0] == modf[0] and el[3] == modf[3] and el[1] != modf[1] and (el not in revisados):
                porcentaje_indicadores.insert(j + 1, modf)
                del porcentaje_indicadores[i + 1]
                revisados.append(modf)
            i += 1
        revisados.append(el)
        j += 1

    definitiva_asignatura = []
    m = n = 0

    # Ciclo para los instrumentos (tabs)
    for d in range(len(datos)):
        n = m
        if m < len(porcentaje_indicadores):
            temp1 = porcentaje_indicadores[m][0]  # Nombre evaluacion
        # Ciclo para los estudiantes (filas)
        for e in range(len(datos[d])):
            if datos[d][e] == []:
                continue
            else:
                definitiva_instrumento = 0
                peso_total = 0
                # Procesa e inserta los valores de los indicadores
                for i in range(len(datos[d][e])):
                    if not db.execute(
                            "select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 3 and COMPETENCIA = ? and asignatura = ? and evaluacion = ?",
                            [estudiantes[e][1], indicadores[d][i], detalles[4], evaluacion[d]]).fetchall():
                        db.execute(
                            "insert into nota_abet values (?,?,?,?,?,?)",
                            [detalles[4], evaluacion[d], indicadores[d][i], 3, estudiantes[e][1],
                             float(datos[d][e][i])])
                    else:
                        db.execute(
                            # ASIGNATURA EVALUACION COMPETENCIA NIVEL CODIGO_ESTUDIANTE NOTA
                            "update nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and NIVEL = 3 and competencia = ? and evaluacion = ? ",
                            [float(datos[d][e][i]), detalles[4], estudiantes[e][1], indicadores[d][i], evaluacion[d]])

                    peso_total += pesos[d][i]
                    definitiva_instrumento += (float(datos[d][e][i]) * pesos[d][i])

                definitiva_instrumento = definitiva_instrumento / peso_total

                # Procesa e inserta los valores de los resultados de programa
                m = n
                resultado = 0.0
                o = 0
                if m < len(porcentaje_indicadores):
                    temp2 = porcentaje_indicadores[m][3]  # Es la competencia
                    peso = 0
                    while temp1 == porcentaje_indicadores[m][0]:
                        if temp2 == porcentaje_indicadores[m][3]:
                            if datos[d][e][o] != "0":
                                resultado += float(datos[d][e][o]) * porcentaje_indicadores[m][2] / 100
                                peso = peso + porcentaje_indicadores[m][2]
                            m += 1
                            o += 1
                        else:
                            if not db.execute(
                                    "select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 1 and competencia = ? and asignatura = ? and evaluacion = ?",
                                    [estudiantes[e][1], temp2, detalles[4], evaluacion[d]]).fetchall():
                                db.execute(
                                    "insert or IGNORE into nota_abet values (?,?,?,?,?,?)",
                                    [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1], round(resultado, 2)])
                            else:
                                db.execute(
                                    "update or IGNORE nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and nivel = 1 and competencia = ? and evaluacion = ?",
                                    [round(resultado, 2), detalles[4], estudiantes[e][1], temp2, evaluacion[d]])
                            resultado = 0.0
                            temp2 = porcentaje_indicadores[m][3]
                        if m >= len(porcentaje_indicadores):
                            if not db.execute(
                                    "select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 1 and competencia = ? and asignatura = ? and evaluacion = ?",
                                    [estudiantes[e][1], temp2, detalles[4], evaluacion[d]]).fetchall():
                                db.execute(
                                    "insert or IGNORE into nota_abet values (?,?,?,?,?,?)",
                                    [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1], round(resultado, 2)])
                            else:
                                db.execute(
                                    "update or IGNORE nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and nivel = 1 and competencia = ? and evaluacion = ?",
                                    [round(resultado, 2), detalles[4], estudiantes[e][1], temp2, evaluacion[d]])
                            break

                    if not db.execute(
                            "select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 1 and competencia = ? and asignatura = ? and evaluacion = ?",
                            [estudiantes[e][1], temp2, detalles[4], evaluacion[d]]).fetchall():
                        db.execute(
                            "insert or IGNORE into nota_abet values (?,?,?,?,?,?)",
                            [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1], round(resultado, 2)])
                    else:
                        db.execute(
                            "update or IGNORE nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and nivel = 1 and competencia = ? and evaluacion = ?",
                            [round(resultado, 2), detalles[4], estudiantes[e][1], temp2, evaluacion[d]])

                # Inserta el valor de la nota definitiva de las evaluaciones
                # definitiva_instrumento = (5*(definitiva_instrumento))/100
                if not db.execute(
                        "select CODIGO_ESTUDIANTE from nota_instrumento where CODIGO_ESTUDIANTE = ? and asignatura = ? and EVALUACION = ?",
                        [estudiantes[e][1], detalles[4], evaluacion[d]]).fetchall():
                    db.execute(
                        "insert or IGNORE into nota_instrumento values (?,?,?,?)",
                        [detalles[4], evaluacion[d], estudiantes[e][1], round(definitiva_instrumento, 2)])
                else:
                    db.execute(
                        # ASIGNATURA EVALUACION CODIGO_ESTUDIANTE NOTA
                        "update or IGNORE nota_instrumento set NOTA = ? where asignatura = ? and codigo_estudiante = ? and EVALUACION = ?",
                        [round(definitiva_instrumento, 2), detalles[4], estudiantes[e][1], evaluacion[d]])

                definitiva_asignatura.append([definitiva_instrumento, evaluacion[d], estudiantes[e][1]])
        db.commit()

    # Procesa e inserta la nueva informacion de nota definitiva de una asignatura en la base de datos
    porcentajes_instrumentos = []
    for i in range(0, len(instrumentos), int(len(instrumentos) / numevals[0][0])):
        porcentajes_instrumentos.append(instrumentos[i])
    # definitiva_asignatura = sorted(definitiva_asignatura, key=itemgetter(2))
    j = 0
    for i in range(len(estudiantes)):
        nota_def = 0.0
        est = estudiantes[i][1]
        while est == definitiva_asignatura[j][2]:
            w = j
            for k in porcentajes_instrumentos:
                if k[4] == definitiva_asignatura[w][1]:
                    nota_def += definitiva_asignatura[w][0] * k[1] / 100
                if len(definitiva_asignatura) / (len(estudiantes) + w) > 1:
                    w += len(estudiantes)

            j += 1
            if j >= len(definitiva_asignatura) - 1:
                break

        if not db.execute(
                "select CODIGO_ESTUDIANTE from nota_definitiva where CODIGO_ESTUDIANTE = ? and asignatura = ? ",
                [estudiantes[e][1], detalles[4]]).fetchall():
            db.execute("insert or IGNORE into nota_definitiva values (?,?,?)",
                       [detalles[4], estudiantes[i][1], round(nota_def, 2)])
        else:
            db.execute("update or IGNORE nota_definitiva set NOTA = ? where asignatura = ? and codigo_estudiante = ?",
                       [round(nota_def, 2), detalles[4], estudiantes[i][1]])
        db.commit()
        flash("Datos guardados")

    # Recarga la pagina de los indicadores
    return redirect(url_for('notas', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        if request.form['username'] != "" and request.form['pswd'] != "":
            cur1 = db.execute("select login, clave from usuario")
            detalles = cur1.fetchall()
            usr = (request.form['username'], request.form['pswd'])
            if usr in detalles:
                session['logged_in'] = True
                cur1 = db.execute("select nivel_acceso from usuario where login = ?", [usr[0]])
                lvlacc = cur1.fetchall()
                session['lvl'] = lvlacc[0][0]
                if lvlacc[0][0] == 4:
                    cur2 = db.execute(
                        "select p.id, p.nombre from usuario u inner join profesor p on u.nombre = p.nombre")
                    idprof = cur2.fetchall()[0]
                    session['id_prof'] = idprof
                if lvlacc[0][0] == 1:
                    session['user'] = "Administrador"
                if lvlacc[0][0] == 2:
                    session['user'] = "Moderador"
                return redirect(url_for('show_periods'))
            else:
                error = "Usuario o contrasena incorrectos, intente de nuevo"
        else:
            error = "No ha introducido datos"

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('lvl', None)
    if 'id_prof' in session:
        session.pop('id_prof', None)
    if 'user' in session:
        session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/<periodo>/<codigo>/<grupo>/reporte', methods=['GET', 'POST'])
@login_required
def reporte(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()

    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select a.nombre, a.codigo, a.grupo, a.periodo, a.id, a.id_carrera, e.nombre_carrera, p.nombre, e.codigo_periodo \
        from asignatura as a, profesor as p, acreditacion_abet as e \
        where a.codigo=? and a.grupo=? and a.periodo=? and a.id_profesor = p.id and a.id_carrera = e.id_carrera and e.periodo=?",
        [codigo, grupo, periodo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) la informacion de las notas de los instrumentos ya contenida en la base de datos
    cur2 = db.execute(
        "select codigo_estudiante, nota from nota_definitiva where asignatura=?",
        [detalles[4]])
    notasDef = cur2.fetchall()

    # Halla el numero de estudiantes que ganan y pierden la asignatura
    perder = 0
    perdieron = []
    aprobados = []
    for x in notasDef:
        if x[1] < 3:
            perdieron.append(x[0])
            perder += 1
        else:
            aprobados.append(x[0])

    # Halla las notas maxima y minima
    maxnota = 0
    minnota = 5
    for i in notasDef:
        if i[1] > maxnota:
            maxnota = i[1]
        if i[1] < minnota:
            minnota = i[1]

    # Recupera datos del web service
    p_periodo = detalles[8]
    # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
    urlget = "http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante"
    # periodo="", grupo="",codigo="",urlget=""
    argmnts = [p_periodo, grupo, codigo, urlget]
    estudiantes = get_students("ws", argmnts)
    # estudiantes = get_students("bd",detalles)

    # Elimina estudiantes repetidos que vienen del web service
    i = 0
    while i < len(estudiantes):
        if (i < len(estudiantes) - 1):
            if (estudiantes[i][1] == estudiantes[i + 1][1]):
                del estudiantes[i]
            else:
                i = i + 1
        else:
            break

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje, f.descripcion,d.porcentaje \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
            and f.carrera=? \
        order by d.id_evaluacion",
        [detalles[4], detalles[5]])
    resprog = cur3.fetchall()

    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur4 = db.execute(
        "select distinct d.evaluacion, e.competencia, e.porcentaje, f.descripcion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 1 and d.asignatura=?",
        [detalles[4]])
    porcresultados = cur4.fetchall()

    # Recupera (de la base de datos) la informacion de las notas de los indicadores ya contenida en la base de datos
    cur5 = db.execute(
        "select evaluacion, codigo_estudiante,competencia, nota from nota_abet where asignatura=? and nivel=1",
        [detalles[4]])
    notasInd = cur5.fetchall()

    # Recupera (de la base de datos) y procesa los datos de resultados de programa
    cur6 = db.execute(
        "select d.resultado_de_programa, d.peso, e.descripcion from formula as d, resultado_de_programa as e \
        where asignatura=? and e.id = d.resultado_de_programa and e.carrera=?",
        [detalles[4], detalles[5]])
    formula = cur6.fetchall()

    # Recupera(de la base de datos) la competencia con su descripcion
    cur8 = db.execute(
        "select distinct e.competencia, f.descripcion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
            and f.carrera=? \
        order by d.id_evaluacion",
        [detalles[4], detalles[5]])
    descAK = dict(cur8.fetchall())

    # formula2 = dict(formula)
    numResultados = len(formula)
    resultados = []
    for a, b, c in formula:
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

    # Procesa los datos de las notas de los resultados de programa totales
    cur9 = db.execute(
        "select d.evaluacion, d.competencia, d.codigo_estudiante, d.nota, e.porcentaje \
        from nota_abet as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e\
        where d.asignatura=? and d.nivel=1 and d.evaluacion = e.evaluacion and d.competencia = e.competencia \
        order by d.competencia",
        [detalles[4]])
    temp1 = cur9.fetchall()

    sumaResultados = dict(zip(resultados, [0] * len(resultados)))
    for i in resultados:
        cur10 = db.execute(
            "select e.evaluacion, dsak.competencia, e.porcentaje \
            from porcentaje_abet as e inner join Descripcion_A_K as dsak on e.Id_COMPETENCIA = dsak.competencia \
            where asignatura=? and dsak.competencia=? \
            order by competencia",
            [detalles[4], i])
        temp2 = cur10.fetchall()
        suma = 0
        for j, k, l in temp2:
            if (l != ""):
                suma += l
        sumaResultados[i] = suma
    resultadosTotales = dict([(e[1], {}) for e in estudiantes])
    resultadosTotalesaprob = dict([(e, {}) for e in aprobados])
    for e in estudiantes:
        resultadosTotales[e[1]] = dict(zip(resultados, [0] * len(resultados)))
    for e in aprobados:
        resultadosTotalesaprob[e] = dict(zip(resultados, [0] * len(resultados)))
    for (a, b, c, d, e) in temp1:
        if (d == "" or e == ""):
            resultadosTotales[c][b] = round(resultadosTotales[c][b], 2)
        else:
            resultadosTotales[c][b] = round(resultadosTotales[c][b] + (d * e / sumaResultados[b]), 2)
        if c in aprobados:
            if (d == "" or e == ""):
                resultadosTotalesaprob[c][b] = round(resultadosTotalesaprob[c][b], 2)
            else:
                resultadosTotalesaprob[c][b] = round(resultadosTotalesaprob[c][b] + (d * e / sumaResultados[b]), 2)

    for est in resultadosTotales:
        for compt in resultadosTotales[est]:
            resultadosTotales[est][compt] = round(resultadosTotales[est][compt], 2)
            if est in aprobados:
                resultadosTotalesaprob[est][compt] = round(resultadosTotalesaprob[est][compt], 2)

    # Procesa los datos de las notas definitivas guardadas previamente
    notasDefinitivas = dict([(e[1], 0) for e in estudiantes])
    for (x, y) in notasDef:
        notasDefinitivas[x] = round(y, 1)
    comptorg = list(resultadosTotales[estudiantes[0][1]].keys())
    comptorg.sort()
    competencias = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    promgeneralind = dict([(c, 0) for c in competencias])
    promgeneralindaprob = dict([(c, 0) for c in competencias])
    notascompt = dict([(c, []) for c in competencias])
    desviacion = dict([(c, 0) for c in competencias])
    desvmed = dict([(c, 0) for c in competencias])
    minimo = dict([(c, 0) for c in competencias])
    maximo = dict([(c, 0) for c in competencias])
    aprueban = dict([(c, 0) for c in competencias])

    for estud in resultadosTotales:
        for compt in promgeneralind:
            if compt in resultadosTotales[estud]:
                notascompt[compt].append(resultadosTotales[estud][compt])
                promgeneralind[compt] += resultadosTotales[estud][compt]
            else:
                notascompt[compt].append(0)
            if estud in aprobados:
                if compt in resultadosTotalesaprob[estud]:
                    promgeneralindaprob[compt] += resultadosTotalesaprob[estud][compt]

    lowest = [['A', 'desc', 5], ['C', 'desc', 5]]
    high = ['A', 'desc', 0]

    for compt in promgeneralind:
        promgeneralind[compt] = round(promgeneralind[compt] / len(estudiantes), 2)
        if promgeneralind[compt] < lowest[1][2] and promgeneralind[compt] > 0:
            if promgeneralind[compt] < lowest[0][2]:
                lowest[1][0] = lowest[0][0]
                lowest[1][2] = lowest[0][2]
                lowest[0][0] = compt
                lowest[0][2] = promgeneralind[compt]
            else:
                lowest[1][0] = compt
                lowest[1][2] = promgeneralind[compt]
        if promgeneralind[compt] > high[2]:
            high[0] = compt
            high[2] = promgeneralind[compt]
        if len(aprobados) > 0:
            promgeneralindaprob[compt] = round(promgeneralindaprob[compt] / len(aprobados), 2)
        else:
            promgeneralindaprob[compt] = 0

    for nota in notascompt:
        desviacion[nota] = round(statistics.stdev(notascompt[nota], promgeneralind[compt]), 2)
        if desviacion[nota] > 0 and promgeneralind[nota] != 0:
            desvmed[nota] = round(desviacion[nota] / promgeneralind[nota], 2)
        minimo[nota] = min(notascompt[nota])
        maximo[nota] = max(notascompt[nota])
        for notas in notascompt[nota]:
            if notas > 3:
                aprueban[nota] += 1
    for nota in aprueban:
        aprueban[nota] = round(aprueban[nota] / len(estudiantes), 2)
        aprueban[nota] = int(aprueban[nota]) * 100
        # for estud in resultadosTotales:
        #    for compt in promgeneralind:
        #        if compt in resultadosTotales[estud]:
        #            desviacion[compt] += resultadosTotales[estud][compt] - promgeneralind[compt]

    lowest[0][1] = descAK[lowest[0][0]]
    lowest[1][1] = descAK[lowest[1][0]]
    high[1] = descAK[high[0]]
    instss = []
    # [ ins[0] for ins in resprog if not (ins[0] in instss]
    [instss.append(item[0]) for item in resprog if item[0] not in instss]
    inssts = dict([(i, 0) for i in instss])
    insxcompt = dict([(i, 0) for i in instss])
    promins = dict([(c, []) for c in competencias])
    for ins in insxcompt:
        insxcompt[ins] = dict([(c, 0) for c in competencias])
    for (a, b, c, d, e, f) in resprog:
        insxcompt[a][c] = d
        promins[c].append(d)
        inssts[a] = f

    # Se actualiza el diccionario para no tener resultados de programa vacios en instrumentos
    for ins in promins:
        for a in range(len(promins[ins])):
            if (promins[ins][a] == ''):
                promins[ins][a] = 0

    # Halla el porcentaje evaluado en cada resultado de programa
    sumaTotal = 0
    for ins in promins:
        for a in promins[ins]:
            sumaTotal += a
    for ins in promins:
        if promins[ins]:
            print(promins[ins])
            if len(promins[ins]) < len(instss):
                [promins[ins].append(0) for i in range(len(instss) - len(promins[ins]))]
            #promins[ins] = round(statistics.mean(promins[ins]), 2)
            sumaTemp = 0
            for a in promins[ins]:
                sumaTemp += a
            promins[ins] = 100 * sumaTemp / sumaTotal
        else:
            promins[ins] = 0

    print("*********************************")
    print(promins)
    print("*********************************")

    cur12 = db.execute(
        "select distinct periodo from acreditacion_abet order by periodo asc"
    )
    periodos = cur12.fetchall()
    pastper = 0
    for per in periodos:
        if per[0] == periodo:
            break
        pastper += 1
    load = 0
    reporteg = 1
    dirar = 'reportes/' + str(periodos[pastper][0]) + str(codigo) + str(grupo)
    if path.isfile(dirar + ".json"):
        dirar = 'reportes/' + str(periodos[pastper][0]) + str(codigo) + str(grupo)
    else:
        dirar = 'reportes/' + str(periodo) + str(codigo) + str(grupo)
    if path.isfile(str(dirar) + ".json"):
        with open(str(dirar) + ".json") as reportef:
            reporteg = json.load(reportef)
            load = 1
    formm = dict([(c, 0) for c in competencias])
    for com in formula:
        formm[com[0]] = com[1]
    entries = dict()
    # if load == 0:
    #    entries = {'detalles': detalles, 'perder': perder, 'maxnota': maxnota[1],'minnota': minnota[1], 'promgeneralind':promgeneralind, 'promgeneralindaprob':promgeneralindaprob, 'estud':len(estudiantes), 'ordcompt': competencias, 'high':high, 'lowest':lowest, 'instrumentos':instss,'desviacion':desviacion,'minimo':minimo, 'maximo':maximo,'aprueban':aprueban,'inspor':inssts,'inscompt':insxcompt, 'promins':promins, 'load':load,'formm':formm}
    # else:
    #    entries = {'detalles': detalles, 'perder': perder, 'maxnota': maxnota[1],'minnota': minnota[1], 'promgeneralind':promgeneralind, 'promgeneralindaprob':promgeneralindaprob, 'estud':len(estudiantes), 'ordcompt': competencias, 'high':high, 'lowest':lowest, 'instrumentos':instss,'desviacion':desviacion,'minimo':minimo, 'maximo':maximo,'aprueban':aprueban,'inspor':inssts,'inscompt':insxcompt, 'promins':promins, 'load':load,'formm':formm,'store':reporteg}
    entries = {'detalles': detalles, 'perder': perder, 'maxnota': maxnota, 'minnota': minnota,
               'promgeneralind': promgeneralind, 'promgeneralindaprob': promgeneralindaprob, 'estud': len(estudiantes),
               'ordcompt': competencias, 'high': high, 'lowest': lowest, 'instrumentos': instss,
               'desviacion': desviacion, 'minimo': minimo, 'maximo': maximo, 'aprueban': aprueban, 'inspor': inssts,
               'inscompt': insxcompt, 'promins': promins, 'load': load, 'formm': formm, 'store': reporteg}
    entries['sestud'] = estudiantes
    entries['comres'] = resultadosTotales
    entries['notdef'] = notasDefinitivas
    entries['devmed'] = desvmed
    entries['nomexcel'] = str(periodo) + str(codigo) + str(grupo) + '.xlsx'
    entries['nompdf'] = str(periodo) + str(codigo) + str(grupo) + '.pdf'
    excel = NotasExcel(periodo, codigo, grupo, entries)
    reportepdf(periodo, codigo, grupo, entries)
    send_from_directory(path.join(app.root_path, app.config['PDF']), entries['nompdf'])
    # ,url_for('reporte', periodo=entries['detalles'][3], codigo=entries['detalles'][1], grupo=entries['detalles'][2])

    return render_template('report.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarPeriodo', methods=['POST'])
@login_required
def guardarReporte(periodo, codigo, grupo):
    # Accede la base de datos
    db = get_db()
    filename = 'reportes/' + str(periodo) + str(codigo) + str(grupo) + ".json"
    data = {"1comments1": request.form["1comments1"], "1comments2": request.form["1comments2"],
            "1comments3": request.form["1comments3"],
            "2comments1": request.form["2comments1"], "3comments1": request.form["3comments1"],
            "3comments2": request.form["3comments2"],
            "3comments3": request.form["3comments3"], "3comments4": request.form["3comments4"],
            "3comments5": request.form["3comments5"],
            "3comments6": request.form["3comments6"], "4comments1": request.form["4comments1"],
            "4comments2": request.form["4comments2"],
            "4comments3": request.form["4comments3"], "5comments1": request.form["5comments1"],
            "5comments2": request.form["5comments2"],
            "5comments3": request.form["5comments3"], "5comments4": request.form["5comments4"],
            "5comments5": request.form["5comments5"],
            "6comments1": request.form["6comments1"]}

    cur1 = db.execute(
        "select a.nombre, a.codigo, a.grupo, a.periodo, a.id, a.id_carrera, e.nombre_carrera, p.nombre \
        from asignatura as a, profesor as p, acreditacion_abet as e \
        where a.codigo=? and a.grupo=? and a.periodo=? and a.id_profesor = p.id and a.id_carrera = e.id_carrera",
        [codigo, grupo, periodo])
    detalles = cur1.fetchall()[0]

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur2 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje, f.descripcion,d.porcentaje \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id and e.asignatura=? \
            and f.carrera=? \
        order by d.id_evaluacion",
        [detalles[4], detalles[5]])
    resprog = cur2.fetchall()
    instss = []
    [instss.append(item[0]) for item in resprog if item[0] not in instss]
    for ints in instss:
        data[ints] = request.form[ints]
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

    # Recarga la pagina del reporte
    return redirect(url_for('reporte', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/excel/<path:filename>', methods=['GET', 'POST'])
def downloadexcel(filename):
    uploads = path.join(app.root_path, app.config['EXCEL'])
    return send_from_directory(uploads, filename)


@app.route('/pdf/<path:filename>', methods=['GET', 'POST'])
def downloadpdf(filename):
    uploads = path.join(app.root_path, app.config['PDF'])
    return send_from_directory(uploads, filename)


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'initdb':
        init_db()
    app.run(host='0.0.0.0')
