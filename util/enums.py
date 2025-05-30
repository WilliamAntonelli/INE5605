from enum import Enum
from exceptions.GeneroNotFoundException import GeneroNotFoundException
from exceptions.ParentescoNotFoundException import ParentescoNotFoundException

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
        
        raise GeneroNotFoundException

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
    OUTROS = "Outros"

class TipoInvestimento(Enum):
    DEBITO = "DEBITO"
    CREDITO = "CREDITO"

class Parentesco(Enum):
    FILHO = (1, "Filho(a)")
    MAE = (2, "Mãe")
    PAI = (3, "Pai")
    CONJUGE = (4, "Cônjuge")
    IRMAO = (5, "Irmão(ã)")
    AVO_MATERNO = (6, "Avô(ó) Materno(a)")
    AVO_PATERNAL = (7, "Avô(ó) Paterno(a)")
    TIO = (8, "Tio(a)")
    PRIMO = (9, "Primo(a)")
    ENTEADO = (10, "Enteado(a)")
    SOGRO = (11, "Sogro(a)")
    CUNHADO = (12, "Cunhado(a)")
    GENRO = (13, "Genro/Nora")
    NETO = (14, "Neto(a)")
    PADRASTO = (15, "Padrasto")
    MADRASTA = (16, "Madrasta")
    OUTRO = (99, "Outro")

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
        
        raise ParentescoNotFoundException