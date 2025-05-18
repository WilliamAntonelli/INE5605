from typing import List
from util.enums import TipoInvestimento
from model.ativo_financeiro import AtivoFinanceiro

class TelaInvestimento:
    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em Investimento --------")
        print("(1) Cadastrar novo Investimento")
        print("(2) Listar Investimentos")
        print("(3) Mostrar Saldo")
        print("(4) Voltar para o Menu Principal")
        return input("Escolha uma opção: ")

    def mostrar_cadastrar_novo_investimento(self, ativos_disponiveis: List[AtivoFinanceiro]) -> tuple[AtivoFinanceiro, TipoInvestimento, float]:
        print("-------- Insira novo Investimento --------")

        while True:
            print("Ativos Financeiros disponíveis:")
            for idx, ativo in enumerate(ativos_disponiveis):
                print(f"({idx}) - {ativo.nome}")

            try:
                ativo_idx = int(input("Escolha o ativo: "))
                if 0 <= ativo_idx < len(ativos_disponiveis):
                    ativo = ativos_disponiveis[ativo_idx]
                    print(f"Você escolheu: {ativo.nome}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

        while True:
            print("Tipos disponíveis:")
            for idx, t in enumerate(TipoInvestimento):
                print(f"({idx}) - {t.name}")
            try:
                tipo_idx = int(input("Escolha o tipo de investimento: "))
                if 0 <= tipo_idx < len(TipoInvestimento):
                    tipo = list(TipoInvestimento)[tipo_idx]
                    print(f"Você escolheu: {tipo.name}")
                    break
                else:
                    print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

        valor = float(input("Insira o valor: "))

        return ativo, tipo, valor

    def mostrar_saldo(self, saldo: float):
        print("-------- Saldo --------")
        print(f"Saldo atual: R$ {saldo:.2f}")


    def mostrar_investimentos(self, investimentos: List[str]) -> None:
        print("-------- Investimentos --------")

        if not investimentos:
            print("Nenhum investimento cadastrado.")

        for count, investimento in enumerate(investimentos):
            print(f"Investimento({count}) - {investimento}")
