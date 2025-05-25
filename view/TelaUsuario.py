from typing import List
from model.usuario import Usuario

class TelaUusuario:

    def __init__(self):
        ...


    def mostrar_tela_inicial(self) -> str:
            
            print("Escolha uma das opções desejadas")
            print("(1) Editar dados")
            print("(2) Ver todos os dados")
            print("(3) Voltar")
    
            opcao_menu = input()
            return opcao_menu

    def mostrar_cadastrar_novo_usuario(self) -> dict:
        nome = input("Digite seu nome: ")
        profissao = input("Digite sua profissão: ")
        idade = int(input("Digite sua idade: "))
        genero = int(input("Digite 1 para homen e 2 para mulher: "))
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        renda = float(input("Digite sua renda: "))
        

        novo_usuario = {
            "nome": nome,
            "profissao": profissao,
            "idade": idade,
            "genero": genero,
            "email": email,
            "senha": senha,
            "renda": renda
        }
        return novo_usuario

    def mostrar_informacoes(self, usuario_dict: dict) -> None:
        print("-------- Dados do usuário ----------")
        for key in usuario_dict:
            print(f"{key}: {usuario_dict[key]}")


    def mostrar_informacoes_edit(self) -> None:

        print("-------- Qual dados você deseja alterar ? ----------")
        print("(1) Nome: ")
        print("(2) Profissão: ")
        print("(3) Idade: ")
        print("(4) Gênero: ")
        print("(5) email: ")
        print("(6) Senha: ")
        print("(7) Renda: ")
        print("(8) Cancelar edição")
        
        opcao_menu = input("Qual o campo você deseja alterar ?")

        if int(opcao_menu) == 8:
             return opcao_menu, None
        
        novo_campo = input("Digite o novo valor: ")
        return opcao_menu, novo_campo
        
