from model.meta import Meta
from model.despesa import Despesa
from model.investimento import Investimento
from typing import List
from model.usuario import Usuario
from util.enums import Genero
from view.TelaUsuario import TelaUusuario
from exceptions.InvalidInputException import InvalidInputException
from DAOs.UsuarioDAO import UsuarioDAO

class ControladorUsuario:

    def __init__(self, controlador_sistema):
        self.__usuario = None
        self.__tela_usuario = TelaUusuario()
        self.__controlador_sistema = controlador_sistema
        self.__usuario_dao = UsuarioDAO()

    
    @property
    def usuario(self):
        return self.__usuario
    
    def executar(self):
        self.tela_inicial()

    def tela_inicial(self) -> str:

        while True:
            try:
                opcao_menu = self.__tela_usuario.mostrar_tela_inicial()
                match int(opcao_menu):
                    case 1:
                        self.editar_usuario()
                    case 2:
                        self.__tela_usuario.mostrar_informacoes(self.get_usuario_in_dict())
                    case 3:
                        break
                    case _:
                        print("Operação não reconhecida, por favor digita uma opção válida")

            except (ValueError, InvalidInputException) as e:
                print("Foi inserido algum valor inconsistente do que esperado pelo sistema")
                print(e)
                
            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")


    def get_usuario_in_dict(self) -> dict:

        usuario_dict = {
                        "nome": self.__usuario.nome,
                        "profissao": self.__usuario.profissao,
                        "idade": self.__usuario.idade,
                        "genero": self.__usuario.genero.descricao,
                        "email": self.__usuario.email,
                        "senha": self.__usuario.senha,
                        "renda": self.__usuario.renda
                    }
        
        return usuario_dict
    

    def editar_usuario(self):
        while True:
            try:
                
                fiels_user_to_setters = {
                    1: "nome",
                    2: "profissao",
                    3: "idade",
                    4: "genero",
                    5: "email",
                    6: "senha",
                    7: "renda"
                }
                
                opcao_menu, novo_campo = self.__tela_usuario.mostrar_informacoes_edit()

                if int(opcao_menu) == 8:
                    break
                
                field = fiels_user_to_setters.get(int(opcao_menu))
                if field is None:
                    print("Operação não reconhecida, por favor digita uma opção válida")
                    continue
                elif field == "genero":
                    novo_campo = Genero.get_by_codigo(int(novo_campo))

                setattr(self.__usuario, field, novo_campo)
                break

            except ValueError:
                print("Operação não reconhecida, por favor digita uma opção válida")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)

    def cadastrar_usuario(self):
        while self.__usuario is None:
            try:

                novo_usuario = self.__tela_usuario.mostrar_cadastrar_novo_usuario()

                novo_usuario = {
                    "nome": "João cabaleiro da silva",
                    "profissao": "Engenheiro de Software",
                    "idade": 30,
                    "email": "joao.silva@email.com",
                    "senha": "senhaSegura123",
                    "renda": 8500.00,
                    "genero": 1
                }

                genero = Genero.get_by_codigo(novo_usuario["genero"])
                self.__usuario = Usuario(novo_usuario["nome"], novo_usuario["profissao"], novo_usuario["idade"], genero, novo_usuario["email"], 
                                         novo_usuario["senha"], novo_usuario["renda"])
                self.__usuario_dao.add(self.__usuario_dao.generate_primery_key(), self.__usuario)
                
            except (ValueError, InvalidInputException):
                print("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except Exception as e:
                print("Algo de errado ocorreu durante a execução do programa")
                print(e)


    def adicionar_transferencia(self, index_familiar, valor, mes, ano):

        familiar = self.__controlador_sistema.controlador_familiar.get_familiar_by_index(index_familiar)
        return self.__usuario.adicionar_transferencia(valor, familiar, mes, ano)
