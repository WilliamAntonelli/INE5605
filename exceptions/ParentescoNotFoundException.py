from exceptions.DataNotFoundException import DataNotFoundException

class ParentescoNotFoundException(DataNotFoundException):
    
    def __init__(self):
        super().__init__("Não foi possivel localizar o parentesco escolhido. Coloque uma informação válida")