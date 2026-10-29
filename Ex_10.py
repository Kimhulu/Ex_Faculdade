import random

jogar = "s"

while jogar == "s":

    numero = random.randint(1, 100)
    tentativas = 5

    palpite = int(input("Adivinhe o número de 1 a 100: "))

    while palpite < 1 or palpite > 100:
        print("Adivinhe o número de 1 a 100!")
        palpite = int(input("Tenta de novo: "))

    while palpite != numero and tentativas > 1:

        tentativas = tentativas - 1

        if palpite < numero:
            print("O número é maior!")
        else:
            print("O número é menor!")

        if palpite == numero + 1 or palpite == numero - 1:
            print("Está quente!")
        elif palpite >= numero + 10 or palpite <= numero - 10:
            print("Está frio!")

        palpite = int(input("Tentativas restantes: " + str(tentativas) + ". Tenta de novo: "))

        while palpite < 1 or palpite > 100:
            print("Adivinhe o número de 1 a 100!")
            palpite = int(input("Tenta de novo: "))

    if palpite == numero:
        print("Acertou, miserável!")
        print("Quantas tentativas utilizou:", 6 - tentativas)
    else:
        print("Perdeu Playboy! O número era:", numero)

    jogar = input("Quer arriscar de novo? (s/n): ").lower()

print("Obrigado por jogar!")
