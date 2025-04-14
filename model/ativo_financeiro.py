from model.investimento import Investimento
from util.enums import ClasseAtivo, TipoAtivo, TipoInvestimento


class AtivoFinanceiro:
    def __init__(self, classe, tipo, nome):
        self.__classe = None
        self.__tipo = None
        self.__nome = nome
        self.__valor = 0
        self.__investimentos = []

        self.classe = classe
        self.tipo = tipo

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, classe):

        if isinstance(classe, ClasseAtivo):
            self.__classe = classe
        else:
            raise Exception("Classe do Ativo inválido, coloque uma classe válida")

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):

        if isinstance(tipo, TipoAtivo):
            self.__tipo = tipo
        else:
            raise Exception("Tipo do Ativo inválido, coloque um tipo válido")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def saldo(self):
        return self.__valor

    @property
    def investimentos(self):
        return self.__investimentos

    def creditar_investimento(self, valor):
        investimento = Investimento(self, valor, TipoInvestimento.CREDITO)
        self.__investimentos.append(investimento)
        self.__valor += valor

    def debitar_investimento(self, valor):
        investimento = Investimento(self, valor, TipoInvestimento.DEBITO)
        self.__investimentos.append(investimento)
        self.__investimentos -= valor
