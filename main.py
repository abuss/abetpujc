# Sistema de evaluacion ABET
# Librerias
from __future__ import division
import sqlite3
from contextlib import closing


from flask import Flask, request, g, redirect, url_for, \
    render_template, flash, session
import flask
import requests
from functools import wraps, reduce 
from operator import itemgetter
import sys
from flask import json

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
#class flask.ext.login.LoginManager(app=app, add_context_processor=True)

         
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
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def get_students(src,args):
     #   print x
     #periodo="", grupo="",codigo="",urlget=""
    if src == "ws":    

        estudiantes = []
        p_periodo = args[0]
        group = args[1]
        proof = {'pCurso': args[2], 'pGrupo' : group, 'pPeriodo' : p_periodo }
        # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
        r = requests.get(args[3], params=proof)
        
        proofjson =r.json()
        for x in proofjson:
            #print (x)
            estudiante = [x['nombre'].capitalize(),int(x['emplid'])]
            estudiantes.append(estudiante)

        for e in estudiantes:
            nombre = e[0].rsplit(' ')
            if len(nombre) >3 :
                temp1 = nombre[0].capitalize()
                temp2 = nombre[1].capitalize()
                nombre[0] = nombre[2].capitalize()
                nombre[1] = nombre[3].capitalize()
                nombre[2] = temp1
                nombre[3] = temp2
            else:
                temp1 = nombre[0].capitalize()
                nombre[0] = nombre[1].capitalize()
                nombre[1] = nombre[2].capitalize()
                nombre[2] = temp1
            e[0] = reduce(lambda x,y:x+' '+y, nombre)
        estudiantes.sort()
        return estudiantes
    elif src == "bd":
        db = get_db()
        cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [args[4]])
        estudiantes = cur2.fetchall()
        #for x in estudiantes:
         #   print (x)
        return estudiantes
    else:
        print("No hay procedimiento para la fuente: ", src)

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
    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los periodos
    cur1 = db.execute(
        "select distinct periodo from acreditacion_abet order by periodo asc"
        )
    periodos = cur1.fetchall()
    per = 1
    if len(periodos) == 0:
        per = 0

    #print(periodos)

    # Agrupa los datos recuperados en una sola lista y la retorna a la pagina web
    entries = {'periodos': periodos, 'hayperiodos': per}
 
    
    

    return render_template('periods.html', entries=entries)

@app.route('/<periodo>',methods=['GET', 'POST'])
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
    if session['lvl'] == 4 :
        cur2 = db.execute(
        "select nombre, codigo, grupo, periodo, id_carrera from asignatura where periodo=? and id_profesor=? order by nombre asc",
        [periodo,session['id_prof'][0][0]])
    else:
        cur2 = db.execute(
        "select nombre, codigo, grupo, periodo, id_carrera from asignatura where periodo=? order by nombre asc",
        [periodo])
    cursos = [dict(title=row[0], cod=row[1], grupo=row[2], periodo=row[3], carrera=row[4]) for row in cur2.fetchall()]

    vacio = 0
    # Agrupa los datos recuperados en una sola lista y la retorna a la pagina web  
    entries = {'carreras': carreras, 'cursos': cursos, 'vacio' : vacio }

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


    # Recupera los estudiantes
    #cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [detalles[4]])
    #estudiantes = cur2.fetchall()
    #for x in estudiantes:
    #   print (x)
    p_periodo = "0940"
    # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
    urlget ="http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante"
     #periodo="", grupo="",codigo="",urlget=""
    #argmnts = [p_periodo,grupo,codigo,geturl]
    #estudiantes = get_students("ws",argmnts)
    estudiantes = get_students("bd",detalles)

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
        "select evaluacion, codigo_estudiante,competencia, nota from nota_abet where asignatura=? and nivel=1",
        [detalles[4]])
    notasInd = cur5.fetchall()
    #print(notasInd)
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
    supinst = []
    for com in resprog:
        if com[1] not in supinst:
            supinst.append(com[1])
    compt = dict([(ind,{}) for ind in supinst])
    tempcompt = []
    idtemp = resprog[0][1]
    for com in resprog:
        if idtemp == com[1]:
            tempcompt.append(com[2])
        else:
            compt[idtemp]=tempcompt
            idtemp = com[1]
            tempcompt = [com[2]]
    compt[supinst[len(supinst)-1]] =tempcompt
    #print('competencias',compt)

    #supinst = list(supinst)
    #print(supinst)
    notasIndicadores = dict([(ind,{}) for ind in supinst])

    for nota in notasIndicadores:
        notasIndicadores[nota] = dict( [(e[1],{}) for e in estudiantes])

    for nota in notasIndicadores:
        for estudiante in notasIndicadores[nota]:
            notasIndicadores[nota][estudiante] = dict( [(comp,{}) for comp in compt[nota]] )
            #print(nota,notasIndicadores[nota][estudiante])

    #notasIndicadores = {}
    #for i in range(1,len(inst)+1):
        #notasIndicadores[i]=dict([(e[1],{}) for e in estudiantes])
    #print("notasInd",notasInd)
    for (x,y,z,w) in notasInd:
        #print("x= ",x," z= ",z ," y= ",y," w= ",w)
        notasIndicadores[x][y][z] = round(w,1)

    #print("not",notasIndicadores)
    #for x in notasIndicadores:
     #   print(x,notasIndicadores[x])
      #  print("\n\n")
    # Procesa los datos de las notas de los instrumentos guardadas previamente
    notasInstrumentos = dict([(ind,{}) for ind in supinst])

    for nota in notasInstrumentos:
        notasInstrumentos[nota] = dict( [(e[1],{}) for e in estudiantes])

    #notasInstrumentos = {}
   # for i in range(1,len(inst)+1):
       # notasInstrumentos[i]=dict([(e[1],{}) for e in estudiantes])

    #print (notasInstrumentos)
   # print(notasIns)
    for (x,y,z) in notasIns:
        notasInstrumentos[x][y] = round(z,1)
   

    # Procesa los datos de las notas de los resultados de programa totales
    cur9 = db.execute(
        "select d.evaluacion, d.competencia, d.codigo_estudiante, d.nota, e.porcentaje \
        from nota_abet as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e\
        where d.asignatura=? and d.nivel=1 and d.evaluacion = e.evaluacion and d.competencia = e.competencia \
        order by d.competencia",
        [detalles[4]])
    temp1 = cur9.fetchall()
    sumaResultados = dict(zip(resultados,[0]*len(resultados)))
    for i in resultados:
        cur10 = db.execute(
            "select e.evaluacion, dsak.competencia, e.porcentaje \
            from porcentaje_abet as e inner join Descripcion_A_K as dsak on e.Id_COMPETENCIA = dsak.competencia \
            where asignatura=? and dsak.competencia=? \
            order by competencia",
            [detalles[4],i])
        temp2 = cur10.fetchall()
        suma = 0
        for j,k,l in temp2:
            suma += l
        sumaResultados[i] = suma
    resultadosTotales = dict( [(e[1],{}) for e in estudiantes])
    for e in estudiantes:
        resultadosTotales[e[1]] = dict(zip(resultados,[0]*len(resultados)))
    #print (resultadosTotales)
    for (a,b,c,d,e) in temp1:
        resultadosTotales[c][b] = round(resultadosTotales[c][b]+(d*e/sumaResultados[b]),2)
        #print("calc res total",a,b,c,d,e,"ops",resultadosTotales[c][b],((round(d*e,2))/sumaResultados[b]),round(d*e,2),sumaResultados[b])
    #print(temp1)

    for est in resultadosTotales:
        for compt in resultadosTotales[est]:
            resultadosTotales[est][compt] = round(resultadosTotales[est][compt],1)
    # Procesa los datos de las notas definitivas guardadas previamente
    notasDefinitivas = dict([(e[1],0) for e in estudiantes])
    for (x,y) in notasDef:
        notasDefinitivas[x] = round(y,1)

    #print "URL: ", r.url
    #print "ContenteCurso: ",r.content
    #print  proofjson.__sizeof__()
    #print "Last Element: ",proofjson.__getitem__(7)
    #print len(proofjson)
    #print dir(proofjson.__getitem__(1).values())
    #print dir(proofjson)

    # for i in estudiantes:
    #     print (i)
    # print (len(inst))

    ################################################################################################
    comptorg = list(resultadosTotales[estudiantes[0][1]].keys())
    comptorg.sort()
    """for k in estudiantes: 
        for j in notasIndicadores[supinst[0]].keys(): 
            if j == k[1]: 
                print(k[0],j)
        for j in comptorg: 
            print(resultadosTotales[k[1]][j],j,k[1])
            #print(notasDefinitivas[k[1]])"""
    #print(notasIndicadores[11])
    #print(supinst[0])
    #print(notasIndicadores[supinst[0]].keys())
    #print(resultadosTotales)
                          
    ################################################################################################
    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'estudiantes': estudiantes, 'resprog': inst, 'numinstrumentos': len(inst),
               'numestudiantes': len(estudiantes), 'notasIndicadores': notasIndicadores, 'conteo': conteo,
               'formula': formula, 'notasInstrumentos': notasInstrumentos, 'notasDefinitivas': notasDefinitivas,
               'resultadosTotales': resultadosTotales, 'periodo': periodo, 'idinst': supinst, 'idcompt':comptorg}
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
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e\
        where e.asignatura = d.asignatura and d.id_evaluacion = e.evaluacion and e.nivel = 1 and d.asignatura=?',
        [detalles[4]]
        )
    evaluaciones = []
    for row in cur3.fetchall():
        evaluaciones.append(row)

    # Recupera (de la base de datos) el numero de evaluaciones
    cur4 = db.execute("select count(*) from instrumento where asignatura=?", [detalles[4]])
    numevals = cur4.fetchall()
    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'resprog': formula, 'suma': suma, 'numevals': numevals[0][0],
               'evaluaciones': evaluaciones, 'conteo': conteo}
    return render_template('defcourse.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarPesosEvaluaciones', methods=['POST'])
@login_required
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

    #print(datos1)
    #print(datos2)
    # Validacion antes de insertar: si el instrumento ya existe no se puede ingresar
    # Si no hay datos repetidos que no pueden ser guardados
    if request.form['hayRepetidos'] == '0':
        # Inserta la nueva informacion en la base de datos
        for i in range(1, int(numero) - 3):
            if not db.execute("select asignatura from instrumento where asignatura = ? and evaluacion = ? ",[detalles[4], datos1[i - 1][0]]).fetchall() :
                db.execute('insert or IGNORE into instrumento (asignatura, evaluacion, porcentaje) values (?,?,?)',
                       [detalles[4], datos1[i - 1][0], datos1[i - 1][1]])
                db.commit()
                cur = db.execute('select id_evaluacion from instrumento where evaluacion=? and asignatura=?',
                             [datos1[i - 1][0], detalles[4]])
                numeroEval = cur.fetchall()
                for j in range(len(resultados)):
                    #NEED FIX HERE!(ASK)
                    idnxt = db.execute('select max(Id) from porcentaje_abet')
                    nxtid = idnxt.fetchall();
                    #insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
                    db.execute('insert or IGNORE into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (?,?,?,?,?)',
                           [detalles[4], numeroEval[0][0], resultados[j][0], datos2[i - 1][j], int(nxtid[0][0])+1])
                    db.commit()
            else:
                db.execute('UPDATE or IGNORE instrumento set porcentaje = ? where asignatura =? and evaluacion = ?',
                       [datos1[i - 1][1],detalles[4], datos1[i - 1][0]])
                db.commit()
                cur = db.execute('select id_evaluacion from instrumento where evaluacion=? and asignatura=?',
                             [datos1[i - 1][0], detalles[4]])
                numeroEval = cur.fetchall()
                for j in range(len(resultados)):
                    #NEED FIX HERE!(ASK)
                    if not db.execute("select asignatura from porcentaje_abet where asignatura = ? and evaluacion = ? and Id_COMPETENCIA = ?",[detalles[4], numeroEval[0][0], resultados[j][0]]).fetchall() :
                        idnxt = db.execute('select max(Id) from porcentaje_abet')
                        nxtid = idnxt.fetchall();
                        #insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
                        db.execute('INSERT or IGNORE into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (?,?,?,?,?)',
                            [detalles[4], numeroEval[0][0], resultados[j][0], datos2[i - 1][j], int(nxtid[0][0])+1])
                        db.commit()
                    else:
                        db.execute('UPDATE or IGNORE porcentaje_abet set porcentaje = ? where asignatura =? and evaluacion = ? and Id_COMPETENCIA = ?',
                       [datos2[i - 1][j],detalles[4], numeroEval[0][0], resultados[j][0]])
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
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",[detalles[4]])
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
@login_required
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
    #print(temp)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            numero = int(request.form['numeroDeFilas' + str(temp[i][j][0]) + str(temp[i][j][2])])
            for k in range(numero - 2):
                datos.append((temp[i][j][0], temp[i][j][2],
                              request.form["indicador" + str(temp[i][j][0]) + str(temp[i][j][2]) + str(k)][:5],
                              request.form["pesoind" + str(temp[i][j][0]) + str(temp[i][j][2]) + str(k)]))
                

   
    
    # Inserta la nueva informacion en la base de datos
    for d in datos:
        if d[2] != '---':
            #insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
            #insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values() insert into porcentaje_abet values
            idnxt = db.execute('select max(Id) from porcentaje_abet')
            nxtid = idnxt.fetchall()
            db.execute('INSERT OR IGNORE  into Descripcion_A_K values (?,?,?)',[ d[2], d[1],3])
            db.execute('INSERT or IGNORE into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (?,?,?,?,?)',
                       [detalles[4], d[0], d[2], int(d[3]),nxtid[0][0]])
            db.execute('UPDATE or IGNORE porcentaje_abet SET PORCENTAJE = ? where ASIGNATURA = ? and EVALUACION = ? and Id_COMPETENCIA = ? and Id = ?',
                       [int(d[3]), detalles[4], d[0], d[2], nxtid[0][0]])
    curmagico = db.execute('select e.evaluacion, e.superior ,e.Id_COMPETENCIA , cast(e.PORCENTAJE as text)   from (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e  where e.nivel = 3 and e.asignatura=?',[detalles[4]])
    registrados = curmagico.fetchall()
    for r in registrados:
        if r not in datos:
            db.execute('DELETE from porcentaje_abet where evaluacion = ? and Id_COMPETENCIA = ? and asignatura = ?',[r[0],r[2],detalles[4]])
    db.commit()
    # Recarga la pagina de los indicadores
    return redirect(url_for('indicadores', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/<periodo>/<codigo>/<grupo>/grades', methods=['GET', 'POST'])
@login_required
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
    # cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre asc", [detalles[4]])
    estudiantes = []
    p_periodo = "0940"
    #proof = {'pCurso': codigo, 'pGrupo' : grupo, 'pPeriodo' : p_periodo }
    geturl = "http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante"
     #periodo="", grupo="",codigo="",urlget=""
    #argmnts = [p_periodo,grupo,codigo,geturl]
    #estudiantes = get_students("ws",argmnts)
    estudiantes = get_students("bd",detalles)

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
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",[detalles[4]])
    porcindicadores = cur4.fetchall()
    #print(porcindicadores)
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
    supinst = reduce(lambda x,y:x+y, supinst)
    #print(supinst)
    #print("notasInd",notasInd)
   # print("resprog",resprog)
    # Procesa los datos de los instrumentos de evaluacion, incluyendo la informacion previamente guardada
    inst = []
    indicadores = []
    i = 0
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1] #Id evaluacion
        temp1.append(resprog[i]) #Evaluacion 
        if i >= len(resprog) - 1:
            break
        i = i + 1
        while numero == resprog[i][1]:
            temp1.append(resprog[i]) #Las competencias que faltan en la evaluacion que se esta revisando
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
    #print("indicadores",indicadores)
    #print("inst",inst)
    # Procesa los datos de las notas guardadas previamente
    #print("notas ind",notasInd)#id,competencia,codigo,nota
#[(e[1],{}) for e in estudiantes]
    supinst = list(supinst)
    subcompt = dict([(ind,{}) for ind in supinst])
    for Subind,idinst in zip(indicadores,supinst):
        subcompt[idinst]=Subind[1]
        #print(Subind)
    #print(subcompt)
    notas = dict([(ind,{}) for ind in supinst])

    for nota in notas:
        notas[nota] = dict( [(e[1],{}) for e in estudiantes])

    for nota in notas:
        for estudiante in notas[nota]:
            notas[nota][estudiante] = dict( [(scomp,{}) for scomp in subcompt[nota]] )
    #print(notas)
        
    #print("notas",notas)
    #tempnota = nota[0][0]
    #nots = 1
    #for nota in notasInd:
     #   while tempnota =:
      #      pass


    #notas = {}
 #   for i in range(1,len(inst)+1):
      #  notas[i]=dict([(e[1],{}) for e in estudiantes])

    for (x,y,z,w) in notasInd:
        notas[x][z][y] = w #x es el instrumento, z es el codigo del estudiante, y es la subcompetencia, w es la nota
        #continue
        #print("x= ",x," z= ",z ," y= ",y," w= ",w)
    #print(notas)
    # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
    entries = {'detalles': detalles, 'estudiantes': estudiantes, 'resprog': inst, 'numinstrumentos': len(inst),
               'numestudiantes': len(estudiantes), 'indicadores': indicadores, 'notas': notas, 'idinst' : supinst}
    return render_template('grades.html', entries=entries)


@app.route('/<periodo>/<codigo>/<grupo>/guardarNotas', methods=['POST'])
@login_required
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
    #cur2 = db.execute("select nombre, codigo from estudiante where asignatura=? order by nombre desc", [detalles[4]])
    #estudiantes = cur2.fetchall()
    p_periodo = "0940"
    # http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/definicionNotas?pCurso=300CSP011&pGrupo=A&pPeriodo=0930
    geturl = "http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante"
     #periodo="", grupo="",codigo="",urlget=""
    #argmnts = [p_periodo,grupo,codigo,geturl]
    #estudiantes = get_students("ws",argmnts)
    estudiantes = get_students("bd",detalles)

    # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
    cur3 = db.execute(
        "select d.evaluacion, d.id_evaluacion, e.competencia, e.porcentaje \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, resultado_de_programa as f \
        where e.porcentaje > 0 and d.id_evaluacion = e.evaluacion and e.competencia = f.id \
            and e.asignatura=? order by d.id_evaluacion",
        [detalles[4]])
    resprog = cur3.fetchall()
    #print("resprog",resprog)
    # Recupera (de la base de datos) la informacion de las evaluaciones ya contenida en la base de datos
    cur3 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",[detalles[4]])
    porcindicadores = cur3.fetchall()
    #print(porcindicadores)
    cur4 = db.execute(
        "select d.evaluacion, e.competencia, e.porcentaje, e.superior, f.descripcion, d.id_evaluacion \
        from instrumento as d, (select * from porcentaje_abet as pa inner join Descripcion_A_K as dsak on pa.Id_COMPETENCIA = dsak.competencia) as e, indicador_de_desempeno as f \
        where d.id_evaluacion = e.evaluacion and f.id = e.competencia and e.nivel = 3 and d.asignatura = ?",[detalles[4]])
    porcentaje_indicadores = cur4.fetchall()
    copia_porcentaje_indicadores = porcentaje_indicadores[:]
    #print("porcentaje_indicadores",porcentaje_indicadores)
    #print("IND1: ", porcentaje_indicadores, "\n\n\nCOPIA", copia_porcentaje_indicadores, "IGUAL?", porcentaje_indicadores == copia_porcentaje_indicadores)
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

    #print(instrumentos)
    # Recupera (de la base de datos) el numero de evaluaciones
    cur6 = db.execute("select count(*) from instrumento where asignatura=?", [detalles[4]])
    numevals = cur6.fetchall()
    # Procesa los datos de los indicadores de evaluacion, incluyendo la informacion previamente guardada
    indicadores = []
    pesos = []
    evaluacion = []
    i = 0
    #print(resprog)
    #print("copia_porcentaje_indicadores", copia_porcentaje_indicadores)
    while i < len(resprog):
        temp1 = []
        numero = resprog[i][1]
        temp1.append(resprog[i])#Temp1 ej: [('Talleres', 31, 'A', 30), ('Talleres', 31, 'J', 70)]

        if i >= len(resprog) - 1:
            break
        i += 1
        
        while numero == resprog[i][1]:
            temp1.append(resprog[i])
            #print(resprog[i])
            if i >= len(resprog) - 1:
                break
            i += 1
        #print("temp1",temp1)
        temp4 = []
        temp5 = []
        for j in range(len(temp1)):
            temp2 = []
            temp3 = []
            k = 0
            #REVISAR ESTO
            while k < len(copia_porcentaje_indicadores):
                if copia_porcentaje_indicadores[k][0] == temp1[j][0] and copia_porcentaje_indicadores[k][3] == temp1[j][2]:
                    temp2.append([copia_porcentaje_indicadores[k][1], copia_porcentaje_indicadores[k][2]])
                    temp3.append(copia_porcentaje_indicadores[k][1])
                    #print("COSAS",[copia_porcentaje_indicadores[k][1], copia_porcentaje_indicadores[k][2]])
                    del copia_porcentaje_indicadores[k]
                else:
                    k = k + 1
            
            for l in range(len(temp2)):
                #print("pesos calc",temp2[l][1],"*",temp1[j][3],"/",10000,"=",temp2[l][1]*temp1[j][3]/10000)
                temp5.append(temp2[l][1]*temp1[j][3]/10000)
            temp4.append(temp3)

        #print(temp4,"reduce",reduce(lambda x, y: x + y, temp4))
        indicadores.append(reduce(lambda x, y: x + y, temp4))
        #print("MAGIC: ",reduce(lambda x, y: x + y, temp4))
        pesos.append(temp5)
        evaluacion.append(numero)
        #print(indicadores, pesos, evaluacion)

    #print ("INDICADORES: ",indicadores)
    #print ("pesos: ",pesos)
    #print ("Evaluacion: ",evaluacion)
    # Recupera de la pagina los datos de las entradas y los procesa
    datos = []
    #print(request.form)
    #print("ind:", indicadores)
    for i in range(len(indicadores)):
        temp1 = []
        for j in range(len(estudiantes)):
            temp2 = []
            for k in range(len(indicadores[i])):
                #print("ind" + str(j+1) + str(estudiantes[i][0]) + str(k))
                if request.form["ind" + str(i+1) + str(estudiantes[j][0]) + str(k)] == "" :
                    temp2.append("0")
                else:    
                    temp2.append(request.form["ind" + str(i+1) + str(estudiantes[j][0]) + str(k)])
                    #print("request form",str(estudiantes[j][0]),request.form["ind" + str(i+1) + str(estudiantes[j][0]) + str(k)])
            temp1.append(temp2)
        datos.append(temp1)
    #print("datos",datos)
    # Elimina de la base de datos los registros viejos
   # db.execute('delete from nota_abet where asignatura=?',[detalles[4]])
    #db.execute('delete from nota_instrumento where asignatura=?',[detalles[4]])
    #db.execute('delete from nota_definitiva where asignatura=?',[detalles[4]])
    #db.commit()
    #print(db.execute('select * from nota_abet where asignatura=?',[detalles[4]]).fetchall())
    # Procesa e inserta la nueva informacion de indicadores, resultados de programa e instrumentos en la base de datos
    # for x in porcentaje_indicadores:
    #     print(x[0],x[1])
    j = 0

    revisados = []
    for el in porcentaje_indicadores:
        i = 0
        for modf in porcentaje_indicadores:
            if el[0] == modf[0] and el[3] == modf[3] and el[1] != modf[1] and (el not in revisados):
                porcentaje_indicadores.insert(j+1,modf)
                del porcentaje_indicadores[i+1]
                revisados.append(modf)
            i+=1
        revisados.append(el)
        j+=1
    
   # print("despues\n")
    #for x in porcentaje_indicadores:
     #   print(x[0],x[1])
    #print(copia_porcentaje_indicadores.sort() == porcentaje_indicadores.sort())


    definitiva_asignatura = []
    m = n = 0
    # Ciclo para los instrumentos (tabs)
    for d in range(len(datos)):
        n = m
        if m < len(porcentaje_indicadores):
            temp1 = porcentaje_indicadores[m][0] #Nombre evaluacion
        # Ciclo para los estudiantes (filas)
        for e in range(len(datos[d])):
            if datos[d][e] == []:
                continue
            else:
                definitiva_instrumento = 0

                # Procesa e inserta los valores de los indicadores
                for i in range(len(datos[d][e])):
                    #print(indicadores[d][i], estudiantes[e][1], int(datos[d][e][i]))
                    if not db.execute("select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 3 and COMPETENCIA = ? and asignatura = ? and evaluacion = ?",[estudiantes[e][1],indicadores[d][i],detalles[4],evaluacion[d]]).fetchall() :
                        db.execute(
                            "insert into nota_abet values (?,?,?,?,?,?)",
                            [detalles[4], evaluacion[d], indicadores[d][i], 3, estudiantes[e][1], int(datos[d][e][i])])
                        #print("Subind INS",indicadores[d][i], 3, estudiantes[e][1], int(datos[d][e][i]))
                    else:
                        db.execute(
                            #ASIGNATURA EVALUACION COMPETENCIA NIVEL CODIGO_ESTUDIANTE NOTA
                            "update nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and NIVEL = 3 and competencia = ? and evaluacion = ? ",
                            [int(datos[d][e][i]),detalles[4],estudiantes[e][1],indicadores[d][i],evaluacion[d]])
                        #print("Subind UPD",indicadores[d][i], 3, estudiantes[e][1], int(datos[d][e][i]),evaluacion[d])

                    definitiva_instrumento += (int(datos[d][e][i])*pesos[d][i])
                    #print("def instrumento",definitiva_instrumento)
                # Procesa e inserta los valores de los resultados de programa
                m = n
                resultado = 0.0
                o = 0
                #print(m,porcentaje_indicadores)
                if m < len(porcentaje_indicadores):
                    temp2 = porcentaje_indicadores[m][3]#Es la competencia
                    while temp1 == porcentaje_indicadores[m][0]:
                        if temp2 == porcentaje_indicadores[m][3]:
                            if datos[d][e][o] != "0":
                                resultado += int(datos[d][e][o])*porcentaje_indicadores[m][2]/100
                                #print(datos[d][e][o],porcentaje_indicadores[m][2],temp2,resultado)
                            m += 1
                            o += 1
                        else:
                            if not db.execute("select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 1 and competencia = ? and asignatura = ? and evaluacion = ?",[estudiantes[e][1],temp2,detalles[4],evaluacion[d]]).fetchall() :
                                db.execute(
                                    "insert or IGNORE into nota_abet values (?,?,?,?,?,?)",
                                    [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1], round(resultado,1)])
                                #print("IndINS",temp2,estudiantes[e][1], round(resultado,1),evaluacion[d])                            
                            else:
                                db.execute(
                                "update or IGNORE nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and nivel = 1 and competencia = ? and evaluacion = ?",
                                [round(resultado,1),detalles[4],estudiantes[e][1],temp2,evaluacion[d]])
                                #print("IndUPD",temp2,estudiantes[e][1], round(resultado,1),evaluacion[d])
                            resultado = 0.0
                            temp2 = porcentaje_indicadores[m][3]
                        if m >= len(porcentaje_indicadores):
                            if not db.execute("select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 1 and competencia = ? and asignatura = ? and evaluacion = ?",[estudiantes[e][1],temp2,detalles[4],evaluacion[d]]).fetchall() :
                                db.execute(
                                    "insert or IGNORE into nota_abet values (?,?,?,?,?,?)",
                                    [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1],round(resultado,1)])
                                #print("IndINS",temp2,estudiantes[e][1], round(resultado,1),evaluacion[d])                            
                            else:
                                db.execute(
                                "update or IGNORE nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and nivel = 1 and competencia = ? and evaluacion = ?",
                                [round(resultado,1),detalles[4],estudiantes[e][1], temp2,evaluacion[d]])
                                #print("IndUPD",temp2,estudiantes[e][1], round(resultado,1),evaluacion[d])
                            break

                    if not db.execute("select CODIGO_ESTUDIANTE from nota_abet where CODIGO_ESTUDIANTE = ? and NIVEL = 1 and competencia = ? and asignatura = ? and evaluacion = ?",[estudiantes[e][1],temp2,detalles[4],evaluacion[d]]).fetchall() :
                        db.execute(
                            "insert or IGNORE into nota_abet values (?,?,?,?,?,?)",
                            [detalles[4], evaluacion[d], temp2, 1, estudiantes[e][1],round(resultado,1)])
                        #print("IndINS",temp2,estudiantes[e][1], round(resultado,1),evaluacion[d])                            
                    else:
                        db.execute(
                        "update or IGNORE nota_abet set NOTA = ? where asignatura = ? and codigo_estudiante = ? and nivel = 1 and competencia = ? and evaluacion = ?",
                        [round(resultado,1),detalles[4],estudiantes[e][1], temp2,evaluacion[d]])
                        #print("IndUPD",temp2,estudiantes[e][1], round(resultado,1),evaluacion[d])

                # Inserta el valor de la nota definitiva de las evaluaciones
                #print("Sdef instrumento",definitiva_instrumento,m)
                definitiva_instrumento = (5*(definitiva_instrumento))/100
                if not db.execute("select CODIGO_ESTUDIANTE from nota_instrumento where CODIGO_ESTUDIANTE = ? and asignatura = ? and EVALUACION = ?",[estudiantes[e][1],detalles[4],evaluacion[d]]).fetchall() :
                    db.execute(
                        "insert or IGNORE into nota_instrumento values (?,?,?,?)",
                        [detalles[4], evaluacion[d], estudiantes[e][1], round(definitiva_instrumento,1)])
                    #print("nota instrumento INS",estudiantes[e][1], round(definitiva_instrumento,1)) 
                else:
                    db.execute(
                        #ASIGNATURA EVALUACION CODIGO_ESTUDIANTE NOTA
                        "update or IGNORE nota_instrumento set NOTA = ? where asignatura = ? and codigo_estudiante = ? and EVALUACION = ?",
                        [round(definitiva_instrumento,1),detalles[4],estudiantes[e][1],evaluacion[d]])
                    #print("nota instrumento UPD",estudiantes[e][1], round(definitiva_instrumento,1)) 

                definitiva_asignatura.append([definitiva_instrumento, evaluacion[d], estudiantes[e][1]])
        db.commit()

    # Procesa e inserta la nueva informacion de nota definitiva de una asignatura en la base de datos
    porcentajes_instrumentos = []
   # print(x for x in definitiva_asignatura)
  #  print(instrumentos)
    #print(0, len(instrumentos), int(len(instrumentos)/numevals[0][0]))
    for i in range(0, len(instrumentos), int(len(instrumentos)/numevals[0][0])):
        porcentajes_instrumentos.append(instrumentos[i])
    #print(porcentajes_instrumentos)
    #print("definitiva_asignatura",definitiva_asignatura)
   # definitiva_asignatura = sorted(definitiva_asignatura, key=itemgetter(2))
    j = 0
    for i in range(len(estudiantes)):
        nota_def = 0.0
        est = estudiantes[i][1]
        #print("DEF",len(definitiva_asignatura))
        #print(est,definitiva_asignatura[j][2])
        while est == definitiva_asignatura[j][2]:
            w = j
            for k in porcentajes_instrumentos:
                #print(definitiva_asignatura[w],w)
                #print(k[4], "==", definitiva_asignatura[w][1])
                if k[4] == definitiva_asignatura[w][1]:
                    #print(nota_def,"+=",definitiva_asignatura[w][0], "*", k[1], "/", 100)
                    nota_def += definitiva_asignatura[w][0] * k[1] / 100
                    #print("noda def",nota_def, definitiva_asignatura[w][0],k[1])
                #print(len(definitiva_asignatura)/(len(estudiantes)+w),len(definitiva_asignatura)/(len(estudiantes)+w) > 0)
                if len(definitiva_asignatura)/(len(estudiantes)+w) > 1:
                    w += len(estudiantes)
                    
            j += 1
            if j >= len(definitiva_asignatura)-1:
                break

        if not db.execute("select CODIGO_ESTUDIANTE from nota_definitiva where CODIGO_ESTUDIANTE = ? and asignatura = ? ",[estudiantes[e][1],detalles[4]]).fetchall() :
            db.execute("insert or IGNORE into nota_definitiva values (?,?,?)", [detalles[4], estudiantes[i][1], round(nota_def,1)])
            #print("definitivaINS",estudiantes[i][1], round(nota_def,1))
        else:
            db.execute("update or IGNORE nota_definitiva set NOTA = ? where asignatura = ? and codigo_estudiante = ?", [round(nota_def,1),detalles[4], estudiantes[i][1]])
            #print("definitivaUPD",estudiantes[i][1], round(nota_def,1))
        db.commit()

    # Recarga la pagina de los indicadores
    return redirect(url_for('notas', periodo=periodo, codigo=codigo, grupo=grupo))


@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        if request.form['username'] != "" and request.form['pswd'] != "" :
            cur1 = db.execute("select login, clave from usuario")
            detalles = cur1.fetchall()
            usr = (request.form['username'],request.form['pswd'])
            if usr in detalles:
                session['logged_in'] = True
                cur1 = db.execute("select nivel_acceso from usuario where login = ?",[usr[0]])
                lvlacc = cur1.fetchall()
                session['lvl'] = lvlacc[0][0]
                if lvlacc[0][0] == 4 :                    
                    cur2 = db.execute("select p.id from usuario u inner join profesor p on u.nombre = p.nombre")
                    idprof = cur2.fetchall()
                    session['id_prof'] = idprof
                return redirect(url_for('show_periods'))            
            else: 
                error = "Usuario o contrasena incorrectos, intente de nuevo"
        else:
            error = "No ha introducido datos"

    return render_template('login.html', error = error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('lvl', None)
    if 'id_prof' in session:
        session.pop('id_prof', None)
    return redirect(url_for('login'))

@app.route('/<periodo>/<codigo>/<grupo>/reporte', methods=['GET', 'POST'])
def reporte(periodo, codigo, grupo):
    db = get_db()
    # Recupera (de la base de datos) los detalles del curso
    cur1 = db.execute(
        "select a.nombre, a.codigo, a.grupo, a.periodo, a.id, p.nombre \
        from asignatura as a, profesor as p \
        where codigo=? and grupo=? and periodo=? and a.id_profesor = p.id",
        [codigo,grupo,periodo])
    detalles = cur1.fetchall()[0]
    # Recupera (de la base de datos) la informacion de las notas de los instrumentos ya contenida en la base de datos
    cur2 = db.execute(
        "select codigo_estudiante, nota from nota_definitiva where asignatura=?",
        [detalles[4]])
    notasDef = cur2.fetchall()
    perder = 0
    print(notasDef)
    for x in notasDef:
        if x[1]  < 3:
            perder += 1
    maxnota = max(notasDef)
    minnota = min(notasDef)

    promgeneralind = dict()
    promgeneralindaprob= dict()
    estud = [] 
    lowest= []
    high= []


    entries = {'detalles': detalles, 'perder': perder, 'maxnota': maxnota[1] ,'minnota': minnota[1], 'promgeneralind':promgeneralind, 'promgeneralindaprob':promgeneralindaprob}
    return render_template('report.html', entries=entries)

if __name__ == '__main__':
    if len(sys.argv)>2 and sys.argv[1]=='initdb':
        init_db()
    app.run()
