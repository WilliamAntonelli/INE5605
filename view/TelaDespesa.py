from typing import List
from util.enums import TipoDespesa, TipoPagamento
from model.categoria import Categoria

class TelaDespesa:
    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em Despesa --------")
        print("(1) Cadastrar nova Despesa")
        print("(2) Alterar")
        print("(3) Mostrar todas as Despesas")
        print("(4) Excluir")
        print("(5) Relatórios")
        print("(6) Voltar para o Menu Principal")
        return input("Escolha uma opção: ")


    def mostrar_cadastrar_nova_despesa(self, categorias: List[Categoria])-> tuple[TipoDespesa,
    Categoria, str, float, TipoPagamento, str, str]:
        print("-------- Insira nova Despesa --------")

        while True:
            print("Tipos disponíveis:")
            for idx, c in enumerate(TipoDespesa):
                print(f"({idx}) - {c.name}")
            try:
                tipo_idx = int(input("Escolha o tipo de despesa: "))
                if 0 <= tipo_idx < len(TipoDespesa):
                    tipo = list(TipoDespesa)[tipo_idx]
                    print(f"Você escolheu: {tipo.name}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")


        while True:
            print("Categorias:")
            for idx, categoria in enumerate(categorias):
                print(f"({idx}) - {categoria.nome}")

            try:
                categoria_idx = int(input("Escolha a categoria: "))
                if 0 <= categoria_idx < len(categorias):
                    categoria = categorias[categoria_idx]
                    print(f"Você escolheu: {categoria.nome}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")


        local = input("Insira o local: ")
        valor = float(input("Insira o valor: "))


        while True:
            print("Tipos de pagamentos:")
            for idx, t in enumerate(TipoPagamento):
                print(f"({idx}) - {t.name}")
            try:
                forma_idx = int(input("Escolha o tipo de pagamento: "))
                if 0 <= forma_idx < len(TipoPagamento):
                    forma = list(TipoPagamento)[forma_idx]
                    print(f"Você escolheu: {forma.name}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

        tem_nota = input("Deseja adicionar nota fiscal a essa despesa? (s/n): ").strip().lower()
        if tem_nota == 's':
            codigo = input("Insira o codigo da nota fiscal: ")
            arquivo = input("Insira o arquivo: ")
        else:
            codigo = "Sem nota fiscal"
            arquivo = None

        return tipo, categoria, local, valor, forma, codigo, arquivo


    def mostrar_despesas(self, despesas: List[str]) -> None:
        print("-------- Despesas --------")

        for count, despesa in enumerate(despesas):
            print(f"Despesa ({(count)}) - {despesa}")

    def mostrar_menu_relatorios(self):
        print("-------- Relatórios em Despesa --------")
        print("(1) Total por Categoria")
        print("(2) Estatisticas (maior, menor e media)")
        print("(3) Voltar")
        return input("Escolha uma opção: ")


    def mostrar_relatorio_total_por_categoria(self, totais: dict):
        print("--------Total de Gastos por Categoria--------")
        for categoria, valor in totais.items():
            print(f"{categoria}: R$ {valor:.2f}")

    def mostrar_estatisticas_despesas(self, maior: float, menor: float, media: float):
        print("--------Estatísticas das Despesas--------")
        print(f"Maior despesa: R$ {maior:.2f}")
        print(f"Menor despesa: R$ {menor:.2f}")
        print(f"Média das despesas: R$ {media:.2f}")