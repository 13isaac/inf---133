from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation

#Clase estudiante para definir que tipo de atributos van a tener los objetos de tipo estudiante 
class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()

#en esta clase se definen las consultas
class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiante_por_id = Field(Estudiante, id=Int())
    estudiante_nombre_apellido=Field(Estudiante, nombre=String(),apellido=String())
    estudiante_carrera=List(Estudiante, carrera=String())

    def resolve_estudiante_carrera(root,info,carrera):
        nuev=[]
        for i in estudiantes:
            if i.carrera == carrera:
                nuev.append(i)
        return nuev

    def resolve_estudiante_nombre_apellido(root,info,nombre,apellido):
        for i in estudiantes:
            if(i.nombre == nombre and i.apellido == apellido):
                return i
        return None

    def resolve_estudiantes(root,info):
        return estudiantes

    def resolve_estudiante_por_id(root, info, id):
        for estudiante in estudiantes:
            if estudiante.id == id:
                return estudiante
        return None
#esta clase es una mutacion para crear un nuevo estudiante
class CrearEstudiante(Mutation):
    class Arguments:
        nombre = String()
        apellido = String()
        carrera = String()

    estudiante = Field(Estudiante)#Fieldse utiliza en el código para definir los campos de un objeto GraphQL y especificar el tipo de datos que pueden contener esos campos.

    def mutate(root, info, nombre, apellido, carrera):#se ejecuta solo cuando se realice la mutacion
        nuevo_estudiante = Estudiante(
            id=len(estudiantes) + 1, 
            nombre=nombre, 
            apellido=apellido, 
            carrera=carrera
        )
        estudiantes.append(nuevo_estudiante)
        return CrearEstudiante(estudiante=nuevo_estudiante)#retorna una instancia de la clase CrearEstudiante, indicando que se a creado con exito el estudiante
#esta clase es una mutacion para eliminar un estudiante
class DeleteEstudiante(Mutation):
    class Arguments:
        id = Int()

    estudiante = Field(Estudiante)

    def mutate(root, info, id):
        for i, estudiante in enumerate(estudiantes):
            if estudiante.id == id:
                estudiantes.pop(i)
                return DeleteEstudiante(estudiante=estudiante)
        return None
    
class DeleteEstudianteArquitectura(Mutation):
    class Arguments:
        carrera=String()
    estudiante=Field(Estudiante)
    def mutate(root,info,carrera):
        for i, estudiante in enumerate(estudiantes):
            print("-------carrera----------",estudiante.carrera,"carreraatrib=",carrera)
            if estudiante.carrera == carrera:
                estudiantes.pop(i)
        return DeleteEstudianteArquitectura(estudiante=estudiante)

class ActualizarEstudiante(Mutation):
    class Arguments:
        id=Int()
        nombre=String()
        apellido=String()
        carrera=String()
    estudiante=Field(Estudiante)
    def mutate(root, info, id,nombre,apellido,carrera):
        for i, estudiante in enumerate(estudiantes):
            if(estudiante.id == id):
                estudiante.nombre=nombre
                estudiante.apellido=apellido
                estudiante.carrera=carrera
                return ActualizarEstudiante(estudiante=estudiante)
        return None
#esta clase define las mutaciones dicponibles, se las define como parte del esquema de graphQL
class Mutations(ObjectType):
    crear_estudiante = CrearEstudiante.Field()#se defina la mutacion crear_estudiante y se la asocia a la clase CrearEstudiante. al poner field() se crea un campo GraphQL para esta mutacion, osea que podemos ejecutar la mutacion crear_estudiante en el esquema GraphQL
    delete_estudiante = DeleteEstudiante.Field()
    actualizar_estudiante=ActualizarEstudiante.Field()
    delete_estudiante_arquitectura=DeleteEstudianteArquitectura.Field()

estudiantes = [
    Estudiante(id=1, nombre="Pedrito", apellido="García", carrera="Ingeniería de Sistemas"),
    Estudiante(id=2, nombre="Jose", apellido="Lopez", carrera="Arquitectura"),
    Estudiante(id=3, nombre="Mario", apellido="Choque", carrera="Arquitectura"),
]

schema = Schema(query=Query, mutation=Mutations)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            print(data)
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
