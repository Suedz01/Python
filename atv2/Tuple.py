# Tuplas possuem uma quantidade de casas fixas
# Tuplas são imutáveis
# Ao em vez de usar colchetes, usa-se Parenteses

tp1 = (2, 1)
tp2 = (4, 6)
tp3 = (3, 5)

serie = [tp1, tp2, tp3]
print(serie)

aluno1 = ("Sued", 21)
aluno2 = ("Olivia", 23)
alunos = [aluno1, aluno2]
print(alunos[0][0], alunos[0][1])

#Há como copiar e compartilhar valores entre tuplas e listas
tp0 = list(tp1)
alunos_tupla = tuple(alunos)
print(tp0)
print(alunos_tupla)