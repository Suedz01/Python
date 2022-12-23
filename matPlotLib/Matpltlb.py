import matplotlib.pyplot as plt
import pandas as pd


#x=[1,3,5,7,9,11,13,15,17]
#y=[1,2,4,6,8,10,12,14,16]

#plt.scatter(x,y) #plotagem de gráfico de dispersão com PONTOS
#plt.plot(x,y) #plotagem de gráfico em função
#plt.show() #ilustração do gráfico
#plt.hist(x,y) #plotagem de gráfico de histograma
#plt.pie() #plotagem de gráfico em pizza

x = pd.read_excel('C:/Users/sueda/OneDrive/Área de Trabalho/UFU/UFU - Periodo 5/E-ELA1/sla.xlsx')
plt.pie(x["Passos"], labels = x["Nomes"], autopct = "%1.3f%%")
plt.show()