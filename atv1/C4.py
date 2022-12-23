for rodada in range(1,11):
    print(rodada)
print("\n")
''' o terceiro argumento é o tamanho do degrau '''

for rodada in range(1,11,5):
    print(rodada)
print("\n")

for rodada in [1,2,3,4,5]:
    print(rodada)
    """break -é um comando que quebra loops"""
    """continue -sai do loop e pula para o próximo comando"""

while True:
    a = int(input("Digite um valor entre 1 e 10: "))
    b = (a >= 1 and a <= 10)
    print(b)
    if (b):
        break