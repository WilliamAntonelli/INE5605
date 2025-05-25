from model.nota_fiscal import NotaFiscal
from util.enums import TipoDespesa, TipoPagamento
from model.categoria import Categoria


class Despesa:
    def __init__(self, tipo, categoria, local, valor, forma, mes, ano, codigo="Sem nota fiscal", arquivo=None):
        self.__tipo_despesa = tipo
        self.__categoria = categoria
        self.__local = local
        self.__valor = valor
        self.__mes = mes
        self.__ano = ano
        self.__tipo_pagamento = forma
        self.__nota_fiscal = NotaFiscal(codigo, arquivo)


    @property
    def tipo_despesa(self):
        return self.__tipo_despesa

    @tipo_despesa.setter
    def tipo_despesa(self, tipo_despesa):

        if isinstance(tipo_despesa, TipoDespesa):
            self.__tipo_despesa = tipo_despesa
        else:
            raise Exception("Tipo da Despesa inválido, coloque um tipo de despesa válido")


    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria_despesa):
        if isinstance(categoria_despesa, Categoria):
            self.__categoria = categoria_despesa
        else:
            raise Exception("Categoria da Despesa inválida, coloque uma categoria de despesa válida")

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local):
        self.__local = local

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
    def tipo_pagamento(self):
        return self.__tipo_pagamento

    @tipo_pagamento.setter
    def tipo_pagamento(self, tipo_pagamento):

        if isinstance(tipo_pagamento, TipoPagamento):
            self.__tipo_pagamento = tipo_pagamento
        else:
            raise Exception("Tipo Pagamento inválido, coloque um pagamento de despesa válido")

    @property
    def nota_fiscal(self):
        return self.__nota_fiscal

    def adicionar_nota_fiscal(self, codigo, arquivo):
        self.__nota_fiscal = NotaFiscal(codigo, arquivo)
