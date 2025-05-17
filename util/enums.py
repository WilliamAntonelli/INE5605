from enum import Enum

class Genero(Enum):
    MASCULINO = (1, "Homen")
    FEMININO = (2, "Mulher")

    def __init__(self, codigo: int, descricao: str):
        self._codigo = codigo
        self._descricao = descricao

    @property
    def codigo(self):
        return self._codigo

    @property
    def descricao(self):
        return self._descricao
    
    @classmethod
    def get_by_codigo(cls, codigo: int):
        for item in cls:
            if item.codigo == codigo:
                return item
        return None

class TipoDespesa(Enum):
    FIXA = "Fixa"
    VARIAVEL = "Variável"
    IMPREVISTOS = "Imprevistos"

class TipoPagamento(Enum):
    CARTAO_CREDITO = "Cartão de cŕedito"
    CARTAO_DEBITO = "Cartão de débito"
    DINHEIRO = "Dinheiro"
    PIX = "PIX"
    BOLETO = "Boleto"

class ClasseAtivo(Enum):
    RENDA_FIXA = "Renda fixa"
    RENDA_VARIAVEL = "Renda variável"
    TESOURO_DIRETO = "Tesouro direto"

class TipoAtivo(Enum):
    ACAO = "Ação"
    FII = "Fundos imobiliários"

class TipoInvestimento(Enum):
    DEBITO = "DEBITO"
    CREDITO = "CREDITO"

class Parentesco(Enum):
    FILHO = "Filho(a)"
    MAE = "Mâe"
    PAI = "Pai"
    CONJUGE = "Conjuge"
    OUTRO = "Outro"

