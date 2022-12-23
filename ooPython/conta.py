class Conta: #Classe geral
    def __init__(self, numero, titular, saldo, limite = 1000):        #definição de atributos e características
        print(f'Construindo objeto...{self}')      #__index__ são funções especiais construtoras
        # Self são as referências que demarcam a memória do local da Classe
        self.__numero = numero      #Atributos privados
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'')

conta1 = Conta(1, "Fulano", 0.0)
conta2 = Conta(2, "Beltrano", 0.0)
conta3 = Conta(3, "Sicrano", 0.0, 2000)

#print(conta2.limite)

#Quando isso acontece, não é mais possível alcançar a primeira 'conta4' - Garbage Collector
conta4 = Conta(123, "Nico", 55.5)
conta4 = Conta(123, "Nico", 55.5)

#Dessa forma é possível alcançar o endereço da segunda conta4
outraRef = conta4
outraRef = None



