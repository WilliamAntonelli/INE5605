from model.nota_fiscal import NotaFiscal
from view.TelaNotaFiscal import TelaNotaFiscal
from typing import List

class ControladorNotaFiscal:
    def __init__(self):
        self.__notas_fiscais = []
        self.__tela_nota_fiscal = TelaNotaFiscal()

    def executar(self):
        self.tela_inicial()

    def tela_inicial(self):

            try:
                while True:
                    opcao_menu = self.__tela_nota_fiscal.mostrar_tela_inicial()
                    match int(opcao_menu):
                        case 1:
                            self.adicionar_nota_fiscal()
                        case 2:
                            self.__tela_nota_fiscal.mostrar_notas_fiscais(self.lista_nota_fiscal_string())
                        case 3:
                            break
                        case _:
                            print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")


    def adicionar_nota_fiscal(self):

        nome_arquivo, arquivo = self.__tela_nota_fiscal.mostrar_cadastrar_nova_nota()

        if any(nota.nome_arquivo == nome_arquivo for nota in self.__notas_fiscais):
            print(f"Já existe uma nota fiscal com o nome '{nome_arquivo}'.")
            return

        nova_nota = NotaFiscal(nome_arquivo, arquivo)
        self.__notas_fiscais.append(nova_nota)
        print("Nota fiscal cadastrada com sucesso!")

    def lista_nota_fiscal_string(self) -> List[str]:
        return [nota_fiscal.nome_arquivo for nota_fiscal in self.__notas_fiscais]