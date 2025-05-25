from controller.ControladorUsuario import ControladorUsuario
from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorMeta import ControladorMeta
from controller.ControladorAtivoFinanceiro import ControladorAtivoFinanceiro
from controller.ControladorInvestimento import ControladorInvestimento
from controller.ControladorDespesa import ControladorDespesa
from controller.ControladorUsuario import ControladorUsuario
from controller.ControladorFamiliar import ControladorFamiliar
from controller.ControladorTransferencia import ControladorTransferencia
from view.TelaSistema import TelaSistema

class ControladorSistema:

    def __init__(self):

        self.__controlador_familiar = ControladorFamiliar(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_meta = ControladorMeta(self.__controlador_usuario)
        self.__controlador_ativo_financeiro = ControladorAtivoFinanceiro()
        self.__controlador_investimento = ControladorInvestimento(self.__controlador_ativo_financeiro, self.__controlador_usuario)
        self.__controlador_despesa = ControladorDespesa(self.__controlador_categoria, self.__controlador_usuario)
        self.__controlador_transferencia = ControladorTransferencia(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
    
    def iniciar(self):
        self.__controlador_usuario.cadastrar_usuario()
        self.abre_tela()

    def abre_tela(self):

        dict_opcoes_para_execucao = {

                1: self.__controlador_familiar,
                2: self.__controlador_categoria, 
                3: self.__controlador_meta, 
                4: self.__controlador_investimento,
                5: self.__controlador_transferencia,
                6: self.__controlador_despesa,
                7: self.__controlador_usuario,
                8: self.__controlador_ativo_financeiro
            }

        while True:
            try:

                opca_menu = self.__tela_sistema.mostrar_tela_inicial()
                if int(opca_menu) == 9:
                    break
                
                controlador = dict_opcoes_para_execucao.get(int(opca_menu))
                if controlador is None:
                    print("Operação não reconhecida, por favor digita uma opção válida")
                else:
                    controlador.executar()
            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")

