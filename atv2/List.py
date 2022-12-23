#https://www.pythonforbeginners.com/basics/lists-methods
#inserção
import rand0m

lista = [1, 2, 3, 4, 4.6, 2, 3, 1, -3]
lista2= [1,2,3,4,'x',2,3,'y']
for i in lista:
    print(i)

#verificação
print(1 in lista)

#identificação de máximos
print(min(lista))
print(max(lista))

#tamanho da lista
print(len(lista))

#acrescentar no final da lista
lista.append(9)
print(lista)

#remover um elemento
lista.pop() #Remove o ultimo elemento
lista.pop(2) #Casa indexada que será removida
lista.remove(4.6) #Valor da casa que será removida
print(lista)

#contagem de repetições
print(lista.count(1))

#retorno da posição
print(lista2.index('y'))

#Tentativa
a= ["a as ", "db", "c", "sda qwd", "edsa sa as"]
b = rand0m.randint(0, 4)
print(b)
print(len(a[b]))
#"_" for letra in palavra ~laço em uma linha