

from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorNotaFiscal import ControladorNotaFiscal
from controller.ControladorMeta import ControladorMeta
from controller.ControladorUsuario import ControladorUsuario
from controller.ControladorFamiliar import ControladorFamiliar
from view.TelaSistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__contralador_familiar = ControladorFamiliar()
        self.__controlador_categoria = ControladorCategoria()
        self.__controlador_nota_fiscal = ControladorNotaFiscal()
        self.__controlador_meta = ControladorMeta()
        self.__controlador_usuario = ControladorUsuario()
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        self.__controlador_usuario.cadastrar_usuario()
        self.abre_tela()

    def abre_tela(self):

        dict_opcoes_para_execucao = {2: self.__controlador_categoria, 3: self.__controlador_meta, 8: self.__controlador_nota_fiscal}

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


