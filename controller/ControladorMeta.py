from model.meta import Meta
from view.TelaMeta import TelaMeta
from typing import List
from datetime import datetime
from DAOs.meta_dao import MetaDAO

class ControladorMeta:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_meta = TelaMeta()
        self.__meta_DAO = MetaDAO()

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
                        self.lista_meta()
                    case 3:
                        self.excluir_meta()
                    case 4:
                        break
                    case _:
                        self.__tela_meta.mostrar_erro("Operação não reconhecida")
        except ValueError:
            self.__tela_meta.mostrar_erro("Operação inválida")
        except Exception as e:
            self.__tela_meta.mostrar_erro(f"Erro inesperado: {str(e)}")

    def adicionar_meta(self):
        try:
            valor, data_texto = self.__tela_meta.mostrar_cadastrar_nova_meta()

            if not valor or not data_texto:
                self.__tela_meta.mostrar_erro("Os campos valor e data são obrigatórios.")
                return

            try:
                data = datetime.strptime(data_texto, "%d/%m/%Y").date()
            except ValueError:
                self.__tela_meta.mostrar_erro("Data inválida! Use o formato DD/MM/AAAA.")
                return

            for meta in self.__meta_DAO.get_all():
                if meta.data_vencimento == data:
                    self.__tela_meta.mostrar_erro(f"Já existe uma meta com vencimento '{data.strftime('%d/%m/%Y')}'.")
                    return

            nova_meta = Meta(valor, data)
            self.__meta_DAO.add(nova_meta)
            self.__tela_meta.mostrar_mensagem("Meta cadastrada com sucesso!")

        except Exception as e:
            self.__tela_meta.mostrar_erro(f"Erro ao adicionar meta: {e}")

    def lista_meta(self):
        try:
            metas = list(self.__meta_DAO.get_all())

            if not metas:
                self.__tela_meta.mostrar_erro("Nenhuma meta cadastrada.")
                return

            lista_strings = [
                f"Objetivo: R${m.valor_objetivo:.2f}, Vencimento: {m.data_vencimento.strftime('%d/%m/%Y')}"
                for m in metas
            ]
            self.__tela_meta.mostrar_metas(lista_strings)
        except Exception as e:
            self.__tela_meta.mostrar_erro(f"Erro ao listar metas: {str(e)}")

    def excluir_meta(self):
        try:
            metas_com_chaves = list(self.__meta_DAO._DAO__cache.items())

            if not metas_com_chaves:
                self.__tela_meta.mostrar_erro("Nenhuma meta para excluir.")
                return

            lista_strings = [
                f"Objetivo: R${m.valor_objetivo:.2f}, Vencimento: {m.data_vencimento.strftime('%d/%m/%Y')}"
                for _, m in metas_com_chaves
            ]

            self.__tela_meta.mostrar_metas(lista_strings)
            indice = self.__tela_meta.pedir_indice("Digite o número da meta que deseja excluir: ")

            if 0 <= indice < len(metas_com_chaves):
                chave_para_remover = metas_com_chaves[indice][0]
                self.__meta_DAO.remove(chave_para_remover)
                self.__tela_meta.mostrar_mensagem(f"Meta excluída com sucesso!")
            else:
                self.__tela_meta.mostrar_erro("Índice inválido.")
        except Exception as e:
            self.__tela_meta.mostrar_erro(f"Erro ao excluir meta: {e}")