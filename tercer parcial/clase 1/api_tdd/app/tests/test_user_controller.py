def test_register_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 201


def test_register_duplicate_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 400
    assert response.json["error"] == "El nombre de usuario ya está en uso"


def test_login_user(test_client):
    user_credentials = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/login", json=user_credentials)
    assert response.status_code == 200

""" def test_rol_create(test_client):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol" """