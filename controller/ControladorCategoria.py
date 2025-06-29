from view.TelaCategoria import TelaCategoria
from model.categoria import Categoria
from typing import List
from exceptions.InvalidInputException import InvalidInputException
from exceptions.DataNotFoundException import DataNotFoundException
from DAOs.CategoriaDAO import CategoriaDAO

class ControladorCategoria:

    def __init__(self, controlador_sistema):
        self.__categorias_dao = CategoriaDAO()
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema

    
    def executar(self):
        self.tela_inicial()
        
    def tela_inicial(self):

        while True:
            try:
                
                opcao_menu = self.__tela_categoria.mostrar_tela_inicial()

                if opcao_menu is None:
                    break

                match int(opcao_menu):
                    case 1:
                        self.adcionar_categoria()
                    case 2:

                        lista_categoria = self.lista_categoria_string()
                        if lista_categoria:
                            self.__tela_categoria.mostrar_categorias(lista_categoria)
                    case 3:
                        break
                    case _:
                        self.__tela_categoria.mostrar_informacoes("Operação não reconhecida, por favor digita uma opção válida")

            except ValueError as e:
                self.__tela_categoria.mostrar_informacoes("Foi inserido algum valor inconsistente do que esperado pelo sistema")

            except (InvalidInputException, DataNotFoundException) as e:
                self.__tela_categoria.mostrar_informacoes(str(e))

            except Exception as e:
                self.__tela_categoria.mostrar_informacoes("Algo inesperado durante a execução do programa, consulte o admnistrador do sistema")
        
    def adcionar_categoria(self):

        nome_categoria = self.__tela_categoria.mostrar_cadastrar_nova_categoria()
        if nome_categoria in list(self.__categorias_dao.get_all()):
            return None

        new_categoria = Categoria(nome_categoria)
        self.__categorias_dao.add(new_categoria)
        return nome_categoria


    def lista_categoria_string(self) -> List[str]:

        if len(self.__categorias_dao.get_all()) == 0:
            self.__tela_categoria.mostrar_informacoes("Nenhuma categoria cadastrada no momento")
            return []
        
        return [categoria.nome for categoria in self.__categorias_dao.get_all()]
    

    def get_categorias(self) -> list:
        return self.__categorias_dao.get_all()