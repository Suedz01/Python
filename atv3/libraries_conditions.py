# not inverte um valor booleano, pode até fazer: 'not not true' = true
# or e and sz
import math

a = int(input("Você quer ver o resultado da raiz de 4[1] ou a de 2[2], [3]sair do prog?"))


if a == 1:
    print(math.sqrt(4))
elif a == 2:
    print(round(math.sqrt(2),2))  # a função round(x,2) pode definir o ponto flutuante com duas casas decimais
else:
    print("você digitou o numero errado, benzin...")

