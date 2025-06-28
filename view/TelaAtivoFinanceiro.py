import PySimpleGUI as sg
from typing import List
from util.enums import ClasseAtivo, TipoAtivo


class TelaAtivoFinanceiro:
    def __init__(self):
        sg.theme("SystemDefault")

    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text("-------- Opções em Ativo Financeiro --------")],
            [sg.Button("Cadastrar novo Ativo Financeiro", key="1")],
            [sg.Button("Listar Ativos Financeiros", key="2")],
            [sg.Button("Voltar para o Menu Principal", key="3")],
        ]

        window = sg.Window("Menu Ativo Financeiro", layout)
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_novo_ativo_financeiro(self) -> tuple[TipoAtivo, ClasseAtivo, str]:
        # Seleção da Classe do Ativo
        classe_opcoes = [classe.name for classe in ClasseAtivo]
        layout_classe = [
            [sg.Text("Escolha a classe do ativo:")],
            [sg.Listbox(classe_opcoes, size=(30, len(classe_opcoes)), key="classe")],
            [sg.Button("Continuar")]
        ]
        window_classe = sg.Window("Classe do Ativo", layout_classe)
        while True:
            evento, valores = window_classe.read()
            if evento == sg.WIN_CLOSED:
                window_classe.close()
                return None
            if valores["classe"]:
                classe = ClasseAtivo[valores["classe"][0]]
                break
        window_classe.close()

        # Seleção do Tipo de Ativo
        tipo_opcoes = [tipo.name for tipo in TipoAtivo]
        layout_tipo = [
            [sg.Text("Escolha o tipo do ativo:")],
            [sg.Listbox(tipo_opcoes, size=(30, len(tipo_opcoes)), key="tipo")],
            [sg.Button("Continuar")]
        ]
        window_tipo = sg.Window("Tipo do Ativo", layout_tipo)
        while True:
            evento, valores = window_tipo.read()
            if evento == sg.WIN_CLOSED:
                window_tipo.close()
                return None
            if valores["tipo"]:
                tipo = TipoAtivo[valores["tipo"][0]]
                break
        window_tipo.close()

        # Inserir o nome do ativo
        layout_nome = [
            [sg.Text("Insira o nome do ativo:")],
            [sg.Input(key="nome")],
            [sg.Button("Cadastrar")]
        ]
        window_nome = sg.Window("Nome do Ativo", layout_nome)
        evento, valores = window_nome.read()
        nome = valores["nome"]
        window_nome.close()

        return classe, tipo, nome

    def mostrar_ativos_financeiros(self, ativos_financeiros: List[str]) -> None:
        texto = "\n".join([f"Ativo {i}: {nome}" for i, nome in enumerate(ativos_financeiros)])
        layout = [[sg.Multiline(texto, size=(50, 15), disabled=True)],
                  [sg.Button("Fechar")]]
        window = sg.Window("Ativos Financeiros", layout)
        window.read()
        window.close()
