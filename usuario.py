from pessoa import Pessoa
from familiar import Familiar

class Usuario(Pessoa):
    def __init__(self, nome, profissao, idade, genero, email, senha, renda):
        super().__init__(nome, profissao, idade, genero)
        self.__email = email
        self.__senha = senha
        self.__renda = renda
        self.__familiares = []
        self.__despesas = []

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def renda(self, renda):
        self.__renda = renda

    @property
    def familiares(self):
        return self.__familiares

    @property
    def despesas(self):
        return self.__despesas

    def adicionar_despesa(self, despesa):
        self.__despesas.append(despesa)

    def criar_familiar(self, nome, profissao, idade, genero, parentesco):
        familiar = Familiar(self, nome, profissao, idade, genero, parentesco)
        self.__familiares.append(familiar)
        return familiar

    def autenticar(self, senha_digitada):
        return self.__senha == senha_digitada