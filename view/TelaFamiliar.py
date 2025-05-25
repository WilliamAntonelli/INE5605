from util.enums import Parentesco
from typing import List

class TelaFamiliar:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em familiares ----------")

        print("(1) Cadastrar novo familiar")
        print("(2) Visualizar familiares")
        print("(3) Editar familiar")
        print("(4) Excluir familiar")
        print("(5) Voltar")

        opcao_menu = input()
        return opcao_menu
    
    def mostrar_cadastrar_novo_familiar(self) -> dict:
        nome = input("Digite o nome do familiar: ")
        profissao = input("Digite a profissão do familiar: ")
        idade = int(input("Digite a idade do familiar: "))
        genero = int(input("Digite 1 para homen e 2 para mulher, para escolher o gênero do familiar: "))
        for parentesco in Parentesco:
            print(f"({parentesco.codigo}) Digite o familiar que deseja adicionar {parentesco.descricao}")
        
        parentesco = int(input())
        

        novo_familiar = {
            "nome": nome,
            "profissao": profissao,
            "idade": idade,
            "genero": genero,
            "parentesco": parentesco
        }

        return novo_familiar
    

    def mostrar_informacoes_edit(self, familiares: List[dict]) -> None:

        for count, familiar in enumerate(familiares):
            print(f"({count}): {familiar.nome}")

        familiar_escolhido = int(input("Qual familiar deseja alterar ?"))

        print("-------- Qual dados do familiar deseja alterar ? ----------")
        print("(1) Nome: ")
        print("(2) Profissão: ")
        print("(3) Idade: ")
        print("(4) Gênero: ")
        print("(5) Parentesco: ")
        print("(6) Cancelar edição")
        
        opcao_menu = input("Qual o campo você deseja alterar ?")

        if int(opcao_menu) == 8:
             return opcao_menu, None
        
        novo_campo = input("Digite o novo valor: ")
        return familiar_escolhido, opcao_menu, novo_campo

    def mostrar_informacoes(self, familiares: List[dict]) -> None:

        print("-------- Dados dos familiares ----------")

        if len(familiares) == 0:
            print("Nenhum usuário cadastrado no momento\n")
            return
        
        for familiar in familiares:
            for key in familiar:
                print(f"{key}: {familiar[key]}")