

from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorNotaFiscal import ControladorNotaFiscal
from controller.ControladorMeta import ControladorMeta
from controller.ControladorAtivoFinanceiro import ControladorAtivoFinanceiro
from controller.ControladorInvestimento import ControladorInvestimento
from view.TelaSistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__controlador_categoria = ControladorCategoria()
        self.__controlador_nota_fiscal = ControladorNotaFiscal()
        self.__controlador_meta = ControladorMeta()
        self.__controlador_ativo_financeiro = ControladorAtivoFinanceiro()
        self.__controlador_investimento = ControladorInvestimento(self.__controlador_ativo_financeiro)
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        self.abre_tela()

    def abre_tela(self):

        dict_opcoes_para_execucao = {2: self.__controlador_categoria, 3: self.__controlador_meta, 4: self.__controlador_investimento,
                                     8: self.__controlador_nota_fiscal, 9: self.__controlador_ativo_financeiro}

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