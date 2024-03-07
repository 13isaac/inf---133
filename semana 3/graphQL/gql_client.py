import requests

# Definir la consulta GraphQL
query = """
    {
        estudiantes{
            nombre
        }
    }
"""
query2="""
    {
        estudiantes{
            nombre
            apellido
        }
    }
"""
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)
response2 = requests.post(url, json={'query': query2})
print(response2.text)
