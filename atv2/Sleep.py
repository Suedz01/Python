from time import sleep

def linha():
    print('-='*20)

def contador(i, f, p):
    linha()
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
    print('FIM!')


#Programa principal
contador(1, 10, 1)
contador(20, 1, 2)
linha()
print('Agora é sua vez!\n')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)