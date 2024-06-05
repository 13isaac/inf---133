import pytest

def test_get_libros(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener la lista de productos
    response = test_client.get("/api/libros", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder crear un nuevo producto
    data = {
        "titulo": "Principito",
        "autor": "Guillermo",
        "edicion": "Quinta",
        "disponibilidad": False,
    }
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["titulo"] == "Principito"
    assert response.json["autor"] == "Guillermo"
    assert response.json["edicion"] == "Quinta"
    assert response.json["disponibilidad"] == False


def test_get_libro(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener un producto específico
    # Este test asume que existe al menos un producto en la base de datos
    response = test_client.get("/api/libros/1", headers=admin_auth_headers)
    assert response.status_code == 200
    assert "titulo" in response.json


def test_get_nonexistent_libro(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar obtener un producto inexistente
    response = test_client.get("/api/libros/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_create_libro_invalid_data(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar crear un producto sin datos requeridos
    data = {"titulo": "El Tren"}  # Falta autor, edicion y disponibilidad
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_libro(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder actualizar un producto existente
    data = {
        "titulo": "El Tren",
        "autor": "Hawkins",
        "edicion": "Primera",
        "disponibilidad": True,
    }
    response = test_client.put("/api/libros/1", json=data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["titulo"] == "El Tren"
    assert response.json["autor"] == "Hawkins"
    assert response.json["edicion"] == "Primera"
    assert response.json["disponibilidad"] == True


def test_update_nonexistent_libro(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar actualizar un producto inexistente
    data = {
        "titulo": "Chocolate",
        "autor": "Paula",
        "edicion": "Segunda",
        "disponibilidad": False,
    }
    response = test_client.put(
        "/api/libros/999", json=data, headers=admin_auth_headers
    )
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_delete_libro(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder eliminar un producto existente
    response = test_client.delete("/api/libros/1", headers=admin_auth_headers)
    assert response.status_code == 204

    # Verifica que el producto ha sido eliminado
    response = test_client.get("/api/libros/1", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_delete_nonexistent_libro(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar eliminar un producto inexistente
    response = test_client.delete("/api/libros/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"
