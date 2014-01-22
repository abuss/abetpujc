
/* Carreras */
insert into carreras (id_carr, nomb_carr) values (40,'Ingeniería de Sistemas y Computación');

/* Profesores */
 insert into profesores (id_prof, nomb_prof, vinc_prof) values (1,'Gerardo M. Sarria M.','TC');
 insert into profesores (id_prof, nomb_prof, vinc_prof) values (2,'Juan Carlos Martinez','TC');

/* Asignaturas */
insert into asignaturas values ('300CIP002','A','Fundamentos y Estructuras de Programación',40,1,'2014-1');
insert into asignaturas values ('300CIS005','A','Procesos de Ingeniería de Software',40,2,'2014-1');

/* Formula de Resultados de Programa */
insert into relevresulprog values ('A','300CIP002','A',5);
insert into relevresulprog values ('C','300CIP002','A',5);
insert into relevresulprog values ('F','300CIP002','A',2);
insert into relevresulprog values ('H','300CIP002','A',3);
insert into relevresulprog values ('I','300CIP002','A',3);

/* Definicion de la Calificacion General */
insert into defcalificacion values ('P1','300CIP002','A','Parcial 1',20);
insert into defcalificacion values ('P2','300CIP002','A','Parcial 2',20);
insert into defcalificacion values ('P3','300CIP002','A','Parcial 3',20);
insert into defcalificacion values ('T1','300CIP002','A','Tarea 1',2);
insert into defcalificacion values ('T2','300CIP002','A','Tarea 2',2);
insert into defcalificacion values ('T3','300CIP002','A','Tarea 3',2);
insert into defcalificacion values ('T4','300CIP002','A','Tarea 4',2);
insert into defcalificacion values ('T5','300CIP002','A','Tarea 5',2);
insert into defcalificacion values ('Exp','300CIP002','A','Exposicion',10);
insert into defcalificacion values ('Pry','300CIP002','A','Proyecto',20);

/* Definicion de la Calificacion ABET */
insert into defnotaabet values ('300CIP002','A','P1','A',80);
insert into defnotaabet values ('300CIP002','A','P1','C',0);
insert into defnotaabet values ('300CIP002','A','P1','F',10);
insert into defnotaabet values ('300CIP002','A','P1','H',10);
insert into defnotaabet values ('300CIP002','A','P1','I',0);
insert into defnotaabet values ('300CIP002','A','P2','A',30);
insert into defnotaabet values ('300CIP002','A','P2','C',50);
insert into defnotaabet values ('300CIP002','A','P2','F',10);
insert into defnotaabet values ('300CIP002','A','P2','H',10);
insert into defnotaabet values ('300CIP002','A','P2','I',0);
insert into defnotaabet values ('300CIP002','A','P3','A',30);
insert into defnotaabet values ('300CIP002','A','P3','C',50);
insert into defnotaabet values ('300CIP002','A','P3','F',10);
insert into defnotaabet values ('300CIP002','A','P3','H',10);
insert into defnotaabet values ('300CIP002','A','P3','I',0);
insert into defnotaabet values ('300CIP002','A','T1','A',50);
insert into defnotaabet values ('300CIP002','A','T1','C',0);
insert into defnotaabet values ('300CIP002','A','T1','F',5);
insert into defnotaabet values ('300CIP002','A','T1','H',15);
insert into defnotaabet values ('300CIP002','A','T1','I',30);
insert into defnotaabet values ('300CIP002','A','T2','A',30);
insert into defnotaabet values ('300CIP002','A','T2','C',0);
insert into defnotaabet values ('300CIP002','A','T2','F',5);
insert into defnotaabet values ('300CIP002','A','T2','H',15);
insert into defnotaabet values ('300CIP002','A','T2','I',50);
insert into defnotaabet values ('300CIP002','A','T3','A',15);
insert into defnotaabet values ('300CIP002','A','T3','C',45);
insert into defnotaabet values ('300CIP002','A','T3','F',5);
insert into defnotaabet values ('300CIP002','A','T3','H',15);
insert into defnotaabet values ('300CIP002','A','T3','I',20);
insert into defnotaabet values ('300CIP002','A','T4','A',15);
insert into defnotaabet values ('300CIP002','A','T4','C',45);
insert into defnotaabet values ('300CIP002','A','T4','F',5);
insert into defnotaabet values ('300CIP002','A','T4','H',15);
insert into defnotaabet values ('300CIP002','A','T4','I',20);
insert into defnotaabet values ('300CIP002','A','T5','A',15);
insert into defnotaabet values ('300CIP002','A','T5','C',45);
insert into defnotaabet values ('300CIP002','A','T5','F',5);
insert into defnotaabet values ('300CIP002','A','T5','H',15);
insert into defnotaabet values ('300CIP002','A','T5','I',20);
insert into defnotaabet values ('300CIP002','A','Exp','A',0);
insert into defnotaabet values ('300CIP002','A','Exp','C',0);
insert into defnotaabet values ('300CIP002','A','Exp','F',35);
insert into defnotaabet values ('300CIP002','A','Exp','H',65);
insert into defnotaabet values ('300CIP002','A','Exp','I',0);
insert into defnotaabet values ('300CIP002','A','Pry','A',15);
insert into defnotaabet values ('300CIP002','A','Pry','C',40);
insert into defnotaabet values ('300CIP002','A','Pry','F',20);
insert into defnotaabet values ('300CIP002','A','Pry','H',0);
insert into defnotaabet values ('300CIP002','A','Pry','I',25);

/* Definicion de los indicadores de desempeño */
insert into indicdesemp values ('A1','Identificar los fundamentos científicos y los principios de ingeniería que rigen un proceso o sistema. (Conocimiento)','A');
insert into indicdesemp values ('A2','Resolver problemas relacionados con la disciplina y otras áreas por medio de la utilización de conocimientos, modelos y formalismos de las ciencias de la computación, las matemáticas y la ingeniería. (Aplicación)','A');
insert into indicdesemp values ('A3','Analizar conjuntos de datos. (Análisis)','A');
insert into indicdesemp values ('A4','Interpretar modelos matemáticos para estimar su precisión y confiabilidad. (Comprensión)','A');
insert into indicdesemp values ('B1','Describir procesos de manera declarativa ignorando los detalles de su implementación. (Comprensión).','B');
insert into indicdesemp values ('B2','Utilizar el lenguaje propio de las matemáticas, la lógica y la ingeniería para especificar requerimientos funcionales y no funcionales de un sistema o proceso. (Aplicación)','B');
insert into indicdesemp values ('B3','Sintetizar la información, evidencias y hechos necesarios para analizar un problema. (Análisis - Síntesis)','B');
insert into indicdesemp values ('B4','Formular hipótesis. (Síntesis)','B');
     
