from flask import jsonify, Blueprint, request
from app.mapping import UserSchema
from app.services import UserService

user = Blueprint('user', __name__)
service = UserService()
user_schema = UserSchema()

"""
Obtiene todas los Usuarios
"""
@user.route('/', methods=['GET'])
def all():
    resp = user_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene un usuario por id
"""
@user.route('/<int:id>', methods=['GET'])
def one(id):
    resp = user_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea un nuevo usuario
"""
@user.route('/', methods=['POST'])
def create():
    user = user_schema.load(request.json)
    resp = user_schema.dump(service.create(user))
    return resp, 201

"""
Actualiza un usuario existente
"""
@user.route('/<int:id>', methods=['PUT'])
def update(id):
    usuario = user_schema.load(request.json)
    resp = user_schema.dump(service.update(id, usuario))
    return resp, 200

"""
Elimina un usuario existente
"""
@user.route('/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Tarea eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la Tarea"
    return jsonify(msg), 204