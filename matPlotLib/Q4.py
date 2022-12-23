import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

arqv1 = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/Q5/Q5.csv', delimiter = ';')

#Variáveis
Vce = arqv1["Vce"] #x
ic_coletor = arqv1["r IC.I"] #y2

#tamanho da imagem
plt.figure(figsize=[5,3])

#Configuração da Aparência
plt.title("Curva do Projeto Coletor-Comum", fontsize=15, fontweight= 'bold', fontstyle = 'italic', fontfamily='serif')
plt.xlabel("Vce [V]", fontsize=10, fontstyle = 'italic', fontfamily='serif')
plt.ylabel("Ic [mA]", fontsize=10, fontstyle = 'italic', fontfamily='serif')
plt.tight_layout() #Otimização do espaçamento

#Tracejado
plt.grid (axis='y')
plt.grid (axis='x')
plt.style.use('ggplot')

#Linhas e funções pltoadas
plt.plot(Vce, ic_coletor, 'b')
plt.show()