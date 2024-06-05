def test_get_libros_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener la lista de productos
    response = test_client.get("/api/libros", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder crear un producto
    data = {"titulo": "Rebelion", "autor": "Cornejo", "edicion": "Segunda", "disponibilidad": False}
    response = test_client.post("/api/libros", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_get_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener un producto específico
    # Este test asume que existe al menos un producto en la base de datos
    response = test_client.get("/api/libros/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "titulo" in response.json
    assert "autor" in response.json
    assert "edicion" in response.json
    assert "disponibilidad" in response.json


def test_update_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder actualizar un producto
    data = {"titulo": "Calculo 1", "autor": "Stward", "edicion": "Primera", "disponibilidad": True}
    response = test_client.put("/api/libros/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder eliminar un producto
    response = test_client.delete("/api/libros/1", headers=user_auth_headers)
    assert response.status_code == 403