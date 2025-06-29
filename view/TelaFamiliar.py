import PySimpleGUI as sg
from util.enums import Parentesco
from typing import List


class TelaFamiliar:
    def __init__(self):
        sg.theme("DarkBlue14")

    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text("🏠 Menu de Familiares", font=("Helvetica", 20))],
            [sg.Button("👨‍👩‍👧 Cadastrar novo familiar", key="1", size=(30, 2))],
            [sg.Button("📋 Visualizar familiares", key="2", size=(30, 2))],
            [sg.Button("✏️ Editar familiar", key="3", size=(30, 2))],
            [sg.Button("❌ Excluir familiar", key="4", size=(30, 2))],
            [sg.Button("⬅️ Voltar", key="5", size=(30, 2))],
        ]
        window = sg.Window("Painel de Familiares", layout, element_justification="c")
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_novo_familiar(self) -> dict:
        layout = [
            [sg.Text("👨‍👩‍👧 Cadastro de Familiar", font=("Helvetica", 18))],
            [sg.Text("Nome:", size=(15, 1)), sg.Input(key="nome")],
            [sg.Text("Profissão:", size=(15, 1)), sg.Input(key="profissao")],
            [sg.Text("Idade:", size=(15, 1)), sg.Input(key="idade")],
            [sg.Text("Gênero:", size=(15, 1)), sg.Combo(["1 - Homem", "2 - Mulher"], key="genero")],
            [sg.Text("Parentesco:", size=(15, 1)), sg.Combo(
                [f"{p.codigo} - {p.descricao}" for p in Parentesco], key="parentesco")],
            [sg.Button("💾 Cadastrar", size=(20, 2))],
        ]
        window = sg.Window("Cadastro Familiar", layout)
        evento, valores = window.read()
        window.close()

        try:
            return {
                "nome": valores["nome"],
                "profissao": valores["profissao"],
                "idade": int(valores["idade"]),
                "genero": 1 if "1" in valores["genero"] else 2,
                "parentesco": int(valores["parentesco"].split(" - ")[0])
            }
        except Exception:
            sg.popup_error("❌ Erro ao preencher os dados. Verifique os campos!")
            return {}

    def mostrar_informacoes_edit(self, familiares: List[dict]) -> tuple:
        if not familiares:
            sg.popup("⚠️ Nenhum familiar cadastrado!")
            return "6", None

        nomes = [f'({i}) {f["nome"]}, {f["idade"]} anos' for i, f in enumerate(familiares)]
        layout = [
            [sg.Text("👨‍👩‍👧 Editar Familiar", font=("Helvetica", 18))],
            [sg.Text("Escolha o familiar:"), sg.Listbox(nomes, size=(40, len(nomes)), key="familiar")],
            [sg.Text("Campo para editar:"), sg.Combo(
                ["1 - Nome", "2 - Profissão", "3 - Idade", "4 - Gênero", "5 - Parentesco", "6 - Cancelar edição"],
                key="campo")],
            [sg.Text("Novo valor:"), sg.Input(key="novo_valor")],
            [sg.Button("✅ Confirmar", size=(20, 2))],
        ]
        window = sg.Window("Editar Familiar", layout)
        evento, valores = window.read()
        window.close()

        if not valores["familiar"] or not valores["campo"]:
            return "6", None

        indice = int(valores["familiar"][0].split(")")[0][1:])
        campo = valores["campo"].split(" - ")[0]

        return indice, campo, valores["novo_valor"]

    def mostrar_informacoes_excluir_familiar(self, familiares: List[dict]) -> int:
        if not familiares:
            sg.popup("⚠️ Nenhum familiar cadastrado!")
            return None

        nomes = [f'({i}) {f["nome"]}, {f["idade"]} anos' for i, f in enumerate(familiares)]
        nomes.append(f'({len(familiares)}) Voltar')

        layout = [
            [sg.Text("❌ Excluir Familiar", font=("Helvetica", 18))],
            [sg.Text("Escolha quem deseja excluir:")],
            [sg.Listbox(nomes, size=(40, len(nomes)), key="escolhido")],
            [sg.Button("🗑️ Excluir", size=(20, 2))],
        ]
        window = sg.Window("Excluir Familiar", layout)
        evento, valores = window.read()
        window.close()

        if not valores["escolhido"]:
            return None

        indice = int(valores["escolhido"][0].split(")")[0][1:])
        if indice == len(familiares):
            return None

        return indice

    def mostrar_informacoes(self, familiares: List[dict]) -> None:
        if not familiares:
            sg.popup("⚠️ Nenhum familiar cadastrado!")
            return

        texto = ""
        for f in familiares:
            for chave, valor in f.items():
                texto += f"{chave.title()}: {valor}\n"
            texto += "\n"

        layout = [
            [sg.Text("📋 Dados dos Familiares", font=("Helvetica", 18))],
            [sg.Multiline(texto, size=(60, 15), disabled=True, font=("Courier", 12))],
            [sg.Button("❎ Fechar", size=(20, 2))],
        ]
        window = sg.Window("Visualizar Familiares", layout)
        window.read()
        window.close()
