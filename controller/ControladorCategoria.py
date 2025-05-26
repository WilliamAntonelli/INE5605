from view.TelaCategoria import TelaCategoria
from model.categoria import Categoria
from typing import List
from exceptions.InvalidInputException import InvalidInputException
from exceptions.DataNotFoundException import DataNotFoundException

class ControladorCategoria:

    def __init__(self, controlador_sistema):
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema
    
    def executar(self):
        self.tela_inicial()
        
    def tela_inicial(self):

        while True:
            try:
                
                opcao_menu = self.__tela_categoria.mostrar_tela_inicial()
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
        
    def adcionar_categoria(self):

        nome_categoria = self.__tela_categoria.mostrar_cadastrar_nova_categoria()
        if nome_categoria in self.__categorias:
            return None

        new_categoria = Categoria(nome_categoria)
        self.__categorias.append(new_categoria)
        return nome_categoria


    def lista_categoria_string(self) -> List[str]:

        if len(self.__categorias) == 0:
            print("Nenhuma categoria cadastrada no momento\n")
            return []
        
        return [categoria.nome for categoria in self.__categorias]
    

    def get_categorias(self) -> list:
        return self.__categorias