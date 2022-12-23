def soma(a, b):
    print(a+b)
def sub(a, b):
    print(a-b)
def div(a, b):
    print(a/b)

print(10 * "#")
print("Bem vindo a Calculadora do Susu", end="\n")
print(10 * "#")

menu = int(input("Você quer:\n[1] Somar\n[2] Subtrair\n[3] Dividir\n-> "))
if (menu == 1):
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    soma(a,b)
elif (menu == 2):
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    sub(a, b)
if (menu == 3):
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    div(a, b)