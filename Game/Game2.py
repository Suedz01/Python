import Game0
import Game1

print(10*"#")
print("Escolha um Jogo", end="\n")
print(10*"#")

menu = int(input("[1] Jogo da Forca\n[2] Jogo da Adivinhação\n-> "))
if (menu == 1):
    Game1.forca()
elif (menu == 2):
    Game0.adivinhacao()