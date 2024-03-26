import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

# GET /pizzas
response = requests.get(url)
print(response.json())

# POST /pizzas 
mi_taco = {
    "base": "Tortilla",
    "guiso": "Pollo",
    "salsa": "Inglesa",
    "toppings": ["Papitas", "Queso"]
}
response = requests.post(url, json=mi_taco, headers=headers)
print("-----------------------------")
print(response.json())

# GET /pizzas
response = requests.get(url)
print("-----------------------------")
print(response.json())

# PUT /pizzas/1
edit_taco = {
    "base": "Masa",
    "guiso": "Tipico",
    "salsa": "Golf",
    "toppings": ["Maiz", "Ensalada"]
}
response = requests.put(url+"/1", json=edit_taco, headers=headers)
print("-----------------------------")
print(response.json())

# GET /pizzas
response = requests.get(url)
print("-----------------------------")
print(response.json())

# DELETE /pizzas/1

response = requests.delete(url + "/1")
print("-----------------------------")
print(response.json())

# GET /pizzas
response = requests.get(url)
print("-----------------------------")
print(response.json())
