from DAOs.DAO import DAO
from model.despesa import Despesa

class DespesaDAO(DAO):
    def __init__(self):
        super().__init__('despesas.pkl')

    def add(self, despesa: Despesa):
        if despesa is not None and isinstance(despesa, Despesa):
            super().add(id(despesa), despesa)

    def update(self, despesa: Despesa):
        if despesa is not None and isinstance(despesa, Despesa):
            super().update(id(despesa), despesa)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)