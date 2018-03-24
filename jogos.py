import forca
import adivinhacao

print("*********************************")
print("*****  Escolha o seu jogo  ******")
print("*********************************")


print("(1) Forca    (2) Advinhacao")
jogo = int(input("Qual vc quer? "))

if (jogo == 1):
    forca.jogar()
elif (jogo == 2):
    adivinhacao.jogar()