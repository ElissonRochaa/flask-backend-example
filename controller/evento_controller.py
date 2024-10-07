from flask import Blueprint, request, jsonify
from service.evento_service import EventoService

evento_bp = Blueprint('evento', __name__)

@evento_bp.route('/evento', methods=['GET'])
def get_eventos():
    eventos = EventoService.get_all_usuario()
    return jsonify(eventos)

