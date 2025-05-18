
from view.TelaCategoria import TelaCategoria
from model.categoria import Categoria
from typing import List

class ControladorCategoria:

    def __init__(self):
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
    
    def executar(self):
        self.tela_inicial()
        
    def tela_inicial(self):

        try:
            while True:
                opcao_menu = self.__tela_categoria.mostrar_tela_inicial()
                match int(opcao_menu):
                    case 1:
                        self.adcionar_categorias()
                    case 2:
                        self.__tela_categoria.mostrar_categorias(self.lista_categoria_string())
                    case 3:
                        break
                    case _:
                        print("Operação não reconhecida, por favor digita uma opção válida")
        except ValueError:
            print("Operação não reconhecida, por favor digita uma opção válida")
        
    def adcionar_categorias(self):

        nome_categoria = self.__tela_categoria.mostrar_cadastrar_nova_categoria()
        if nome_categoria in self.__categorias:
            return None

        new_categoria = Categoria(nome_categoria)
        self.__categorias.append(new_categoria)
        return nome_categoria

    def lista_categoria_string(self) -> List[str]:
        return [categoria.nome for categoria in self.__categorias]

    def get_categorias(self) -> list:
        return self.__categorias