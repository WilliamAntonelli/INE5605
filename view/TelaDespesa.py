import PySimpleGUI as sg
from typing import List
from util.enums import TipoDespesa, TipoPagamento
from model.categoria import Categoria
from model.despesa import Despesa

class TelaDespesa:
    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text('-------- Opções em Despesa --------')],
            [sg.Button('Cadastrar nova Despesa', key='1')],
            [sg.Button('Alterar', key='2')],
            [sg.Button('Mostrar todas as Despesas', key='3')],
            [sg.Button('Mostrar despesas por mês', key='4')],
            [sg.Button('Excluir', key='5')],
            [sg.Button('Relatórios', key='6')],
            [sg.Button('Voltar', key='7')]
        ]
        window = sg.Window('Despesa', layout)
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_nova_despesa(self, categorias: List[Categoria]):
        tipos_despesa = [t.name for t in TipoDespesa]
        tipos_pagamento = [t.name for t in TipoPagamento]
        nomes_categorias = [c.nome for c in categorias]

        layout = [
            [sg.Text('Tipo de Despesa:'), sg.Combo(tipos_despesa, key='tipo_despesa')],
            [sg.Text('Categoria:'), sg.Combo(nomes_categorias, key='categoria')],
            [sg.Text('Local:'), sg.Input(key='local')],
            [sg.Text('Valor:'), sg.Input(key='valor')],
            [sg.Text('Tipo de Pagamento:'), sg.Combo(tipos_pagamento, key='tipo_pagamento')],
            [sg.Text('Mês:'), sg.Input(key='mes')],
            [sg.Text('Ano:'), sg.Input(key='ano')],
            [sg.Checkbox('Adicionar nota fiscal?', key='tem_nota')],
            [sg.Text('Código da Nota:'), sg.Input(key='codigo')],
            [sg.Text('Arquivo da Nota:'), sg.Input(key='arquivo')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Cadastrar Despesa', layout)
        evento, valores = window.read()
        window.close()

        if evento == 'Confirmar':
            try:
                tipo_despesa = TipoDespesa[valores['tipo_despesa']]
                categoria = categorias[nomes_categorias.index(valores['categoria'])]
                local = valores['local']
                valor = float(valores['valor'])
                tipo_pagamento = TipoPagamento[valores['tipo_pagamento']]
                mes = int(valores['mes'])
                ano = int(valores['ano'])
                codigo = valores['codigo'] if valores['tem_nota'] else 'Sem nota fiscal'
                arquivo = valores['arquivo'] if valores['tem_nota'] else None
                return tipo_despesa, categoria, local, valor, tipo_pagamento, mes, ano, codigo, arquivo
            except Exception as e:
                self.mostrar_erro(f'Erro: {e}')
        return None

    def mostrar_despesas(self, despesas: List[str]):
        if not despesas:
            sg.popup('Nenhuma despesa cadastrada.')
            return

        lista_formatada = []
        for indice, despesa in enumerate(despesas):
            lista_formatada.append(f"{indice} - {despesa}")

        sg.popup_scrolled('-------- Despesas --------', '\n'.join(lista_formatada))

    def mostrar_despesas_mes_ano(self) -> tuple:
        layout = [
            [sg.Text('Digite o mês:'), sg.Input(key='mes')],
            [sg.Text('Digite o ano:'), sg.Input(key='ano')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Despesas por Mês/Ano', layout)
        evento, valores = window.read()
        window.close()
        if evento == 'Confirmar':
            try:
                return int(valores['mes']), int(valores['ano'])
            except:
                self.mostrar_erro('Dados inválidos.')
        return -1, -1

    def mostrar_despesas_e_selecionar(self, despesas: List[str]) -> int:
        if not despesas:
            sg.popup('Nenhuma despesa cadastrada.')
            return -1

        lista_formatada = []
        for indice, despesa in enumerate(despesas):
            lista_formatada.append(f"{indice} - {despesa}")

        layout = [
            [sg.Text('Selecione a despesa:')],
            [sg.Listbox(values=lista_formatada, size=(60, 10), key='despesa')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Selecionar Despesa', layout)
        evento, valores = window.read()
        window.close()

        if evento == 'Confirmar' and valores['despesa']:
            linha = valores['despesa'][0]
            indice = int(linha.split(' - ')[0])
            return indice
        return -1

    def mostrar_menu_relatorios(self) -> str:
        layout = [
            [sg.Text('-------- Relatórios de Despesas --------')],
            [sg.Button('Total por Categoria', key='1')],
            [sg.Button('Estatísticas Gerais', key='2')],
            [sg.Button('Voltar', key='3')]
        ]
        window = sg.Window('Relatórios', layout)
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_relatorio_total_por_categoria(self, totais: dict):
        texto = "\n".join([f"{categoria}: R$ {total:.2f}" for categoria, total in totais.items()])
        sg.popup_scrolled('Total por Categoria', texto)

    def mostrar_estatisticas_despesas(self, maior, menor, media):
        texto = f"Maior Despesa: R$ {maior:.2f}\nMenor Despesa: R$ {menor:.2f}\nMédia das Despesas: R$ {media:.2f}"
        sg.popup(texto)

    def mostrar_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error(f'ERRO: {mensagem}')

    def mostrar_informacoes_editar_despesa(self, despesas: List[str], despesa_objetos: List[Despesa], categorias: List[Categoria]) -> tuple:
        if not despesas:
            sg.popup('Nenhuma despesa cadastrada.')
            return None, None, None

        lista_formatada = []
        for indice, despesa in enumerate(despesas):
            lista_formatada.append(f"{indice} - {despesa}")

        layout = [
            [sg.Text('Selecione a despesa que deseja editar:')],
            [sg.Listbox(values=lista_formatada, size=(60, 10), key='despesa_selecionada')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Selecionar Despesa', layout)
        evento, valores = window.read()
        window.close()

        if evento == 'Confirmar' and valores['despesa_selecionada']:
            linha = valores['despesa_selecionada'][0]
            indice = int(linha.split(' - ')[0])
            despesa = despesa_objetos[indice]

            layout_campos = [
                [sg.Text('Escolha o campo a editar:')],
                [sg.Button('Tipo de Despesa'), sg.Button('Categoria'), sg.Button('Local'), sg.Button('Valor')],
                [sg.Button('Tipo de Pagamento'), sg.Button('Mês'), sg.Button('Ano')],
                [sg.Button('Tem Nota Fiscal'), sg.Button('Código da Nota'), sg.Button('Arquivo da Nota')],
                [sg.Button('Cancelar')]
            ]
            window = sg.Window('Campos para Editar', layout_campos)
            evento_campo, _ = window.read()
            window.close()

            if evento_campo:
                campo = evento_campo.lower().replace(' ', '_')

                valor_atual = ''
                if campo == 'tipo_de_despesa':
                    valor_atual = despesa.tipo_despesa.name
                    novas_opcoes = [t.name for t in TipoDespesa]
                elif campo == 'categoria':
                    valor_atual = despesa.categoria.nome
                    novas_opcoes = [c.nome for c in categorias]
                elif campo == 'tipo_de_pagamento':
                    valor_atual = despesa.tipo_pagamento.name
                    novas_opcoes = [t.name for t in TipoPagamento]
                elif campo == 'tem_nota_fiscal':
                    valor_atual = 'Sim' if despesa.nota_fiscal.codigo != 'Sem nota fiscal' else 'Não'
                    novas_opcoes = ['Sim', 'Não']
                elif campo == 'codigo_da_nota':
                    valor_atual = despesa.nota_fiscal.codigo
                    novas_opcoes = None
                elif campo == 'arquivo_da_nota':
                    valor_atual = despesa.nota_fiscal.arquivo
                    novas_opcoes = None
                else:
                    valor_atual = getattr(despesa, campo, '')

                layout_valor = [
                    [sg.Text(f'Valor atual: {valor_atual}')],
                ]

                if campo in ['tipo_de_despesa', 'categoria', 'tipo_de_pagamento', 'tem_nota_fiscal']:
                    layout_valor.append([sg.Combo(novas_opcoes, key='novo_valor')])
                else:
                    layout_valor.append([sg.Input(key='novo_valor')])

                layout_valor.append([sg.Button('Confirmar'), sg.Button('Cancelar')])

                window = sg.Window('Novo Valor', layout_valor)
                evento_valor, valores_novo = window.read()
                window.close()

                if evento_valor == 'Confirmar':
                    return indice, campo, valores_novo['novo_valor']

        return None, None, None