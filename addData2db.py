
def add_data(g):
    g.db.execute('insert into carreras (id_carr, nomb_carr) values (?,?)',
                 [40,'Ingenieria de Sistemas y Computacion'])
    g.db.execute('insert into profesores (id_prof, nomb_prof, vinc_prof) values (?,?,?)',
                 [1,'Gerardo M. Sarria M.','TC'])
    g.db.execute('insert into asignaturas values (?,?,?,?,?)',
                 ['300CIP001','A','Introduccion a la Programacion',40,1])
    g.db.execute('insert into asignaturas values (?,?,?,?,?)',
                 ['300CIP002','A','Fundamentos y Estructuras de Programacion',40,1])
    g.db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['A','300CIP001','A',5])
    g.db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['B','300CIP001','A',2])
    g.db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['C','300CIP001','A',5])
    g.db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['D','300CIP001','A',2])
##    g.db.execute('insert into relevresulprog values (?,?,?,?)',
##                 ['E','300CIP001','A',0])
##    g.db.execute('insert into relevresulprog values (?,?,?,?)',
##                 ['F','300CIP001','A',0])
##    g.db.execute('insert into relevresulprog values (?,?,?,?)',
##                 ['G','300CIP001','A',0])
##    g.db.execute('insert into relevresulprog values (?,?,?,?)',
##                 ['H','300CIP001','A',0])
##    g.db.execute('insert into relevresulprog values (?,?,?,?)',
##                 ['I','300CIP001','A',0])
    g.db.execute('insert into relevresulprog values (?,?,?,?)',
                 ['J','300CIP001','A',0])
##    g.db.execute('insert into relevresulprog values (?,?,?,?)',
##                 ['K','300CIP001','A',0])
    g.db.commit()

