import PySimpleGUI as sg

class TelaSistema:

    def __init__(self):
        sg.ChangeLookAndFeel('DarkTeal4')

    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text("Bem-vindo ao Sistema Financeiro", font=("Helvetica", 20), justification='center')],
            [sg.Text("Escolha uma das opções abaixo:", font=("Helvetica", 12))],
            [sg.Button("Familiares", key="1", size=(25, 2), pad=5)],
            [sg.Button("Categoria", key="2", size=(25, 2), pad=5)],
            [sg.Button("Metas", key="3", size=(25, 2), pad=5)],
            [sg.Button("Investimentos", key="4", size=(25, 2), pad=5)],
            [sg.Button("Transferências", key="5", size=(25, 2), pad=5)],
            [sg.Button("Despesas", key="6", size=(25, 2), pad=5)],
            [sg.Button("Informações do Usuário", key="7", size=(25, 2), pad=5)],
            [sg.Button("Ativos Financeiros", key="8", size=(25, 2), pad=5)],
        ]

        window = sg.Window("Menu Principal", layout, element_justification="center")
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_informacoes(self, message_error, title="Error") -> None:
        sg.popup(message_error, title=title)
