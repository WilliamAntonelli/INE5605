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
            for idx, c in enumerate(ClasseAtivo):
                print(f"({idx}) - {c.name}")
            try:
                classe_idx = int(input("Escolha a classe do ativo: "))
                if 0 <= classe_idx < len(ClasseAtivo):
                    classe = list(ClasseAtivo)[classe_idx]
                    print(f"Você escolheu: {classe.name}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

        while True:
            print("Tipos disponíveis:")
            for idx, t in enumerate(TipoAtivo):
                print(f"({idx}) - {t.name}")
            try:
                tipo_idx = int(input("Escolha o tipo do ativo: "))
                if 0 <= tipo_idx < len(TipoAtivo):
                    tipo = list(TipoAtivo)[tipo_idx]
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

        for count, ativo_financeiro in enumerate(ativos_financeiros):
            print(f"Ativos Financeiros({(count)}) - {ativo_financeiro}")
