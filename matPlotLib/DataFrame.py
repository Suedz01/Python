import pandas as pd

dicionario = {'Nome': ['Alexandre', 'Gabriel', 'Felix'],
              'Idade': [15,16,20],
              'Aprovado': ['Sim', 'Não', 'Sim']}

data = pd.DataFrame(dicionario)
print(data)