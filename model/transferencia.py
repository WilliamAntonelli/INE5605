from model.familiar import Familiar
from model.usuario import Usuario
from exceptions.InvalidInputException import InvalidInputException


class Transferencia:
    def __init__(self, valor: float, usuario: Usuario, familiar: Familiar):
        self._valor = 0.0
        self._usuario = None
        self._familiar = None
        
        self.valor = valor
        self.usuario = usuario
        self.familiar = familiar

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):

        if value <= 0:
            raise InvalidInputException("Valor de tranferência inválido, coloque um valor válido")

        self._valor = value

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):

        if not isinstance(value, Usuario):
            raise InvalidInputException("Usuario inválido, coloque um usuario válido")

        self._usuario = value

    @property
    def familiar(self):
        return self._familiar

    @familiar.setter
    def familiar(self, value):

        if not isinstance(value, Familiar):
            raise InvalidInputException("Familiar inválido, coloque um familiar válido")
        
        self._familiar = value