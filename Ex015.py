dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
valor = float((dias * 60) + (km * 0.15))
print('O total a págar é de R${:.2f}' .format(valor))
