from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
chocolates = {}


class Chocolates:
    def __init__(self, cho_type, cho_sabor, cho_peso, relleno):
        self.cho_type = cho_type
        self.cho_sabor = cho_sabor
        self.cho_peso = cho_peso
        self.relleno=relleno

class Tableta(Chocolates):
    def __init__(self, cho_sabor, cho_peso):
        super().__init__("tableta", cho_sabor, cho_peso, relleno=None)


class Bombon(Chocolates):
    def __init__(self, cho_sabor, cho_peso, relleno):
        self.relleno=relleno
        super().__init__("bombon", cho_sabor, cho_peso, relleno)

class Trufa(Chocolates):
    def __init__(self, cho_sabor, cho_peso, relleno):
        self.relleno=relleno
        super().__init__("trufa", cho_sabor, cho_peso, relleno)

class ChocolateFactory:
    @staticmethod
    def create_chocolate(cho_type, cho_sabor, cho_peso, relleno):
        if cho_type == "tableta":
            return Tableta(cho_sabor, cho_peso)
        elif cho_type == "bombon":
            return Bombon(cho_sabor, cho_peso, relleno)
        elif cho_type == "trufa":
            return Trufa(cho_sabor, cho_peso, relleno)
        else:
            raise ValueError("Tipo de chocolate no válido")

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

class ChocoService:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_chocolate(self, data):
        cho_type = data.get("cho_type", None)
        cho_sabor = data.get("cho_sabor", None)
        cho_peso = data.get("cho_peso", None)
        relleno = data.get("relleno", None)
        chocolate = self.factory.create_chocolate(
            cho_type, cho_sabor, cho_peso, relleno
        )
        if chocolates:
            clave, valor = chocolates.popitem()
            chocolates[clave] = valor
            chocolates[int(clave)+1]=chocolate
        else:
            chocolates[1] = chocolate
        return chocolate

    def list_chocolate(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_choco(self, chocolate_id, data):
        if chocolate_id in chocolates:
            chocolate = chocolates[chocolate_id]
            cho_sabor = data.get("cho_sabor", None)
            cho_peso = data.get("cho_peso", None)
            if cho_sabor:
                chocolate.cho_sabor = cho_sabor
            if cho_peso:
                chocolate.cho_peso = cho_peso
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            return None

class ChocolateRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.choco_service = ChocoService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.choco_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.choco_service.list_chocolate()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            choco_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.choco_service.update_choco(choco_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            choco_id = int(self.path.split("/")[-1])
            response_data = self.choco_service.delete_chocolate(choco_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()
