class Conta: #Classe geral
    def __init__(self, numero, titular, saldo, limite = 1000):
        print(f'Construindo objeto...{self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O saldo da conta é de {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):       #Encapsulamento - "Self" vai endereçar o local da memória
        self.sacar(valor)
        destino.depositar(valor)

#Getters - devolvem valores, basta colocar "get" no início da função
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    """def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)"""