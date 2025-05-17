from typing import List

class TelaNotaFiscal:
    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em Nota Fiscal --------")
        print("(1) Cadastrar nova Nota Fiscal")
        print("(2) Listar Notas Fiscais")
        print("(3) Voltar para o Menu Principal")
        return input("Escolha uma opção: ")

    def mostrar_cadastrar_nova_nota(self) -> tuple[str, str]:
        print("-------- Insira nova nota fiscal --------")
        nome_arquivo = input("Insira o nome do arquivo: ")
        arquivo = input("Insira o conteúdo ou caminho do arquivo: ")
        return nome_arquivo, arquivo


    def mostrar_notas_fiscais(self, notas_fiscais: List[str]) -> None:
        print("-------- Notas Fiscais --------")

        for count, nota_fiscal in enumerate(notas_fiscais):
            print(f"Nota fiscal({(count)}) - {nota_fiscal}")