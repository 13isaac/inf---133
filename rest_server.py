from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes=[
    {
        "id":1,
        "nombre":"Pedrito",
        "apellido":"Garcia",
        "carrera":"Ingenieria de Sistemas",
    },
]

#GET debería utilizarse solo para solicitudes que no modifiquen datos (lectura), mientras que POST también se puede usar para modificar o agregar datos
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200) #indica que la respuesta a sido exitosa
            self.send_header('Content-type', 'application/json') #se envia el encabexado de la respuesta HTTP, como se indica que el tipo de respuesta sera un archivo json
            self.end_headers()#finaliza el envio del encabezado
            self.wfile.write(json.dumps(estudiantes).encode('utf-8')) #json.dumps(estudiantes) convierte la lista de estudiantes en formato JSON,('utf-8') codifica el JSON en bytes para poder escribirlo en el flujo de salida
        elif self.path == '/buscar_nombre':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            filtrados=list(filter(lambda x:x['nombre'][0]=='P',estudiantes))
            self.wfile.write(json.dumps(filtrados).encode('utf-8'))
        elif self.path == '/contar_carreras':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            carrera=[{estudiantes[0]['carrera']:0}]
            for i in estudiantes:
                clave=i['carrera']
                if clave in carrera[0]:
                    carrera[0][clave] += 1
                else:
                    carrera[0].update({clave:1})
            self.wfile.write(json.dumps(carrera).encode('utf-8'))
        elif self.path =='/total_estudiantes':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            cantidad=[{"cantidad":len(estudiantes)+1}]
            self.wfile.write(json.dumps(cantidad).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no existente"}).encode('utf-8'))

    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length=int(self.headers['Content-Length'])#Esta línea obtiene la longitud del contenido de la solicitud POST del encabezado Content-Length. El encabezado Content-Length indica la longitud en bytes del cuerpo de la solicitud
            post_data=self.rfile.read(content_length)# Aquí se lee el cuerpo de la solicitud POST utilizando el método read del objeto self.rfile
            post_data=json.loads(post_data.decode('utf-8')) #Esta línea decodifica el contenido de la solicitud, que está en formato JSON, utilizando la codificación UTF-8. Luego, se utiliza json.loads para convertir el contenido decodificado en un objeto Python
            post_data['id']=len(estudiantes)+1 #Aquí se agrega un nuevo campo "id" al objeto post_data. El valor del campo "id" se establece como el número total de estudiantes en la lista más uno, lo que garantiza que cada estudiante tenga un ID único
            estudiantes.append(post_data) #Esta línea agrega el objeto post_data, que representa al nuevo estudiante, a la lista de estudiantes existente.
            self.send_response(201) #Aquí se envía el código de respuesta HTTP 201, que indica que la solicitud POST fue exitosa y se creó un nuevo recurso.
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no existente"}).encode('utf-8'))

def run_server(port=8000):
    try:
        server_address=('',port)
        httpd=HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando el servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()