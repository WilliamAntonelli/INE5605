from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorNotaFiscal import ControladorNotaFiscal
from controller.ControladorMeta import ControladorMeta
from controller.ControladorUsuario import ControladorUsuario
from controller.ControladorFamiliar import ControladorFamiliar
from controller.ControladorTransferencia import ControladorTransferencia
from view.TelaSistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__contralador_familiar = ControladorFamiliar()
        self.__controlador_categoria = ControladorCategoria()
        self.__controlador_nota_fiscal = ControladorNotaFiscal()
        self.__controlador_meta = ControladorMeta()
        self.__controlador_usuario = ControladorUsuario()
        self.__controlador_transferencia = ControladorTransferencia()
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        self.__controlador_usuario.cadastrar_usuario()
        self.abre_tela()

    def abre_tela(self):

        dict_opcoes_para_execucao = {

            1: self.__contralador_familiar, 
            2: self.__controlador_categoria,
            3: self.__controlador_meta,
            4: "",
            5: self.__controlador_transferencia,
            6: "",
            7: self.__controlador_usuario,
            8: self.__controlador_nota_fiscal
        }

        while True:
            try:

                opca_menu = self.__tela_sistema.mostrar_tela_inicial()
                if int(opca_menu) == 9:
                    break
                
                controlador = dict_opcoes_para_execucao.get(int(opca_menu))
                if controlador is None:
                    print("Operação não reconhecida, por favor digita uma opção válida")
                    continue
                
                controlador.executar()
                        
            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")


