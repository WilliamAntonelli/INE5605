

from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorUsuario import ControladorUsuario
from view.TelaSistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__controlador_categoria = ControladorCategoria()
        self.__controlador_usuario = ControladorUsuario()
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        self.__controlador_usuario.cadastrar_usuario()
        self.abre_tela()

    def abre_tela(self):

        dict_opcoes_para_execucao = {2: self.__controlador_categoria}

        try:

            while True:
                opca_menu = self.__tela_sistema.mostrar_tela_inicial()
                acao = dict_opcoes_para_execucao.get(int(opca_menu))
                if acao is None:
                    print("Operação não reconhecida, por favor digita uma opção válida")
                else:
                    acao.executar()
        except ValueError:
            print("Operação não reconhecida, por favor digita uma opção válida")


