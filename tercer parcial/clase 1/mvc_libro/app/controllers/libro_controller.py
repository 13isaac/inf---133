from flask import Blueprint, request, jsonify
from app.models.libro_model import Libro
from app.views.libro_view import render_libro_list, render_libro_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from app.utils.decorators import jwt_required, role_required

libro_bp = Blueprint("libro", __name__)

@libro_bp.route("/libros", methods=["GET"])
@jwt_required
@role_required(roles=["admin", "user"])
def get_libros():
    libros = Libro.get_all()
    return jsonify(render_libro_list(libros))

@libro_bp.route("/libros/<int:id>", methods=["GET"])
@jwt_required
@role_required(roles=["admin", "user"])
def get_libro(id):
    libro = Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error": "Libro no encontrado"}), 404

@libro_bp.route("/libros", methods=["POST"])
@jwt_required
@role_required(roles=["admin"])
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
@jwt_required
@role_required(roles=["admin"])
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
@jwt_required
@role_required(roles=["admin"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    libro.delete()
    
    return "", 204
