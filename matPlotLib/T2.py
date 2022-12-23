import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def eixos_layout(): #Configuração da Aparência
    plt.title("Vi e Vout por tempo", fontsize=15, fontweight='bold', fontstyle='italic', fontfamily='serif')
    plt.xlabel("Tempo [ms]", fontsize=10, fontstyle='italic', fontfamily='serif')
    plt.ylabel("Voltagem [V]", fontsize=10, fontstyle='italic', fontfamily='serif')
    plt.tight_layout()  # Otimização do espaçamento

def plot_figure(x, y, z): #Linhas e funções pltoadas
    plt.plot(x, y, 'r', label='Vout')
    plt.plot(x, y, 'r', linewidth=5, alpha=0.1)
    plt.plot(x, z, 'b', label='Vi')
    plt.plot(x, z, 'b', linewidth=5, alpha=0.1)

def ponto_vermelho(): #vira e volta dá uns erros aqui - seriam os pontos vermelhos no gráfico
    plt.scatter(0.1, 2.55, Color="red")
    plt.scatter(0.37, -17.5, Color="red")
    plt.text(0.015, 3.2, "(X = 0.1 | Y = 2.5)")
    plt.text(0.27, -16.7, "(X = 0.3 | Y = -17.4)")

arqv1 = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/TESTE/Vin.csv', delimiter = ';')
arqv2 = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/TESTE/Vout.csv', delimiter = ';')

#Definição dos eixos
tempo = np.arange(0, 0.001, 0.000005) * 1000
Vin = arqv1["r Vi.Vt"]
Vout = arqv2["r Vout.Vt"]

#Tamanho da imagem
plt.figure(figsize=[8,5])

eixos_layout()
plot_figure(tempo, Vout, Vin)
#ponto_vermelho()

plt.legend(framealpha=0.1, facecolor='gray') #Apresentar a legenda/ Transparência/ Cor da Label
plt.style.use('ggplot')
plt.show()