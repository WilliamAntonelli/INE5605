import PySimpleGUI as sg
from typing import List

class TelaCategoria:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkTeal4')

    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text("Menu de Categorias", font=("Helvetica", 20))],
            [sg.Button("Cadastrar nova categoria", key="1", size=(30, 2), pad=10)],
            [sg.Button("Listar categorias", key="2", size=(30, 2), pad=10)],
            [sg.Button("Voltar", key="3", size=(30, 2), pad=10)],
        ]
        window = sg.Window("Categorias", layout, element_justification="c")
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_nova_categoria(self) -> str:
        layout = [
            [sg.Text("Nova Categoria", font=("Helvetica", 16))],
            [sg.Text("Nome da categoria:"), sg.Input(key="categoria")],
            [sg.Button("Cadastrar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Cadastro de Categoria", layout)
        evento, valores = window.read()
        window.close()

        if evento in (sg.WIN_CLOSED, "Cancelar") or not valores["categoria"].strip():
            return ""

        return valores["categoria"].strip()

    def mostrar_categorias(self, categorias: List[str]) -> None:
        texto = "\n".join([
            f"Categoria({i}) - {cat}" for i, cat in enumerate(categorias)
        ]) or "Nenhuma categoria cadastrada."

        layout = [
            [sg.Text("Categorias Cadastradas", font=("Helvetica", 16))],
            [sg.Multiline(texto, size=(50, 15), disabled=True)],
            [sg.Button("Fechar")]
        ]
        window = sg.Window("Lista de Categorias", layout)
        window.read()
        window.close()

    def mostrar_informacoes(self, message_error, title="Error") -> None:
        sg.popup(message_error, title=title)
