from ContasBanco import ContaCorrente, CartaoCredito
#programa
conta_abel = ContaCorrente('Abel', '000.111.222-33', '0001', '0001009-2')

cartao_abel = CartaoCredito("Abel",conta_abel)

print(cartao_abel.conta_corrente._conta)
print(cartao_abel.numero)
print(cartao_abel.Validade)
print(cartao_abel.cvc) 