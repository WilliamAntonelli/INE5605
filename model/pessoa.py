from util.enums import Genero
from abc import ABC, abstractmethod
from exceptions.InvalidInputException import InvalidInputException
from exceptions.StringEmptyException import StringEmptyException
from exceptions.GeneroNotFoundException import GeneroNotFoundException


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, profissao: str, idade: int, genero: Genero):
        self.__nome = ""
        self.__profissao = ""
        self.__idade = 0
        self.__genero = None

        self.nome = nome
        self.profissao = profissao
        self.idade = idade
        self.genero = genero


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):

        nome_valido = nome.strip()
        if len(nome_valido) == 0:
            raise StringEmptyException

        self.__nome = nome

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):

        profissao_valida = profissao.strip()
        if len(profissao_valida) == 0:
            raise StringEmptyException
    
        self.__profissao = profissao

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        
        idade = int(idade)
        if idade <= 0:
            raise InvalidInputException("Idade inválida, coloque uma idade válida")
        
        self.__idade = idade

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):

        if not isinstance(genero, Genero):
            raise GeneroNotFoundException
        
        self.__genero = genero

            
    def exibir_dados(self):
        return f"Nome: {self.__nome} | Profissão: {self.__profissao} | Idade: {self.__idade} | Gênero: {self.__genero.value}"
