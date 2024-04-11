import sqlite3

conn = sqlite3.connect("personal.db")

print("\nINNER JOIN")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario 
    FROM EMPLEADOS
    JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id
    """
)
for row in cursor:
    print(row)

conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = 3
    WHERE id = 2
    """
)

conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)

conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)

conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)

conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS (cargo_id, departamento_id, nombres,apellido_paterno,apellido_materno,fecha_contratacion,fecha_creacion) 
    VALUES (3, 1, 'Carlos','Sanchez','Rodriguez','09-04-2024','09-04-2024')
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (2, 3500, '05-05-2023','05-012-2024.','05-05-2023')
    """
)

print("\nINNER JOIN")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_paterno, SALARIOS.salario 
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)


conn.commit()

# Cerrar conexión
conn.close()
