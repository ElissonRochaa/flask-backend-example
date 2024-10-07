from repository.usuario_repository import UsuarioRepository

class UsuarioService:

    @staticmethod
    def get_all_usuario():
        usuarios = UsuarioRepository.get_all()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def get_usuario_by_id(id):
        usuario = UsuarioRepository.get_by_id(id)
        return usuario.to_dict() if usuario else None