
def add_data(db):
    # Carreras
    db.execute('insert into carreras (id_carr, nomb_carr) values (?,?)',
                 [40,'Ingenieria de Sistemas y Computacion'])

    # Profesores
    db.execute('insert into profesores (id_prof, nomb_prof, vinc_prof) values (?,?,?)',
                 [1,'Gerardo M. Sarria M.','TC'])
    db.execute('insert into profesores (id_prof, nomb_prof, vinc_prof) values (?,?,?)',
                 [2,'Juan Carlos Martinez','TC'])

    # Asignaturas
    db.execute('insert into asignaturas values (?,?,?,?,?,?)',
                 ['300CIP002','A','Fundamentos y Estructuras de Programacion',40,1,'2014-1'])
    db.execute('insert into asignaturas values (?,?,?,?,?,?)',
                 ['300CIS005','A','Procesos de Ingenieria de Software',40,2,'2014-1'])

    # Formula de Resultados de Programa
    db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['A','300CIP002','A',5])
    db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['C','300CIP002','A',5])
    db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['F','300CIP002','A',2])
    db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['H','300CIP002','A',3])
    db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['I','300CIP002','A',3])

    # Definicion de la Calificacion General
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['P1','300CIP002','A','Parcial 1',20])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['P2','300CIP002','A','Parcial 2',20])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['P3','300CIP002','A','Parcial 3',20])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['T1','300CIP002','A','Tarea 1',2])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['T2','300CIP002','A','Tarea 2',2])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['T3','300CIP002','A','Tarea 3',2])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['T4','300CIP002','A','Tarea 4',2])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['T5','300CIP002','A','Tarea 5',2])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['Exp','300CIP002','A','Exposicion',10])
    db.execute('insert into defcalificacion values (?,?,?,?,?)',
                 ['Pry','300CIP002','A','Proyecto',20])

    # Definicion de la Calificacion ABET
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P1','A',80])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P1','C',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P1','F',10])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P1','H',10])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P1','I',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P2','A',30])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P2','C',50])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P2','F',10])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P2','H',10])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P2','I',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P3','A',30])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P3','C',50])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P3','F',10])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P3','H',10])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','P3','I',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T1','A',50])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T1','C',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T1','F',5])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T1','H',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T1','I',30])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T2','A',30])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T2','C',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T2','F',5])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T2','H',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T2','I',50])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T3','A',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T3','C',45])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T3','F',5])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T3','H',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T3','I',20])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T4','A',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T4','C',45])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T4','F',5])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T4','H',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T4','I',20])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T5','A',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T5','C',45])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T5','F',5])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T5','H',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','T5','I',20])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Exp','A',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Exp','C',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Exp','F',35])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Exp','H',65])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Exp','I',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Pry','A',15])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Pry','C',40])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Pry','F',20])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Pry','H',0])
    db.execute('insert into defnotaabet values (?,?,?,?,?)',
                 ['300CIP002','A','Pry','I',25])

    
    db.commit()

