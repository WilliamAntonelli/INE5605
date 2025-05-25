

class TelaSistema:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("Bem vindo ao sistema de controlador financeiro")
        print("Escolha uma das opções desejadas")
        print("(1) Familiares")
        print("(2) Categoria")
        print("(3) Metas")
        print("(4) Investimentos")
        print("(5) Tranferências")
        print("(6) Despesas")
        print("(7) Informações do Usuário")
        print("(8) Ativos Financeiros")
        opcao_menu = input()
        return opcao_menu