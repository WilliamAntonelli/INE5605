from typing import List
from util.enums import Parentesco

class TelaTransferencia:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em transferência ----------")

        print("(1) Cadastrar nova transferência")
        print("(2) Visualizar transferências")
        print("(3) Visualizar transferências por mês e ano")
        print("(4) Visualizar transferências por parentesco")
        print("(5) Voltar")

        opcao_menu = input()
        return opcao_menu
    
    def mostrar_cadastrar_nova_tranferencia(self, familiares: List[dict]) -> set:

        print("-------- Escolha para qual familiar você quer transferir ----------")

        for count, familiar in enumerate(familiares):
            print(f'({count}): nome: {familiar["nome"]}, idade: {familiar["idade"]}')
        
        print(f"({len(familiares)}) Voltar a tela de transferências")
        familiar_escolhido = int(input("Para qual familiar deseja enviar ? "))

        if familiar_escolhido == len(familiares): return familiar_escolhido, None, None, None

        valor = float(input("Digite o valor que deseja transferir: "))
        mes = int(int(input("Mês da transfêrencia (1-12): ")))
        ano = int(input('Ano da transferência: '))
        return familiar_escolhido, valor, mes, ano
    
    def mostrar_transferencias(self, transferencias: List[dict]) -> None:

        print("-------- Suas transferências ----------")

        for count, transferencia in enumerate(transferencias):
            print(f'({count}) - Origem: {transferencia["origem"]}, destino: {transferencia["destino"]}, valor: {transferencia["valor"]}, data: {transferencia["mes"]}/{transferencia["ano"]}')
        
        print()

    def mostrar_filtro_mes_ano_transferencias(self) -> tuple:

        print("-------- Seus filtros para transferências ----------")

        mes = int(int(input("Mês da transfêrencia (1-12): ")))
        ano = int(input('Ano da transferência: '))

        return mes, ano
    
    def mostrar_filtro_parentesco_transferencias(self) -> tuple:


        print("-------- Escolha para qual familar você deseja ver as transferências ----------")

        for parentesco in Parentesco:
            print(f"({parentesco.codigo}) - {parentesco.descricao}")
        
        parentesco = int(input("Para qual familiar deseja enviar ? "))
        return parentesco