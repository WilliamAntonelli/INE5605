import PySimpleGUI as sg
from typing import List
from util.enums import ClasseAtivo, TipoAtivo

class TelaAtivoFinanceiro:
    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text('-------- Opções em Ativo Financeiro --------')],
            [sg.Button('Cadastrar novo Ativo Financeiro', key='1')],
            [sg.Button('Listar Ativos Financeiros', key='2')],
            [sg.Button('Voltar para o Menu Principal', key='3')]
        ]
        window = sg.Window('Ativo Financeiro', layout)
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_novo_ativo_financeiro(self) -> tuple:
        classes = [c.name for c in ClasseAtivo]
        tipos = [t.name for t in TipoAtivo]

        layout = [
            [sg.Text('Escolha a classe do ativo:'), sg.Combo(classes, key='classe')],
            [sg.Text('Escolha o tipo do ativo:'), sg.Combo(tipos, key='tipo')],
            [sg.Text('Digite o nome do ativo:'), sg.Input(key='nome')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastrar Ativo Financeiro', layout)
        evento, valores = window.read()
        window.close()

        if evento == 'Confirmar':
            try:
                classe = ClasseAtivo[valores['classe']]
                tipo = TipoAtivo[valores['tipo']]
                nome = valores['nome']
                return classe, tipo, nome
            except:
                self.mostrar_erro('Erro ao selecionar classe ou tipo.')
        return None

    def mostrar_ativos_financeiros(self, ativos: List[str]):
        sg.popup_scrolled('-------- Ativos Financeiros --------', '\n'.join(ativos))

    def mostrar_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error(f'ERRO: {mensagem}')