from view.TelaAtivoFinanceiro import TelaAtivoFinanceiro
from model.ativo_financeiro import AtivoFinanceiro
from typing import List

class ControladorAtivoFinanceiro:
    def __init__(self):
        self.__ativos_financeiros = []
        self.__tela_ativo_financeiro = TelaAtivoFinanceiro()

    def executar(self):
        self.tela_inicial()

    def tela_inicial(self):
        try:
            while True:
                opcao_menu = self.__tela_ativo_financeiro.mostrar_tela_inicial()
                match int(opcao_menu):
                    case 1:
                        self.adicionar_ativo_financeiro()
                    case 2:
                        self.__tela_ativo_financeiro.mostrar_ativos_financeiros(self.lista_ativos_financeiros_string())
                    case 3:
                        break
                    case _:
                        self.__tela_ativo_financeiro.mostrar_erro("Operação não reconhecida, por favor digite uma opção válida")
        except ValueError:
            self.__tela_ativo_financeiro.mostrar_erro("Operação não reconhecida, por favor digite uma opção válida")
        except Exception as e:
            self.__tela_ativo_financeiro.mostrar_erro(f"Ocorreu um erro inesperado: {str(e)}")

    def adicionar_ativo_financeiro(self):
        try:
            classe, tipo, nome = self.__tela_ativo_financeiro.mostrar_cadastrar_novo_ativo_financeiro()

            if nome is None or nome.strip() == "":
                self.__tela_ativo_financeiro.mostrar_erro("O nome do Ativo Financeiro não pode ser vazio.")
                return

            if any(ativo.nome == nome for ativo in self.__ativos_financeiros):
                self.__tela_ativo_financeiro.mostrar_erro(f"Já existe esse Ativo Financeiro '{nome}'.")
                return

            novo_ativo = AtivoFinanceiro(classe, tipo, nome)
            self.__ativos_financeiros.append(novo_ativo)
            self.__tela_ativo_financeiro.mostrar_mensagem("Ativo Financeiro criado com sucesso!")

        except ValueError:
            self.__tela_ativo_financeiro.mostrar_erro("Erro: Valor inválido informado.")
        except TypeError:
            self.__tela_ativo_financeiro.mostrar_erro("Erro: Tipo de dado incorreto.")
        except Exception as e:
            self.__tela_ativo_financeiro.mostrar_erro(f"Ocorreu um erro ao adicionar o Ativo Financeiro: {str(e)}")

    def lista_ativos_financeiros_string(self) -> List[str]:
        return [ativo.nome for ativo in self.__ativos_financeiros]

    def get_ativos_financeiros(self) -> list:
        return self.__ativos_financeiros