
class NotaFiscal:
    def __init__(self, codigo: str, arquivo: str | None):
        self.__codigo = codigo
        self.__arquivo = arquivo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def arquivo(self):
        return self.__arquivo

    @arquivo.setter
    def arquivo(self, arquivo):
        self.__arquivo = arquivo
