from typing import List
from model.usuario import Usuario

class TelaUusuario:

    def __init__(self):
        ...

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
        
