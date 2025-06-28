import PySimpleGUI as sg
from typing import List

class TelaMeta:
    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text('-------- Opções em Meta --------')],
            [sg.Button('Cadastrar nova Meta', key='1')],
            [sg.Button('Listar Metas', key='2')],
            [sg.Button('Excluir Meta', key='3')],
            [sg.Button('Voltar', key='4')]
        ]
        window = sg.Window('Meta', layout)
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_nova_meta(self):
        layout = [
            [sg.Text('Valor do objetivo:'), sg.Input(key='valor')],
            [sg.Text('Data de vencimento (DD/MM/AAAA):'), sg.Input(key='data')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastrar Meta', layout)
        evento, valores = window.read()
        window.close()

        if evento == 'Confirmar':
            try:
                valor = float(valores['valor'])
                data = valores['data']
                return valor, data
            except ValueError:
                self.mostrar_erro('Valor inválido.')
        return None, None

    def mostrar_metas(self, metas: List[str]):
        if not metas:
            sg.popup('Nenhuma meta cadastrada.')
            return

        lista_formatada = []
        for indice, meta in enumerate(metas):
            lista_formatada.append(f"{indice} - {meta}")

        sg.popup_scrolled('-------- Metas Cadastradas --------', '\n'.join(lista_formatada))

    def pedir_indice(self, mensagem: str) -> int:
        layout = [
            [sg.Text(mensagem)],
            [sg.Input(key='indice')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Escolher Índice', layout)
        evento, valores = window.read()
        window.close()

        if evento == 'Confirmar':
            try:
                return int(valores['indice'])
            except ValueError:
                self.mostrar_erro('Índice inválido.')
        return -1

    def mostrar_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error(f'ERRO: {mensagem}')
