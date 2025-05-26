from view.TelaFamiliar import TelaFamiliar
from model.familiar import Familiar
from typing import List
from util.enums import Genero, Parentesco
from exceptions.InvalidInputException import InvalidInputException
from exceptions.DataNotFoundException import DataNotFoundException

class ControladorFamiliar:

    def __init__(self, controlador_sistema):
        
        self.__tela_familiar = TelaFamiliar()
        self.__controlador_sistema = controlador_sistema
    
    def executar(self):
        self.tela_inicial()

    def tela_inicial(self):

        while True:
            try:

                opcao_menu = self.__tela_familiar.mostrar_tela_inicial()
                match int(opcao_menu):
                    case 1:
                        self.adicionar_familiar()
                    case 2:
                        self.__tela_familiar.mostrar_informacoes(self.lista_famialiares())
                    case 3:
                        self.editar_familiar()
                    case 4:
                        self.excluir_familiar()
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

    def adicionar_familiar(self):
            
        novo_familiar_dict = self.__tela_familiar.mostrar_cadastrar_novo_familiar()

        int(novo_familiar_dict["genero"])
        genero = Genero.get_by_codigo(int(novo_familiar_dict["genero"]))
        parentesco = Parentesco.get_by_codigo(int(novo_familiar_dict["parentesco"]))
        self.__controlador_sistema.controlador_usuario.usuario.adicionar_familiar(
                novo_familiar_dict["nome"], novo_familiar_dict["profissao"], int(novo_familiar_dict["idade"]), genero, parentesco
            )
        
    def editar_familiar(self):
        while True:
            try:
                
                fiels_familiares_to_setters = {
                    1: "nome",
                    2: "profissao",
                    3: "idade",
                    4: "genero",
                    5: "parentesco"
                }
                
                lista_familiares = self.lista_famialiares()
                if len(lista_familiares) == 0:
                    print("Nenhum familiar cadastrado no momento\n")
                    return
                
                index_familiar_escolhido, opcao_menu, novo_campo = self.__tela_familiar.mostrar_informacoes_edit(lista_familiares)

                if int(opcao_menu) == 8:
                    return
                
                field = fiels_familiares_to_setters.get(int(opcao_menu))
                if field is None:
                    raise ValueError

                elif field == "genero":
                    novo_campo = Genero.get_by_codigo(int(novo_campo))
                elif field == "parentesco":
                    novo_campo = Parentesco.get_by_codigo(int(novo_campo))

                self.__controlador_sistema.controlador_usuario.usuario.editar_info_familiar(index_familiar_escolhido, field, novo_campo)
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

    def excluir_familiar(self):

        while True:
            try:
                
                lista_familiares = self.lista_famialiares()
                index_familiar_escolhido = self.__tela_familiar.mostrar_informacoes_excluir_familiar(lista_familiares)

                if index_familiar_escolhido is None or len(lista_familiares) == index_familiar_escolhido:
                    return

                self.__controlador_sistema.controlador_usuario.usuario.excluir_familiar_by_index(index_familiar_escolhido)
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

    def get_familiar_by_index(self, index_familiar):


        if index_familiar < 0 or index_familiar >= len(self.__controlador_sistema.controlador_usuario.usuario.familiares):
            raise InvalidInputException("Familiar não cadastrado em usuário")
        
        return self.__controlador_sistema.controlador_usuario.usuario.familiares[index_familiar]   

    def lista_famialiares(self) -> List[dict]:

        return [{
            "nome": familiar.nome,
            "profissao": familiar.profissao,
            "idade": familiar.idade,
            "genero": familiar.genero.descricao,
            "parentesco": familiar.parentesco.descricao
        } for familiar in self.__controlador_sistema.controlador_usuario.usuario.familiares]
    