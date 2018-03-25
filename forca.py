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

    palavra_secreta = "banana".lower()

    letras_chutadas = set()

    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().lower()
        if chute in letras_chutadas:
            print(f"Letra {chute} já chutada. Vc já chutou as letras{sorted(letras_chutadas)}")
            continue
        else:
            letras_chutadas.add(chute)

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    fim_de_jogo(pontuacao)


if (__name__ == "__main__"):
    jogar()
