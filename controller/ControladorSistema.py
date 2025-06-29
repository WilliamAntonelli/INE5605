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
        self.__controlador_meta = ControladorMeta(self)
        self.__controlador_ativo_financeiro = ControladorAtivoFinanceiro()
        self.__controlador_investimento = ControladorInvestimento(self.__controlador_ativo_financeiro, self)
        self.__controlador_despesa = ControladorDespesa(self.__controlador_categoria, self)
        self.__controlador_transferencia = ControladorTransferencia(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_familiar(self):
        return self.__controlador_familiar
    
    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
    
    @property
    def controlador_categoria(self):
        return self.__controlador_categoria
    
    @property
    def controlador_meta(self):
        return self.__controlador_meta
    
    @property
    def controlador_ativo_financeiro(self):
        return self.__controlador_ativo_financeiro
    
    @property
    def controlador_investimento(self):
        return self.__controlador_investimento
    
    @property
    def controlador_despesa(self):
        return self.__controlador_despesa
    
    @property
    def controlador_transferencais(self):
        return self.__controlador_transferencia
    
    def iniciar(self):
        make_login = self.__controlador_usuario.cadastrar_usuario_or_make_login()

        if not make_login:
            return

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

                opcao_menu = self.__tela_sistema.mostrar_tela_inicial()

                if opcao_menu is None or int(opcao_menu) == 9:
                    break
                
                controlador = dict_opcoes_para_execucao.get(int(opcao_menu))
                if controlador is None:
                    self.__tela_sistema.mostrar_informacoes("Operação não reconhecida, por favor digita uma opção válida")
                else:
                    controlador.executar()

            except ValueError:
                self.__tela_sistema.mostrar_informacoes("Operação não reconhecida, por favor digita uma opção válida")
