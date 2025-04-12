from pessoa import Pessoa

class Familiar(Pessoa):
    def __init__(self, nome, profissao, idade, genero, parentesco, usuario):
        super().__init__(nome, profissao, idade, genero)
        self.__parentesco = parentesco
        self.__usuario = usuario

    @property
    def parentesco(self):
        return self.__parentesco

    @parentesco.setter
    def parentesco(self, parentesco):
        self.__parentesco = parentesco

    @property
    def usuario(self):
        return self.__usuario

    def exibir_familiar(self):
        return f"{self.exibir_dados()} | Parentesco: {self.__parentesco} "