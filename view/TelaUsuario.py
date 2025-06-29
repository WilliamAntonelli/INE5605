import PySimpleGUI as sg
from model.usuario import Usuario


class TelaUusuario:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkTeal4')

    def mostrar_tela_inicial(self) -> str:
        layout = [
            [sg.Text("👤 Menu de Usuário", font=("Helvetica", 20), justification='center')],
            [sg.Button("✏️ Editar dados", key="1", size=(25, 2), pad=10)],
            [sg.Button("📄 Ver todos os dados", key="2", size=(25, 2), pad=10)],
            [sg.Button("⬅️ Voltar", key="3", size=(25, 2), pad=10)],
        ]
        window = sg.Window("Painel de Usuário", layout, element_justification="c")
        evento, _ = window.read()
        window.close()
        return evento

    def mostrar_cadastrar_novo_usuario(self) -> dict:
        layout = [
            [sg.Text("📝 Cadastro de Novo Usuário", font=("Helvetica", 18))],
            [sg.Text("Nome:", size=(15, 1)), sg.Input(key="nome", size=(30, 1))],
            [sg.Text("Profissão:", size=(15, 1)), sg.Input(key="profissao", size=(30, 1))],
            [sg.Text("Idade:", size=(15, 1)), sg.Input(key="idade", size=(30, 1))],
            [sg.Text("Gênero:", size=(15, 1)),
             sg.Combo(["1 - Homem", "2 - Mulher"], key="genero", size=(28, 1))],
            [sg.Text("Email:", size=(15, 1)), sg.Input(key="email", size=(30, 1))],
            [sg.Text("Senha:", size=(15, 1)), sg.Input(key="senha", password_char="*", size=(30, 1))],
            [sg.Text("Renda:", size=(15, 1)), sg.Input(key="renda", size=(30, 1))],
            [sg.Button("💾 Cadastrar", size=(20, 2), pad=(0, 15))],
        ]

        window = sg.Window("Cadastro", layout, element_justification="left")
        evento, valores = window.read()
        window.close()

        try:
            novo_usuario = {
                "nome": valores["nome"],
                "profissao": valores["profissao"],
                "idade": int(valores["idade"]),
                "genero": 1 if "1" in valores["genero"] else 2,
                "email": valores["email"],
                "senha": valores["senha"],
                "renda": float(valores["renda"])
            }
        except (ValueError, TypeError):
            sg.popup_error("❌ Erro nos dados fornecidos. Verifique os campos.")
            return {}

        return novo_usuario

    def mostrar_informacoes(self, usuario_dict: dict) -> None:
        texto = "\n".join([f"{chave.title()}: {valor}" for chave, valor in usuario_dict.items()])
        layout = [
            [sg.Text("📄 Dados do Usuário", font=("Helvetica", 18))],
            [sg.Multiline(texto, size=(50, 12), disabled=True, font=("Courier", 12))],
            [sg.Button("❎ Fechar", size=(20, 2))],
        ]
        window = sg.Window("Dados", layout, element_justification="center")
        window.read()
        window.close()

    def mostrar_informacoes_edit(self) -> tuple:
        campos = {
            "1": "Nome",
            "2": "Profissão",
            "3": "Idade",
            "4": "Gênero",
            "5": "Email",
            "6": "Senha",
            "7": "Renda",
            "8": "Cancelar edição"
        }

        layout = [
            [sg.Text("🛠️ Edição de Dados", font=("Helvetica", 18))],
            [sg.Text("Escolha o campo:", size=(15, 1)),
             sg.Combo(list(campos.values()), key="campo", size=(30, 1))],
            [sg.Text("Novo valor:", size=(15, 1)), sg.Input(key="novo_valor", size=(30, 1))],
            [sg.Button("✅ Confirmar", size=(20, 2))],
        ]

        window = sg.Window("Editar Usuário", layout)
        evento, valores = window.read()
        window.close()

        if not valores["campo"]:
            return "8", None

        for k, v in campos.items():
            if v == valores["campo"]:
                if k == "8":
                    return k, None
                return k, valores["novo_valor"]
