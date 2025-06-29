import PySimpleGUI as sg
from typing import List
from util.enums import Parentesco

class TelaTransferencia:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkTeal4')

    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text("Menu de Transferências", font=("Helvetica", 20))],
            [sg.Button("Cadastrar nova transferência", key="1", size=(30, 2), pad=10)],
            [sg.Button("Visualizar transferências", key="2", size=(30, 2), pad=10)],
            [sg.Button("Transferências por mês e ano", key="3", size=(30, 2), pad=10)],
            [sg.Button("Transferências por parentesco", key="4", size=(30, 2), pad=10)],
            [sg.Button("Voltar", key="5", size=(30, 2), pad=10)],
        ]
        window = sg.Window("Transferências", layout, element_justification="c")
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_nova_tranferencia(self, familiares: List[dict]) -> set:
        opcoes = [f'{i} - {f["nome"]}, {f["idade"]} anos' for i, f in enumerate(familiares)]

        layout = [
            [sg.Text("Escolha um familiar", font=("Helvetica", 16))],
            [sg.Listbox(opcoes, key='familiar', size=(40, 6))],
            [sg.Text("Valor da transferência:"), sg.Input(key='valor')],
            [sg.Text("Mês (1-12):"), sg.Input(key='mes')],
            [sg.Text("Ano:"), sg.Input(key='ano')],
            [sg.Button("✅ Confirmar"), sg.Button("❌ Cancelar")]
        ]
        window = sg.Window("Nova Transferência", layout)
        evento, valores = window.read()
        window.close()

        if evento in (sg.WIN_CLOSED, "❌ Cancelar") or not valores["familiar"]:
            return len(familiares), None, None, None

        index = int(valores["familiar"][0].split(" - ")[0])
        if index == len(familiares):
            return index, None, None, None

        try:
            valor = float(valores["valor"])
            mes = int(valores["mes"])
            ano = int(valores["ano"])
            return index, valor, mes, ano

        except ValueError:
            sg.popup_error("❌ Dados inválidos!")
            return index, None, None, None

    def mostrar_transferencias(self, transferencias: List[dict]) -> None:
        texto = "\n".join([
            f'{i} - Origem: {t["origem"]}, Destino: {t["destino"]}, Valor: R$ {t["valor"]:.2f}, Data: {t["mes"]}/{t["ano"]}'
            for i, t in enumerate(transferencias)
        ]) or "Nenhuma transferência encontrada."

        layout = [
            [sg.Text("Suas Transferências", font=("Helvetica", 16))],
            [sg.Multiline(texto, size=(60, 15), disabled=True)],
            [sg.Button("Fechar")]
        ]
        window = sg.Window("Transferências", layout)
        window.read()
        window.close()

    def mostrar_filtro_mes_ano_transferencias(self) -> tuple:
        layout = [
            [sg.Text("Filtrar por mês e ano", font=("Helvetica", 16))],
            [sg.Text("Mês (1-12):"), sg.Input(key='mes')],
            [sg.Text("Ano:"), sg.Input(key='ano')],
            [sg.Button("✅ Confirmar"), sg.Button("❌ Cancelar")]
        ]
        window = sg.Window("Filtro por Mês/Ano", layout)
        evento, valores = window.read()
        window.close()

        if evento in (sg.WIN_CLOSED, "❌ Cancelar"):
            return None, None

        try:
            return int(valores["mes"]), int(valores["ano"])
        except ValueError:
            sg.popup_error("❌ Dados inválidos!")
            return None, None

    def mostrar_filtro_parentesco_transferencias(self) -> int:
        layout = [
            [sg.Text("Filtrar por Parentesco", font=("Helvetica", 16))],
            [sg.Listbox(
                values=[f"{p.codigo} - {p.descricao}" for p in Parentesco],
                key='parentesco', size=(40, 6)
            )],
            [sg.Button("✅ Confirmar"), sg.Button("❌ Cancelar")]
        ]
        window = sg.Window("Filtro por Parentesco", layout)
        evento, valores = window.read()
        window.close()

        if evento in (sg.WIN_CLOSED, "Cancelar") or not valores["parentesco"]:
            return None

        return int(valores["parentesco"][0].split(" - ")[0])

    def mostrar_informacoes(self, message_error, title="Error") -> None:
        sg.popup(message_error, title=title)
