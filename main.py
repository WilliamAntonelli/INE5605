from model.usuario import Usuario
from util.enums import TipoDespesa, CategoriaDespesa, TipoPagamento, Genero, Parentesco


def main():

    usuario_teste = Usuario("Filipe Pereira", "Programador", 24, Genero.MASCULINO,
                            "lipe_0109@hotmail.com", "123456", 5556)

    usuario_teste.adicionar_familiar("Carlos", "Encanador", 144,  Genero.MASCULINO, Parentesco.PAI)
    usuario_teste.adicionar_familiar("Mae", "professora", 144, Genero.MASCULINO, Parentesco.MAE)

    for x in usuario_teste.familiares:
        print(x.exibir_dados())

    print(usuario_teste.exibir_dados())

    usuario_teste.nome = "Cal"

if __name__ == "__main__":
    print("Começando o sistema")
    main()