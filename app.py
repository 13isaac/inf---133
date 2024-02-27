from http.server import HTTPServer,SimpleHTTPRequestHandler
def run(server_class=HTTPServer,handler_class=SimpleHTTPRequestHandler):
    try:
        server_adress=('',8000)
        httpd=server_class(server_adress,handler_class)
        print('Iniciando servidor web en http://localhost:8000/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Pagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run()

