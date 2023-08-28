class ContaBancaria:
    def __init__(self,titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero =numero
    def Depositar (self,dep):
        self.saldo += dep
        print("Depositando...", self.saldo)
    def sacar (self,tira):
        self.saldo -= tira
        print("sacando..", self.saldo)
    def exibir (self):
        print(self.saldo)


Conta = ContaBancaria("Lorena", 1.300, 4765)
Conta.Depositar(1.300)
Conta.exibir()