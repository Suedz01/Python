import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

arqv1 = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/ELAXPTA/Plot/vin2.csv', delimiter = ';')
arqv2 = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/ELAXPTA/Plot/vout2.csv', delimiter = ';')

#Tempo = arqv1["time"]
Tempo = np.arange(0, 1, 0.005) * 5

#Definindo curvas
vin1 = arqv1["r Vin2.Vt"] *1000
vout1 = arqv2["r Vout2.Vt"] *1000

plt.figure(figsize=[6,3]) #tamanho da imagem

#Configuração da Aparência
plt.title("Ganho de Tensão", fontsize=15, fontweight= 'bold', fontstyle = 'italic', fontfamily='serif')
plt.xlabel("Tempo [ms]", fontsize=10, fontstyle = 'italic', fontfamily='serif')
plt.ylabel("V [mV]", fontsize=10, fontstyle = 'italic', fontfamily='serif')
plt.tight_layout() #Otimização do espaçamento

#Tracejado
plt.grid (axis='y')
plt.grid (axis='x')
plt.grid(True, which="both", linestyle='--')
#plt.xlim(0,5)
plt.ylim(-145, 145)

#Linhas e funções pltoadas
plt.plot(Tempo, vout1, 'b', label = 'Vout')
plt.plot(Tempo, vin1, 'r', label = 'Vin')
plt.legend()

#plt.legend(framealpha=0.1, facecolor='gray') #Apresentar a legenda/ Transparência/ Cor da Label
plt.show()