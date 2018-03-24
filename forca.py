pontuacao = 1000

def cabecalho():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def fim_de_jogo(pontuacao):
    print("Sua pontuacao final foi:", pontuacao)
    print("*********************************")
    print("         Fim do Jogo")
    print("*********************************")

################################################################################################################
# Inicio do código #

def jogar():

    cabecalho()

    fim_de_jogo(pontuacao)


if (__name__ == "__main__"):
    jogar()