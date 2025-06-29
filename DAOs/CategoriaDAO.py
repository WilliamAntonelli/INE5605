from DAOs.DAO import DAO
from model.categoria import Categoria

class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categoria.pkl')

    def add(self, categoria: Categoria):
        if categoria is not None and isinstance(categoria, Categoria):
            super().add(id(categoria), categoria)

    def update(self, categoria: Categoria):
        if categoria is not None and isinstance(categoria, Categoria):
            super().update(id(categoria), categoria)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)