from typing import List
from model.categoria import Categoria

class TelaCategoria:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em categoria ----------")

        print("(1) Cadastrar nova categoria")
        print("(2) Listar categorias")
        print("(3) Voltar")

        opcao_menu = input()
        return opcao_menu

    def mostrar_cadastrar_nova_categoria(self) -> str:
        print("-------- Insira nova Categoria ----------")

        nova_categoria = input("Insira o novo nome da categoria")
        return nova_categoria

    def mostrar_categorias(self, categorias: List[str]) -> None:
        print("-------- CATEGORIAS ----------")

        for count, categoria in enumerate(categorias):
            print(f"Categoria({str(count)}) - {categoria}")