valor = float(input('Digite o valor R$:'))
desconto = valor + (valor * (4.74 / 100))
hora = desconto + (desconto * (1.99/100))
print('Para receber {}, deve-se cobrar {}' .format(valor,hora))
