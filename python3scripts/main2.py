--- main.py	(original)
+++ main.py	(refactored)
@@ -1,6 +1,6 @@
 # Sistema de evaluacion ABET
 # Librerias
-from __future__ import division
+
 import sqlite3
 from contextlib import closing
 
@@ -12,6 +12,7 @@
 from operator import itemgetter
 import sys
 from flask import json
+from functools import reduce
 
 # Inicializacion de variables
 app = Flask(__name__)
@@ -85,8 +86,8 @@
     prueba = requests.get("http://pruebas.javerianacali.edu.co:8080/WS/consultas/academicas/cursoEstudiante?pCurso=300CIG006&pGrupo=A&pPeriodo=0940")
     # Agrupa los datos recuperados en una sola lista y la retorna a la pagina web
     entries = {'periodos': periodos}
-    print ("URL: ", prueba.url)
-    print ("INFO: ",prueba.text)
+    print(("URL: ", prueba.url))
+    print(("INFO: ",prueba.text))
     
     
 
@@ -146,11 +147,11 @@
     pevaljson =peval.json()
     proofjson =r.json()
 
-    print ("ContenteCurso: ",r.content)
+    print(("ContenteCurso: ",r.content))
 
     #proofjson.sort()
     for x in proofjson:
-        estudiante = [x.values()[1].capitalize(),x.values()[2]]
+        estudiante = [list(x.values())[1].capitalize(),list(x.values())[2]]
         estudiantes.append(estudiante)
     estudiantes.sort()
     # Recupera (de la base de datos) los datos de los instrumentos de evaluacion
@@ -252,7 +253,7 @@
         order by d.competencia",
         [detalles[4]])
     temp1 = cur9.fetchall()
-    sumaResultados = dict(zip(resultados,[0]*len(resultados)))
+    sumaResultados = dict(list(zip(resultados,[0]*len(resultados))))
     for i in resultados:
         cur10 = db.execute(
             "select evaluacion, competencia, porcentaje \
@@ -267,7 +268,7 @@
         sumaResultados[i] = suma
     resultadosTotales = {}
     for e in estudiantes:
-        resultadosTotales[e[1]] = dict(zip(resultados,[0]*len(resultados)))
+        resultadosTotales[e[1]] = dict(list(zip(resultados,[0]*len(resultados))))
     for (a,b,c,d,e) in temp1:
         resultadosTotales[c][b] = round(resultadosTotales[c][b]+((d*e)/sumaResultados[b]),1)
 
@@ -286,7 +287,7 @@
 
     for i in estudiantes:
         print (i)
-    print (len(inst))
+    print((len(inst)))
 
     # Agrupa los datos recuperados y procesados en una sola lista y la retorna a la pagina web
     entries = {'detalles': detalles, 'estudiantes': estudiantes, 'resprog': inst, 'numinstrumentos': len(inst),
@@ -497,7 +498,7 @@
     # Procesa los datos guardados en la base de datos, necesarios para hacer la insercion
     temp = []
     i = 0
-    while i < range(len(instrumentos)):
+    while i < list(range(len(instrumentos))):
         temp1 = []
         resprog = instrumentos[i][0]
         temp1.append(instrumentos[i])
@@ -564,7 +565,7 @@
     proofjson =r.json()
     #proofjson.sort()
     for x in proofjson:
-        estudiante = [x.values()[1].capitalize(),x.values()[2]]
+        estudiante = [list(x.values())[1].capitalize(),list(x.values())[2]]
         estudiantes.append(estudiante)
     
     estudiantes.sort()
@@ -772,7 +773,7 @@
 
                 # Procesa e inserta los valores de los indicadores
                 for i in range(len(datos[d][e])):
-                    if datos[d][e][i] != u'':
+                    if datos[d][e][i] != '':
                         db.execute(
                             "insert into nota_abet values (?,?,?,?,?,?)",
                             [detalles[4], evaluacion[d], indicadores[d][i], 3, estudiantes[e][1], int(datos[d][e][i])])
