from exceptions.InvalidInputException import InvalidInputException

class StringEmptyException(InvalidInputException):
    
    def __init__(self):
        super().__init__("Não foi possivel usar o dado digitado pois a string está vazia. Precisa conter pelo menos um charcter")
