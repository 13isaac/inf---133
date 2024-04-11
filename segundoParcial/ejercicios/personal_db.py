import sqlite3

conn = sqlite3.connect("personal.db")

try :
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

try :
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")

try:
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        cargo_id INTEGER NOT NULL,
        departamento_id INTEGER NOT NULL,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (cargo_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (departamento_id) REFERENCES CARGOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")

try:
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")

conn.commit()

# Cerrar conexión
conn.close()

