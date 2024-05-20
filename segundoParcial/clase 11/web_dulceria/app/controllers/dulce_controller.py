#listar plnatas, listar por id, crear dulce,actualizar dulce, borrar dulce
from flask import Blueprint,request,jsonify
from views.dulce_view import render_dulce_list,render_dulce_detail
from utils.decorators import jwt_required,roles_required
from models.dulceria_model import Dulce

dulce=Blueprint("dulce",__name__)

@dulce.route("/dulces",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_dulces():
    dulces=Dulce.get_all()
    return jsonify(render_dulce_list(dulces))

@dulce.route("/dulces/<int:id>",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_dulce(id):
    dulce=Dulce.get_by_id(id)
    if not dulce:
        return jsonify({"error":"Dulce no encontrada"}),404
    return jsonify(render_dulce_detail(dulce))

@dulce.route("/dulces",methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_dulce():
    data=request.json
    marca=data.get("marca")
    peso=data.get("peso")
    sabor=data.get("sabor")
    origen=data.get("origen")

    if not marca or peso is None or not sabor or not origen:
        return jsonify({"error":"Faltan atributos requeridos"}),400
    
    dulce=Dulce(marca,peso,sabor,origen)
    dulce.save()
    return jsonify(render_dulce_detail(dulce)),201

@dulce.route("/dulces/<int:id>",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_dulce(id):
    dulce=Dulce.get_by_id(id)
    if not dulce:
        return jsonify({"error":"Dulce no encontrada"}),404
    data=request.json
    marca=data.get("marca")
    peso=data.get("peso")
    sabor=data.get("sabor")
    origen=data.get("origen")

    dulce.update(marca,peso,sabor,origen)
    return jsonify(render_dulce_detail(dulce)),200

@dulce.route("/dulces/<int:id>",methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_dulce(id):
    dulce=Dulce.get_by_id(id)
    if not dulce:
        return jsonify({"Error":"Dulce no encontrada"}),404
    
    dulce.delete()
    return "", 204