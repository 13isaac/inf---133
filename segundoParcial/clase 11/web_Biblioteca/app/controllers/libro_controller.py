from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.libro_model import Libro
from views import libro_view
from utils.decorators import role_required

libro_bp = Blueprint("libro", __name__)

@libro_bp.route("/libros", methods=["GET"])
@login_required
def get_libros():
    libros = Libro.get_all()
    return libro_view.list_libros(libros)

@libro_bp.route("/libros/create", methods=["GET", "POST"])
@login_required
@role_required(role=["admin"])
def create_libro():
    if request.method == "POST":
        if current_user.has_role("admin"):
            data = request.json
            titulo = data.get("titulo")
            autor = data.get("autor")
            edicion = data.get("edicion")
            disponibilidad = data.get("disponibilidad")
            libro = Libro(titulo=titulo, autor=autor, edicion=edicion,disponibilidad=bool(disponibilidad) )
            libro.save()
            flash("Libro creado exitosamente", "success")
            return redirect(url_for("libro.list_libros"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return libro_view.create_libro()

# Ruta para actualizar un animal existente
@libro_bp.route("/libros/<int:id>/update", methods=["PUT"])
@login_required
@role_required(role=["admin"])
def update_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        return "Libro no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            titulo = request.form("titulo")
            autor = request.form("autor")
            edicion = request.form("edicion")
            disponibilidad = request.form("disponibilidad")
            libro.update(titulo=titulo, autor=autor, edcion=edicion,disponibilidad=disponibilidad)
            flash("Libro actualizado exitosamente", "success")
            return redirect(url_for("libro.list_libros"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return libro_view.update_libro(libro)

@libro_bp.route("/libros/<int:id>/delete", methods=["DELETE"])
@role_required(role=["admin"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return "Libro no encotrado", 404
    
    if current_user.has_role("admin"):
        libro.delete()
        flash("Libro eliminado exitosamente", "success")
        return redirect(url_for("libro.list_libros"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
