from view.TelaFamiliar import TelaFamiliar
from model.familiar import Familiar
from typing import List
from util.enums import Genero, Parentesco

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
                        self.adcionar_familiar()
                    case 2:
                        self.__tela_familiar.mostrar_informacoes(self.lista_famialiares())
                    case 3:
                        self.editar_familiar()
                    case 4:
                        break
                    case 5:
                        break
                    case _:
                        print("Operação não reconhecida, por favor digita uma opção válida")

            except ValueError:
                print("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)

    def adcionar_familiar(self):

        novo_familiar_dict = self.__tela_familiar.mostrar_cadastrar_novo_familiar()

        genero = Genero.get_by_codigo(novo_familiar_dict["genero"])
        parentesco = Parentesco.get_by_codigo(novo_familiar_dict["parentesco"])
        self.__controlador_sistema.controlador_usuario.usuario.adicionar_familiar(
                novo_familiar_dict["nome"], novo_familiar_dict["profissao"], novo_familiar_dict["idade"], genero, parentesco
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
                
                index_familiar_escolhido, opcao_menu, novo_campo = self.__tela_familiar.mostrar_informacoes_edit(self.lista_famialiares())

                if int(opcao_menu) == 8:
                    break
                
                field = fiels_familiares_to_setters.get(int(opcao_menu))
                if field is None:
                    raise ValueError

                if field == "genero":
                    field = Genero.get_by_codigo(novo_campo)
                if field == "parentesco":
                    field = Parentesco.get_by_codigo(novo_campo)

                setattr(self.__controlador_sistema.controlador_usuario.usuarios.familiares[index_familiar_escolhido], field, novo_campo)
                break

            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)

    def lista_famialiares(self) -> List[dict]:

        return [{
            "nome": familiar.nome,
            "profissao": familiar.profissao,
            "idade": familiar.idade,
            "genero": familiar.genero.descricao,
            "parentesco": familiar.parentesco.descricao
        } for familiar in self.__controlador_sistema.controlador_usuario.usuario.familiares]