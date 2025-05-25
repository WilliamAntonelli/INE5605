from typing import List
from util.enums import ClasseAtivo, TipoAtivo

class TelaAtivoFinanceiro:
    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em Ativo Financeiro --------")
        print("(1) Cadastrar novo Ativo Financeiro")
        print("(2) Listar Ativos Financeiros")
        print("(3) Voltar para o Menu Principal")
        return input("Escolha uma opção: ")


    def mostrar_cadastrar_novo_ativo_financeiro(self) -> tuple[TipoAtivo, ClasseAtivo, str]:
        print("-------- Insira novo Ativo Financeiro --------")

        while True:
            print("Classes disponíveis:")
            for indice, classe in enumerate(ClasseAtivo):
                print(f"({indice}) - {classe.name}")
            try:
                classe_por_indice = int(input("Escolha a classe do ativo: "))
                if 0 <= classe_por_indice < len(ClasseAtivo):
                    classe = list(ClasseAtivo)[classe_por_indice]
                    print(f"Você escolheu: {classe.name}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

        while True:
            print("Tipos disponíveis:")
            for indice, tipo in enumerate(TipoAtivo):
                print(f"({indice}) - {tipo.name}")
            try:
                tipo_por_indice = int(input("Escolha o tipo do ativo: "))
                if 0 <= tipo_por_indice < len(TipoAtivo):
                    tipo = list(TipoAtivo)[tipo_por_indice]
                    print(f"Você escolheu: {tipo.name}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

        nome = input("Insira o nome do ativo: ")

        return classe, tipo, nome


    def mostrar_ativos_financeiros(self, ativos_financeiros: List[str]) -> None:
        print("-------- Ativos Financeiros --------")

        for indice, ativo_financeiro in enumerate(ativos_financeiros):
            print(f"Ativos Financeiros({(indice)}) - {ativo_financeiro}")
