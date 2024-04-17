import requests

# URL del servidor Flask
url = 'http://localhost:5000/'

# Realizar una solicitud GET al servidor Flask
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
params = {'nombre': 'isaac'}
response = requests.get(url+'saludar', params=params)

# Verificar si la solicitud GET fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

##########################
response = requests.get(url+'/sumar?num1=5&num2=3')
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

########################################
response = requests.get(url+'/palindromo?cadena=reconocer')
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

############################################
response = requests.get(url+'/contar?cadena=exepciones&vocal=e')
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

