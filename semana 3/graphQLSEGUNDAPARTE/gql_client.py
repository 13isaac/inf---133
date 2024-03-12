import requests
#se pones graphql al
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print("-------lista antes de ser modificada---------")
print(response.text)

# Definir la consulta GraphQL con parametros
query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print("-------esudiante buscado por id---------")
print(response.text)

# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print("-------creacion de estudiante---------")
print(response_mutation.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print("-------lista despues de ser modificada---------")
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print("-------eliminando estudiante---------")
print(response_mutation.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print("-------lista despues de ser modificada---------")
print(response.text)

#----busqueda por nombre y apellido, Jose Lopez estudiante_nombre_apellido
query_nom_ap = """
    {
        estudianteNombreApellido(nombre: "Jose",apellido: "Lopez"){
            id
            nombre
            apellido
            carrera
        }
    }
"""
response_nom_ap = requests.post(url, json={'query': query_nom_ap})
print("-------esudiante buscado por nombre y apellido---------")
print(response_nom_ap.text)

#------------busqueda por carrera arquitectura, una lista entera, resolve_estudiante_carrera-----------
query_carrera="""
    {
        estudianteCarrera(carrera: "Arquitectura"){
            id
            nombre
            apellido
            carrera
        }
    }
"""
response_carrera=requests.post(url, json={'query': query_carrera})
print("-------esudiantes buscado por carrera---------")
print(response_carrera.text)

#-----------creando 3 estudiantes de la carrera de arquitectura----------
query_estu1="""
    mutation{
        crearEstudiante(nombre: "Carlos", apellido: "Barza", carrera: "Arquitectura"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
query_estu2="""
    mutation{
        crearEstudiante(nombre: "Alain", apellido: "Huanquita", carrera: "Arquitectura"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
query_estu3="""
    mutation{
        crearEstudiante(nombre: "Chavi", apellido: "Hernandez", carrera: "Arquitectura"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_crear_arqui = requests.post(url, json={'query': query_estu1})
response_crear_arqui = requests.post(url, json={'query': query_estu2})
response_crear_arqui = requests.post(url, json={'query': query_estu3})
response = requests.post(url, json={'query': query_lista})
print("-------lista despues de ser añadidos 3 estudiantes---------")
print(response.text)
#buscando estudiantes de la carrera de arquitectura
response_carrera=requests.post(url, json={'query': query_carrera})
print("-------esudiantes buscado por carrera---------")
print(response_carrera.text)

#actualizar los datos de los estudiantes mediante el id ActualizarEstudiante
query_actualizar="""
    mutation{
        actualizarEstudiante(id: 6, nombre: "Jhon", apellido: "Condori", carrera: "Derecho"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_act=requests.post(url, json={'query': query_actualizar})
print("-------esudiante actualizado---------")
print(response_act.text)
response = requests.post(url, json={'query': query_lista})
print("-------lista despues de actualizar un estudiante---------")
print(response.text)

#Realiza la consulta desde el cliente para actualizar la carrera del estudiante “Jose Lopez”, cambia su carrera por “Antropología”
query_nom_ap = """
    {
        estudianteNombreApellido(nombre: "Jose",apellido: "Lopez"){
            id
            nombre
            apellido
        }
    }
"""
response_nom_ap = requests.post(url, json={'query': query_nom_ap})
data = response_nom_ap.json()
id = int(data['estudianteNombreApellido']['id'])
nombre=str(data['estudianteNombreApellido']['nombre'])
apellido=str(data['estudianteNombreApellido']['apellido'])
print(id,"---------",nombre,"---------",apellido)
query_actualizar2 = f"""
    mutation{{
        actualizarEstudiante(id: {id}, nombre: "{nombre}", apellido: "{apellido}", carrera: "Antropologia"){{
            estudiante{{
                id
                nombre
                apellido
                carrera
            }}
        }}
    }}
"""
response_act2=requests.post(url, json={'query': query_actualizar2})
print("-------actualizacion de la carrera de Jose Lopez---------")
print(response_act2.text)
response = requests.post(url, json={'query': query_lista})
print("-------lista despues de actualizar la carrera de Jose Lopez---------")
print(response.text)

#Mutacion para eliminar todos los estudiantes de arquitectura DeleteEstudianteArquitectura
query_del_arqui = """
mutation {
        deleteEstudianteArquitectura(carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_del=requests.post(url, json={'query': query_del_arqui})
response = requests.post(url, json={'query': query_lista})
print("-------lista despues de eliminar a los estudiantes de arquitectura---------")
print(response.text)
print(response_del.text)




