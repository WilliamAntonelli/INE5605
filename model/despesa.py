from model.nota_fiscal import NotaFiscal
from model.categoria import Categoria
from util.enums import TipoDespesa, TipoPagamento


class Despesa:
    def __init__(self, tipo_despesa, categoria_despesa, local, valor, tipo_pagamento):
        self.__tipo_despesa = None
        self.__categoria = None
        self.__local = local
        self.__valor = valor
        self.__tipo_pagamento = None
        self.__nota_fiscal = None

        self.tipo_despesa = tipo_despesa
        self.categoria = categoria_despesa
        self.tipo_pagamento = tipo_pagamento


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
    def local(self, value):
        self.__local = value

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value

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

    def adicionar_nota_fiscal(self, nome_nota, arquivo):
        nota = NotaFiscal(nome_nota, arquivo)
        self.__nota_fiscal = nota
