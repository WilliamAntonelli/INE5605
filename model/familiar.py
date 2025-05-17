from model.pessoa import Pessoa
from util.enums import Parentesco


class Familiar(Pessoa):
    def __init__(self, nome, profissao, idade, genero, parentesco):
        super().__init__(nome, profissao, idade, genero)
        self.__parentesco = None

        self.parentesco = parentesco

    @property
    def parentesco(self):
        return self.__parentesco

    @parentesco.setter
    def parentesco(self, parentesco):
        if isinstance(parentesco, Parentesco):
            self.__parentesco = parentesco
        else:
            raise Exception("Parentesco inválido, coloque um tipo de parentesco válido")

    def exibir_dados(self):
        return f"{super().exibir_dados()} | Parentesco: {self.__parentesco} "