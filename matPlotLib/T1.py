import pandas as pd
import matplotlib.pyplot as plt
arqv1 = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/UFU/UFU - Periodo 5/E-ELA1/Estudando a parte/T1/VIN.csv', delimiter = ';')
arqv2 = pd.read_csv('C:/Users/sueda/OneDrive/Área de Trabalho/UFU/UFU - Periodo 5/E-ELA1/Estudando a parte/T1/VOUT.csv', delimiter = ';')

Vin = arqv1["r Vin.Vt"]
Time = arqv1["time"]

"""
plt.plot(Fonte,IDz)
plt.show()
"""

fig = plt.figure()
myaxes = fig.add_axes([0.1,0.1,2,2])
myaxes.plot(Time, Vin, 'r', lw=3, label = Vin)
myaxes.legend()
plt.show()