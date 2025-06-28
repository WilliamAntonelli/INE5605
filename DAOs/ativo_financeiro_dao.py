from DAOs.DAO import DAO
from model.ativo_financeiro import AtivoFinanceiro

class AtivoFinanceiroDAO(DAO):
    def __init__(self):
        super().__init__('ativos_financeiros.pkl')

    def add(self, ativo: AtivoFinanceiro):
        if ativo is not None and isinstance(ativo, AtivoFinanceiro) and isinstance(ativo.nome, str):
            super().add(ativo.nome, ativo)

    def update(self, ativo: AtivoFinanceiro):
        if ativo is not None and isinstance(ativo, AtivoFinanceiro) and isinstance(ativo.nome, str):
            super().update(ativo.nome, ativo)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)