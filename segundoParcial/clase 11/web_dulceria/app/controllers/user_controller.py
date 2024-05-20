from flask import Blueprint,request,jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

user=Blueprint("user",__name__)

@user.route("/register",methods=["POST"])
def register():
    data=request.json
    username=data.get("username")
    password=data.get("password")
    role=data.get("role")

    if not username or not password:
        return jsonify({"error":"Se requiere nombre de usuario y contraseña"}),400
    user=User.find_by_username(username)
    if user:
        return jsonify({"error":"El nombre de usuario ya existe"}), 400
    new_user=User(username,role,password)
    new_user.save()
    return jsonify({"message":"El usuario se creo exitosamente"}),201

@user.route("/login",methods=["POST"])
def login():
    data = request.json
    username=data.get("username")
    password=data.get("password")

    user=User.find_by_username(username)
    if user and check_password_hash(user.password_hash,password):
        access_token=create_access_token(
            identity={"username":username,"roles":user.roles}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error":"Credenciales invalidas"}),401