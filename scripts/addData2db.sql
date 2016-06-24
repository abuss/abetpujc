
BEGIN TRANSACTION;

/*----------*/
/* Carreras */
/*----------*/
insert into acreditacion_abet values (40,'Ingeniería de Sistemas y Computación','2015-2',5);
insert into acreditacion_abet values (10,'Ingeniería Industrial','2015-2',3);
insert into acreditacion_abet values (40,'Ingeniería de Sistemas y Computación','2015-1',5);
insert into acreditacion_abet values (10,'Ingeniería Industrial','2015-1',3);
insert into acreditacion_abet values (40,'Ingeniería de Sistemas y Computación','2014-2',5);
insert into acreditacion_abet values (10,'Ingeniería Industrial','2014-2',3);
insert into acreditacion_abet values (40,'Ingeniería de Sistemas y Computación','2014-1',5);
insert into acreditacion_abet values (10,'Ingeniería Industrial','2014-1',3);

/*------------*/
/* Profesores */
/*------------*/
insert into profesor values (1,'Gerardo M. Sarria M.','TC');
insert into profesor values (2,'Juan Carlos Martinez','TC');
insert into profesor values (3,'Michell Andrés Gómez Leiva','TC');
insert into profesor values (4,'Camilo Rueda','TC');
insert into profesor values (5,'Maria Constanza Pabon','TC');
insert into profesor values (6,'Diego Fdo. Polo','HC');
insert into profesor values (7,'Gloria I. Alvarez','TC');
insert into profesor values (8,'Maribel Sacanamboy','TC');
insert into profesor values (9,'Andrés Navarro','TC');
insert into profesor values (10,'Jose Eduardo Tofiño','TC');
insert into profesor values (11,'Jorge Francisco Estela','TC');

/*-------------*/
/* Asignaturas */
/*-------------*/
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIP002','A','Fundamentos y Estructuras de Programación',40,1,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG006','A','Arquitectura del Computador II',40,8,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG010','A','Aspectos Sociales y Profesionales',40,6,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG007','A','Computabilidad y Lenguajes Formales',40,7,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG008','A','Computación Gráfica',40,9,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS002','A','Desarrollo Formal de Programas',40,4,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CID001','A','Gestión y Modelado de Datos',40,5,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG002','A','Lógica en Ciencias de la Computación',40,10,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300MAG031','A','Matemáticas Discretas para la Computación',40,3,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS005','A','Procesos de Ingeniería de Software',40,2,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300IGQ001','A','Termodinámica',10,11,'2015-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIP002','A','Fundamentos y Estructuras de Programación',40,1,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG006','A','Arquitectura del Computador II',40,8,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG010','A','Aspectos Sociales y Profesionales',40,6,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG007','A','Computabilidad y Lenguajes Formales',40,7,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG008','A','Computación Gráfica',40,9,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS002','A','Desarrollo Formal de Programas',40,4,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CID001','A','Gestión y Modelado de Datos',40,5,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG002','A','Lógica en Ciencias de la Computación',40,10,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300MAG031','A','Matemáticas Discretas para la Computación',40,3,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS005','A','Procesos de Ingeniería de Software',40,2,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300IGQ001','A','Termodinámica',10,11,'2015-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIP002','A','Fundamentos y Estructuras de Programación',40,1,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG006','A','Arquitectura del Computador II',40,8,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG010','A','Aspectos Sociales y Profesionales',40,6,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG007','A','Computabilidad y Lenguajes Formales',40,7,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG008','A','Computación Gráfica',40,9,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS002','A','Desarrollo Formal de Programas',40,4,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CID001','A','Gestión y Modelado de Datos',40,5,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG002','A','Lógica en Ciencias de la Computación',40,10,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300MAG031','A','Matemáticas Discretas para la Computación',40,3,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS005','A','Procesos de Ingeniería de Software',40,2,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300IGQ001','A','Termodinámica',10,11,'2014-2');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIP002','A','Fundamentos y Estructuras de Programación',40,1,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG006','A','Arquitectura del Computador II',40,8,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG010','A','Aspectos Sociales y Profesionales',40,6,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG007','A','Computabilidad y Lenguajes Formales',40,7,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG008','A','Computación Gráfica',40,9,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS002','A','Desarrollo Formal de Programas',40,4,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CID001','A','Gestión y Modelado de Datos',40,5,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIG002','A','Lógica en Ciencias de la Computación',40,10,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300MAG031','A','Matemáticas Discretas para la Computación',40,3,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300CIS005','A','Procesos de Ingeniería de Software',40,2,'2014-1');
insert into asignatura (codigo,grupo,nombre,id_carrera,id_profesor,periodo) values ('300IGQ001','A','Termodinámica',10,11,'2014-1');

/*------------------------*/
/* Resultados de Programa */
/*------------------------*/
insert into resultado_de_programa values (40,'A','Habilidad para aplicar conocimientos de matemáticas, ciencias e ingeniería','');
insert into resultado_de_programa values (40,'B','Habilidad para analizar un problema e identificar los requerimientos necesarios para su definición y solución','');
insert into resultado_de_programa values (40,'C','Habilidad para diseñar, implementar y evaluar procesos y sistemas computacionales','');
insert into resultado_de_programa values (40,'D','Habilidad para funcionar en equipos de trabajo','');
insert into resultado_de_programa values (40,'E','Entendimiento de la responsabilidad profesional y ética','');
insert into resultado_de_programa values (40,'F','Habilidad para comunicarse efectivamente','');
insert into resultado_de_programa values (40,'G','Habilidad para analizar los impactos de la computación y la ingeniería en las personas, organizaciones y la sociedad','');
insert into resultado_de_programa values (40,'H','Reconocimiento de la necesidad de, y la habilidad para, continuar con el desarrollo profesional','');
insert into resultado_de_programa values (40,'I','Habilidad para usar las técnicas, destrezas y herramientas modernas para la práctica de la computación','');
insert into resultado_de_programa values (40,'J','Habilidad para aplicar los fundamentos y principios de las matemáticas y de la computación en el modelamiento y diseño de sistemas computacionales','');
insert into resultado_de_programa values (40,'K','Habilidad para aplicar los principios de diseño y desarrollo de software en la construcción de sistemas de diferente complejidad','');
insert into resultado_de_programa values (10,'A','Habilidad para aplicar conocimientos de matemáticas, ciencias e ingeniería','');
insert into resultado_de_programa values (10,'B','La habilidad para diseñar y conducir experimentos así como para analizar e interpretar datos','');
insert into resultado_de_programa values (10,'C','La habilidad para diseñar un sistema, componente o proceso para satisfacer necesidades deseadas dentro de restricciones realistas','');
insert into resultado_de_programa values (10,'D','La habilidad para funcionar en equipos multidisciplinarios','');
insert into resultado_de_programa values (10,'E','La habilidad para identificar, formular y resolver problemas de ingeniería','');
insert into resultado_de_programa values (10,'F','El entendimiento de la responsabilidad profesional y ética','');
insert into resultado_de_programa values (10,'G','La habilidad para comunicarse efectivamente','');
insert into resultado_de_programa values (10,'H','La educación amplia y necesaria para entender los impactos de las soluciones de ingeniería en contextos globales económicos, ambientales y sociales','');
insert into resultado_de_programa values (10,'I','El reconocimiento de la necesidad de, y la habilidad para, continuar el aprendizaje a lo largo de la vida','');
insert into resultado_de_programa values (10,'J','El conocimiento de asuntos contemporáneos','');
insert into resultado_de_programa values (10,'K','La habilidad para usar las técnicas, destrezas y herramientas modernas de ingeniería necesarias para la práctica de la ingeniería','');

/*--------------------------------------------*/
/* Definicion de los indicadores de desempeño */
/*--------------------------------------------*/
/* Ingenieria de Sistemas */
/*
insert into indicador_de_desempeno values (40,'A.1','Identifica los fundamentos científicos y los principios de ingeniería que rigen un proceso o sistema. (Conocimiento)','A');
insert into indicador_de_desempeno values (40,'A.2','Resuelve problemas relacionados con la disciplina y otras áreas por medio de la utilización de conocimientos, modelos y formalismos de las ciencias de la computación, las matemáticas y la ingeniería. (Aplicación)','A');
insert into indicador_de_desempeno values (40,'A.3','Analiza conjuntos de datos. (Análisis)','A');
insert into indicador_de_desempeno values (40,'A.4','Interpreta modelos matemáticos para estimar su precisión y confiabilidad. (Comprensión)','A');
insert into indicador_de_desempeno values (40,'B.1','Describe procesos de manera declarativa ignorando los detalles de su implementación. (Comprensión).','B');
insert into indicador_de_desempeno values (40,'B.2','Utiliza el lenguaje propio de las matemáticas, la lógica y la ingeniería para especificar requerimientos funcionales y no funcionales de un sistema o proceso. (Aplicación)','B');
insert into indicador_de_desempeno values (40,'B.3','Sintetiza la información, evidencias y hechos necesarios para analizar un problema. (Análisis - Síntesis)','B');
insert into indicador_de_desempeno values (40,'B.4','Formula hipótesis. (Síntesis)','B');
insert into indicador_de_desempeno values (40,'C.1','Utiliza estándares de codificación en la implementación de componentes de software. (Aplicación)','C');
insert into indicador_de_desempeno values (40,'C.2','Identifica componentes, interacciones, relaciones e interfaces entre componentes. (Análisis)','C');
insert into indicador_de_desempeno values (40,'C.3','Diseña procesos y componentes de software haciendo uso de la notación, técnicas y herramientas adecuadas. (Síntesis)','C');
insert into indicador_de_desempeno values (40,'C.4','Evalua un componente de software de acuerdo a su complejidad temporal y espacial. (Evaluación)','C');
insert into indicador_de_desempeno values (40,'D.1','Reconoce el rol cada vez más predominante de la computación en entornos multidisciplinarios. (Conocimiento)','D');
insert into indicador_de_desempeno values (40,'D.2','Participa en tareas y en la toma de decisiones. (Respuesta - Afectivo)','D');
insert into indicador_de_desempeno values (40,'D.3','Integra diferentes puntos de vista, información, críticas y retroalimentación para proponer una solución. (Síntesis)','D');
insert into indicador_de_desempeno values (40,'D.4','Define tareas, roles y responsabilidades. (Aplicación)','C');
insert into indicador_de_desempeno values (40,'E.1','Identifica los códigos de ética relacionados con la disciplina. (Conocimiento)','E');
insert into indicador_de_desempeno values (40,'E.2','Muestra responsabilidad y un adecuado comportamiento profesional. (Valuación)','E');
insert into indicador_de_desempeno values (40,'E.3','Identifica pros y contras en decisiones éticas relacionadas con la práctica profesional. (Análisis)','E');
insert into indicador_de_desempeno values (40,'E.4','Discute y justifica decisiones éticas. (Evaluación)','E');
insert into indicador_de_desempeno values (40,'F.1','Produce textos de manera efectiva teniendo en cuenta la estructura, coherencia, flujo, ortografía y correcto uso del lenguaje. (Aplicación)','F');
insert into indicador_de_desempeno values (40,'F.2','Comunica de manera efectiva de acuerdo al público objetivo haciendo uso correcto del lenguaje, estilo, tiempo y expresión corporal. (Aplicación)','F');
insert into indicador_de_desempeno values (40,'F.3','Utiliza recursos gráficos para comunicar y expresar una idea. (Aplicación)','F');
insert into indicador_de_desempeno values (40,'F.4','Defiende ideas con precisión y claridad. (Evaluación)','F');
insert into indicador_de_desempeno values (40,'G.1','Identifica los eventos históricos y contemporáneos que la computación y la ingeniería han afectado. (Comprensión)','G');
insert into indicador_de_desempeno values (40,'G.2','Utiliza los conocimientos para identificar los impactos de las soluciones en ingeniería y computación. (Aplicación)','G');
insert into indicador_de_desempeno values (40,'G.3','Analiza los impactos locales y globales de la computación y la ingeniería. (Análisis)','G');
insert into indicador_de_desempeno values (40,'G.4','Juzga los impactos de la computación y la ingeniería en el mundo. (Evaluación)','G');
insert into indicador_de_desempeno values (40,'H.1','Reconoce la importancia del conocimiento tanto en amplitud como en profundidad. (Compresión)','H');
insert into indicador_de_desempeno values (40,'H.2','Aplica nuevo conocimiento para resolver un problema o desarrollar una solución. (Aplicación)','H');
insert into indicador_de_desempeno values (40,'H.3','Interpreta y evaluar información de diferentes fuentes y establecer conexiones con conocimientos previos. (Síntesis - Evaluación)','H');
insert into indicador_de_desempeno values (40,'H.4','Muestra disposición par aprender nuevas cosas por medio de estudio personal. (Valuación)','H');
insert into indicador_de_desempeno values (40,'I.1','Utiliza herramientas de desarrollo de software. (Aplicación)','I');
insert into indicador_de_desempeno values (40,'I.2','Utiliza herramientas de diseño, modelamiento y simulación. (Aplicación)','I');
insert into indicador_de_desempeno values (40,'I.3','Combina herramientas de software y hardware para resolver un problema. (Síntesis)','I');
insert into indicador_de_desempeno values (40,'I.4','Demuestra flexibilidad para adaptarse a diferentes paradigmas y lenguajes de programación. (Valuación)','I');
insert into indicador_de_desempeno values (40,'J.1','Reconoce la importancia del modelamiento cuando se resuelve un problema. (Compresión)','J');
insert into indicador_de_desempeno values (40,'J.2','Relaciona conceptos y principios teóricos para la resolución efectiva de un problema. (Síntesis)','J');
insert into indicador_de_desempeno values (40,'J.3','Combina principios de matemáticas, computación e ingeniería para modelar una situación. (Síntesis)','J');
insert into indicador_de_desempeno values (40,'J.4','Evalua decisiones de diseño basándose en principios matemáticos y de computación. (Evaluación)','J');
insert into indicador_de_desempeno values (40,'K.1','Hace seguimiento a cronogramas y adaptar los recursos necesarios para cumplir con sus hitos. (Aplicación)','K');
insert into indicador_de_desempeno values (40,'K.2','Implementa e integra componentes de software respetando los criterios de diseño. (Aplicación)','K');
insert into indicador_de_desempeno values (40,'K.3','Establece invariantes y propiedades de componentes de software. (Análisis)','K');
insert into indicador_de_desempeno values (40,'K.4','Evalua y verifica soluciones de software con respecto a las restricciones y requerimientos establecidos. (Aplicación - Evaluación)','K');
*/
insert into indicador_de_desempeno values (40,'A.1.1','Identifica los principios fundamentales científicos y de ingeniería que gobiernan un proceso o sistema dado','A');
insert into indicador_de_desempeno values (40,'A.1.2','Aplica conceptos matemáticos y físicos para resolver problemas','A');
insert into indicador_de_desempeno values (40,'A.1.3','Analiza conjuntos de datos usando métodos estadísticos','A');
insert into indicador_de_desempeno values (40,'A.1.4','Interpreta modelos matemáticos para estimar precisión y fiabilidad','A');
insert into indicador_de_desempeno values (40,'A.2.1','Resuelve problemas relacionados con la disciplina y otras áreas usando conocimiento, modelos y formalismos de las ciencias de la computación','A');
insert into indicador_de_desempeno values (40,'A.2.2','Usa técnicas y conocimiento de la ingeniería para gestionar un proyecto','A');
insert into indicador_de_desempeno values (40,'B.1.1','Identifica y formula un problema','B');
insert into indicador_de_desempeno values (40,'B.1.2','Describe procesos declarativamente, abstraídos del comportamiento de la implementación','B');
insert into indicador_de_desempeno values (40,'B.1.3','Analiza riesgos y relación costo-beneficio de la ingeniería','B');
insert into indicador_de_desempeno values (40,'B.1.4','Analiza escenarios con incertidumbre','B');
insert into indicador_de_desempeno values (40,'B.1.5','Formula hipótesis','B');
insert into indicador_de_desempeno values (40,'B.1.6','Identifica oportunidades que derivan de tecnología (computacional)','B');
insert into indicador_de_desempeno values (40,'B.2.1','Identifica requerimientos estáticos y dinámicos (e.g. variables, entidades, relaciones, acciones, casos de uso)','B');
insert into indicador_de_desempeno values (40,'B.2.2','Identifica requerimientos técnicos (e.g. seguridad, rendimiento, arquitectura, usabilidad, escalabilidad)','B');
insert into indicador_de_desempeno values (40,'B.2.3','Identifica requerimientos no-técnicos (e.g. costo de la solución, aspectos ambientales, sociales, económicos)','B');
insert into indicador_de_desempeno values (40,'B.3.1','Identifica conflictos y restricciones y requerimientos contradictorios al igual que chequea consistencia y completitud del análisis de requerimientos','B');
insert into indicador_de_desempeno values (40,'B.3.2','Usa notación y metodologías estándares para realizar el análisis de requerimientos','B');
insert into indicador_de_desempeno values (40,'C.1.1','Diseña procesos y artefactos de software siguiendo una apropiada metodología de diseño, herramietnas y notación','C');
insert into indicador_de_desempeno values (40,'C.1.2','Desarrolla un nivel de abstracción apropiado en el diseño','C');
insert into indicador_de_desempeno values (40,'C.1.3','Propone y evalua alternativas en cada fase del diseño para escoger la mejor','C');
insert into indicador_de_desempeno values (40,'C.1.4','Valida un diseño o modelo','C');
insert into indicador_de_desempeno values (40,'C.2.1','Usa estándares de codificación y documentación','C');
insert into indicador_de_desempeno values (40,'C.3.1','Valida sistemas (i.e. depuración y análisis de entrada-salida)','C');
insert into indicador_de_desempeno values (40,'C.3.2','Analiza rendimientos (i.e. estima la eficiencia temporal y espacial de una solución)','C');
insert into indicador_de_desempeno values (40,'D.1.1','Forma equipos de trabajo efectivos','D');
insert into indicador_de_desempeno values (40,'D.1.2','Muestra sentido de responsabilidad y compromiso a los objetivos y asignaciones del equipo','D');
insert into indicador_de_desempeno values (40,'D.1.3','Reconoce el rol en el equipo y es capaz de compartir responsabilidades con los otros miembros','D');
insert into indicador_de_desempeno values (40,'D.1.4','Respeta y valora los diferentes puntos de vista y acepta la retroalimentación y críticas de otros miembros del equipo','D');
insert into indicador_de_desempeno values (40,'D.1.5','Muestra creatividad, liderazgo, iniciativa y toma de decisiones','D');
insert into indicador_de_desempeno values (40,'D.1.6','Reconoce el rol incremental de la computación en escenarios multidisciplinarios','D');
insert into indicador_de_desempeno values (40,'E.1.1','Demuestra habilidad para tomar decisiones éticas bien informadas','E');
insert into indicador_de_desempeno values (40,'E.1.2','Demuestra conocimiento de un código de ética profesional y actua acorde a él','E');
insert into indicador_de_desempeno values (40,'E.2.1','Demuestra excelencia profesional cuando trabaja en una organización','E');
insert into indicador_de_desempeno values (40,'F.1.1','Define una estrategia de comunicación acorde a una audiencia objetivo','F');
insert into indicador_de_desempeno values (40,'F.1.2','Comunica y defiende ideas con precisión y claridad','F');
insert into indicador_de_desempeno values (40,'F.1.3','Procesa información de una variedad de fuentes','F');
insert into indicador_de_desempeno values (40,'F.2.1','Comunica efectivamente de manera escrita con coherencia, flujo, correcta ortografía, puntuación y gramática','F');
insert into indicador_de_desempeno values (40,'F.2.2','Identifica y utiliza diferentes estilos de escritura','F');
insert into indicador_de_desempeno values (40,'F.3.1','Comunica efectivamente con el lenguaje, estilo, tiempo, flujo y estrategia no verbales (gesturas, contacto visual, pose) apropiados','F');
insert into indicador_de_desempeno values (40,'F.3.2','Escucha atentamente para mejorar el conocimiento, desarrollar un mejor entendimiento y responder y hacer preguntas efectivamente','F');
insert into indicador_de_desempeno values (40,'F.4.1','Usa apropiadamente medios (digitales) para mejorar las presentaciones orales','F');
insert into indicador_de_desempeno values (40,'F.4.2','Usa recursos gráficos y diagramas para explicar una idea','F');
insert into indicador_de_desempeno values (40,'F.5.1','Realiza lecturas técnicas y escrituras en inglés','F');
insert into indicador_de_desempeno values (40,'F.5.2','Posee habilidades básicas de comunicación oral en inglés','F');
insert into indicador_de_desempeno values (40,'G.1.1','Analiza, identifica y entiende el impacto de la computación (y la ingeniería) en un contexto global','G');
insert into indicador_de_desempeno values (40,'G.1.2','Analiza, identifica y entiende los impactos económicos de soluciones computacionales (y de ingeniería)','G');
insert into indicador_de_desempeno values (40,'G.1.3','Analiza, identifica y entiende los impactos sociales de soluciones computacionales (y de ingeniería)','G');
insert into indicador_de_desempeno values (40,'G.1.4','Analiza, identifica y entiende el impacto ambiental de soluciones de ingeniería (y computación)','G');
insert into indicador_de_desempeno values (40,'G.1.5','Analiza, identifica y entiende los impactos éticos de soluciones computacionales (y de ingeniería)','G');
insert into indicador_de_desempeno values (40,'H.1.1','Reconoce la importancia del conocimiento tanto en profundidad como en anchura','H');
insert into indicador_de_desempeno values (40,'H.1.2','Reconoce la relevancia de un proceso de aprendizaje disciplinado','H');
insert into indicador_de_desempeno values (40,'H.1.3','Está atento a la naturaleza dinámica y evolutiva de la ciencia, la ingeniería, la tecnología y la industria, y reconoce la relevancia de continuar el aprendizaje después de la graduación','H');
insert into indicador_de_desempeno values (40,'H.1.4','Atiende un entrenamiento extracurricular','H');
insert into indicador_de_desempeno values (40,'H.1.5','Desea aprender un nuevo contenido a través de investigación y estudio individual','H');
insert into indicador_de_desempeno values (40,'H.2.1','Muestra habilidades para saber y entender nuevos desarrollos en las ciencias de la computación y áreas relacionadas','H');
insert into indicador_de_desempeno values (40,'H.2.2','Muestra responsabilidad en el automejoramiento para sobrepasar debilidades','H');
insert into indicador_de_desempeno values (40,'H.2.3','Es capaz de accesar, coleccionar, clasificar e interpretar y evaluar críticamente información de múltiples fuentes y enlazarla con conocimiento previo','H');
insert into indicador_de_desempeno values (40,'H.2.4','Observa cuidadosa y críticamente artefactos computacionales y modelos para alcanzar un entendimiento de las razones detrás de sus diseños','H');
insert into indicador_de_desempeno values (40,'I.1.1','Es conciente de la relación entre software y hardware cuando se implementan soluciones tecnológicas','I');
insert into indicador_de_desempeno values (40,'I.2.1','Usa herramientas de diseño de software, simulación y modelado','I');
insert into indicador_de_desempeno values (40,'I.2.2','Muestra flexibilidad para adaptarse a diferentes lenguajes y paradigmas de programación','I');
insert into indicador_de_desempeno values (40,'I.2.3','Usa apropiadamente herramientas de desarrollo de software','I');
insert into indicador_de_desempeno values (40,'I.2.4','Muestra proficiencia en el uso, configuración y ajustes de herramientas, aplicaciones y servicios de software y sistemas operativos','I');
insert into indicador_de_desempeno values (40,'I.3.1','Está al tanto del estado del arte de las prácticas usadas en ciencias de la computación','I');
insert into indicador_de_desempeno values (40,'I.3.2','Demuestra habilidad para engancharse en una experiencia de diseño computacional basado en industria','I');
insert into indicador_de_desempeno values (40,'J.1.1','Identifica problemas y asuntos donde la computación puede jugar un rol fundamental y reconoce la limitación de los sitemas basados en computadores','J');
insert into indicador_de_desempeno values (40,'J.1.2','Identifica restricciones y requerimientos que pueden ser usados para evaluar soluciones','J');
insert into indicador_de_desempeno values (40,'J.1.3','Usa conceptos de la matemática y la computación para definir transformaciones entre problemas','J');
insert into indicador_de_desempeno values (40,'J.1.4','Identifica principios de computación, ingeniería y científicos que pueden ser aplicados en la solución de un problema','J');
insert into indicador_de_desempeno values (40,'J.1.5','Piensa holísticamente','J');
insert into indicador_de_desempeno values (40,'J.2.1','Reconoce el rol de la matemática y la lógica como herramientas para modelar sistemas y procesos y para guiar un diseño','J');
insert into indicador_de_desempeno values (40,'J.2.2','Identifica y combina principios matemáticos, computacionales y de ingeniería que pueden ser aplicados cuando se modela una situación','J');
insert into indicador_de_desempeno values (40,'J.2.3','Reconoce la importancia de modelar cuando se resuelve un problema','J');
insert into indicador_de_desempeno values (40,'J.3.1','Toma decisiones bien informadas, basadas en principios matemáticos y computacionales, cuando diseña','J');
insert into indicador_de_desempeno values (40,'K.1.1','Asigna y estima tiempos y recursos acorde a la complejidad de la situación','K');
insert into indicador_de_desempeno values (40,'K.1.2','Asegura la calidad del software','K');
insert into indicador_de_desempeno values (40,'K.1.3','Sigue cronogramas y adapta recursos para conseguir objetivos','K');
insert into indicador_de_desempeno values (40,'K.2.1','Toma una buena y bien informada decisión sobre el lenguaje y herramientas que deben ser usados en la implementación','K');
insert into indicador_de_desempeno values (40,'K.2.2','Implementa e integra componentes de software que siguen fielmente criterios de diseño','K');
insert into indicador_de_desempeno values (40,'K.2.3','Establece invariantes y propiedades de software para probar la correctitud de una solución','K');
insert into indicador_de_desempeno values (40,'K.3.1','Evalua, verifica y valida con respecto a requerimientos y restricciones de sistemas','K');
insert into indicador_de_desempeno values (40,'K.3.2','Afina e integra hardware','K');
insert into indicador_de_desempeno values (40,'K.3.3','Identifica la evolución de un software','K');

/* Ingenieria Industrial */
insert into indicador_de_desempeno values (10,'A.1','Aplicar conceptos y conocimiento de matemáticas y estadística para resolver problemas de ingeniería o relacionados con la disciplina. (Aplicación)','A');
insert into indicador_de_desempeno values (10,'A.2','Aplicar conceptos y conocimiento de física y química para resolver problemas de ingeniería o relacionados con la disciplina. (Aplicación)','A');
insert into indicador_de_desempeno values (10,'A.3','Seleccionar y aplicar conceptos claves de ciencias de la ingeniería y conceptos nucleares de la disciplina para resolver problemas de ingeniería o de Ingeniería Industrial. (Aplicación)','A');
insert into indicador_de_desempeno values (10,'B.4','Interpretar información numérica relacionada con problemas de ingeniería o relacionados con la disciplina. (Aplicación)','B');
insert into indicador_de_desempeno values (10,'E.1','Identificar problemas de ingeniería y los modelos, recursos y suposiciones necesarios para resolverlos. (Análisis)','E');
insert into indicador_de_desempeno values (10,'E.2','Diseñar e implementar las estrategias necesarias para resolver problemas deingeniería. (Síntesis)','E');
insert into indicador_de_desempeno values (10,'E.3','Integrar conocimientos de Ingeniería Industrial, ciencias y matemáticas a la solución de problemas de ingeniería o relacionados con la disciplina. (Síntesis)','E');
insert into indicador_de_desempeno values (10,'E.4','Evaluar la validez de las soluciones a problemas de ingeniería y hacer recomendaciones en consecuencia. (Evaluación)','E');
insert into indicador_de_desempeno values (10,'F.2',' Valorar los impactos de la ingeniería y de la profesión sobre la sociedad. (Evaluación)','F');
insert into indicador_de_desempeno values (10,'F.3','Demostrar la habilidad para tomar decisiones éticas bien informadas al resolver problemas de ingeniería o relacionados con la disciplina. (caracterización por un valor)','F');
insert into indicador_de_desempeno values (10,'G.1','Producir comunicación escrita efectiva en relación con: organización, estructura, uso del idioma y terminología, enfoque, concisión y adaptación a la audiencia. (Aplicación)','G');
insert into indicador_de_desempeno values (10,'G.2','Producir comunicación oral efectiva en relación con: organización, estructura, uso del idioma y terminología, enfoque, concisión y adaptación a la audiencia. (Aplicación)','G');
insert into indicador_de_desempeno values (10,'G.3','Producir comunicación gráfica efectiva en relación con: organización, estructura y uso del idioma. (Aplicación)','G');
insert into indicador_de_desempeno values (10,'H.1','Estimar los impactos locales y globales, económicos, ambientales y sociales y las ventajas y desventajas de los productos y proyectos de la ingeniería. (Evaluación)','H');
insert into indicador_de_desempeno values (10,'J.1','Identificar y analizar las problemáticas sociales, económicas, políticas y ambientales de actualidad en relación con la práctica de la ingeniería y de la profesión. (Análisis)','J');
insert into indicador_de_desempeno values (10,'J.2','Estimar los impactos de la tecnología, la ingeniería y la profesión sobre las problemáticas locales, nacionales y globales. (Evaluación)','J');
insert into indicador_de_desempeno values (10,'K.1','Demostrar competencia en el uso de herramientas apropiadas de hardware, i.e. computadores, equipos de ingeniería, etc. (Aplicación)','K');
insert into indicador_de_desempeno values (10,'K.2','Demostrar competencia en el uso de herramientas apropiadas de software; i.e. hojas de cálculo, procesadores de texto, aplicaciones de diseño, CAD, simuladores, etc. (Aplicación)','K');

/*-----------------------------------*/
/* Formula de Resultados de Programa */
/*-----------------------------------*/
/* Periodo 2015-2 */
insert into formula values ('A',1,5);
insert into formula values ('C',1,5);
insert into formula values ('F',1,2);
insert into formula values ('H',1,3);
insert into formula values ('I',1,3);

insert into formula values ('A',2,4);
insert into formula values ('C',2,4);
insert into formula values ('D',2,1);
insert into formula values ('F',2,1);
insert into formula values ('I',2,2);
insert into formula values ('J',2,2);
insert into formula values ('K',2,2);

insert into formula values ('D',3,1);
insert into formula values ('E',3,5);
insert into formula values ('F',3,5);
insert into formula values ('G',3,5);
insert into formula values ('H',3,2);

insert into formula values ('A',4,4);
insert into formula values ('F',4,1);
insert into formula values ('J',4,4);

insert into formula values ('A',5,5);
insert into formula values ('C',5,4);
insert into formula values ('F',5,4);
insert into formula values ('H',5,1);
insert into formula values ('I',5,3);
insert into formula values ('J',5,3);

insert into formula values ('A',6,1);
insert into formula values ('B',6,2);
insert into formula values ('E',6,1);
insert into formula values ('G',6,1);
insert into formula values ('I',6,1);
insert into formula values ('J',6,5);
insert into formula values ('K',6,5);

insert into formula values ('A',7,2);
insert into formula values ('C',7,5);
insert into formula values ('E',7,1);
insert into formula values ('F',7,1);
insert into formula values ('G',7,2);
insert into formula values ('I',7,5);

insert into formula values ('A',8,3);
insert into formula values ('J',8,3);
insert into formula values ('K',8,3);

insert into formula values ('A',9,3);
insert into formula values ('I',9,1);
insert into formula values ('J',9,3);

insert into formula values ('A',10,4);
insert into formula values ('B',10,5);
insert into formula values ('C',10,5);
insert into formula values ('D',10,1);
insert into formula values ('F',10,2);
insert into formula values ('I',10,2);
insert into formula values ('J',10,1);
insert into formula values ('K',10,2);

insert into formula values ('A',11,3);
insert into formula values ('B',11,2);
insert into formula values ('E',11,3);
insert into formula values ('F',11,2);
insert into formula values ('G',11,2);
insert into formula values ('H',11,3);
insert into formula values ('J',11,3);
insert into formula values ('K',11,2);

/* Periodo 2015-1 */
insert into formula values ('A',12,5);
insert into formula values ('C',12,5);
insert into formula values ('F',12,2);
insert into formula values ('H',12,3);
insert into formula values ('I',12,3);

insert into formula values ('A',13,4);
insert into formula values ('C',13,4);
insert into formula values ('D',13,1);
insert into formula values ('F',13,1);
insert into formula values ('I',13,2);
insert into formula values ('J',13,2);
insert into formula values ('K',13,2);

insert into formula values ('D',14,1);
insert into formula values ('E',14,5);
insert into formula values ('F',14,5);
insert into formula values ('G',14,5);
insert into formula values ('H',14,2);

insert into formula values ('A',15,4);
insert into formula values ('F',15,1);
insert into formula values ('J',15,4);

insert into formula values ('A',16,5);
insert into formula values ('C',16,4);
insert into formula values ('F',16,4);
insert into formula values ('H',16,1);
insert into formula values ('I',16,3);
insert into formula values ('J',16,3);

insert into formula values ('A',17,1);
insert into formula values ('B',17,2);
insert into formula values ('E',17,1);
insert into formula values ('G',17,1);
insert into formula values ('I',17,1);
insert into formula values ('J',17,5);
insert into formula values ('K',17,5);

insert into formula values ('A',18,2);
insert into formula values ('C',18,5);
insert into formula values ('E',18,1);
insert into formula values ('F',18,1);
insert into formula values ('G',18,2);
insert into formula values ('I',18,5);

insert into formula values ('A',19,3);
insert into formula values ('J',19,3);
insert into formula values ('K',19,3);

insert into formula values ('A',20,3);
insert into formula values ('I',20,1);
insert into formula values ('J',20,3);

insert into formula values ('A',21,4);
insert into formula values ('B',21,5);
insert into formula values ('C',21,5);
insert into formula values ('D',21,1);
insert into formula values ('F',21,2);
insert into formula values ('I',21,2);
insert into formula values ('J',21,1);
insert into formula values ('K',21,2);

insert into formula values ('A',22,3);
insert into formula values ('B',22,2);
insert into formula values ('E',22,3);
insert into formula values ('F',22,2);
insert into formula values ('G',22,2);
insert into formula values ('H',22,3);
insert into formula values ('J',22,3);
insert into formula values ('K',22,2);

/* Periodo 2014-2 */
insert into formula values ('A',23,5);
insert into formula values ('C',23,5);
insert into formula values ('F',23,2);
insert into formula values ('H',23,3);
insert into formula values ('I',23,3);

insert into formula values ('A',24,4);
insert into formula values ('C',24,4);
insert into formula values ('D',24,1);
insert into formula values ('F',24,1);
insert into formula values ('I',24,2);
insert into formula values ('J',24,2);
insert into formula values ('K',24,2);

insert into formula values ('D',25,1);
insert into formula values ('E',25,5);
insert into formula values ('F',25,5);
insert into formula values ('G',25,5);
insert into formula values ('H',25,2);

insert into formula values ('A',26,4);
insert into formula values ('F',26,1);
insert into formula values ('J',26,4);

insert into formula values ('A',27,5);
insert into formula values ('C',27,4);
insert into formula values ('F',27,4);
insert into formula values ('H',27,1);
insert into formula values ('I',27,3);
insert into formula values ('J',27,3);

insert into formula values ('A',28,1);
insert into formula values ('B',28,2);
insert into formula values ('E',28,1);
insert into formula values ('G',28,1);
insert into formula values ('I',28,1);
insert into formula values ('J',28,5);
insert into formula values ('K',28,5);

insert into formula values ('A',29,2);
insert into formula values ('C',29,5);
insert into formula values ('E',29,1);
insert into formula values ('F',29,1);
insert into formula values ('G',29,2);
insert into formula values ('I',29,5);

insert into formula values ('A',30,3);
insert into formula values ('J',30,3);
insert into formula values ('K',30,3);

insert into formula values ('A',31,3);
insert into formula values ('I',31,1);
insert into formula values ('J',31,3);

insert into formula values ('A',32,4);
insert into formula values ('B',32,5);
insert into formula values ('C',32,5);
insert into formula values ('D',32,1);
insert into formula values ('F',32,2);
insert into formula values ('I',32,2);
insert into formula values ('J',32,1);
insert into formula values ('K',32,2);

insert into formula values ('A',33,3);
insert into formula values ('B',33,2);
insert into formula values ('E',33,3);
insert into formula values ('F',33,2);
insert into formula values ('G',33,2);
insert into formula values ('H',33,3);
insert into formula values ('J',33,3);
insert into formula values ('K',33,2);

/* Periodo 2014-1 */
insert into formula values ('A',34,5);
insert into formula values ('C',34,5);
insert into formula values ('F',34,2);
insert into formula values ('H',34,3);
insert into formula values ('I',34,3);

insert into formula values ('A',35,4);
insert into formula values ('C',35,4);
insert into formula values ('D',35,1);
insert into formula values ('F',35,1);
insert into formula values ('I',35,2);
insert into formula values ('J',35,2);
insert into formula values ('K',35,2);

insert into formula values ('D',36,1);
insert into formula values ('E',36,5);
insert into formula values ('F',36,5);
insert into formula values ('G',36,5);
insert into formula values ('H',36,2);

insert into formula values ('A',37,4);
insert into formula values ('F',37,1);
insert into formula values ('J',37,4);

insert into formula values ('A',38,5);
insert into formula values ('C',38,4);
insert into formula values ('F',38,4);
insert into formula values ('H',38,1);
insert into formula values ('I',38,3);
insert into formula values ('J',38,3);

insert into formula values ('A',39,1);
insert into formula values ('B',39,2);
insert into formula values ('E',39,1);
insert into formula values ('G',39,1);
insert into formula values ('I',39,1);
insert into formula values ('J',39,5);
insert into formula values ('K',39,5);

insert into formula values ('A',40,2);
insert into formula values ('C',40,5);
insert into formula values ('E',40,1);
insert into formula values ('F',40,1);
insert into formula values ('G',40,2);
insert into formula values ('I',40,5);

insert into formula values ('A',41,3);
insert into formula values ('J',41,3);
insert into formula values ('K',41,3);

insert into formula values ('A',42,3);
insert into formula values ('I',42,1);
insert into formula values ('J',42,3);

insert into formula values ('A',43,4);
insert into formula values ('B',43,5);
insert into formula values ('C',43,5);
insert into formula values ('D',43,1);
insert into formula values ('F',43,2);
insert into formula values ('I',43,2);
insert into formula values ('J',43,1);
insert into formula values ('K',43,2);

insert into formula values ('A',44,3);
insert into formula values ('B',44,2);
insert into formula values ('E',44,3);
insert into formula values ('F',44,2);
insert into formula values ('G',44,2);
insert into formula values ('H',44,3);
insert into formula values ('J',44,3);
insert into formula values ('K',44,2);

/*---------------------------------------*/
/* Definicion de la Calificacion General */
/*---------------------------------------*/
/* Periodo 2015-2 */
/*
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Parcial 1',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Parcial 2',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Parcial 3',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Tarea 1',2);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Tarea 2',2);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Tarea 3',2);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Tarea 4',2);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Tarea 5',2);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Exposicion',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (1,'Proyecto',20);

insert into instrumento (asignatura, evaluacion, porcentaje) values (2,'Parcial 1',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (2,'Parcial 2',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (2,'Parcial 3',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (2,'Parcial 4',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (2,'Proyecto 1',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (2,'Proyecto 2',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (2,'Laboratorio',10);

insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Exposición Códigos Ética',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Exposición Riesgos',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Socialización 1',5);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Socialización 2',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Informe Noticias',5);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Informe Lectura (tema ensayo 1)',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Ensayo 1',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Ensayo Trabajo Final',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (3,'Exposición Trabajo Final',15);

insert into instrumento (asignatura, evaluacion, porcentaje) values (4,'Parcial I',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (4,'Parcial II',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (4,'Parcial III',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (4,'Proyecto I',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (4,'Talleres',20);

insert into instrumento (asignatura, evaluacion, porcentaje) values (5,'Parcial',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (5,'Proyecto',30);
insert into instrumento (asignatura, evaluacion, porcentaje) values (5,'Reportes',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (5,'Presentación y discusiones',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (5,'Tarea',5);
insert into instrumento (asignatura, evaluacion, porcentaje) values (5,'Talleres',20);

insert into instrumento (asignatura, evaluacion, porcentaje) values (6,'Tareas y Talleres',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (6,'Primer Parcial',30);
insert into instrumento (asignatura, evaluacion, porcentaje) values (6,'Segundo Parcial',30);
insert into instrumento (asignatura, evaluacion, porcentaje) values (6,'Proyecto',25);

insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Parcial I',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Parcial II',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Parcial III',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Proyecto I',15);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Proyecto II',18);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Tarea I',5);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Tarea II',5);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Tarea III',3);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Tarea IV',3);
insert into instrumento (asignatura, evaluacion, porcentaje) values (7,'Laboratorios',6);

insert into instrumento (asignatura, evaluacion, porcentaje) values (8,'Exam I',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (8,'Exam II',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (8,'Exam III',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (8,'Assignments',25);

insert into instrumento (asignatura, evaluacion, porcentaje) values (9,'Primer parcial',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (9,'Segundo parcial',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (9,'Tercer parcial',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (9,'Exámenes cortos y tareas',25);

insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Tareas, Trabajos y Quices',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Exposición',5);
insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Miniproyecto - Metodología Ágil',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Primer Parcial',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Segundo Parcial',20);
insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Proyecto Semestral - Primera Entrega - Requerimientos',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Proyecto Semestral - Segunda Entrega - Diseño',10);
insert into instrumento (asignatura, evaluacion, porcentaje) values (10,'Proyecto Semestral - Tercera Entrega - Desarrollo y pruebas',15);

insert into instrumento (asignatura, evaluacion, porcentaje) values (11,'Tareas, Trabajos y Quices',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (11,'Primer Parcial',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (11,'Segundo Parcial',25);
insert into instrumento (asignatura, evaluacion, porcentaje) values (11,'Tercer Parcial',25);
*/

/*------------------------------------*/
/* Definicion de la Calificacion ABET */
/*------------------------------------*/
insert into Descripcion_A_K (competencia, Nivel) values ('A',1);
insert into Descripcion_A_K (competencia, Nivel) values ('B',1);
insert into Descripcion_A_K (competencia, Nivel) values ('C',1);
insert into Descripcion_A_K (competencia, Nivel) values ('D',1);
insert into Descripcion_A_K (competencia, Nivel) values ('E',1);
insert into Descripcion_A_K (competencia, Nivel) values ('F',1);
insert into Descripcion_A_K (competencia, Nivel) values ('G',1);
insert into Descripcion_A_K (competencia, Nivel) values ('H',1);
insert into Descripcion_A_K (competencia, Nivel) values ('I',1);
insert into Descripcion_A_K (competencia, Nivel) values ('J',1);
insert into Descripcion_A_K (competencia, Nivel) values ('K',1);
--insert into porcentaje_abet values(ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id_Pregunta)
--insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
/* Periodo 2015-2 */
/*
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'A',80,1);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'C',0,2);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'F',10,3);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'H',10,4);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,1,'I',0,5);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,2,'A',30,6);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,2,'C',50,7);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,2,'F',10,8);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,2,'H',10,9);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,2,'I',0,10);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,3,'A',30,11);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,3,'C',50,12);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,3,'F',10,13);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,3,'H',10,14);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,3,'I',0,15);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,4,'A',50,16);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,4,'C',0,17);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,4,'F',5,18);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,4,'H',15,19);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,4,'I',30,20);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,5,'A',30,21);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,5,'C',0,22);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,5,'F',5,23);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,5,'H',15,24);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,5,'I',50,25);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,6,'A',15,26);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,6,'C',45,27);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,6,'F',5,28);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,6,'H',15,29);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,6,'I',20,30);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,7,'A',15,31);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,7,'C',45,32);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,7,'F',5,33);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,7,'H',15,34);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,7,'I',20,35);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,8,'A',15,36);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,8,'C',45,37);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,8,'F',5,38);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,8,'H',15,39);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,8,'I',20,40);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,9,'A',0,41);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,9,'C',0,42);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,9,'F',35,43);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,9,'H',65,44);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,9,'I',0,45);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,10,'A',15,46);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,10,'C',40,47);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,10,'F',20,48);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,10,'H',0,49);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (1,10,'I',25,50);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,11,'A',35,51);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,11,'C',40,52);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,11,'D',0,53);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,11,'F',0,54);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,11,'I',15,55);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,11,'J',10,56);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,11,'K',0,57);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,12,'A',25,58);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,12,'C',41,59);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,12,'D',0,60);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,12,'F',0,61);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,12,'I',14,62);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,12,'J',20,63);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,12,'K',0,64);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,13,'A',30,65);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,13,'C',27,66);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,13,'D',0,67);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,13,'F',0,68);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,13,'I',17,69);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,13,'J',26,70);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,13,'K',0,71);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,14,'A',70,72);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,14,'C',0,73);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,14,'D',0,74);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,14,'F',30,75);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,14,'I',0,76);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,14,'J',0,77);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,14,'K',0,78);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,15,'A',10,79);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,15,'C',20,80);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,15,'D',10,81);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,15,'F',3,82);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,15,'I',17,83);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,15,'J',10,84);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,15,'K',30,85);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,16,'A',10,86);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,16,'C',20,87);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,16,'D',15,88);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,16,'F',10,89);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,16,'I',10,90);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,16,'J',5,91);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,16,'K',30,92);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,17,'A',10,93);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,17,'C',18,94);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,17,'D',16,95);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,17,'F',10,96);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,17,'I',10,97);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,17,'J',16,98);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (2,17,'K',20,99);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,18,'D',15,100);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,18,'E',45,101);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,18,'F',20,102);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,18,'G',5,103);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,18,'H',15,104);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,19,'D',15,105);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,19,'E',20,106);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,19,'F',20,107);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,19,'G',25,108);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,19,'H',20,109);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,20,'D',0,110);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,20,'E',30,111);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,20,'F',20,112);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,20,'G',50,113);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,20,'H',0,114);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,21,'D',0,115);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,21,'E',60,116);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,21,'F',20,117);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,21,'G',0,118);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,21,'H',20,119);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,22,'D',0,120);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,22,'E',10,121);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,22,'F',10,122);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,22,'G',80,123);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,22,'H',0,124);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,23,'D',0,125);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,23,'E',0,126);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,23,'F',45,127);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,23,'G',30,128);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,23,'H',25,129);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,24,'D',0,130);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,24,'E',25,131);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,24,'F',30,132);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,24,'G',45,133);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,24,'H',0,134);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,25,'D',0,135);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,25,'E',25,136);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,25,'F',30,137);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,25,'G',45,138);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,25,'H',0,139);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,26,'D',15,140);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,26,'E',15,141);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,26,'F',20,142);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,26,'G',30,143);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (3,26,'H',20,144);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,27,'A',70,145);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,27,'F',20,146);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,27,'J',10,147);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,28,'A',50,148);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,28,'F',20,149);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,28,'J',30,150);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,29,'A',20,151);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,29,'F',10,152);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,29,'J',70,153);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,30,'A',50,154);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,30,'F',10,155);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,30,'J',40,156);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,31,'A',30,157);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,31,'F',0,158);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (4,31,'J',70,159);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,32,'A',25,160);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,32,'C',0,161);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,32,'F',0,162);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,32,'H',0,163);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,32,'I',0,164);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,32,'J',0,165);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,33,'A',0,166);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,33,'C',10,167);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,33,'F',0,168);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,33,'H',0,169);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,33,'I',5,170);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,33,'J',15,171);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,34,'A',0,172);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,34,'C',0,173);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,34,'F',10,174);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,34,'H',0,175);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,34,'I',0,176);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,34,'J',0,177);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,35,'A',0,178);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,35,'C',0,179);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,35,'F',10,180);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,35,'H',0,181);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,35,'I',0,182);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,35,'J',0,183);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,36,'A',0,184);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,36,'C',0,185);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,36,'F',0,186);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,36,'H',5,187);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,36,'I',0,188);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,36,'J',0,189);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,37,'A',0,190);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,37,'C',10,191);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,37,'F',0,192);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,37,'H',0,193);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,37,'I',10,194);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (5,37,'J',0,195);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,38,'A',6,196);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,38,'B',13,197);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,38,'E',6,198);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,38,'G',6,199);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,38,'I',13,200);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,38,'J',25,201);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,38,'K',31,202);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,39,'A',6,203);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,39,'B',13,204);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,39,'E',6,205);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,39,'G',6,206);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,39,'I',0,207);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,39,'J',38,208);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,39,'K',31,209);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,40,'A',6,210);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,40,'B',13,211);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,40,'E',6,212);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,40,'G',6,213);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,40,'I',0,214);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,40,'J',38,215);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,40,'K',31,216);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,41,'A',6,217);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,41,'B',13,218);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,41,'E',6,219);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,41,'G',6,220);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,41,'I',13,221);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,41,'J',25,222);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (6,41,'K',31,223);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,42,'A',15,224);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,42,'C',60,225);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,42,'E',0,226);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,42,'F',10,227);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,42,'G',15,228);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,42,'I',0,229);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,43,'A',35,230);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,43,'C',15,231);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,43,'E',0,232);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,43,'F',0,233);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,43,'G',0,234);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,43,'I',50,235);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,44,'A',10,236);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,44,'C',40,237);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,44,'E',0,238);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,44,'F',0,239);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,44,'G',0,240);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,44,'I',50,241);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,45,'A',0,242);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,45,'C',40,243);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,45,'E',10,244);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,45,'F',5,245);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,45,'G',15,246);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,45,'I',30,247);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,46,'A',0,248);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,46,'C',40,249);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,46,'E',10,250);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,46,'F',0,251);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,46,'G',10,252);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,46,'I',40,253);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,47,'A',0,254);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,47,'C',0,255);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,47,'E',20,256);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,47,'F',35,257);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,47,'G',45,258);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,47,'I',0,259);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,48,'A',0,260);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,48,'C',0,261);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,48,'E',20,262);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,48,'F',35,263);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,48,'G',45,264);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,48,'I',0,265);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,49,'A',90,266);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,49,'C',0,267);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,49,'E',0,268);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,49,'F',10,269);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,49,'G',0,270);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,49,'I',0,271);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,50,'A',30,272);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,50,'C',60,273);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,50,'E',0,274);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,50,'F',10,275);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,50,'G',0,276);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,50,'I',0,277);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,51,'A',0,278);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,51,'C',0,279);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,51,'E',0,280);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,51,'F',0,281);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,51,'G',0,282);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (7,51,'I',100,283);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,52,'A',100,284);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,52,'J',0,285);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,52,'K',0,286);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,53,'A',100,287);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,53,'J',0,288);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,53,'K',0,289);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,54,'A',70,290);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,54,'J',15,291);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,54,'K',15,292);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,55,'A',0,293);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,55,'J',50,294);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (8,55,'K',50,295);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,56,'A',60,296);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,56,'I',0,297);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,56,'J',40,298);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,57,'A',60,299);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,57,'I',0,300);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,57,'J',40,301);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,58,'A',60,302);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,58,'I',0,303);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,58,'J',40,304);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,59,'A',30,305);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,59,'I',40,306);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (9,59,'J',30,307);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'A',36,308);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'B',28,309);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'C',20,310);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'D',0,311);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'F',10,312);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'I',0,313);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'J',6,314);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,60,'K',0,315);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'A',75,316);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'B',0,317);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'C',0,318);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'D',0,319);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'F',25,320);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'I',0,321);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'J',0,322);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,61,'K',0,323);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'A',0,324);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'B',30,325);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'C',20,326);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'D',15,327);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'F',10,328);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'I',15,329);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'J',0,330);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,62,'K',10,331);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'A',35,332);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'B',55,333);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'C',0,334);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'D',0,335);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'F',10,336);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'I',0,337);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'J',0,338);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,63,'K',0,339);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'A',20,340);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'B',0,341);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'C',70,342);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'D',0,343);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'F',10,344);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'I',0,345);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'J',0,346);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,64,'K',0,347);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'A',0,348);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'B',60,349);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'C',0,350);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'D',10,351);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'F',10,352);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'I',20,353);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'J',0,354);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,65,'K',0,355);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'A',0,356);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'B',0,357);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'C',44,358);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'D',8,359);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'F',0,360);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'I',15,361);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'J',33,362);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,66,'K',0,363);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'A',0,364);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'B',0,365);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'C',0,366);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'D',8,367);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'F',7,368);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'I',30,369);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'J',0,370);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (10,67,'K',55,371);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'A',36,372);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'B',28,373);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'E',20,374);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'F',0,375);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'G',10,376);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'H',0,377);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'J',6,378);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,68,'K',0,379);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'A',75,380);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'B',0,381);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'E',0,382);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'F',0,383);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'G',25,384);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'H',0,385);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'J',0,386);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,69,'K',0,387);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'A',0,388);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'B',30,389);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'E',20,390);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'F',15,391);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'G',10,392);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'H',15,393);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'J',0,394);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,70,'K',10,395);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'A',35,396);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'B',55,397);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'E',0,398);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'F',0,399);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'G',10,400);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'H',0,401);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'J',0,402);
insert into porcentaje_abet (ASIGNATURA, EVALUACION, Id_COMPETENCIA, PORCENTAJE, Id) values (11,71,'K',0,403);
*/


/*----------*/
/* Usuarios */
/*----------*/
insert into usuario values ('jfe','Jorge Francisco Estela','123',4);
insert into usuario values ('Mod','Jorge Francisco Estela','123',2);
insert into usuario values ('gsarria', 'Gerardo M. Sarria M.', '123',4);
insert into usuario values ('admin', 'Admin', 'mlp123', 1);

/*---------*/
/* Pruebas */
/*---------*/
/* Prueba: Estudiantes (Ya se hace con los web services*/
insert into estudiante values ('100001','Pepito Perez',1);
insert into estudiante values ('200002','Pepita Mendieta',1);
insert into estudiante values ('300001','Pepito Perez',2);
insert into estudiante values ('400002','Pepita Mendieta',2);
insert into estudiante values ('500001','Pepito Perez',3);
insert into estudiante values ('600002','Pepita Mendieta',3);
insert into estudiante values ('700001','Pepito Perez',4);
insert into estudiante values ('800002','Pepita Mendieta',4);
insert into estudiante values ('900001','Pepito Perez',5);
insert into estudiante values ('110002','Pepita Mendieta',5);
insert into estudiante values ('120001','Pepito Perez',6);
insert into estudiante values ('130002','Pepita Mendieta',6);
insert into estudiante values ('140001','Pepito Perez',7);
insert into estudiante values ('150002','Pepita Mendieta',7);
insert into estudiante values ('160001','Pepito Perez',8);
insert into estudiante values ('170002','Pepita Mendieta',8);
insert into estudiante values ('180001','Pepito Perez',9);
insert into estudiante values ('190002','Pepita Mendieta',9);
insert into estudiante values ('200001','Pepito Perez',10);
insert into estudiante values ('210002','Pepita Mendieta',10);
insert into estudiante values ('220001','Pepito Perez',11);
insert into estudiante values ('230002','Pepita Mendieta',11);

/* Prueba: Definicion de los porcentajes de los instrumentos */
insert into porcentaje_abet values (1,1,'A.1.1',25,3,'A');
insert into porcentaje_abet values (1,1,'A.1.3',25,3,'A');
insert into porcentaje_abet values (1,1,'A.2.2',50,3,'A');
insert into porcentaje_abet values (1,1,'F.2.1',30,3,'F');
insert into porcentaje_abet values (1,1,'F.5.2',70,3,'F');
insert into porcentaje_abet values (1,1,'H.1.5',45,3,8);
insert into porcentaje_abet values (1,1,'H.2.4',55,3,'H'); 

insert into porcentaje_abet values (1,2,'A.1.1',25,3,'A');
insert into porcentaje_abet values (1,2,'A.1.3',25,3,'A');
insert into porcentaje_abet values (1,2,'A.2.2',50,3,'A');
insert into porcentaje_abet values (1,2,'C.1.1',100,3,'C');
insert into porcentaje_abet values (1,2,'F.2.1',30,3,'F');
insert into porcentaje_abet values (1,2,'F.5.1',70,3,'F');
insert into porcentaje_abet values (1,2,'H.1.3',45,3,'H');
insert into porcentaje_abet values (1,2,'H.2.2',55,3,'H'); 



COMMIT;
