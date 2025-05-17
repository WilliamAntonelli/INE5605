from typing import List

class TelaMeta:
    def __init__(self):
        ...

    def mostrar_tela_inicial(self) -> str:
        print("-------- Opções em Meta-------")
        print("(1) Cadastrar nova Meta")
        print("(2) Listar Metas")
        print("(3) Voltar")
        return input("Escolha uma opção: ")

    def mostrar_cadastrar_nova_meta(self) -> tuple[float, str]:
        print("-------- Insira nova meta --------")
        valor = float(input("Insira o valor do objetivo: "))
        data = input("Insira a data de vencimento (AAAA-MM-DD): ")
        return valor, data

    def mostrar_metas(self, metas: List[str]) -> None:
        print("-------- Metas Cadastradas --------")
        for count, meta in enumerate(metas):
            print(f"Meta({count}) - {meta}")
