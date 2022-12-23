import pandas as pd
import matplotlib.pyplot as plt
VD = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/UFU/UFU - Periodo 5/E-ELA1/SEMANA03/VD.csv', delimiter = ';')
ID = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/UFU/UFU - Periodo 5/E-ELA1/SEMANA03/ID.csv', delimiter = ';')

VDz = VD["B"]
Fonte = VD["Fonte"]
IDz = ID["A"]
"""
plt.plot(Fonte,IDz)
plt.show()
"""

fig = plt.figure()
myaxes = fig.add_axes([0.1,0.1,1.6,1.6])
myaxes.plot(Fonte, VDz, 'r', lw=3, label = VDz)
myaxes.plot(Fonte, IDz, 'b', lw=3)
myaxes.legend()
plt.show()