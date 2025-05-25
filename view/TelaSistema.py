

class TelaSistema:

    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("Bem vindo ao sistema de controlador financeiro")
        print("Escolha uma das opções desejadas")
        print("(1) Familiar")
        print("(2) Categoria")
        print("(3) Metas")
        print("(4) Investimentos")
        print("(5) Tranferências")
        print("(6) Despesas")
        print("(7) Informações do usuário")
        print("(8) Notas Fiscais")
        print("(9) Sair do Sistema")
       
        opcao_menu = input()
        return opcao_menu