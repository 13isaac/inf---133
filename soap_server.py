from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

def suma_dos_numeros(a,b):
    return f'{a} + {b} = {(a+b)}'

def palindromo(palabra):
    palabra=palabra.replace(" ", "").lower()
    if (palabra==palabra[::-1]):
        return True
    else:
        return False

dispatcher=SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo":str},
    args={"nombre":str},
)

dispatcher.register_function(
    "SumaDosNumeros",
    suma_dos_numeros,
    returns={"suma_dos_numeros":str},
    args={"a":int,"b":int},
)

dispatcher.register_function(
    "CadenaPalindromo",
    palindromo,
    returns={"palindromo":bool},
    args={"palabra":str},
)

server=HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher=dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()