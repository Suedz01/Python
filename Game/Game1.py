import random

def forca():
    impressão_abertura()
    misterio = carregar_palavra()
    tela_palavra = letras_acertadas(misterio)

    enforcou = False
    acertou = False
    erros = 0

    print("\nPalavra misteriosa:")
#junção dos espaços
    for i in tela_palavra:
        print(i, end='')
    print('\n')

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in misterio):
            controle_chute(misterio, chute, tela_palavra)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in tela_palavra

        for i in tela_palavra:
            print(i, end='')
        print('\n')

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(misterio)

    print("Fim do jogo")

def impressão_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregar_palavra():
    arquivo = open("Palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    casa = random.randrange(0,len(palavras))
    misterio = palavras[casa].upper()
    return misterio

def letras_acertadas(misterio):
    lista = ["_" for letra in misterio]
    return lista

def pede_chute():
    a = input("Qual letra?\n-> ")
    a = a.strip().upper()
    return a

def controle_chute(misterio, chute, tela_palavra):
    index = 0
    for letra in misterio:
        if (chute == letra):
            tela_palavra[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \ /   ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    forca()