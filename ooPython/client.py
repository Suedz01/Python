#Execução de métodos sem que seja necessário ()
class Cliente:
   def __init__(self, nome):
       self.__nome = nome

#Get
   @property
   def nome(self):
       print("chamando @property nome()")
       return self .__nome.title()

#Set
   @nome.setter
   def nome(self, nome):
       print("chamando setter nome()")
       self.__nome = nome

cliente = Cliente("xlex")
print(cliente.nome)
cliente.nome = "Felix"
print(cliente.nome)