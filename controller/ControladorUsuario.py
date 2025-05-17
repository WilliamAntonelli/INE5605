from model.usuario import Usuario
from util.enums import Genero
from view.TelaUsuario import TelaUusuario

class ControladorUsuario:

    def __init__(self):
        self.__usuario = None
        self.__tela_usuario = TelaUusuario()

    
    @property
    def usuario(self):
        return self.__usuario
    
    def executar(self):
        self.tela_inicial()

    def cadastrar_usuario(self):
        while self.__usuario is None:
            try:
                novo_usuario = self.__tela_usuario.mostrar_cadastrar_novo_usuario()

                genero = Genero.get_by_codigo(novo_usuario["genero"])
                self.__usuario = Usuario(novo_usuario["nome"], novo_usuario["profissao"], novo_usuario["idade"], genero, novo_usuario["email"], 
                                         novo_usuario["senha"], novo_usuario["renda"])
            except ValueError:
                print("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)

        