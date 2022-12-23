import random

def adivinhacao():
    numero_secreto = random.randrange(1,101)
    pontuação = 1000

    print(10*"#")
    print("Bem vindo ao jogo de Adivinhação", end="\n")
    print(10*"#")

    menu = int(input("\nNível:\n[1] Fácil\n[2] Médio\n[3] Difícil\n-> "))
    while True:
        if (menu == 1):
            tentativas = 15
        elif(menu == 2):
            tentativas = 10
        else:
            tentativas = 5
        if (menu >=1 and menu <=3):
            break

    for rodadas in range(1, tentativas + 1):
        print(10*"#")
        print("\nTentativas {} de {}\n".format(rodadas, tentativas))
        print(10*"#")
        while True:
            chute = int(input("Digite um número entre 1~100: "))
            chute
            chute_certo = chute >=1 and chute <=100
            if (chute_certo):
                break

        acertou = numero_secreto == chute
        menor   = numero_secreto > chute
        maior   = numero_secreto < chute

        if (acertou):
            print("Você acertou...")
            print("Sua pontuação final foi equivalente a {}. Parabéns!!".format(pontuação))
            break
        else:
            if(maior):
                print("Seu chute foi maior que o número...")
                diferença = abs(chute - numero_secreto)
                pontuação = pontuação - diferença
            elif(menor):
                print("Seu chute foi menor que o número...")
                diferença = abs(chute - numero_secreto)
                pontuação = pontuação - diferença

    print("O número secreto era:", numero_secreto)
    print("Sua pontuação final foi equivalente a {}.".format(pontuação))

#Esse passo permite que o código seja rodado diretamente
if (__name__ == "__main__"):
    adivinhacao()