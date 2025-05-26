from model.familiar import Familiar
from model.usuario import Usuario
from exceptions.InvalidInputException import InvalidInputException


class Transferencia:
    def __init__(self, valor: float, usuario: Usuario, familiar: Familiar, mes, ano):
        self.__valor = 0.0
        self.__usuario = None
        self.__familiar = None
        self.__mes = 0
        self.__ano = 0
        
        self.valor = valor
        self.usuario = usuario
        self.familiar = familiar
        self.set_data(mes, ano)
        

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):

        if value <= 0:
            raise InvalidInputException("Valor de tranferência inválido, coloque um valor válido")

        self.__valor = value

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):

        if not isinstance(value, Usuario):
            raise InvalidInputException("Usuario inválido, coloque um usuario válido")

        self.__usuario = value

    @property
    def familiar(self):
        return self.__familiar

    @familiar.setter
    def familiar(self, value):

        if not isinstance(value, Familiar):
            raise InvalidInputException("Familiar inválido, coloque um familiar válido")
        
        self.__familiar = value

    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    def set_data(self, mes: int, ano: int):

        mes = int(mes)
        ano = int(ano)
        if mes < 1 or mes > 12 or ano < 2000 or ano > 2100:
            raise InvalidInputException("Data inválida, por favor coloque uma data válida")
        
        self.__mes = mes
        self.__ano = ano