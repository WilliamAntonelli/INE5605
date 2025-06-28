from model.investimento import Investimento
from view.TelaInvestimento import TelaInvestimento
from typing import List
from controller.ControladorAtivoFinanceiro import ControladorAtivoFinanceiro
from controller.ControladorUsuario import ControladorUsuario

class ControladorInvestimento:
    def __init__(self, controlador_ativo_financeiro, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__investimentos = []
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
                        self.__tela_investimento.mostrar_saldo(self.__saldo)
                    case 4:
                        self.excluir_investimento()
                    case 5:
                        break
                    case _:
                        self.__tela_investimento.mostrar_erro("Operação não reconhecida, por favor escolha uma opção válida.")
        except ValueError:
            self.__tela_investimento.mostrar_erro("Operação inválida, por favor escolha uma opção válida.")
        except Exception as e:
            self.__tela_investimento.mostrar_erro(f"Ocorreu um erro inesperado: {str(e)}")

    def adicionar_investimento(self):
        try:
            ativos = self.__ativos_financeiros.get_ativos_financeiros()

            if not ativos:
                self.__tela_investimento.mostrar_erro("Nenhum ativo cadastrado. Cadastre um ativo antes de criar um investimento.")
                return

            resultado = self.__tela_investimento.mostrar_cadastrar_novo_investimento(ativos)
            if resultado is None:
                return

            ativo, tipo, valor, mes, ano = resultado

            novo_investimento = Investimento(ativo, tipo, valor, mes, ano)
            self.__investimentos.append(novo_investimento)

            if tipo.name == "CREDITO":
                self.__saldo += valor
                self.__tela_investimento.mostrar_mensagem(f"CRÉDITO registrado. Valor: R$ {valor:.2f}")
            elif tipo.name == "DEBITO":
                if self.__saldo >= valor:
                    self.__saldo -= valor
                    self.__tela_investimento.mostrar_mensagem(f"DÉBITO registrado. Valor: R$ {valor:.2f}")
                else:
                    self.__tela_investimento.mostrar_erro("Saldo insuficiente para realizar o débito. Débito não registrado.")
                    self.__investimentos.pop()
                    return

            self.__tela_investimento.mostrar_mensagem("Investimento criado com sucesso!")

        except Exception as e:
            self.__tela_investimento.mostrar_erro(f"Erro ao adicionar investimento: {str(e)}")

    def lista_investimento_string(self) -> List[str]:
        return [
            f"{investimento.ativo.nome} | Tipo: {investimento.tipo_investimento.name} | Valor: R$ {investimento.valor:.2f} | Mês: {investimento.mes} | Ano: {investimento.ano}"
            for investimento in self.__investimentos
        ]

    def excluir_investimento(self):
        investimentos = self.__investimentos

        if not investimentos:
            self.__tela_investimento.mostrar_erro("Não há investimentos para excluir.")
            return

        lista_strings = self.lista_investimento_string()
        indice = self.__tela_investimento.selecionar_investimento_para_excluir(lista_strings)

        if 0 <= indice < len(investimentos):
            investimento = investimentos.pop(indice)

            if investimento.tipo_investimento.name == "CREDITO":
                self.__saldo -= investimento.valor
            elif investimento.tipo_investimento.name == "DEBITO":
                self.__saldo += investimento.valor

            self.__tela_investimento.mostrar_mensagem("Investimento excluído com sucesso.")
        else:
            self.__tela_investimento.mostrar_mensagem("Exclusão cancelada ou índice inválido.")