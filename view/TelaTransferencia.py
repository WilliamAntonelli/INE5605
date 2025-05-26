from typing import List

class TelaTransferencia:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em transferência ----------")

        print("(1) Cadastrar nova transferência")
        print("(2) Visualizar transferências")
        print("(3) Voltar")

        opcao_menu = input()
        return opcao_menu
    
    
    def mostrar_cadastrar_nova_tranferencia(self, familiares: List[dict]) -> set:

        print("-------- Escolha para qual familiar você quer transferir ----------")

        for count, familiar in enumerate(familiares):
            print(f"({count}): nome: {familiar["nome"]}, idade: {familiar["idade"]}")
        
        print(f"({len(familiares)}) Voltar a tela de transferências")
        familiar_escolhido = int(input("Qual familiar deseja alterar ?"))

        if familiar_escolhido == len(familiares): return familiar_escolhido, None

        valor = float(input("Digite o valor que deseja transferir"))
        return familiar_escolhido, valor

    
    def mostrar_transferencias(self, transferencias: List[dict]) -> None:

        print("-------- Suas transferências ----------")

        for count, transferencia in enumerate(transferencias):
            print(f"({count}) - Origem: {transferencia["origem"]}, destino: {transferencia["destino"]}, valor: {transferencia["valor"]}")
        
        print()