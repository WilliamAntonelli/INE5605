from DAOs.DAO import DAO
from model.meta import Meta

class MetaDAO(DAO):
    def __init__(self):
        super().__init__('metas.pkl')

    def add(self, meta: Meta):
        if meta is not None and isinstance(meta, Meta):
            super().add(id(meta), meta)

    def update(self, meta: Meta):
        if meta is not None and isinstance(meta, Meta):
            super().update(id(meta), meta)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)