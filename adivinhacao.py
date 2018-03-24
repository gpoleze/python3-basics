from random import random, randint

def cabecalho():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def fim_de_jogo(pontuacao):
    print("Sua pontuacao final foi:", pontuacao)
    print("*********************************")
    print("         Fim do Jogo")
    print("*********************************")


def acertou(chute,numero_secreto):
    return (chute == numero_secreto)


def vitoria(pontuacao):
    print("Parabens, vc acertou o numero secreto!")
    fim_de_jogo(pontuacao)
    exit(0)


def derrota(numero_secreto):
    print("\nVocê perdeu, o numero secreto era", numero_secreto, "\n")


def errou(chute,numero_secreto):
    if (chute > numero_secreto):
        print("Seu chute foi maior que o numero secreto")
    else:
        print("Seu chute foi menor que o numero secreto")

def colhe_chute():
    chute = input("Digite o seu número entre 1 e 100: ")
    return int(chute)

def fora_do_intervalo(chute):
    return (1 > chute or chute > 100)

def defineMaxTentativas(nivel):
    if (nivel == 1):
        return 20
    if (nivel == 2):
        return 10
    return 5

def escolheNivelDificuldade():
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nivel: "))
    return defineMaxTentativas(nivel)



################################################################################################################
# Inicio do código #

def jogar():

    numero_secreto = randint(1, 100)
    max_de_tentativas = 0
    nivel = 0
    pontuacao = 1000

    cabecalho()

    max_de_tentativas = escolheNivelDificuldade()


    def pontos_perdidos(chute):
        return abs(numero_secreto - chute)


    for rodada in range(0, max_de_tentativas):
        print("Tentativa {} de {}".format(rodada + 1,max_de_tentativas))
        chute = colhe_chute()
        # fora = fora_do_intervalo(chute)

        if (fora_do_intervalo(chute)):
            print("Valor fora do intervalo")
            continue

        if (acertou(chute,numero_secreto)):
            vitoria(pontuacao)
        else:
            errou(chute,numero_secreto)
            pontuacao -= pontos_perdidos(chute)

    derrota(numero_secreto)

    fim_de_jogo(pontuacao)

if (__name__ == "__main__"):
    jogar()