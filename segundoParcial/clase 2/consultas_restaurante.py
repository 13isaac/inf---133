import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")


#actualizar el precio del plato con id2 a 9.99

print("\nACTUALIZANDO")
cursor=conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)

cursor=conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)

print("PLATOS ACTUALIZADO:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

cursor = conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE plato_id = 3
    """
)
print("PEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)
#todos los pedidos junto con los nombres de los platos y los numeros de mesa
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)

#Todos los platos que ha sido pedidos incluso los que no se han pedido

print("\nPEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio, MESAS.numero
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id
    LEFT JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id;
    """
)
for row in cursor:
    print(row)
