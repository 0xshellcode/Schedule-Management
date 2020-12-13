DROP TABLE Cursos;
DROP TABLE Periodos;
DROP TABLE Salones;
DROP TABLE Horario;
DROP TABLE Reservaciones;

CREATE TABLE IF NOT EXISTS Salones (
 IDSalon VARCHAR(8),
 Capacidad INTEGER,
 Tipo VARCHAR(3),
 PRIMARY KEY (IDSalon),
 CONSTRAINT salones_tipo_check check (tipo in ('C', 'SC', 'A'))
);

CREATE TABLE IF NOT EXISTS Cursos(
 Clave VARCHAR(10),
 Secc INTEGER,
 Titulo VARCHAR(30) NOT NULL,
 Prof VARCHAR(30) NOT NULL,
 PRIMARY KEY (Clave, Secc)
);

CREATE TABLE IF NOT EXISTS Periodos(
 Titulo VARCHAR(20),
 Fechaini TIMESTAMP NOT NULL,
 Fechafin TIMESTAMP NOT NULL,
 PRIMARY KEY (Titulo)
);

Create Table IF NOT EXISTS Horario(
  Clave VARCHAR(10),
  Secc INTEGER,
  DiaSem INTEGER,
  Hora INTEGER,
  Minuto INTEGER,
  Duracion INTEGER,
  Periodo VARCHAR(30),
  Semestre INTEGER,
  IDSalon VARCHAR(8) REFERENCES Salones,
  PRIMARY KEY (Clave, Secc),
  FOREIGN KEY (Clave) REFERENCES Cursos(Clave),
  CONSTRAINT SEMESTRE_CK  CHECK (Semestre BETWEEN 1 AND 9),
  CONSTRAINT DIASEM_CK    CHECK (DiaSem   BETWEEN 1 AND 7),
  CONSTRAINT MINUTO_CK    CHECK (Minuto   BETWEEN 0 AND 29),
  CONSTRAINT HORA_CK      CHECK (Hora     BETWEEN 0 AND 23)
);


Create Table IF NOT EXISTS Reservaciones(
  IDSalon VARCHAR(8) REFERENCES Salones,
  Nombre VARCHAR(30) NOT NULL,
  FechaHora TIMESTAMP NOT NULL,
  Duracion INTEGER,
  PRIMARY KEY (IDSalon, FechaHora),
  FOREIGN KEY (IDSalon) REFERENCES Salones(IDSalon)
);

INSERT INTO Salones
VALUES ('CS107', 20, 'C');
INSERT INTO Salones
VALUES ('CN109', 23, 'C');
INSERT INTO Salones
VALUES ('CN113', 18, 'SC');
INSERT INTO Salones
VALUES ('IA104', 28, 'C');
INSERT INTO Salones
VALUES ('CN124', 20, 'C');
INSERT INTO Salones
VALUES ('NE111', 32, 'A');
INSERT INTO Salones
VALUES ('HU106', 50, 'A');
INSERT INTO Salones
VALUES ('CN125', 20, 'C');

-- Primavera

INSERT INTO Cursos
VALUES ('Lis2082', 1, 'Bases de datos', 'Zechinelli Martini');
INSERT INTO Cursos
VALUES ('Lis2082', 2, 'Bases de datos', 'Zechinelli Martini');
INSERT INTO Cursos
VALUES ('Lis2012', 1, 'Matematicas Discretas', 'Zobeida Guzman');
INSERT INTO Cursos
VALUES ('Lis2012', 2, 'Matematicas Discretas', 'Zobeida Guzman');
INSERT INTO Cursos
VALUES ('Lis2022', 1, 'Arquitecturas Computacionales', 'Oleg Starovstenko');
INSERT INTO Cursos
VALUES ('Lis2022', 2, 'Arquitecturas Computacionales', 'Gibran');
INSERT INTO Cursos
VALUES ('Lis2062', 1, 'Sistemas Operativos', 'Mireya Paredes');
INSERT INTO Cursos
VALUES ('Lis2062', 2, 'Sistemas Operativos', 'Ingrid Kirschning');
INSERT INTO Cursos
VALUES ('Lis2052', 1, 'Ecuaciones Diferenciales', 'Profesor Y');
INSERT INTO Cursos
VALUES ('Lis2052', 2, 'Ecuaciones Diferenciales', 'Profesor X');

-- Otoño

INSERT INTO Cursos
VALUES ('Lfa3082', 1, 'Analisis Numerico', 'Maxim Ivanov');
INSERT INTO Cursos
VALUES ('Lfa3082', 2, 'Analisis Numerico', 'Gerardo Arizmendi');
INSERT INTO Cursos
VALUES ('Lis3032', 1, 'Interaccion Humano-Computadora', 'Gerardo Ayala');
INSERT INTO Cursos
VALUES ('Lis3032', 2, 'Interaccion Humano-Computadora', 'Ofelia Cervantes');
INSERT INTO Cursos
VALUES ('Art0022', 1, 'Arte y Cultura de las Americas', 'Marisol Hernandez');
INSERT INTO Cursos
VALUES ('Art0012', 2, 'Arte, Historia y Cultura', 'Claudia Ivett');
INSERT INTO Cursos
VALUES ('Lis3052', 1, 'Practicas En La Profesion I', 'NA');
INSERT INTO Cursos
VALUES ('Lis3052', 2, 'Practicas En La Profesion I', 'NA');
INSERT INTO Cursos
VALUES ('Lrt3032', 1, 'Sistemas Embedidos', 'Gibran');
INSERT INTO Cursos
VALUES ('Lrt3032', 2, 'Sistemas Embedidos', 'Oleg Starovstenko');
INSERT INTO Cursos
VALUES ('Lis3042', 1, 'Teoria de la Computacion', 'Ingrid Kirschning');
INSERT INTO Cursos
VALUES ('Lis3042', 2, 'Teoria de la Computacion', 'Gerardo Ayala');



INSERT INTO Periodos
VALUES ('Otono 2020','2020-08-01' ,'2020-12-30');
INSERT INTO Periodos
VALUES ('Primavera 2020','2020-01-14' ,'2020-05-8');
-- INSERT INTO Periodos
-- VALUES ('Otono 2020','2020-08-7' ,'2020-12-11');
-- INSERT INTO Periodos
-- VALUES ('Primavera 2020','2020-01-01' ,'2020-05-30');


INSERT INTO Horario
VALUES('Lis2082', 1, 1, 11, 0, 50, 'Primavera 2020', 4, 'CN124');
INSERT INTO Horario
VALUES('Lis2012', 1, 2, 11, 30, 65, 'Primavera 2020', 4, 'CS107');
INSERT INTO Horario
VALUES('Lis2022', 1, 1, 9, 0, 50, 'Primavera 2020', 4, 'CN109');
INSERT INTO Horario
VALUES('Lis2062', 1, 2, 8, 30, 65, 'Primavera 2020', 4, 'IA104');
INSERT INTO Horario
VALUES('Lis2052', 1, 1, 15, 0, 50, 'Primavera 2020', 4, 'NE111');


INSERT INTO Reservaciones
VALUES('CN124', 'Zechinelli Martini', '2020-01-14 11:00:00', 50);
INSERT INTO Reservaciones
VALUES('CS107', 'Zobeida Guzman', '2020-01-15 11:30:00', 65);
INSERT INTO Reservaciones
VALUES('CN109', 'Oleg Starovstenko', '2020-01-14 09:00:00', 50);
INSERT INTO Reservaciones
VALUES('CN113', 'Oleg Starovstenko', '2020-01-18 09:00:00', 110);
INSERT INTO Reservaciones
VALUES('IA104', 'Mireya Paredes', '2020-01-15 08:30:00', 65);
INSERT INTO Reservaciones
VALUES('NE111', 'Profesor X', '2020-01-14 15:00:00', 50);
INSERT INTO Reservaciones
VALUES('CN125', 'Profesor Y', '2020-01-19 10:00:00', 60);
