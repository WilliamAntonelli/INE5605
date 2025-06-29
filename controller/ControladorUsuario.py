from getpass import fallback_getpass

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

                if opcao_menu is None:
                    break

                match int(opcao_menu):
                    case 1:
                        self.editar_usuario()
                    case 2:
                        self.__tela_usuario.mostrar_informacoes_list(self.get_usuario_in_dict())
                    case 3:
                        break
                    case _:
                        self.__tela_usuario.mostrar_informacoes("Operação não reconhecida, por favor digita uma opção válida")

            except ValueError:
                self.__tela_usuario.mostrar_informacoes("Foi inserido algum valor inconsistente do que esperado pelo sistema")

            except InvalidInputException as e:
                self.__tela_usuario.mostrar_informacoes(str(e))

            except Exception:
                self.__tela_usuario.mostrar_informacoes("Algo de errado ocorreu durante a execução do programa, contact o adminstrador do sistema")


    def get_usuario_in_dict(self) -> dict:

        usuario_dict = {
                        "cpf": self.__usuario.cpf,
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

                if opcao_menu is None or int(opcao_menu) == 8:
                    break
                
                field = fiels_user_to_setters.get(int(opcao_menu))
                if field is None:
                    self.__tela_usuario.mostrar_informacoes("Operação não reconhecida, por favor digita uma opção válida")
                    continue
                elif field == "genero":
                    novo_campo = Genero.get_by_codigo(int(novo_campo))

                setattr(self.__usuario, field, novo_campo)
                self.__usuario_dao.update(self.__usuario.cpf, self.__usuario)
                break

            except ValueError:
                self.__tela_usuario.mostrar_informacoes("Operação não reconhecida, por favor digita uma opção válida")

            except InvalidInputException as e:
                self.__tela_usuario.mostrar_informacoes(str(e))

            except Exception as e:
                self.__tela_usuario.mostrar_informacoes("Algo de errado ocorreu durante a execução do programa, contact o adminstrador do sistema")

    def cadastrar_usuario(self):
        while self.__usuario is None:
            try:

                novo_usuario = self.__tela_usuario.mostrar_cadastrar_novo_usuario()

                # novo_usuario = {
                #     "cpf": "0000",
                #     "nome": "João cabaleiro da silva",
                #     "profissao": "Engenheiro de Software",
                #     "idade": 30,
                #     "email": "joao.silva@email.com",
                #     "senha": "senhaSegura123",
                #     "renda": 8500.00,
                #     "genero": 1
                # }

                genero = Genero.get_by_codigo(novo_usuario["genero"])
                self.__usuario = Usuario(novo_usuario["cpf"], novo_usuario["nome"], novo_usuario["profissao"],
                                         novo_usuario["idade"], genero, novo_usuario["email"], novo_usuario["senha"],
                                         novo_usuario["renda"])
                self.__usuario_dao.add(self.__usuario.cpf, self.__usuario)
                return True
                
            except ValueError:
                self.__tela_usuario.mostrar_informacoes("Dados do usuário não inválidos, por favor coloque as informações de acordo com o requerido")

            except InvalidInputException as e:
                self.__tela_usuario.mostrar_informacoes(str(e))

            except Exception as e:
                self.__tela_usuario.mostrar_informacoes("Algo de errado ocorreu durante a execução do programa, contact o adminstrador do sistema")


    def cadastrar_usuario_or_make_login(self):

        user = self.__usuario_dao.get_current_user()

        if user is not None:

            senha = self.__tela_usuario.pegar_senha()

            if senha is None:
                return False

            if senha != user.senha:
                self.__tela_usuario.mostrar_informacoes("Você digitou a senha incorreta, tente novamente")
                return self.cadastrar_usuario_or_make_login()

            self.__usuario = user
            return True
        else:
            return self.cadastrar_usuario()

    def adicionar_transferencia(self, index_familiar, valor, mes, ano):

        familiar = self.__controlador_sistema.controlador_familiar.get_familiar_by_index(index_familiar)
        transferencia = self.__usuario.adicionar_transferencia(valor, familiar, mes, ano)
        self.__usuario_dao.update(self.__usuario.cpf, self.__usuario)
        return transferencia

