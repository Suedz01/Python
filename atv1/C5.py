import random

#round é o mesmo que arredondar
#random.random() é uma função que vai de [0.0,1.0)

n = round(random.random() * 3)
print(n)
print(type(n))

m = random.randrange(1,8)
print(m)
print(type(m))

# // -retornar apenas a parte inteira: integer division
a = 13//3
print(a)
b = 37//9
print(b)