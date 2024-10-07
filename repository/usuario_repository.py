
from entity.usuario import Usuario
from db import db

class UsuarioRepository:

    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()
    
    @staticmethod
    def create(data):
        novo_usuario = Usuario(
            nome = data['nome'],
            email = data['email'],
            senha = data['senha']
        )
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario
    
    @staticmethod
    def update(id, data):
        usuario = UsuarioRepository.get_by_id(id)
        if usuario:
            usuario.nome = data.get('nome', usuario.nome)
            usuario.email = data.get('email', usuario.email)
            usuario.senha = data.get('senha', usuario.senha)
            db.session.commit()
        return usuario
    
    @staticmethod
    def delete(id):
        usuario = UsuarioRepository.get_by_id(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        return usuario
