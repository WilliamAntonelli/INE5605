from model.investimento import Investimento
from view.TelaInvestimento import TelaInvestimento
from typing import List
from controller.ControladorAtivoFinanceiro import ControladorAtivoFinanceiro
from controller.ControladorUsuario import ControladorUsuario

class ControladorInvestimento:
    def __init__(self, controlador_ativo_financeiro: ControladorAtivoFinanceiro, controlador_usuario: ControladorUsuario):
        self.__usuario = controlador_usuario
        self.__tela_investimento = TelaInvestimento()
        self.__ativos_financeiros = controlador_ativo_financeiro
        self.__saldo = 0

    def executar(self):
        self.tela_inicial()

    def tela_inicial(self):

            try:
                while True:
                    opcao_menu = self.__tela_investimento.mostrar_tela_inicial()
                    match int(opcao_menu):
                        case 1:
                            self.adicionar_investimento()
                        case 2:
                            self.__tela_investimento.mostrar_investimentos(self.lista_investimento_string())
                        case 3:
                            self.__tela_investimento.mostrar_saldo(self.mostrar_saldo_string())
                        case 4:
                            break
                        case _:
                            print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

    def adicionar_investimento(self):
        ativos = self.__ativos_financeiros.get_ativos_financeiros()

        if not ativos:
            print("Nenhum ativo cadastrado. Cadastre um ativo antes de criar um investimento.")
            return

        ativo, tipo, valor, mes, ano = self.__tela_investimento.mostrar_cadastrar_novo_investimento(ativos)

        novo_investimento = Investimento(ativo, tipo, valor, mes, ano)
        self.__usuario.investimentos.append(novo_investimento)

        if tipo.name == "CREDITO":
            self.__saldo += valor
            print(f"CRÉDITO registrado. Valor creditado: R$ {valor:.2f}")
        elif tipo.name == "DEBITO":
            if  self.__saldo >= valor:
                self.__saldo -= valor
                print(f"DÉBITO registrado. Valor debitado: R$ {valor:.2f}")
            else:
                print("Saldo insuficiente para realizar o débito. Débito não registrado.")
                self.__investimentos.pop()
                return

        print("Investimento criado com sucesso!")


    def mostrar_saldo_string(self) -> float:
        return self.__saldo


    def lista_investimento_string(self) -> List[str]:
        return [(f"{investimento.ativo.nome} - Valor: R$ {investimento.valor:.2f} - Mês: {investimento.mes}"
                 f" - Ano: {investimento.ano}") for investimento in self.__usuario.investimentos]