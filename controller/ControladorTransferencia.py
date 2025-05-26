from view.TelaTransferencia import TelaTransferencia
from exceptions.InvalidInputException import InvalidInputException
from typing import List

class ControladorTransferencia:

    def __init__(self, controlador_sistema):

        self.__tela_transferencia = TelaTransferencia()
        self.__controlador_sistema = controlador_sistema

    def executar(self):
        self.tela_inicial()

    def tela_inicial(self) -> str:
        self.mostrar_informacoes()
    

    def mostrar_informacoes(self):

        while True:
            try:

                opcao_menu = self.__tela_transferencia.mostrar_tela_inicial()
                
                match int(opcao_menu):
                    case 1:
                        self.cadastrar_transferencia()
                    case 2:
                        self.mostrar_tranferencias(self.__controlador_sistema.controlador_usuario.usuario.transferencias)
                    case 3:
                        return
                    
                    case _:
                        print("Operação não reconhecida, por favor digita uma opção válida")

            except (ValueError, InvalidInputException):
                print("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)

    def mostrar_tranferencias(self, transferencias):

        if len(transferencias) == 0:
            print("Nenhuma transferência foi cadastrada")
            return

        transferencia_dict = [{
            "origem": _transferencia.usuario.nome,
            "destino": _transferencia.familiar.nome,
            "valor": _transferencia.valor
        } for _transferencia in transferencias]
    
        self.__tela_transferencia.mostrar_transferencias(transferencia_dict)

    

    def cadastrar_transferencia(self):
        while True:
            try:
               
               lista_familiares = self.__controlador_sistema.controlador_familiar.lista_famialiares()

               if len(lista_familiares) == 0:
                    print("Nenhum familiar cadastrado no momento\n")
                    return

               index_familiar_escolhido, valor = self.__tela_transferencia.mostrar_cadastrar_nova_tranferencia(lista_familiares)

               if index_familiar_escolhido is None or len(lista_familiares) == index_familiar_escolhido:
                   return
               

               self.__controlador_sistema.controlador_usuario.adicionar_transferencia(index_familiar_escolhido, valor)
               return
               
                
            except (ValueError, InvalidInputException):
                print("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)