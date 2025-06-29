from model.despesa import Despesa
from view.TelaDespesa import TelaDespesa
from typing import List
from controller.ControladorCategoria import ControladorCategoria
from controller.ControladorUsuario import ControladorUsuario
from util.enums import TipoDespesa, TipoPagamento
from DAOs.despesa_dao import DespesaDAO

class ControladorDespesa:
    def __init__(self, controlador_categoria, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_despesa = TelaDespesa()
        self.__categorias = controlador_categoria
        self.__despesa_DAO = DespesaDAO()

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
                        self.editar_despesa()
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
        except Exception as e:
            self.__tela_despesa.mostrar_erro(f"Ocorreu um erro inesperado: {str(e)}")

    def adicionar_despesa(self):
        categorias = self.__categorias.get_categorias()

        if not categorias:
            self.__tela_despesa.mostrar_erro("Nenhuma categoria cadastrada.")
            return

        dados = self.__tela_despesa.mostrar_cadastrar_nova_despesa(categorias)
        if dados is None:
            return

        tipo_despesa, categoria, local, valor, forma, mes, ano, codigo, arquivo = dados
        nova_despesa = Despesa(tipo_despesa, categoria, local, valor, forma, mes, ano, codigo, arquivo)
        self.__despesa_DAO.add(nova_despesa)
        self.__tela_despesa.mostrar_mensagem("Despesa criada com sucesso!")

    def editar_despesa(self):
        despesas = list(self.__despesa_DAO.get_all())

        if not despesas:
            self.__tela_despesa.mostrar_erro("Nenhuma despesa cadastrada.")
            return

        index, campo, novo_valor = self.__tela_despesa.mostrar_informacoes_editar_despesa(
            self.lista_despesa_string(despesas), despesas, self.__categorias.get_categorias()
        )

        if index is None:
            return

        despesa = despesas[index]

        try:
            match campo:
                case "tipo_de_despesa":
                    despesa.tipo_despesa = TipoDespesa[novo_valor]
                case "categoria":
                    categorias = self.__categorias.get_categorias()
                    despesa.categoria = categorias[[c.nome for c in categorias].index(novo_valor)]
                case "local":
                    despesa.local = novo_valor
                case "valor":
                    despesa.valor = float(novo_valor)
                case "tipo_de_pagamento":
                    despesa.tipo_pagamento = TipoPagamento[novo_valor]
                case "mes":
                    despesa.mes = int(novo_valor)
                case "ano":
                    despesa.ano = int(novo_valor)
                case "tem_nota_fiscal":
                    if novo_valor == 'Sim':
                        despesa.nota_fiscal.codigo = ''
                        despesa.nota_fiscal.arquivo = ''
                    else:
                        despesa.nota_fiscal.codigo = 'Sem nota fiscal'
                        despesa.nota_fiscal.arquivo = None
                case "codigo_da_nota":
                    despesa.nota_fiscal.codigo = novo_valor
                case "arquivo_da_nota":
                    despesa.nota_fiscal.arquivo = novo_valor

            self.__despesa_DAO.update(despesa)
            self.__tela_despesa.mostrar_mensagem("Despesa alterada com sucesso!")

        except Exception as e:
            self.__tela_despesa.mostrar_erro(f"Erro ao editar despesa: {e}")

    def excluir_despesa(self):
        despesas = list(self.__despesa_DAO.get_all())

        if not despesas:
            self.__tela_despesa.mostrar_erro("Nenhuma despesa cadastrada.")
            return

        indice = self.__tela_despesa.mostrar_despesas_e_selecionar(self.lista_despesa_string(despesas))

        if 0 <= indice < len(despesas):
            despesa = despesas[indice]
            self.__despesa_DAO.remove(id(despesa))
            self.__tela_despesa.mostrar_mensagem("Despesa excluída com sucesso!")
        else:
            self.__tela_despesa.mostrar_erro("Índice inválido.")

    def listar_despesas_por_mes(self):
        mes, ano = self.__tela_despesa.mostrar_despesas_mes_ano()
        despesas_filtradas = [
            d for d in self.__despesa_DAO.get_all()
            if d.mes == mes and d.ano == ano
        ]

        if not despesas_filtradas:
            self.__tela_despesa.mostrar_erro("Nenhuma despesa encontrada.")
            return

        self.__tela_despesa.mostrar_despesas(self.lista_despesa_string(despesas_filtradas))

    def lista_despesa_string(self, despesas: List = None) -> List[str]:
        if despesas is None:
            despesas = list(self.__despesa_DAO.get_all())

        return [
            f"{d.tipo_despesa.name} | {d.categoria.nome} | {d.local} | R$ {d.valor:.2f} | "
            f"{d.tipo_pagamento.name} | Mês: {d.mes} | Ano: {d.ano} | Nota Fiscal: {d.nota_fiscal.codigo} | {d.nota_fiscal.arquivo}"
            for d in despesas
        ]

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

    def total_por_categoria(self):
        totais = {}
        for despesa in self.__despesa_DAO.get_all():
            nome_categoria = despesa.categoria.nome
            totais[nome_categoria] = totais.get(nome_categoria, 0) + despesa.valor
        self.__tela_despesa.mostrar_relatorio_total_por_categoria(totais)

    def estatisticas_despesas(self):
        despesas = list(self.__despesa_DAO.get_all())
        if not despesas:
            self.__tela_despesa.mostrar_erro("Nenhuma despesa cadastrada.")
            return
        valores = [d.valor for d in despesas]
        maior = max(valores)
        menor = min(valores)
        media = sum(valores) / len(valores)
        self.__tela_despesa.mostrar_estatisticas_despesas(maior, menor, media)