from view.TelaAtivoFinanceiro import TelaAtivoFinanceiro
from model.ativo_financeiro import AtivoFinanceiro
from DAOs.ativo_financeiro_dao import AtivoFinanceiroDAO
from typing import List

class ControladorAtivoFinanceiro:
    def __init__(self):
        self.__ativo_DAO = AtivoFinanceiroDAO()
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
                        self.lista_ativos_financeiros()
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

            if self.__ativo_DAO.get(nome):
                self.__tela_ativo_financeiro.mostrar_erro(f"Já existe um Ativo Financeiro com o nome '{nome}'.")
                return

            novo_ativo = AtivoFinanceiro(classe, tipo, nome)
            self.__ativo_DAO.add(novo_ativo)
            self.__tela_ativo_financeiro.mostrar_mensagem("Ativo Financeiro criado com sucesso!")

        except ValueError:
            self.__tela_ativo_financeiro.mostrar_erro("Erro: Valor inválido informado.")
        except TypeError:
            self.__tela_ativo_financeiro.mostrar_erro("Erro: Tipo de dado incorreto.")
        except Exception as e:
            self.__tela_ativo_financeiro.mostrar_erro(f"Ocorreu um erro ao adicionar o Ativo Financeiro: {str(e)}")

    def lista_ativos_financeiros(self):
        try:
            ativos = self.__ativo_DAO.get_all()
            lista_nomes = [ativo.nome for ativo in ativos]
            self.__tela_ativo_financeiro.mostrar_ativos_financeiros(lista_nomes)
        except Exception as e:
            self.__tela_ativo_financeiro.mostrar_erro(f"Erro ao listar ativos: {str(e)}")

    def get_ativos_financeiros(self) -> List[AtivoFinanceiro]:
        return list(self.__ativo_DAO.get_all())