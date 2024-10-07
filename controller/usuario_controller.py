from flask import Blueprint, request, jsonify
from service.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('', methods=['GET'])
def get_usuarios():
    usuarios = UsuarioService.get_all_usuario()
    return jsonify(usuarios)

@usuario_bp.route('/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuario = UsuarioService.get_usuario_by_id(usuario_id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'message': 'Usuario não encontrado '}), 404