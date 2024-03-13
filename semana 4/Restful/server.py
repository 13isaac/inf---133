from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]


class EstudiantesService:
    @staticmethod #metodoo que no depende de el estado de la clase
    def buscar_estudiante(id):
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"] == id),
            None,
        )

    @staticmethod
    def actualizar_estudiante(id, data):  #metodo para actualizar estudiante 
        estudiante = EstudiantesService.buscar_estudiante(id)
        if estudiante:
            estudiante.update(data)
            return estudiantes
        else:
            return None
    
    @staticmethod 
    def buscar_estudiante_por_nombre(nombre): # metodo par a buscar estudinates mediante el nombre 
        return [
            estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre
        ]

    @staticmethod
    def borrar_estudiante(): #metodo para borrar estudiante
        estudiantes.clear()
        return estudiantes
    
    @staticmethod
    def añadir_estudiente(data): #metodo para añadir un nuevo estudiante
        data["id"] = len(estudiantes) + 1
        estudiantes.append(data)
        return estudiantes



class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data): #metodo para controlar las respuestas
        handler.send_response(status)   
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == "/estudiantes":
            if "nombre" in query_params:
                nombre = query_params["nombre"][0]
                estudiantes_filtrados = EstudiantesService.buscar_estudiante_por_nombre(nombre)
                if estudiantes_filtrados != []:
                    HTTPResponseHandler.handle_response(
                        self, 200, estudiantes_filtrados
                    )
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])
            else:
                HTTPResponseHandler.handle_response(self, 200, estudiantes)
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = EstudiantesService.buscar_estudiante(id)
            if estudiante:
                HTTPResponseHandler.handle_response(self, 200, [estudiante])
            else:
                HTTPResponseHandler.handle_response(self, 204, [])
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_POST(self):
        if self.path == "/estudiantes":
            data = self.read_data()
            estudiantes = EstudiantesService.añadir_estudiente(data)
            HTTPResponseHandler.handle_response(self, 201, estudiantes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_PUT(self):
        if self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            data = self.read_data()
            estudiantes = EstudiantesService.actualizar_estudiante(id, data)
            if estudiantes:
                HTTPResponseHandler.handle_response(self, 200, estudiantes)
            else:
                HTTPResponseHandler.handle_response(
                    self, 404, {"Error": "Estudiante no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_DELETE(self):
        if self.path == "/estudiantes":
            estudiantes = EstudiantesService.borrar_estudiante()
            HTTPResponseHandler.handle_response(self, 200, estudiantes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def read_data(self): #metodo para leer respuestas del servidor 
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
