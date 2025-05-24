from model.meta import Meta
from model.despesa import Despesa
from model.investimento import Investimento
from typing import List

class ControladorUsuario:
    def __init__(self):
        self.metas: List[Meta] = []
        self.despesas: List[Despesa] = []
        self.investimentos: List[Investimento] = []