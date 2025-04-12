class Pessoa:
    def __init__(self, nome, profissao, idade, genero):
        self.__nome = nome
        self.__profissao = profissao
        self.__idade = idade
        self.__genero = genero

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    def exibir_dados(self):
        return f"Nome: {self.__nome} | Profissão: {self.__profissao} | Idade: {self.__idade} | Gênero: {self.__genero}"
