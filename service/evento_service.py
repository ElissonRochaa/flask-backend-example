from repository.evento_repository import EventoRepository

class EventoService:

    @staticmethod
    def get_events():
        return EventoRepository.get_all()
