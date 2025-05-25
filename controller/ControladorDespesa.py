from model.despesa import Despesa
from view.TelaDespesa import TelaDespesa
from typing import List
from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorUsuario import ControladorUsuario

class ControladorDespesa:
    def __init__(self, controlador_categoria: ControladorCategoria, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_despesa = TelaDespesa()
        self.__categorias = controlador_categoria

    def executar(self):
        self.tela_inicial()

    def tela_inicial(self):

            try:
                while True:
                    opcao_menu = self.__tela_despesa.mostrar_tela_inicial()
                    match int(opcao_menu):
                        case 1:
                            self.adicionar_despesa()
                        case 2:
                            self.alterar_despesa()
                        case 3:
                            self.__tela_despesa.mostrar_despesas(self.lista_despesa_string())
                        case 4:
                            self.listar_despesas_por_mes()
                        case 5:
                            self.excluir_despesa()
                        case 6:
                            self.relatorios_despesa()
                        case 7:
                            break
                        case _:
                            print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {str(e)}")

    def adicionar_despesa(self):
        try:
            categoria = self.__categorias.get_categorias()

            if not categoria:
                print("Nenhuma categoria cadastrada. Cadastre uma categoria antes de criar uma despesa.")
                return

            tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo = \
            (self.__tela_despesa.mostrar_cadastrar_nova_despesa(categoria))

            if not codigo or not isinstance(codigo, str):
                raise ValueError("Código da nota fiscal inválido. Você deve digitar o código.")
            if arquivo is not None and not isinstance(arquivo, str):
                raise ValueError("Arquivo inválido. Você deve digitar o nome do arquivo.")

            nova_despesa = Despesa(tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo)
            self.__usuario.despesas.append(nova_despesa)

            print("Despesa criada com sucesso!")


        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except TypeError as te:
            print(f"Erro de tipo: {te}")
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar a despesa: {e}")


    def lista_despesa_string(self, despesas: List = None) -> List[str]:
        if despesas is None:
            despesas = self.__usuario.despesas

        return [(f"{d.tipo_despesa.name} | {d.categoria.nome} | {d.local} "
                 f"| R$ {d.valor:.2f} | {d.tipo_pagamento.name} | Mês: {d.mes} | Ano: {d.ano} "
                 f"| Informações de nota fiscal: {d.nota_fiscal.codigo} | {d.nota_fiscal.arquivo}")
                for d in despesas]

    def listar_despesas_por_mes(self):
        try:
            mes, ano = self.__tela_despesa.mostrar_despesas_mes_ano()
            despesas_filtradas = [d for d in self.__usuario.despesas if d.mes == mes and d.ano == ano]

            if not despesas_filtradas:
                print(f"Nenhuma despesa encontrada para {mes}/{ano}.")
                return

            despesas_str = self.lista_despesa_string(despesas_filtradas)
            self.__tela_despesa.mostrar_despesas(despesas_str)
        except Exception as e:
            print(f"Erro ao buscar despesas por mês: {e}")


    def alterar_despesa(self):
        try:
            if not self.__usuario.despesas:
                print("Nenhuma despesa cadastrada para alterar.")
                return

            indice = self.__tela_despesa.mostrar_despesas_e_selecionar(self.lista_despesa_string())

            if 0 <= indice < len(self.__usuario.despesas):
                tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo = \
                    self.__tela_despesa.mostrar_cadastrar_nova_despesa(self.__categorias.get_categorias())

                nova_despesa = Despesa(tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo)
                self.__usuario.despesas[indice] = nova_despesa

                print("Despesa alterada com sucesso!")
            else:
                print("Índice inválido. Nenhuma despesa foi alterada.")
        except Exception as e:
            print(f"Erro ao alterar despesa: {e}")



    def excluir_despesa(self):
        try:
            if not self.__usuario.despesas:
                print("Nenhuma despesa cadastrada para excluir.")
                return

            indice = self.__tela_despesa.mostrar_despesas_e_selecionar(self.lista_despesa_string())

            if 0 <= indice < len(self.__usuario.despesas):
                despesa_excluida = self.__usuario.despesas.pop(indice)
                print(f"Despesa '{despesa_excluida.local}' removida com sucesso!")
            else:
                print("Índice inválido. Nenhuma despesa foi excluída.")
        except Exception as e:
            print(f"Erro ao excluir despesa: {e}")


    def relatorios_despesa(self):
        while True:
            opcao = self.__tela_despesa.mostrar_menu_relatorios()
            match int(opcao):
                case 1:
                    self.total_por_categoria()
                case 2:
                    self.estatisticas_despesas()
                case 3:
                    break
                case _:
                    print("Opção inválida.")

    def total_por_categoria(self):
        totais = {}
        for despesa in self.__usuario.despesas:
            nome_categoria = despesa.categoria.nome
            if nome_categoria in totais:
                totais[nome_categoria] += despesa.valor
            else:
                totais[nome_categoria] = despesa.valor

        self.__tela_despesa.mostrar_relatorio_total_por_categoria(totais)

    def estatisticas_despesas(self):
        if not self.__usuario.despesas:
            print("Nenhuma despesa cadastrada.")
            return

        valores = [despesa.valor for despesa in self.__usuario.despesas]
        maior = max(valores)
        menor = min(valores)
        media = sum(valores) / len(valores)

        self.__tela_despesa.mostrar_estatisticas_despesas(maior, menor, media)