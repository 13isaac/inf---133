# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask y la asigna a la variable 'app'.
# '__name__' es un parámetro especial que representa el nombre del módulo actual.
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)


# Este decorador asociará la función 'hello_world()' con la ruta raíz ('/') de la aplicación.
# Esto significa que cuando alguien acceda a la ruta raíz en el navegador, Flask ejecutará esta función.
@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

# Ruta para saludar utilizando el método GET.
@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

####################
@app.route("/sumar", methods=["GET"])
def sumar():
    a = request.args.get("num1")
    b = request.args.get("num2")
    if not (a and b):
        return (
            jsonify({"error": "Se requiere dos parámetros de la URL."}),
            400,
        )
    a=int(a)
    b=int(b)
    return jsonify({"mensaje": f"la suma es {a+b}"})

###################################################
@app.route("/palindromo", methods=["GET"])
def palindromo():
    palabra = request.args.get("cadena")
    if not palabra:
        return (
            jsonify({"error": "Se requiere una palabra en los parámetros de la URL."}),
            400,
        )
    c=palabra[::-1]
    if c==palabra:
        return jsonify({"mensaje": f"la palabra {palabra} es palindromo"})
    else:
        return jsonify({"mensaje": f"la palabra {palabra} no es palindromo"})
    
##################################################
@app.route("/contar", methods=["GET"])
def contar():
    palabra = request.args.get("cadena")
    vocal=request.args.get("vocal")
    if not palabra:
        return (
            jsonify({"error": "Se requiere la cadena de la URL."}),
            400,
        )
    if not vocal:
        return (
            jsonify({"error": "Se requiere la vocal de la URL."}),
            400,
        )
    contar_vocales = palabra.count(vocal)
    return jsonify({"mensaje": f"la palabra {palabra} tiene {contar_vocales} cantidad de {vocal}"})

##################################################################################

# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == "__main__":
    app.run()
