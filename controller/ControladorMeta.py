from model.meta import Meta
from view.TelaMeta import TelaMeta
from typing import List
from controller.ControladorUsuario import ControladorUsuario

class ControladorMeta:
    def __init__(self, controlador_usuario: ControladorUsuario):
        self.__usuario = controlador_usuario
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
                        break
                    case _:
                        print("Operação não reconhecida, por favor digita uma opção válida")
        except ValueError:
            print("Operação não reconhecida, por favor digita uma opção válida")


    def adicionar_meta(self):
        valor, data = self.__tela_meta.mostrar_cadastrar_nova_meta()

        if any(meta.data_vencimento == data for meta in self.__usuario.metas):
            print(f"Já existe uma meta com data de vencimento '{data}'.")
            return

        nova_meta = Meta(valor, data)
        self.__usuario.metas.append(nova_meta)
        print("Meta cadastrada com sucesso!")


    def lista_meta_string(self) -> List[str]:
        return [f"Objetivo: R${meta.valor_objetivo:.2f}, Vencimento: {meta.data_vencimento}" for meta in self.__usuario.metas]