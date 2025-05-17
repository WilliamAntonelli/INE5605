from util.enums import Parentesco
from typing import List

class TelaFamiliar:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em familiares ----------")

        print("(1) Cadastrar novo familiar")
        print("(2) Visualizar familiares")
        print("(2) Editar familiar")
        print("(4) Voltar")

        opcao_menu = input()
        return opcao_menu
    
    def mostrar_cadastrar_novo_familiar(self) -> dict:
        nome = input("Digite o nome do familiar: ")
        profissao = input("Digite a profissão do familiar: ")
        idade = int(input("Digite a idade do familiar: "))
        genero = int(input("Digite 1 para homen e 2 para mulher, para escolher o gênero do familiar: "))
        for parentesco in Parentesco:
            print(f"Digite o familiar que deseja adicionar {parentesco.value}")
        
        parentesco = input()
        

        novo_familiar = {
            "nome": nome,
            "profissao": profissao,
            "idade": idade,
            "genero": genero,
            "parentesco": parentesco
        }

        return novo_familiar

    def mostrar_informacoes(self, familiares: List[dict]) -> None:
        print("-------- Dados dos familiares ----------")

        for familiar in familiares:
            for key in familiar:
                print(f"{key}: {familiar[key]}")