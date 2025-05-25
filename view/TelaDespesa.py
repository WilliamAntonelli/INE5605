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
        print("(4) Mostrar despesas por mês")
        print("(5) Excluir")
        print("(6) Relatórios")
        print("(7) Voltar para o Menu Principal")
        return input("Escolha uma opção: ")


    def mostrar_cadastrar_nova_despesa(self, categorias: List[Categoria])-> tuple[TipoDespesa,
    Categoria, str, float, TipoPagamento, int, int, str, str]:
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

        while True:
            local = input("Insira o local: ").strip()
            if local:
                break
            else:
                print("O campo 'local' não pode estar em branco. Tente novamente.")

        while True:
            try:
                valor = float(input("Insira o valor: "))
                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("Valor inválido. Digite um número.")

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

        while True:
            try:
                mes = int(input("Insira o mês de referência (1 a 12): "))
                if 1 <= mes <= 12:
                    break
                else:
                    print("Mês inválido. Digite um número entre 1 e 12.")
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

        while True:
            try:
                ano = int(input("Insira o ano de referência (2000 a 2100): "))
                if 2000 <= ano <= 2100:
                    break
                else:
                    print("Ano inválido. Digite um número entre 2000 e 2100.")
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")


        tem_nota = input("Deseja adicionar nota fiscal a essa despesa? (s/n): ").strip().lower()
        if tem_nota == 's':
            codigo = input("Insira o codigo da nota fiscal: ")
            arquivo = input("Insira o arquivo: ")
        else:
            codigo = "Sem nota fiscal"
            arquivo = None

        return tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo


    def mostrar_despesas(self, despesas: List[str]) -> None:
        print("-------- Despesas --------")

        for count, despesa in enumerate(despesas):
            print(f"Despesa ({(count)}) - {despesa}")

    def mostrar_despesas_e_selecionar(self, despesas: List[str]) -> int:
        print("-------- Selecione uma Despesa --------")
        for idx, d in enumerate(despesas):
            print(f"({idx}) - {d}")
        while True:
            try:
                escolha = int(input("Digite o número da despesa que deseja selecionar: "))
                if 0 <= escolha < len(despesas):
                    return escolha
                else:
                    print("Índice fora do intervalo. Tente novamente.")
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")


    def despesas_mes_ano(self) -> tuple[int, int]:
        while True:
            try:
                mes = int(input("Digite o mês (1 a 12): "))
                if 1 <= mes <= 12:
                    break
                else:
                    print("Mês inválido. Deve estar entre 1 e 12.")
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

        while True:
            try:
                ano = int(input("Digite o ano (2000 a 2100): "))
                if 2000 <= ano <= 2100:
                    break
                else:
                    print("Ano inválido. Deve estar entre 2000 e 2100.")
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

        return mes, ano


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