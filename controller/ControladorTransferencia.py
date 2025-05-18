from view.TelaTransferencia import TelaTransferencia
from exceptions.InvalidInputException import InvalidInputException

class ControladorTransferencia:

    def __int__(self, controlador_sistema):

        self.__controlador_sistema = controlador_sistema
        self.__transferencias = []
        self.__tela_transferencia = TelaTransferencia()

    def executar(self):
        self.tela_inicial()

    def tela_inicial(self) -> str:

        while True:
            try:
                opcao_menu = self.__tela_transferencia.mostrar_tela_inicial()
                match int(opcao_menu):
                    case 1:
                        self.cadastrar_transferencia()
                    case 2:
                        self.mostrar_informacoes()
                    case 3:
                        break
                    case _:
                        print("Operação não reconhecida, por favor digita uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")
    

    def mostrar_informacoes(self):
        while True:
            try:

                ...
                
            except (ValueError, InvalidInputException):
                print("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)

    def cadastrar_transferencia(self):
        while True:
            try:

               ...
                
            except (ValueError, InvalidInputException):
                print("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)
