from DAOs.DAO import DAO
from model.usuario import Usuario

#cada entidade terá uma classe dessa, implementação bem simples.
class UsuarioDAO(DAO):
    
    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self, key: int, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario):
            super().add(key, usuario)

    def update(self, key: int, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and isinstance(key, int):
            super().update(key, usuario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)

    def generate_primery_key(self) -> int:

        usuarios = [usuario.id for usuario in super().get_all()]

        if len(usuarios) == 0:
            return 1

        return max(usuarios) + 1