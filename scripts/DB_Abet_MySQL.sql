SET SESSION FOREIGN_KEY_CHECKS=0;

/* Drop Tables */

DROP TABLE NOTASCURSO;
DROP TABLE DEFNOTAABET;
DROP TABLE DEFCALIFICACION;
DROP TABLE RELEVRESULPROG;
DROP TABLE ASIGNATURAS;
DROP TABLE CARRERAS;
DROP TABLE ESTUDIANTES;
DROP TABLE INDICDESEMP;
DROP TABLE PROFESORES;
DROP TABLE RESULPROGRAMA;
DROP TABLE USUARIOS;




/* Create Tables */

CREATE TABLE ASIGNATURAS
(
	-- C�digo de la Asignatura. Ej. 300CIP001
	ID_ASIG CHAR(9) NOT NULL COMMENT 'C�digo de la Asignatura. Ej. 300CIP001',
	-- Ej. A
	GRUPO_ASIG CHAR(1) NOT NULL COMMENT 'Ej. A',
	-- Ej. INTRODUCCION A LA PROGRAMACION
	NOMB_ASIG VARCHAR(40) NOT NULL COMMENT 'Ej. INTRODUCCION A LA PROGRAMACION',
	-- Ej. 40
	ID_CARR INT(2) UNSIGNED NOT NULL UNIQUE COMMENT 'Ej. 40',
	-- Ej. 0012941
	ID_PROF INT UNSIGNED NOT NULL UNIQUE COMMENT 'Ej. 0012941',
	PRIMARY KEY (ID_ASIG, GRUPO_ASIG),
	UNIQUE (ID_ASIG, GRUPO_ASIG)
);


CREATE TABLE CARRERAS
(
	-- Ej. 40
	ID_CARR INT(2) UNSIGNED NOT NULL UNIQUE COMMENT 'Ej. 40',
	-- Ej. Ingenier�a de Sistemas y Computaci�n
	NOMB_CARR VARCHAR(35) NOT NULL UNIQUE COMMENT 'Ej. Ingenier�a de Sistemas y Computaci�n',
	PRIMARY KEY (ID_CARR)
);


CREATE TABLE DEFCALIFICACION
(
	-- Identificaci�n para la Evaluaci�n. Ej. Expos, Parcial1
	ID_EVAL VARCHAR(6) NOT NULL COMMENT 'Identificaci�n para la Evaluaci�n. Ej. Expos, Parcial1',
	-- C�digo de la Asignatura. Ej. 300CIP001
	ID_ASIG CHAR(9) NOT NULL COMMENT 'C�digo de la Asignatura. Ej. 300CIP001',
	-- Ej. A
	GRUPO_ASIG CHAR(1) NOT NULL COMMENT 'Ej. A',
	-- Ej. Exposici�n
	DESC_EVAL VARCHAR(20) NOT NULL COMMENT 'Ej. Exposici�n',
	-- Porcentaje de la evaluaci�n con respecto a la nota total de la asignatura
	PORCEVAL INT(3) UNSIGNED COMMENT 'Porcentaje de la evaluaci�n con respecto a la nota total de la asignatura',
	PRIMARY KEY (ID_EVAL, ID_ASIG, GRUPO_ASIG)
);


CREATE TABLE DEFNOTAABET
(
	-- C�digo de la Asignatura. Ej. 300CIP001
	ID_ASIG CHAR(9) NOT NULL COMMENT 'C�digo de la Asignatura. Ej. 300CIP001',
	-- Ej. A
	GRUPO_ASIG CHAR(1) NOT NULL COMMENT 'Ej. A',
	-- Identificaci�n para la Evaluaci�n. Ej. Expos, Parcial1
	ID_EVAL VARCHAR(6) NOT NULL COMMENT 'Identificaci�n para la Evaluaci�n. Ej. Expos, Parcial1',
	-- Ej. A1
	ID_INDDESEMP CHAR(2) NOT NULL UNIQUE COMMENT 'Ej. A1',
	PORC_ABET INT(3) UNSIGNED,
	PRIMARY KEY (ID_ASIG, GRUPO_ASIG, ID_EVAL, ID_INDDESEMP)
);


CREATE TABLE ESTUDIANTES
(
	-- Ej. 0201001
	ID_EST INT UNSIGNED NOT NULL UNIQUE COMMENT 'Ej. 0201001',
	-- Jose Luis Perez Gomez
	NOMB_EST VARCHAR(35) NOT NULL COMMENT 'Jose Luis Perez Gomez',
	PRIMARY KEY (ID_EST)
);


CREATE TABLE INDICDESEMP
(
	-- Ej. A1
	ID_INDDESEMP CHAR(2) NOT NULL UNIQUE COMMENT 'Ej. A1',
	-- Ej. (A1) Identificar los fundamentos cient�ficos y los principios de ingenier�a que rigen un proceso o sistema.
	DESC_INDDESEMP VARCHAR(100) NOT NULL COMMENT 'Ej. (A1) Identificar los fundamentos cient�ficos y los principios de ingenier�a que rigen un proceso o sistema.',
	-- Ej. A .. K
	ID_RESPROG CHAR(1) NOT NULL UNIQUE COMMENT 'Ej. A .. K',
	PRIMARY KEY (ID_INDDESEMP)
);


CREATE TABLE NOTASCURSO
(
	-- C�digo de la Asignatura. Ej. 300CIP001
	ID_ASIG CHAR(9) NOT NULL COMMENT 'C�digo de la Asignatura. Ej. 300CIP001',
	-- Ej. A
	GRUPO_ASIG CHAR(1) NOT NULL COMMENT 'Ej. A',
	-- Identificaci�n para la Evaluaci�n. Ej. Expos, Parcial1
	ID_EVAL VARCHAR(6) NOT NULL COMMENT 'Identificaci�n para la Evaluaci�n. Ej. Expos, Parcial1',
	-- Ej. A1
	ID_INDDESEMP CHAR(2) NOT NULL UNIQUE COMMENT 'Ej. A1',
	-- Ej. 0201001
	ID_EST INT UNSIGNED NOT NULL COMMENT 'Ej. 0201001',
	-- Ej. 2013-2
	PERIODO VARCHAR(6) COMMENT 'Ej. 2013-2',
	-- Nota de cada estudiantes por aignartura, por evaluaci�n por Indicador de desempe�o ABET. Ej. 4.2
	NOTA_EVAL DECIMAL(4,2) DEFAULT 0.0 >= 0 COMMENT 'Nota de cada estudiantes por aignartura, por evaluaci�n por Indicador de desempe�o ABET. Ej. 4.2',
	UNIQUE (ID_EST, ID_EVAL)
);


CREATE TABLE PROFESORES
(
	-- Ej. 0012941
	ID_PROF INT UNSIGNED NOT NULL UNIQUE COMMENT 'Ej. 0012941',
	-- EJ. Sarria Montemiranda,Gerardo Mauricio
	NOMB_PROF VARCHAR(35) NOT NULL COMMENT 'EJ. Sarria Montemiranda,Gerardo Mauricio',
	-- Ej. HC, MT, TC
	VINC_PROF TEXT NOT NULL COMMENT 'Ej. HC, MT, TC',
	PRIMARY KEY (ID_PROF)
);


CREATE TABLE RELEVRESULPROG
(
	-- Ej. A .. K
	ID_RESPROG CHAR(1) NOT NULL COMMENT 'Ej. A .. K',
	-- C�digo de la Asignatura. Ej. 300CIP001
	ID_ASIG CHAR(9) NOT NULL COMMENT 'C�digo de la Asignatura. Ej. 300CIP001',
	-- Ej. A
	GRUPO_ASIG CHAR(1) NOT NULL COMMENT 'Ej. A',
	-- Ej. 1 , 2, .., 5 (Dependiendo de la carrera)
	PESO SMALLINT UNSIGNED NOT NULL COMMENT 'Ej. 1 , 2, .., 5 (Dependiendo de la carrera)',
	PRIMARY KEY (ID_RESPROG, ID_ASIG, GRUPO_ASIG),
	UNIQUE (ID_RESPROG, ID_ASIG, GRUPO_ASIG)
);


CREATE TABLE RESULPROGRAMA
(
	-- Ej. A .. K
	ID_RESPROG CHAR(1) NOT NULL UNIQUE COMMENT 'Ej. A .. K',
	-- Ej. La habilidad para aplicar conocimientos de matem�ticas, ciencias e ingenier�a.
	DESCR_RESPROG VARCHAR(100) NOT NULL COMMENT 'Ej. La habilidad para aplicar conocimientos de matem�ticas, ciencias e ingenier�a.',
	-- Ej. Students must show an ability to efectively apply knowledge, techniques, principles and theories from continuous and discrete mathematics, logic, statistics, probability, physics as well as core computing and engineering knowledge to: (1)analyze, model and design
	-- systems and processes; and (2) propose and evaluate solutions to problems.
	DEF_RESPROG TEXT COMMENT 'Ej. Students must show an ability to efectively apply knowledge, techniques, principles and theories from continuous and discrete mathematics, logic, statistics, probability, physics as well as core computing and engineering knowledge to: (1)analyze, mode',
	PRIMARY KEY (ID_RESPROG)
);


CREATE TABLE USUARIOS
(
	-- Id del usuario con acceso al sistema. Ej. gsariia
	ID_USU VARCHAR(15) NOT NULL UNIQUE COMMENT 'Id del usuario con acceso al sistema. Ej. gsariia',
	-- Nombre completo del usuario con acceso al sistema
	NOM_USU VARCHAR(35) COMMENT 'Nombre completo del usuario con acceso al sistema',
	-- Clave de acceso. Se sugiere que este enceiptada (Ej. MD5)
	CLAVE VARCHAR(15) NOT NULL COMMENT 'Clave de acceso. Se sugiere que este enceiptada (Ej. MD5)',
	-- Nivel de Acceso: Ej 1,2,3 o 4
	NIVEL_ACC SMALLINT(1) UNSIGNED DEFAULT 4 COMMENT 'Nivel de Acceso: Ej 1,2,3 o 4',
	PRIMARY KEY (ID_USU)
);



/* Create Foreign Keys */

ALTER TABLE DEFCALIFICACION
	ADD FOREIGN KEY (ID_ASIG, GRUPO_ASIG)
	REFERENCES ASIGNATURAS (ID_ASIG, GRUPO_ASIG)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE RELEVRESULPROG
	ADD FOREIGN KEY (ID_ASIG, GRUPO_ASIG)
	REFERENCES ASIGNATURAS (ID_ASIG, GRUPO_ASIG)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE ASIGNATURAS
	ADD FOREIGN KEY (ID_CARR)
	REFERENCES CARRERAS (ID_CARR)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE DEFNOTAABET
	ADD FOREIGN KEY (ID_ASIG, GRUPO_ASIG, ID_EVAL)
	REFERENCES DEFCALIFICACION (ID_ASIG, GRUPO_ASIG, ID_EVAL)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE NOTASCURSO
	ADD FOREIGN KEY (ID_ASIG, GRUPO_ASIG, ID_EVAL, ID_INDDESEMP)
	REFERENCES DEFNOTAABET (ID_ASIG, GRUPO_ASIG, ID_EVAL, ID_INDDESEMP)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE NOTASCURSO
	ADD FOREIGN KEY (ID_EST)
	REFERENCES ESTUDIANTES (ID_EST)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE DEFNOTAABET
	ADD FOREIGN KEY (ID_INDDESEMP)
	REFERENCES INDICDESEMP (ID_INDDESEMP)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE ASIGNATURAS
	ADD FOREIGN KEY (ID_PROF)
	REFERENCES PROFESORES (ID_PROF)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE INDICDESEMP
	ADD FOREIGN KEY (ID_RESPROG)
	REFERENCES RESULPROGRAMA (ID_RESPROG)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE RELEVRESULPROG
	ADD FOREIGN KEY (ID_RESPROG)
	REFERENCES RESULPROGRAMA (ID_RESPROG)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;



