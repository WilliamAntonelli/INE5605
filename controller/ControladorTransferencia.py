from view.TelaTransferencia import TelaTransferencia
from exceptions.InvalidInputException import InvalidInputException
from typing import List
from exceptions.DataNotFoundException import DataNotFoundException
from DAOs.TransferenciaDAO import TransferenciaDAO
from util.enums import Parentesco

class ControladorTransferencia:

    def __init__(self, controlador_sistema):

        self.__tela_transferencia = TelaTransferencia()
        self.__controlador_sistema = controlador_sistema
        self.__dao = TransferenciaDAO()

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
                        self.mostrar_filtro_mes_ano_transferencias(self.__controlador_sistema.controlador_usuario.usuario.transferencias)
                    case 4:
                        self.mostrar_filtro_parentesco_transferencias(self.__controlador_sistema.controlador_usuario.usuario.transferencias)
                    case 5:
                        return
                    
                    case _:
                        print("Operação não reconhecida, por favor digita uma opção válida")

            except (ValueError, InvalidInputException) as e:
                print("Foi inserido algum valor inconsistente do que esperado pelo sistema")
                print(e)

            except DataNotFoundException as e:
                print("Algum dado inserido não foi encontrado")
                print(e)

            except Exception as e:
                print("Algo inesperado durante a execução do programa, consulte o admnistrador do sistema")
                print(e)

    def mostrar_tranferencias(self, transferencias):

        if len(transferencias) == 0:
            print("Nenhuma transferência foi cadastrada")
            return

        transferencia_dict = [{
            "origem": _transferencia.usuario.nome,
            "destino": _transferencia.familiar.nome,
            "valor": _transferencia.valor,
            "mes": _transferencia.mes,
            "ano": _transferencia.ano
        } for _transferencia in transferencias]
    
        self.__tela_transferencia.mostrar_transferencias(transferencia_dict)

    def cadastrar_transferencia(self):

        while True:
            try:
               
               lista_familiares = self.__controlador_sistema.controlador_familiar.lista_famialiares()

               if len(lista_familiares) == 0:
                    print("Nenhum familiar cadastrado no momento\n")
                    return

               index_familiar_escolhido, valor, mes, ano = self.__tela_transferencia.mostrar_cadastrar_nova_tranferencia(lista_familiares)

               if index_familiar_escolhido is None or len(lista_familiares) == index_familiar_escolhido:
                   return
               

               nova_transferencia = self.__controlador_sistema.controlador_usuario.adicionar_transferencia(index_familiar_escolhido, valor, mes, ano)
               self.__dao.add(self.__dao.generate_primery_key(), nova_transferencia)
               return
               
            except (ValueError, InvalidInputException) as e:
                print("Foi inserido algum valor inconsistente do que esperado pelo sistema")
                print(e)

            except DataNotFoundException as e:
                print("Algum dado inserido não foi encontrado")
                print(e)

            except Exception as e:
                print("Algo inesperado durante a execução do programa, consulte o admnistrador do sistema")
                print(e)

    def mostrar_filtro_mes_ano_transferencias(self, transferencias):

        mes, ano = self.__tela_transferencia.mostrar_filtro_mes_ano_transferencias()

        if mes < 1 or mes > 12 or ano < 2000 or ano > 2100:
            raise InvalidInputException("Data inválida, por favor coloque uma data válida")
        
        transferencia_dict = [{
            "origem": _transferencia.usuario.nome,
            "destino": _transferencia.familiar.nome,
            "valor": _transferencia.valor,
            "mes": _transferencia.mes,
            "ano": _transferencia.ano
        } for _transferencia in transferencias if _transferencia.mes == mes and _transferencia.ano == ano]

        if len(transferencia_dict) == 0:
            print("Nenhuma transferência foi encontrada para esse filtro de mês e ano")
            return
    
        self.__tela_transferencia.mostrar_transferencias(transferencia_dict)
        
    
        return mes, ano
    
    def mostrar_filtro_parentesco_transferencias(self, transferencias):


        parentesco = self.__tela_transferencia.mostrar_filtro_parentesco_transferencias()
        parentesco = Parentesco.get_by_codigo(int(parentesco))
        
        transferencia_dict = [{
            "origem": _transferencia.usuario.nome,
            "destino": _transferencia.familiar.nome,
            "valor": _transferencia.valor,
            "mes": _transferencia.mes,
            "ano": _transferencia.ano
        } for _transferencia in transferencias if _transferencia.familiar.parentesco == parentesco]

        if len(transferencia_dict) == 0:
            print("Nenhuma transferência foi encontrada para esse parente")
            return
    
        self.__tela_transferencia.mostrar_transferencias(transferencia_dict)