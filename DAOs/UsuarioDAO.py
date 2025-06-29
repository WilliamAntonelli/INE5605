from DAOs.DAO import DAO
from model.usuario import Usuario

#cada entidade terá uma classe dessa, implementação bem simples.
class UsuarioDAO(DAO):
    
    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self, key, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario):
            super().add(key, usuario)

    def update(self, key, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario):
            super().update(key, usuario)

    def get(self, key):
        return super().get(key)

    def get_current_user(self):

        user = super().get_all()
        if len(user) > 0:
            return list(user)[0]
        return None

    def remove(self, key: int):
        return super().remove(key)