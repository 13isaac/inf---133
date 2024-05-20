from flask import render_template
from flask_login import current_user

def list_libros(libros):
    return render_template(
        "libros.html",
        libros=libros,
        title="Lista de libros",
        current_user=current_user,
    )

def create_libro():
    return render_template(
        "create_libro.html", title="Crear Libro", current_user=current_user
    )


# La función `update_animal` recibe un libro
# y renderiza el template `update_animal.html`
def update_libro(libro):
    return render_template(
        "update_libro.html",
        title="Editar Libro",
        libro=libro,
        current_user=current_user,
    )