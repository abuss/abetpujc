
/* Drop Tables */

DROP TABLE IF EXISTS NOTASCURSO;
DROP TABLE IF EXISTS DEFNOTAABET;
DROP TABLE IF EXISTS DEFCALIFICACION;
DROP TABLE IF EXISTS RELEVRESULPROG;
DROP TABLE IF EXISTS ASIGNATURAS;
DROP TABLE IF EXISTS CARRERAS;
DROP TABLE IF EXISTS ESTUDIANTES;
DROP TABLE IF EXISTS INDICDESEMP;
DROP TABLE IF EXISTS PROFESORES;
DROP TABLE IF EXISTS RESULPROGRAMA;
DROP TABLE IF EXISTS USUARIOS;




/* Create Tables */

CREATE TABLE CARRERAS 
(
        -- Ej. 40
	ID_CARR INT NOT NULL,
        -- Ej. Ingeniería de Sistemas y Computación
	NOMB_CARR TEXT NOT NULL,

        PRIMARY KEY (ID_CARR)
);


CREATE TABLE PROFESORES
(
        -- Ej. 0012941
	ID_PROF INT NOT NULL,
        -- EJ. Sarria Montemiranda,Gerardo Mauricio
	NOMB_PROF TEXT NOT NULL,
        -- Ej. HC, MT, TC
	VINC_PROF TEXT NOT NULL,

        PRIMARY KEY (ID_PROF)
);


CREATE TABLE ASIGNATURAS
(
        -- Código de la Asignatura. Ej. 300CIP001
	ID_ASIG TEXT NOT NULL,
        -- Ej. A
	GRUPO_ASIG TEXT NOT NULL,
        -- Ej. INTRODUCCION A LA PROGRAMACION
	NOMB_ASIG CHAR(50) NOT NULL,
        -- Ej. 40
	ID_CARR INTEGER NOT NULL,
        -- Ej. 0012941
	ID_PROF INTEGER NOT NULL,
        -- Ej. 2013-2
        PERIODO TEXT NOT NULL,

	PRIMARY KEY (ID_ASIG, GRUPO_ASIG, PERIODO),
	FOREIGN KEY (ID_CARR)
	REFERENCES CARRERAS (ID_CARR),
	FOREIGN KEY (ID_PROF)
	REFERENCES PROFESORES (ID_PROF),
	UNIQUE (ID_ASIG, GRUPO_ASIG, PERIODO)
);


CREATE TABLE DEFCALIFICACION
(
	-- Identificación para la Evaluacion. Ej. Expos, Parcial1
	ID_EVAL TEXT NOT NULL,
	-- Codigo de la Asignatura. Ej. 300CIP001
	ID_ASIG TEXT NOT NULL,
	-- Ej. A
	GRUPO_ASIG TEXT NOT NULL,
	-- Ej. Exposicion
	DESC_EVAL TEXT NOT NULL,
	-- Porcentaje de la evaluacion con respecto a la nota total de la asignatura
	PORCEVAL INT,

	PRIMARY KEY (ID_EVAL, ID_ASIG, GRUPO_ASIG),
	FOREIGN KEY (ID_ASIG, GRUPO_ASIG)
	REFERENCES ASIGNATURAS (ID_ASIG, GRUPO_ASIG)
);


CREATE TABLE RESULPROGRAMA
(
	-- Ej. A .. K
	ID_RESPROG TEXT PRIMARY KEY NOT NULL,
	-- Ej. La habilidad para aplicar conocimientos de matematicas, ciencias e ingenieria.
	DESCR_RESPROG TEXT NOT NULL,
	-- Ej. Students must show an ability to efectively apply knowledge, techniques, principles and theories from continuous and discrete mathematics, logic, statistics, probability, physics as well as core computing and engineering knowledge to: (1)analyze, model and design
	-- systems and processes; and (2) propose and evaluate solutions to problems.
	DEF_RESPROG TEXT
);


CREATE TABLE INDICDESEMP
(
	-- Ej. A1
	ID_INDDESEMP TEXT NOT NULL UNIQUE,
	-- Ej. (A1) Identificar los fundamentos cientificos y los principios de ingeniería que rigen un proceso o sistema.
	DESC_INDDESEMP TEXT NOT NULL,
	-- Ej. A .. K
	ID_RESPROG TEXT NOT NULL,

	PRIMARY KEY (ID_INDDESEMP),
	FOREIGN KEY (ID_RESPROG)
	REFERENCES RESULPROGRAMA (ID_RESPROG)
);


CREATE TABLE RELEVRESULPROG
(
	-- Ej. A .. K
	ID_RESPROG TEXT NOT NULL,
	-- Código de la Asignatura. Ej. 300CIP001
	ID_ASIG TEXT NOT NULL,
	-- Ej. A
	GRUPO_ASIG TEXT NOT NULL,
	-- Ej. 1 , 2, .., 5 (Dependiendo de la carrera)
	PESO INTEGER NOT NULL,

	PRIMARY KEY (ID_RESPROG, ID_ASIG, GRUPO_ASIG),
	FOREIGN KEY (ID_ASIG, GRUPO_ASIG)
	REFERENCES ASIGNATURAS (ID_ASIG, GRUPO_ASIG),
	FOREIGN KEY (ID_RESPROG)
	REFERENCES RESULPROGRAMA (ID_RESPROG),
	UNIQUE (ID_RESPROG, ID_ASIG, GRUPO_ASIG)
);


CREATE TABLE DEFNOTAABET
(
	-- Codigo de la Asignatura. Ej. 300CIP001
	ID_ASIG TEXT NOT NULL,
	-- Ej. A
	GRUPO_ASIG TEXT NOT NULL,
	-- Identificacion para la Evaluacion. Ej. Expos, Parcial1
	ID_EVAL TEXT NOT NULL,
	-- Ej. A
	ID_RESPROG TEXT NOT NULL,
	PORC_ABET INTEGER,

	PRIMARY KEY (ID_ASIG, GRUPO_ASIG, ID_EVAL, ID_RESPROG),
	FOREIGN KEY (ID_ASIG, GRUPO_ASIG, ID_EVAL)
	REFERENCES DEFCALIFICACION (ID_ASIG, GRUPO_ASIG, ID_EVAL)
);


CREATE TABLE ESTUDIANTES
(
	-- Ej. 0201001
	ID_EST INT PRIMARY KEY NOT NULL,
	-- Jose Luis Perez Gomez
	NOMB_EST TEXT NOT NULL
);


CREATE TABLE NOTASCURSO
(
	-- Codigo de la Asignatura. Ej. 300CIP001
	ID_ASIG TEXT NOT NULL,
	-- Ej. A
	GRUPO_ASIG TEXT NOT NULL,
	-- Identificación para la Evaluacion. Ej. Expos, Parcial1
	ID_EVAL TEXT NOT NULL,
	-- Ej. A1
	ID_INDDESEMP TEXT NOT NULL UNIQUE,
	-- Ej. 0201001
	ID_EST INTEGER NOT NULL,
	-- Nota de cada estudiantes por asignatura, por evaluacion por Indicador de desempeno ABET. Ej. 4.2
	NOTA_EVAL NUMERIC DEFAULT 0.0,

	FOREIGN KEY (ID_EST)
	REFERENCES ESTUDIANTES (ID_EST),
	FOREIGN KEY (ID_ASIG, GRUPO_ASIG, ID_EVAL, ID_INDDESEMP)
	REFERENCES DEFNOTAABET (ID_ASIG, GRUPO_ASIG, ID_EVAL, ID_INDDESEMP),
	UNIQUE (ID_EST, ID_EVAL)
);




CREATE TABLE USUARIOS
(
	-- Id del usuario con acceso al sistema. Ej. gsariia
	ID_USU TEXT NOT NULL UNIQUE,
	-- Nombre completo del usuario con acceso al sistema
	NOM_USU TEXT,
	-- Clave de acceso. Se sugiere que este encriptada (Ej. MD5)
	CLAVE TEXT NOT NULL,
	-- Nivel de Acceso: Ej 1,2,3 o 4
	NIVEL_ACC INTEGER DEFAULT 4,

	PRIMARY KEY (ID_USU)
);

