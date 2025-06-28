from DAOs.DAO import DAO
from model.investimento import Investimento

class InvestimentoDAO(DAO):
    def __init__(self):
        super().__init__('investimentos.pkl')

    def add(self, investimento: Investimento):
        if investimento is not None and isinstance(investimento, Investimento):
            super().add(id(investimento), investimento)

    def update(self, investimento: Investimento):
        if investimento is not None and isinstance(investimento, Investimento):
            super().update(id(investimento), investimento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)