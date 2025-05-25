from util.enums import TipoInvestimento


class Investimento:
    def __init__(self, ativo, tipo, valor, mes, ano):
        self.__ativo = ativo
        self.__tipo_investimento = tipo
        self.__valor = valor
        self.__mes = mes
        self.__ano = ano

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
    def valor(self, valor):
        self.__valor = valor

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def tipo_investimento(self):
        return self.__tipo_investimento

    @tipo_investimento.setter
    def tipo_investimento(self, tipo_investimento):

        if isinstance(tipo_investimento, TipoInvestimento):
            self.__tipo_investimento = tipo_investimento
        else:
            raise Exception("Tipo de investimento inválido, coloque um tipo válido")



