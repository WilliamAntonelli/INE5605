from typing import List

class TelaTransferencia:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em transferência ----------")

        print("(1) Cadastrar nova transferência")
        print("(2) Listar transferências")

        opcao_menu = input()
        return opcao_menu
    
    def mostrar_informacoes_familiares(self, familiares: List[dict]) -> None:
        print("-------- Escolha para qual familiar você quer transferir ----------")

        for familiar in familiares:
            for key in familiar:
                print(f"{key}: {familiar[key]}")