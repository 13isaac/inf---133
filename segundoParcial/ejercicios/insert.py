import sqlite3

conn = sqlite3.connect("personal.db")

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Ventas', '10-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Marketing', '11-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Gerente de Ventas', 'Senior', '10-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Analista de Marketing', 'Junior', '11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Representante de Ventas', 'Junior', '12-04-2020')
    """
)
# Consultar datos
conn.execute(
    """
    INSERT INTO EMPLEADOS (cargo_id, departamento_id, nombres,apellido_paterno,apellido_materno,fecha_contratacion,fecha_creacion) 
    VALUES (1, 1, 'Juan','Gonzales','Perez','15-05-2023','15-05-2023')
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS (cargo_id, departamento_id, nombres,apellido_paterno,apellido_materno,fecha_contratacion,fecha_creacion) 
    VALUES (2, 2, 'Maria','Lopez','Martinez','20-06-2023','20-06-2023,')
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (1, 3000, '01-04-2024','30-04-2025,','01-04-2024')
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (2, 3500, '01-07-2023','30-04-2024','01-07-2023')
    """
)


conn.commit()

# Cerrar conexión
conn.close()
