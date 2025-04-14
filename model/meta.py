class Meta:
    def __init__(self, valor_objetivo, data_vencimento):
        self._valor_objetivo = valor_objetivo
        self._data_vencimento = data_vencimento

    @property
    def valor_objetivo(self):
        return self._valor_objetivo

    @valor_objetivo.setter
    def valor_objetivo(self, value):
        self._valor_objetivo = value

    @property
    def data_vencimento(self):
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, value):
        self._data_vencimento = value