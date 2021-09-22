class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print(f"Seu saldo atual e de R$ {self.saldo:,.2f}")
        pass

    def depositar(self, valor):
        self.saldo += valor
        pass

    def sacar(self,valor):
        self.saldo -= valor
        pass
    

#programa
conta_abel = ContaCorrente("Abel", "111.222.333-44")
print(conta_abel.nome)
print(conta_abel.cpf)
print(conta_abel.consultar_saldo())
print(conta_abel.depositar(valor =10000))
print(conta_abel.consultar_saldo())
print(conta_abel.sacar(valor=900))
print(conta_abel.consultar_saldo())
        