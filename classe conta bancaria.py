
class ContaBancaria:
    def __init__(self, titular, saldo=0): #saldo já possui um valor padrão
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("SALDO INSUFICIENTE")
    
    def exibir_saldo(self):
        print("SALDO: R$ {self.saldo:.2}")