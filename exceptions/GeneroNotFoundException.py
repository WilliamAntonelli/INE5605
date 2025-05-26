
from exceptions.DataNotFoundException import DataNotFoundException

class GeneroNotFoundException(DataNotFoundException):
    
    def __init__(self):
        super().__init__("Não foi possivel localizar o genero escolhido. Coloque uma informação válida")