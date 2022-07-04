r = float( input( 'Quanto dinheiro você tem na carteira?  R$'))
d = r / 5.12
print('Com R${:.2f} você pode comprar US${:.2f}' .format(r,d))

dollar = float(input('Digite o valor em dollar:'))
real = dollar * 5.12
print('Você pagará R${:.2f}' .format(real))