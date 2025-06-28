from DAOs.DAO import DAO
from model.transferencia import Transferencia

#cada entidade terá uma classe dessa, implementação bem simples.
class TransferenciaDAO(DAO):
    def __init__(self):
        super().__init__('transferencia.pkl')

    def add(self, key: int, transferencia: Transferencia):
        if transferencia is not None and isinstance(transferencia, Transferencia):
            super().add(key, transferencia)

    def update(self, key: int, transferencia: Transferencia):
        if transferencia is not None and isinstance(transferencia, Transferencia) and isinstance(key, int):
            super().update(key, transferencia)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)

    def generate_primery_key(self) -> int:

        transferencias = [transferencia.id for transferencia in super().get_all()]

        if len(transferencias) == 0:
            return 1

        return max(transferencias) + 1