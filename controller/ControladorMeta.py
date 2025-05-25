from model.meta import Meta
from view.TelaMeta import TelaMeta
from typing import List
from datetime import datetime

class ControladorMeta:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_meta = TelaMeta()

    def executar(self):
        self.tela_inicial()

    def tela_inicial(self):
        try:
            while True:
                opcao_menu = self.__tela_meta.mostrar_tela_inicial()
                match int(opcao_menu):
                    case 1:
                        self.adicionar_meta()
                    case 2:
                        self.__tela_meta.mostrar_metas(self.lista_meta_string())
                    case 3:
                        self.excluir_meta()
                    case 4:
                        break
                    case _:
                        print("Operação não reconhecida, por favor digite uma opção válida")
        except ValueError:
            print("Operação não reconhecida, por favor digita uma opção válida")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {str(e)}")


    def adicionar_meta(self):
        try:
            valor, data = self.__tela_meta.mostrar_cadastrar_nova_meta()

            if not valor or not data:
                print("Os campos valor e data são obrigatórios.")
                return

            try:
                data = datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")
                return

            if any(meta.data_vencimento == data for meta in self.__controlador_sistema.controlador_usuario.usuario.metas):
                print(f"Já existe uma meta com data de vencimento '{data}'.")
                return

            nova_meta = Meta(valor, data)
            self.__controlador_sistema.controlador_usuario.usuario.metas.append(nova_meta)
            print("Meta cadastrada com sucesso!")

        except ValueError:
            print("Erro: Valor inválido informado.")
        except TypeError:
            print("Erro: Tipo de dado incorreto.")
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar a meta: {str(e)}")


    def lista_meta_string(self) -> List[str]:
        return [f"Objetivo: R${meta.valor_objetivo:.2f}, Vencimento: {meta.data_vencimento.strftime('%d/%m/%Y')}" for meta in self.__controlador_sistema.controlador_usuario.usuario.metas]


    def excluir_meta(self):
        if not self.__controlador_sistema.controlador_usuario.usuario.metas:
            print("Não há metas para excluir.")
            return

        self.__tela_meta.mostrar_metas(self.lista_meta_string())
        try:
            indice = int(input("Digite o número da meta que deseja excluir: "))
            if 0 <= indice < len(self.__controlador_sistema.controlador_usuario.usuario.metas):
                removida = self.__controlador_sistema.controlador_usuario.usuario.metas.pop(indice)
                print(f"Meta com valor R$ {removida.valor_objetivo:.2f} excluída com sucesso.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")