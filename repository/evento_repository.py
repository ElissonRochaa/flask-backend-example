from entity.evento import Evento
from db import db

class EventoRepository:

    @staticmethod
    def get_all():
        return Evento.query.all()