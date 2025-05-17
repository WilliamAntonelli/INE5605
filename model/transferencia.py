
class Transferencia:
    def __init__(self, valor, usuario, familiar):
        self._valor = valor
        self._usuario = usuario
        self._familiar = familiar

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):
        self._usuario = value

    @property
    def familiar(self):
        return self._familiar

    @familiar.setter
    def familiar(self, value):
        self._familiar = value