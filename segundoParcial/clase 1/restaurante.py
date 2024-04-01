# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Crear tabla de PLATOS
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio DECIMAL NOT NULL,
    categoria TEXT NOT NULL);
    """
)

#Crear tabla de mesas
conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,    
    numero INTEGER NOT NULL);
    """
)

#crear tabla de PEDIDOS
conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id),
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id));
    """
)

#-----------------insertando a PLATOS-----------------------
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizaa', 10.99, 'Italiana') 
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa', 8.99, 'Americana') 
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Sushi', 12.99, 'JAPONESA') 
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensalada', 6.99, 'Vegetariana') 
    """
)
#-----------------insertando a MESAS-----------------------
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1) 
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2) 
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3) 
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4) 
    """
)
##-----------------insertando a PEDIDOS-----------------------
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (1, 2, 2, '2024-04-01') 
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (2, 3, 1, '2024-04-01') 
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (3, 1, 3, '2024-04-02') 
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (4, 4, 1, '2024-04-02') 
    """
)

print("\nPLATOS:")
cursor = conn.execute(
    "SELECT * FROM PLATOS"
)
for row in cursor:
    print(row)

print("\nMESAS:")
cursor = conn.execute(
    "SELECT * FROM MESAS"
)
for row in cursor:
    print(row)

print("\nPEDIDOS:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)
for row in cursor:
    print(row)

""" DELETE FROM MATRICULACION
WHERE id=1 """
