
def add_data(g):
    g.db.execute('insert into carreras (id_carr, nomb_carr) values (?,?)',
                 [40,'Ingenieria de Sistemas y Computacion'])
    g.db.execute('insert into profesores (id_prof, nomb_prof, vinc_prof) values (?,?,?)',
                 [1,'Gerardo M. Sarria M.','TC'])
    g.db.execute('insert into asignaturas values (?,?,?,?,?)',
                 ['300CIP001','A','Introduccion a la Programacion',40,1])
    g.db.execute('insert into asignaturas values (?,?,?,?,?)',
                 ['300CIP022','A','Fundamentos y Estructuras de Programacion',40,1])
    g.db.commit()

