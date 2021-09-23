from datetime import datetime
import pytz
from random import randint 


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do Cliente
        cpf (str) = CPF do Cliente
        agencia = Agencia responsavel da conta do cliente
        conta = Numero da Conta Corrente do Cliente
        saldo = Saldo Disponivel na Conta do Cliente
        Limite = Limite do cheque especial daquele cliente
        transacoes = Historico de Transacoes do Cliente
    """   
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf,agencia, conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._conta = conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        """
            Exibe o saldo da conta corrente
        """
        print(f"Seu saldo atual e de R$ {self._saldo:,.2f}")

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        
    def limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar(self,valor):
        if self._saldo - valor < self.limite_conta():
            print("Voce nao tem saldo suficiente para sacar esse valor")
            self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print(f"Seu limite do cheque especial e de R$ {self.limite_conta():,.2f}")

    def consultar_transacoes(self):
        print("Historico de Transacoes: ")
        print("Valor, Saldo Data e Hora")
        for transacao in self._transacoes:
            print(transacao)        

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor,self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor,conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular_da_conta, conta_corrente) -> None:
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular_da_conta = titular_da_conta
        self.Validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year +4)
        self.cvc = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


#programa
conta_abel = ContaCorrente('Abel', '000.111.222-33', '0001', '0001009-2')

cartao_abel = CartaoCredito("Abel",conta_abel)

print(cartao_abel.conta_corrente._conta)
print(cartao_abel.numero)
print(cartao_abel.Validade)
print(cartao_abel.cvc)