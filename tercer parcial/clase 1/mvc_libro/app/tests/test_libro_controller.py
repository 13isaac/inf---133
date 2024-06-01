def test_get_libros(test_client, auth_headers):
    response = test_client.get("/api/libros", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []

def test_create_libro(test_client, auth_headers):
    data = {"titulo":"Rey Leon","autor":"Vivaldi","edicion":"Primera","disponibilidad":False}
    response = test_client.post("/api/libros",json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["titulo"] == "Rey Leon"

def test_get_libro(test_client,auth_headers):
    data = {"titulo":"Principito","autor":"Guillermo","edicion":"Quinta","disponibilidad":True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.get(f"/api/animals/{libro_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["titulo"] == "Principito"

def test_update_libro(test_client, auth_headers):
    data = {"titulo":"El Tren","autor":"Hawkins","edicion":"Segunda","disponibilidad":True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    update_data = {"titulo":"El Tren","autor":"Hawkins","edicion":"Primera","disponibilidad":False}
    response = test_client.put(
        f"/api/libros/{libro_id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json["edicion"] == "Primera"
    assert response.json["disponibilidad"] == False

def test_delete_animal(test_client, auth_headers):
    data = {"titulo":"Manual","autor":"Constructor","edicion":"Ultima","disponibilidad":True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.delete(f"/api/libros/{libro_id}", headers=auth_headers)
    assert response.status_code == 204

    response = test_client.delete(f"/api/libros/{libro_id}", headers=auth_headers)
    assert response.status_code == 404