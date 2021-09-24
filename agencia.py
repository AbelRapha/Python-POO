from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nivel recomendado. Caixa Atual: {self.caixa:,.2f}')
        else:
            print(f'O caixa esta ok. Caixa Atual {self.caixa:,.2f}')
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print(f'Emprestimo nao disponivel.')
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self,site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)
        self.caixa = 1000000
        

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero= randint(1001, 9999))
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self,valor):
        self.caixa -= valor
        
        if valor > self.caixa:
            print("Nao e possivel realizar a transferencia. Saldo Insuficiente")
        else:
            self.caixa_paypal += valor
    
    def sacar_paypal(self,valor):
        self.caixa_paypal -= valor
        if self.caixa_paypal < valor:
            print("Saldo insuficiente para realizar a transacao")
        else: 
            self.caixa += valor
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000


       
agencia1 = Agencia(2222222, 2223300239, 4568)
agencia_virtual = AgenciaVirtual('www.kdsjahdksa.com.br', 222223333, 1224433456,1234 )

agencia_virtual.verificar_caixa()

agencia_comum = AgenciaComum(2222222,223432353)
agencia_comum.verificar_caixa()

agencia_comum.depositar_paypal(1000)
print(agencia_comum.caixa_paypal)
agencia_comum.sacar_paypal(200)
print(agencia_comum.caixa_paypal)