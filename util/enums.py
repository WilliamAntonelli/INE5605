from enum import Enum

class Genero(Enum):
    MASCULINO = "Homen"
    FEMININO = "Mulher"

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
    FILHO = "Filho(a)"
    MAE = "Mâe"
    PAI = "Pai"
    CONJUGE = "Conjuge"
    OUTRO = "Outro"

