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
                            self.excluir_investimento()
                        case 5:
                            break
                        case _:
                            print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {str(e)}")

    def adicionar_investimento(self):
        try:
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
                    self.__usuario.investimentos.pop()
                    return

            print("Investimento criado com sucesso!")

        except ValueError:
            print("Erro: Valor inválido informado.")
        except TypeError:
            print("Erro: Tipo de dado incorreto.")
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar o investimento: {str(e)}")


    def mostrar_saldo_string(self) -> float:
        return self.__saldo


    def lista_investimento_string(self) -> List[str]:
        return [(f"{investimento.ativo.nome} - Valor: R$ {investimento.valor:.2f} - Mês: {investimento.mes}"
                 f" - Ano: {investimento.ano}") for investimento in self.__usuario.investimentos]

    def excluir_investimento(self):
        if not self.__usuario.investimentos:
            print("Não há investimentos para excluir.")
            return

        self.__tela_investimento.mostrar_investimentos(self.lista_investimento_string())
        try:
            indice = int(input("Digite o número do investimento que deseja excluir: "))
            if 0 <= indice < len(self.__usuario.investimentos):
                investimento = self.__usuario.investimentos.pop(indice)

                if investimento.tipo_investimento.name == "CREDITO":
                    self.__saldo -= investimento.valor
                elif investimento.tipo_investimento.name == "DEBITO":
                    self.__saldo += investimento.valor

                print("Investimento excluído com sucesso.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")