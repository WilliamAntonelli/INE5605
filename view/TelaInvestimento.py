import PySimpleGUI as sg
from typing import List
from util.enums import TipoInvestimento
from model.ativo_financeiro import AtivoFinanceiro

class TelaInvestimento:
    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text('-------- Opções em Investimento --------')],
            [sg.Button('Cadastrar novo Investimento', key='1')],
            [sg.Button('Listar Investimentos', key='2')],
            [sg.Button('Mostrar Saldo', key='3')],
            [sg.Button('Excluir Investimento', key='4')],
            [sg.Button('Voltar', key='5')]
        ]
        window = sg.Window('Investimento', layout)
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_novo_investimento(self, ativos_disponiveis: List[AtivoFinanceiro]):
        nomes_ativos = [a.nome for a in ativos_disponiveis]
        tipos_investimento = [t.name for t in TipoInvestimento]

        layout = [
            [sg.Text('Ativo:'), sg.Combo(nomes_ativos, key='ativo')],
            [sg.Text('Tipo de Investimento:'), sg.Combo(tipos_investimento, key='tipo')],
            [sg.Text('Valor:'), sg.Input(key='valor')],
            [sg.Text('Mês:'), sg.Input(key='mes')],
            [sg.Text('Ano:'), sg.Input(key='ano')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Cadastrar Investimento', layout)
        evento, valores = window.read()
        window.close()

        if evento == 'Confirmar':
            try:
                ativo = ativos_disponiveis[nomes_ativos.index(valores['ativo'])]
                tipo = TipoInvestimento[valores['tipo']]
                valor = float(valores['valor'])
                mes = int(valores['mes'])
                ano = int(valores['ano'])
                return ativo, tipo, valor, mes, ano
            except Exception as e:
                self.mostrar_erro(f'Erro ao cadastrar investimento: {e}')
        return None

    def mostrar_investimentos(self, investimentos: List[str]):
        investimentos_numerados = [
            f"{index} - {investimento}" for index, investimento in enumerate(investimentos)
        ]
        sg.popup_scrolled('-------- Investimentos --------', '\n'.join(investimentos_numerados))

    def mostrar_saldo(self, saldo: float):
        sg.popup(f'Saldo atual: R$ {saldo:.2f}')

    def selecionar_investimento_para_excluir(self, investimentos: List[str]) -> int:
        layout = [[sg.Text('Selecione o investimento para excluir:')]]
        for index, investimento in enumerate(investimentos):
            layout.append([sg.Button(f"{index} - {investimento}", key=str(index))])
        layout.append([sg.Button('Cancelar')])

        window = sg.Window('Excluir Investimento', layout)
        evento, _ = window.read()
        window.close()

        if evento and evento.isdigit():
            return int(evento)
        return -1

    def mostrar_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error(f'ERRO: {mensagem}')