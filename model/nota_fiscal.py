
class NotaFiscal:
    def __init__(self, nome_arquivo, arquivo=None):
        self._nome_arquivo = nome_arquivo
        self._arquivo = arquivo

    @property
    def nome_arquivo(self):
        return self._nome_arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, value):
        self._nome_arquivo = value

    @property
    def arquivo(self):
        return self._arquivo

    @arquivo.setter
    def arquivo(self, value):
        self._arquivo = value
