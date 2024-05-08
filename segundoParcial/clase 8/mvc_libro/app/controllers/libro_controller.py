from flask import Blueprint, request, jsonify
from models.libro_model import Libro
from views.libro_view import render_libro_list, render_libro_detail


libro_bp = Blueprint("animal", __name__)

@libro_bp.route("/libros", methods=["GET"])
def get_libros():
    libros = Libro.get_all()
    return jsonify(render_libro_list(libros))

@libro_bp.route("/libros/<int:id>", methods=["GET"])
def get_libro(id):
    libro = Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error": "Libro no encontrado"}), 404

@libro_bp.route("/libros", methods=["POST"])
def create_libro():
    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    if titulo is None or autor is None or edicion is None or disponibilidad is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    libro = Libro(titulo=titulo, autor=autor, edicion=edicion,disponibilidad=bool(disponibilidad) )
    libro.save()

    return jsonify(render_libro_detail(libro)), 201


# Ruta para actualizar un animal existente
@libro_bp.route("/libros/<int:id>", methods=["PUT"])
def update_animal(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    libro.update(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=bool(disponibilidad))

    return jsonify(render_libro_detail(libro))

@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    libro.delete()
    
    return "", 204
