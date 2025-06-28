from model.meta import Meta
from view.TelaMeta import TelaMeta
from typing import List
from datetime import datetime

class ControladorMeta:
    def __init__(self, controlador_sistema):
        self.__metas = []
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
                        self.__tela_meta.mostrar_erro("Operação não reconhecida")
        except ValueError:
            self.__tela_meta.mostrar_erro("Operação não reconhecida")
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

            if any(meta.data_vencimento == data for meta in self.__controlador_sistema.controlador_usuario.usuario.metas):
                self.__tela_meta.mostrar_erro(f"Já existe uma meta com vencimento '{data}'.")
                return

            nova_meta = Meta(valor, data)
            self.__metas.append(nova_meta)
            self.__tela_meta.mostrar_mensagem("Meta cadastrada com sucesso!")

        except Exception as e:
            self.__tela_meta.mostrar_erro(f"Erro ao adicionar meta: {e}")

    def lista_meta_string(self) -> List[str]:
        return [
            f"Objetivo: R${m.valor_objetivo:.2f}, Vencimento: {m.data_vencimento.strftime('%d/%m/%Y')}"
            for m in self.__metas
        ]

    def excluir_meta(self):
        metas = self.__metas

        if not metas:
            self.__tela_meta.mostrar_erro("Nenhuma meta para excluir.")
            return

        self.__tela_meta.mostrar_metas(self.lista_meta_string())
        indice = self.__tela_meta.pedir_indice("Digite o número da meta que deseja excluir: ")

        if 0 <= indice < len(metas):
            removida = metas.pop(indice)
            self.__tela_meta.mostrar_mensagem(f"Meta com valor R$ {removida.valor_objetivo:.2f} excluída.")
        else:
            self.__tela_meta.mostrar_erro("Índice inválido.")