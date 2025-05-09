from util.enums import TipoInvestimento


class Investimento:
    def __init__(self, ativo, valor, tipo_investimento):
        self.__ativo = ativo
        self.__valor = valor
        self.__tipo_investimento = None

        self.tipo_investimento = tipo_investimento

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, value):
        self.__ativo = value

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value

    @property
    def tipo_investimento(self):
        return self.__tipo_investimento

    @tipo_investimento.setter
    def tipo_investimento(self, tipo_investimento):

        if isinstance(tipo_investimento, TipoInvestimento):
            self.__tipo_investimento = tipo_investimento
        else:
            raise Exception("Tipo de investimento inválido, coloque um tipo válido")



