class TelaTransferencia:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em transferência ----------")

        print("(1) Cadastrar nova transferência")
        print("(2) Listar todas as transferências")

        opcao_menu = input()
        return opcao_menu