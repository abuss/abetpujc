/* Drop Tables */

BEGIN TRANSACTION;

DROP TABLE IF EXISTS ACREDITACION_ABET;
DROP TABLE IF EXISTS ASIGNATURA;
DROP TABLE IF EXISTS Descripcion_A_K;
DROP TABLE IF EXISTS ESTUDIANTE;
DROP TABLE IF EXISTS FORMULA;
DROP TABLE IF EXISTS INDICADOR_DE_DESEMPENO;
DROP TABLE IF EXISTS INSTRUMENTO;
DROP TABLE IF EXISTS NOTA_ABET;
DROP TABLE IF EXISTS NOTA_DEFINITIVA;
DROP TABLE IF EXISTS NOTA_INSTRUMENTO;
DROP TABLE IF EXISTS PORCENTAJE_ABET;
DROP TABLE IF EXISTS PROFESOR;
DROP TABLE IF EXISTS Pregunta;
DROP TABLE IF EXISTS RESULTADO_DE_PROGRAMA;
DROP TABLE IF EXISTS USUARIO;

/* Create Tables */

--BEGIN TRANSACTION;

CREATE TABLE ACREDITACION_ABET 
(
        -- Ej. 40
	ID_CARRERA INT NOT NULL,
        -- Ej. Ingenier�a de Sistemas y Computaci�n
	NOMBRE_CARRERA TEXT NOT NULL,
        -- Ej. 2014-1
	PERIODO TEXT NOT NULL,
	      -- Ej. 3, 5
	RELEVANCIA INT NOT NULL,

	PRIMARY KEY (ID_CARRERA, PERIODO)
);


CREATE TABLE ASIGNATURA
(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
        -- C�digo de la Asignatura. Ej. 300CIP001
	CODIGO TEXT NOT NULL,
        -- Ej. A
	GRUPO TEXT NOT NULL,
        -- Ej. INTRODUCCION A LA PROGRAMACION
	NOMBRE CHAR(50) NOT NULL,
        -- Ej. 40
	ID_CARRERA INT NOT NULL,
        -- Ej. 0012941
	ID_PROFESOR INT NOT NULL,
        -- Ej. 2013-2
  PERIODO TEXT NOT NULL,

	FOREIGN KEY (ID_CARRERA, PERIODO)
	REFERENCES ACREDITACION_ABET (ID_CARRERA, PERIODO),
	FOREIGN KEY (ID_PROFESOR)
	REFERENCES PROFESOR (ID),
	UNIQUE (CODIGO, GRUPO, PERIODO)
);

CREATE TABLE Descripcion_A_K  ( 
	-- Ej. A, B.1, C.1.1
	competencia	TEXT PRIMARY KEY NOT NULL,
	--Id de la descripcion padre, niveles 2 o 3.
	superior   	TEXT,
	-- Nivel 1 corresponde a A..K, 
	-- Nivel 2 corresponde a A.1, A.2, H.1, ...
	-- Nivel 3 corresponde a A.1.1, A.1.2, C.2.3, ...
	-- Si es un nivel 1 es el papa en el arbol de jerarquia
	Nivel      	INTEGER NOT NULL,
	FOREIGN KEY(superior)
	REFERENCES Descripcion_A_K(competencia)
);

CREATE TABLE ESTUDIANTE
(
		-- Ej. 0201001
	CODIGO INT NOT NULL,
		-- Jose Luis Perez Gomez
	NOMBRE TEXT NOT NULL,
		-- Ej. Introducci�n a la Programaci�n
	ASIGNATURA INTEGER,

	PRIMARY KEY (CODIGO,ASIGNATURA),
	FOREIGN KEY (ASIGNATURA)
	REFERENCES ASIGNATURA (ID)
);

CREATE TABLE FORMULA
(
		-- Ej. A .. K
	RESULTADO_DE_PROGRAMA TEXT NOT NULL,
		-- Id de la Asignatura.
	ASIGNATURA INT NOT NULL,
		-- Ej. 1 , 2, .., 5 (Dependiendo de la carrera)
	PESO INT NOT NULL,

	PRIMARY KEY (RESULTADO_DE_PROGRAMA, ASIGNATURA),
	FOREIGN KEY (ASIGNATURA)
	REFERENCES ASIGNATURA (ID),
	FOREIGN KEY (RESULTADO_DE_PROGRAMA)
	REFERENCES RESULTADO_DE_PROGRAMA (ID)
);

CREATE TABLE INDICADOR_DE_DESEMPENO
(
    -- Ej. 40
	CARRERA INT NOT NULL,
		-- Ej. A1
	ID TEXT NOT NULL,
		-- Ej. (A1) Identificar los fundamentos cientificos y los principios de ingenier�a que rigen un proceso o sistema.
	DESCRIPCION TEXT NOT NULL,
		-- Ej. A .. K
	RESULTADO_DE_PROGRAMA TEXT NOT NULL,

	PRIMARY KEY (ID,CARRERA),
	FOREIGN KEY (RESULTADO_DE_PROGRAMA)
	REFERENCES RESULTADO_DE_PROGRAMA (ID),
	FOREIGN KEY (CARRERA)
	REFERENCES ACREDITACION_ABET (ID_CARRERA)
);

CREATE TABLE INSTRUMENTO  ( 
		-- Identificaci�n para la Evaluacion.
	ID_EVALUACION INTEGER PRIMARY KEY AUTOINCREMENT,
		-- Id de la Asignatura.
	ASIGNATURA INT NOT NULL,
		-- Ej. Exposicion, Parcial 1, Proyecto
	EVALUACION TEXT NOT NULL,
		-- Porcentaje de la evaluacion con respecto a la nota total de la asignatura
	PORCENTAJE INT NOT NULL,

	FOREIGN KEY (ASIGNATURA)
	REFERENCES ASIGNATURA (ID)
);

CREATE TABLE NOTA_ABET
(
		-- Id de la Asignatura
	ASIGNATURA TEXT NOT NULL,
		-- Identificaci�n para la Evaluacion. Ej. Expos, Parcial1
	EVALUACION INT NOT NULL,
		-- Ej. A.1.1
	COMPETENCIA TEXT NOT NULL,
  	-- Nivel 1 corresponde a A..K,
		-- Nivel 2 corresponde a A.1, A.2, H.1, ...
		-- Nivel 3 corresponde a A.1.1, A.1.2, C.2.3, ...
	NIVEL INT NOT NULL,
		-- Ej. 0201001
	CODIGO_ESTUDIANTE INT NOT NULL,
		-- Nota de cada estudiantes por evaluacion
	NOTA INT DEFAULT 0,

	PRIMARY KEY (ASIGNATURA, EVALUACION, COMPETENCIA, CODIGO_ESTUDIANTE, NIVEL)
	FOREIGN KEY (CODIGO_ESTUDIANTE)
	REFERENCES ESTUDIANTE (CODIGO),
	FOREIGN KEY (ASIGNATURA, EVALUACION)
	REFERENCES INSTRUMENTO (ASIGNATURA, ID_EVALUACION)
);

CREATE TABLE NOTA_DEFINITIVA
(
		-- Id de la Asignatura.
	ASIGNATURA TEXT NOT NULL,
		-- Ej. 0201001
	CODIGO_ESTUDIANTE INT NOT NULL,
		-- Nota de cada estudiantes por evaluacion
	NOTA NUMERIC DEFAULT 0.0,

	PRIMARY KEY (ASIGNATURA,  CODIGO_ESTUDIANTE)
	FOREIGN KEY (CODIGO_ESTUDIANTE)
	REFERENCES ESTUDIANTE (CODIGO),
	FOREIGN KEY (ASIGNATURA)
	REFERENCES ASIGNATURA (ASIGNATURA)
);

CREATE TABLE NOTA_INSTRUMENTO
(
		-- Id de la Asignatura.
	ASIGNATURA TEXT NOT NULL,
		-- Identificaci�n para la Evaluacion. Ej. Expos, Parcial1
	EVALUACION INT NOT NULL,
		-- Ej. 0201001
	CODIGO_ESTUDIANTE INT NOT NULL,
		-- Nota de cada estudiantes por evaluacion.
	NOTA NUMERIC DEFAULT 0.0,

	PRIMARY KEY (ASIGNATURA, EVALUACION, CODIGO_ESTUDIANTE)
	FOREIGN KEY (CODIGO_ESTUDIANTE)
	REFERENCES ESTUDIANTE (CODIGO),
	FOREIGN KEY (ASIGNATURA, EVALUACION)
	REFERENCES INSTRUMENTO (ASIGNATURA, ID_EVALUACION)
);

CREATE TABLE Pregunta  ( 
	--Id de la pregunta.
	Id INTEGER NOT NULL,

	Porcentaje INTEGER NOT NULL,
	-- Id del instrumento al que pertence.
	Id_instrumento	INTEGER NOT NULL,
	FOREIGN KEY(Id_instrumento)
	REFERENCES INSTRUMENTO(ID_EVALUACION)
);

CREATE TABLE PORCENTAJE_ABET  ( 
	-- Id de la Asignatura.
	ASIGNATURA    	INT NOT NULL,
	-- Id de la evaluacion.
	EVALUACION    	INT NOT NULL,
	-- Id de la competencia que se esta evaluando.
	Id_COMPETENCIA	TEXT NOT NULL,
	--Porcentaje que se le da.
	PORCENTAJE    	INT NOT NULL,
	-- Id del porcentaje
	Id           	INTEGER,
	-- Id de la pregunta.
	Id_Pregunta   	INTEGER,
	PRIMARY KEY(ASIGNATURA,EVALUACION,Id_COMPETENCIA),
	FOREIGN KEY(Id_COMPETENCIA)
	REFERENCES Descripcion_A_K(competencia),
	FOREIGN KEY(Id_Pregunta)
	REFERENCES Pregunta(Id),
	FOREIGN KEY(ASIGNATURA, EVALUACION)
	REFERENCES INSTRUMENTO(ASIGNATURA, ID_EVALUACION)
);

CREATE TABLE PROFESOR
(
        -- Ej. 0012941
	ID INT PRIMARY KEY NOT NULL,
        -- EJ. Sarria Montemiranda, Gerardo Mauricio
	NOMBRE TEXT NOT NULL,
        -- Ej. HC, MT, TC
	VINCULACION TEXT
);




CREATE TABLE RESULTADO_DE_PROGRAMA
(
    -- Ej. 40
	CARRERA INT NOT NULL,
		-- Ej. A .. K
	ID TEXT NOT NULL,
		-- Ej. La habilidad para aplicar conocimientos de matematicas, ciencias e ingenieria.
	DESCRIPCION TEXT NOT NULL,
		-- Ej. Students must show an ability to efectively apply knowledge, techniques, principles and theories from continuous and discrete mathematics, logic, statistics, probability, physics as well as core computing and engineering knowledge to: (1)analyze, model and design
		-- systems and processes; and (2) propose and evaluate solutions to problems.
	DEFINICION TEXT,

	PRIMARY KEY (ID,CARRERA),
	FOREIGN KEY (CARRERA)
	REFERENCES ACREDITACION_ABET (ID_CARRERA)
);


CREATE TABLE USUARIO
(
		-- Id del usuario con acceso al sistema. Ej. gsarria
	LOGIN TEXT PRIMARY KEY NOT NULL,
		-- Nombre completo del usuario con acceso al sistema
	NOMBRE TEXT,
		-- Clave de acceso. Se sugiere que este encriptada (Ej. MD5)
	CLAVE TEXT NOT NULL,
		-- Nivel de Acceso: Ej 1,2,3 o 4
	NIVEL_ACCESO INT DEFAULT 4
);
COMMIT;