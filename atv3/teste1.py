"""
Ftemp=int(input("Digite uma temperatura em Fahrenheit:"))
Ctemp= (Ftemp-32)* 5/9
print("A temperatura", Ftemp,"em fahrenheint em celcius é:", Ctemp)
"""

segs = int(input("Insira uma quantidade de segundos: "))
mins = segs // 60
segs = segs % 60
hours = mins // 60
mins = mins % 60
days = hours // 24
hours = hours % 24

print("O resultado do cálculo foi:\n")
print("Segundos:",segs,"\nMinutos:",mins,"\nHoras:",hours,"\nDias:", days)
