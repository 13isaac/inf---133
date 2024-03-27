import requests

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_choco_data = {
    "cho_type": "tableta",
    "cho_sabor": "fresa",
    "cho_peso": 10
}
response = requests.post(url=url, json=new_choco_data, headers=headers)
print("--------------------")
print(response.json())

new_choco_data = {
    "cho_type": "bombon",
    "cho_sabor": "queso",
    "cho_peso": 25,
    "relleno": "clara"
}
response = requests.post(url=url, json=new_choco_data, headers=headers)
print("--------------------")
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print("--------------------")
print(response.json())

# PUT /deliveries/{vehicle_id}
choco_id_to_update = 1
updated_choco_data = {
    "cho_sabor": "banana"
}
response = requests.put(f"{url}/{choco_id_to_update}", json=updated_choco_data)
print("--------------------")
print("Chocolate actualizado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print("--------------------")
print(response.json())

# DELETE /deliveries/{vehicle_id}
choco_id_to_delete = 1
response = requests.delete(f"{url}/{choco_id_to_delete}")
print("--------------------")
print("Chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print("--------------------")
print(response.json())
