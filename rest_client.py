import requests

url="http://localhost:8000/"
#GET consulta a la ruta /lista_estudiantes
ruta_get=url+"lista_estudiantes"
get_response=requests.request(method="GET", url=ruta_get)
print(get_response.text)
#POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post=url+"agrega_estudiante"
nuevo_estudiante={
    "nombre":"Juanito",
    "apellido":"Pérez",
    "carrera":"Ingenieria Agronomica",
}

post_response=requests.request(method="POST",url=ruta_post,json=nuevo_estudiante)
print(post_response.text)

#-------buscar_nombre-----------
rutaGet_buscar=url+"buscar_nombre"
rutaGetB_response=requests.request(method="GET",url=rutaGet_buscar)
print(rutaGetB_response.text)

#-----------contar_carreras---------
rutaGET_contar=url+"contar_carreras"
rutaGETC_response=requests.request(method="GET",url=rutaGET_contar)
print(rutaGETC_response.text)

#--------total_estudiantes---------
rutaGET_total=url+"total_estudiantes"
rutaGETT_response=requests.request(method="GET",url=rutaGET_total)
print(rutaGETT_response.text)