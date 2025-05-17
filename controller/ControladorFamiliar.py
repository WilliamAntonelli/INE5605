from view.TelaFamiliar import TelaFamiliar
from model.familiar import Familiar
from typing import List
from util.enums import Genero

class ControladorFamiliar:

    def __init__(self):
        
        self.__familiares = []
        self.__tela_familiar = TelaFamiliar()
    
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
                        self.__tela_familiar.mostrar_informacoes(self.lista_categoria_string())
                    case 3:
                        ...
                    case 4:
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

        novo_familiar = Familiar(novo_familiar_dict["nome"], novo_familiar_dict["profissao"], novo_familiar_dict["idade"], genero, novo_familiar_dict["parentesco"])
        self.__familiares.append(novo_familiar)

    def lista_famialiares(self) -> List[dict]:
        return [{
            "nome": familiar.nome,
            "profissao": familiar.profissao
        } for familiar in self.__familiares]