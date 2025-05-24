from model.despesa import Despesa
from view.TelaDespesa import TelaDespesa
from typing import List
from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorUsuario import ControladorUsuario

class ControladorDespesa:
    def __init__(self, controlador_categoria: ControladorCategoria, controlador_usuario: ControladorUsuario):
        self.__usuario = controlador_usuario
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
                            self.excluir_despesa()
                        case 5:
                            self.relatorios_despesa()
                        case 6:
                            break
                        case _:
                            print("Operação não reconhecida, por favor digite uma opção válida")
            except ValueError:
                print("Operação não reconhecida, por favor digite uma opção válida")

    def adicionar_despesa(self):

        categoria = self.__categorias.get_categorias()

        if not categoria:
            print("Nenhuma categoria cadastrado. Cadastre uma categoria antes de criar uma despesa.")
            return

        tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo = \
        (self.__tela_despesa.mostrar_cadastrar_nova_despesa(categoria))

        nova_despesa = Despesa(tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo)
        self.__usuario.despesas.append(nova_despesa)

        print("Despesa criada com sucesso!")


    def lista_despesa_string(self) -> List[str]:
        return [(f"{despesa.tipo_despesa.name} | {despesa.categoria.nome} | {despesa.local} "
                 f"| R$ {despesa.valor:.2f} | {despesa.tipo_pagamento.name} | Mês: {despesa.mes} | Ano: {despesa.ano}"
                 f"| Informações de nota fiscal: "
                 f"{despesa.nota_fiscal.codigo} | {despesa.nota_fiscal.arquivo}")
            for despesa in self.__usuario.despesas]


    def buscar_despesa_por_idx(self, idx: int) -> Despesa | None:
        if 0 <= idx < len(self.__despesas):
            return self.__usuario.despesas[idx]
        return None

    def buscar_despesas_por_local(self, local: str) -> List[Despesa]:
        return [d for d in self.__usuario.despesas if d.local.lower() == local.lower()]


    def alterar_despesa(self):
        try:
            if not self.__usuario.despesas:
                print("Nenhuma despesa cadastrada para alterar.")
                return

            idx = self.__tela_despesa.mostrar_despesas_e_selecionar(self.lista_despesa_string())

            if 0 <= idx < len(self.__usuario.despesas):
                tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo = \
                    self.__tela_despesa.mostrar_cadastrar_nova_despesa(self.__categorias.get_categorias())

                nova_despesa = Despesa(tipo, categoria, local, valor, forma, mes, ano, codigo, arquivo)
                self.__usuario.despesas[idx] = nova_despesa  # Atualiza a despesa na lista do usuário

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

            idx = self.__tela_despesa.mostrar_despesas_e_selecionar(self.lista_despesa_string())

            if 0 <= idx < len(self.__usuario.despesas):
                despesa_excluida = self.__usuario.despesas.pop(idx)
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

        valores = [despesa.valor for despesa in self.__despesas]
        maior = max(valores)
        menor = min(valores)
        media = sum(valores) / len(valores)

        self.__tela_despesa.mostrar_estatisticas_despesas(maior, menor, media)