from functools import wraps

def my_decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la funcion")
        result=(func(args[0].upper(),**kwargs))
        print("Despues de llamar a la funcion")
        return result
    return wrapper

@my_decorador
def greet(name):
    """funcion para saludar a alguien"""
    print(f'Hola {name}!')

greet("Isaac")

print(greet.__name__)

print(greet.__doc__)

