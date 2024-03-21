from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

# Base de datos simulada de publicaciones
db = {
    1: {
        "title": "Mi primera publicación",
        "content": "¡Hola mundo! Esta es mi primera publicación en el blog.",
    },
    2: {
        "title": "Otra publicación",
        "content": "¡Bienvenidos a mi blog! Aquí hay otra publicación.",
    },
}
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class BlogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar las cabeceras de respuesta

        # Generar la respuesta JSON de acuerdo a la solicitud
        if self.path == "/posts":
            self.wfile.write(json.dumps(list(db.values())).encode())
        elif self.path.startswith("/posts/"):
            post_id = int(self.path.split("/")[-1])
            post = db.get(post_id)
            if post:
                HTTPDataHandler.handle_response(self, 200, post)
            else:
                HTTPDataHandler.handle_response(self, 404, {"message": "Publicacion no encontrada"})
        else:
            HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})

    def do_POST(self):
        data = HTTPDataHandler.handle_reader(self)
        # Crear una nueva publicación
        if self.path == "/posts":
            title = data.get("title")
            content =data.get("content")
            new_post_id = max(db.keys()) + 1
            db[new_post_id] = {"title": title, "content": content}
            HTTPDataHandler.handle_response(self, 200, new_post_id)
        else:
            HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})

    def do_PUT(self):
        # Actualizar una publicación existente
        if self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                post_params = parse_qs(post_data.decode())
                db[post_id]["title"] = post_params.get("title", [db[post_id]["title"]])[
                    0
                ]
                db[post_id]["content"] = post_params.get(
                    "content", [db[post_id]["content"]]
                )[0]
                HTTPDataHandler.handle_response(self, 200, post_id)
            else:
                HTTPDataHandler.handle_response(self, 404, {"message": "Publicacion no encontrada"})
        else:
            HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})

    def do_DELETE(self):
        # Eliminar una publicación existente
        if self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                del db[post_id]
                HTTPDataHandler.handle_response(self, 200, {""})
            else:
                HTTPDataHandler.handle_response(self, 404, {"message": "Publicacion no encontrada"})
        else:
            HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})


def run_server(server_class=HTTPServer, handler_class=BlogHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
