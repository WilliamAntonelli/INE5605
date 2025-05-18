from model.ativo_financeiro import AtivoFinanceiro
from model.despesa import Despesa
from model.pessoa import Pessoa
from model.familiar import Familiar
from model.meta import Meta


class Usuario(Pessoa):

    def __init__(self, nome, profissao, idade, genero, email, senha, renda):
        super().__init__(nome, profissao, idade, genero)
        self.__email = email
        self.__senha = senha
        self.__renda = renda

        #----
        self.__familiares = []
        self.__metas = []
        self.__despesas = []
        self.__transferencias = []
        self.__ativos = []

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

    def adicionar_familiar(self, nome, profissao, idade, genero, parentesco):
        familiar = Familiar(nome, profissao, idade, genero, parentesco)
        self.__familiares.append(familiar)
        return familiar

    def excluir_familiar(self, nome):
        self.__familiares = [x for x in self.__familiares if x.nome != nome]

    @property
    def metas(self):
        return self.__metas

    def adicionar_meta(self, meta):
        if isinstance(meta,Meta):
            self.__metas.append(meta)
        else:
            raise Exception("Meta inválida, coloque um meta válida")

    @property
    def despesas(self):
        return self.__despesas

    def adicionar_despesa(self, despesa):
        if isinstance(despesa, Despesa):
            self.__despesas.append(despesa)
        else:
            raise Exception("Despesa inválida, coloque um despesa válida")

    def excluir_despesa(self, despesa):

        if isinstance(despesa, Despesa):
            self.__despesas.remove(despesa)
        else:
            raise Exception("Despesa inválida, coloque um despesa válida")

    @property
    def transferencias(self):
        return self.__familiares

    def adicionar_transferencia(self, valor, familiar):

        from model.transferencia import Transferencia

        if isinstance(familiar, Familiar):
            transferencia = Transferencia(valor, self, familiar)
            self.__transferencias.append(transferencia)
        else:
            raise Exception("Familiar inválida, coloque um familiar válido")

    def excluir_transferencia(self, transferencia):

        if isinstance(transferencia, Transferencia):
            self.__transferencias.remove(transferencia)
        else:
            raise Exception("Transferencia inválida, coloque um transferencia válida")


    @property
    def ativos(self):
        return self.__ativos

    def adicionar_ativo(self, ativo):

        if isinstance(ativo, AtivoFinanceiro):
            self.__ativos.append(ativo)
        else:
            raise Exception("Ativo inválido, coloque um ativo válido")

    def excluir_ativo(self, ativo):

        if isinstance(ativo, AtivoFinanceiro):
            self.__ativos.remove(ativo)
        else:
            raise Exception("Ativo inválido, coloque um ativo válido")

    def exibir_dados(self):
        return f"{super().exibir_dados()} | Renda: {self.__renda} | Email: {self.__email}"