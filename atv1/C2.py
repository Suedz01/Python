print("Bem vindo ao jogo de Adivinhação")

numero_secreto = 33

a = "Cherazard"
b = "Unicornio"
print(a+b)

chute = int(input("Digite o seu número: "))
print("você chutou o número", chute)

"""Booleanos"""

acertou = numero_secreto == chute
menor   = numero_secreto > chute
maior   = numero_secreto < chute

if(acertou):
    print("Você acertou...")
else:
    if(maior):
        print("Seu chute foi maior que o número...")
    elif(menor):
        print("Seu chute foi menor que o número...")